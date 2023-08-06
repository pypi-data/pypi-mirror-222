#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : ChatCompletion
# @Time         : 2023/7/31 16:07
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  :

from meutils.pipe import *
from meutils.pipe import ttl_cache
from meutils.decorators.retry import retrying


class ErnieCompletion(object):

    def create(self):
        pass

    @property
    def _url(self):
        access_token = self._get_access_token(self.ernie_api_key.split(':'))
        url = f'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token={access_token}'
        return url

    @staticmethod
    @retrying
    @ttl_cache(ttl=7 * 24 * 3600)
    def _get_access_token(api_key, secret_key):
        """
        使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
        """

        url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={api_key}&client_secret={secret_key}"

        response = requests.request("POST", url)
        # print(response.json())
        return response.json().get("access_token")
