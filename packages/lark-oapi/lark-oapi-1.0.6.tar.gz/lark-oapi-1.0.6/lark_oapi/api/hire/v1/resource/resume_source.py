# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.list_resume_source_request import ListResumeSourceRequest
from ..model.list_resume_source_response import ListResumeSourceResponse


class ResumeSource(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def list(self, request: ListResumeSourceRequest,
             option: Optional[RequestOption] = None) -> ListResumeSourceResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListResumeSourceResponse = JSON.unmarshal(str(resp.content, UTF_8), ListResumeSourceResponse)
        response.raw = resp

        return response
