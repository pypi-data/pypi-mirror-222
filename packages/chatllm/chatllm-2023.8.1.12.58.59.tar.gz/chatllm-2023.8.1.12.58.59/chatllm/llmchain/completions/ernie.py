#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : ernie
# @Time         : 2023/7/31 16:34
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  : https://cloud.baidu.com/doc/WENXINWORKSHOP/s/flfmc9do2

from meutils.pipe import *
from meutils.cache_utils import ttl_cache
from meutils.decorators.retry import retrying


class ErnieBotCompletion(object):

    @classmethod
    def create(
        cls,
        messages: List[Dict[str, Any]],  # [{'role': 'user', 'content': '讲个故事'}]
        **kwargs,
        # {'model': 'gpt-3.5-turbo', 'request_timeout': None, 'max_tokens': None, 'stream': False, 'n': 1, 'temperature': 0.7, 'api_key': 'sk-...', 'api_base': 'https://api.openai-proxy.com/v1', 'organization': ''}
    ):

        api_key, secret_key = kwargs.pop('api_key').split(':')
        post_kwargs = {
            'url': cls.create_url(api_key, secret_key),
            'json': {
                'messages': messages,

                'stream': kwargs.get('stream'),
                'temperature': np.clip(kwargs.get('temperature', 0), 0.01, 1),
            },
            'stream': kwargs.get('stream')
        }

        response = requests.post(**post_kwargs)
        if kwargs.get('stream'):
            return cls.stream_create(response)

        else:
            resp = response.json()

            resp['object'] = "chat.completion"
            resp['choices'] = [
                {"message": {"role": "assistant", "content": resp.pop('result')}, "index": 0, "finish_reason": "stop"}
            ]
            resp['token_usage'] = resp.pop('usage', {})
            return resp

    @staticmethod
    def stream_create(response):
        _chunk = ''
        stream_resp = {}
        for chunk in response.iter_content(chunk_size=256, decode_unicode=True):
            if chunk:
                _chunk += chunk
                if '\n\n' not in _chunk:
                    continue

                chunks = _chunk.rsplit('\n\n', 1)
                stream_resp = json.loads(chunks[0].strip('data: \n\n'))
                _chunk = chunks[1]

                content = stream_resp.pop('result')
                stream_resp['object'] = "chat.completion.chunk"
                stream_resp['choices'] = [
                    {"delta": {"role": "assistant", "content": content}, "index": 0, "finish_reason": None}]

                stream_resp['token_usage'] = stream_resp.pop('usage', {})
                yield stream_resp

        stream_resp = stream_resp or json.loads(_chunk.strip('data: \n\n'))  # 只有一行

        stream_resp['token_usage'] = stream_resp.pop('usage', {})
        stream_resp['choices'] = [{"delta": {}, "index": 0, "finish_reason": "stop"}]
        yield stream_resp

    @staticmethod
    @retrying
    @ttl_cache(ttl=7 * 24 * 3600)
    def create_url(api_key, secret_key):
        """
        使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
        """

        url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={api_key}&client_secret={secret_key}"
        response = requests.request("POST", url)
        access_token = response.json().get("access_token")
        url = f'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token={access_token}'
        return url


if __name__ == '__main__':
    from meutils.pipe import *

    ec = ErnieBotCompletion()
    r = ec.create(
        [{'role': 'user', 'content': '你是谁'}],
        stream=True,
        api_key=os.getenv('ERNIE_API_KEY')
    )
    for i in r:
        print(i['choices'][0]['delta'].get('content', ''), end='')
