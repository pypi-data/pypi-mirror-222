#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : spark
# @Time         : 2023/8/1 12:20
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  :

import hmac
import hashlib
from urllib.parse import urlparse, urlencode

from meutils.pipe import *
from meutils.cache_utils import ttl_cache
from meutils.decorators.retry import retrying


class SparkBot(object):
    # 初始化
    def __init__(self, APPID, APIKey, APISecret, gpt_url):
        self.APPID = APPID
        self.APIKey = APIKey
        self.APISecret = APISecret

        self.gpt_url = gpt_url

    # 生成url
    def create_url(self):
        from time import mktime
        from datetime import datetime
        from wsgiref.handlers import format_date_time

        gpt_url = "ws://spark-api.xf-yun.com/v1.1/chat"
        self.host = urlparse(gpt_url).netloc
        self.path = urlparse(gpt_url).path

        # 生成RFC1123格式的时间戳
        now = datetime.now()
        date = format_date_time(mktime(now.timetuple()))

        # 拼接字符串
        signature_origin = "host: " + self.host + "\n"
        signature_origin += "date: " + date + "\n"
        signature_origin += "GET " + self.path + " HTTP/1.1"

        # 进行hmac-sha256进行加密
        signature_sha = hmac.new(self.APISecret.encode('utf-8'), signature_origin.encode('utf-8'),
                                 digestmod=hashlib.sha256).digest()

        signature_sha_base64 = base64.b64encode(signature_sha).decode(encoding='utf-8')

        authorization_origin = f'api_key="{self.APIKey}", algorithm="hmac-sha256", headers="host date request-line", signature="{signature_sha_base64}"'

        authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')

        # 将请求的鉴权参数组合为字典
        v = {
            "authorization": authorization,
            "date": date,
            "host": self.host
        }
        # 拼接鉴权参数，生成url
        url = f"ws://spark-api.xf-yun.com/v1.1/chat?{urlencode(v)}"
        # 此处打印出建立连接时候的url,参考本demo的时候可取消上方打印的注释，比对相同参数时生成的url与自己代码生成的url是否一致
        return url
