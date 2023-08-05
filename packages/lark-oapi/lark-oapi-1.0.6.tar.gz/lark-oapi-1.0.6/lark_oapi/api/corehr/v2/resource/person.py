# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_person_request import CreatePersonRequest
from ..model.create_person_response import CreatePersonResponse
from ..model.patch_person_request import PatchPersonRequest
from ..model.patch_person_response import PatchPersonResponse


class Person(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreatePersonRequest, option: Optional[RequestOption] = None) -> CreatePersonResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreatePersonResponse = JSON.unmarshal(str(resp.content, UTF_8), CreatePersonResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchPersonRequest, option: Optional[RequestOption] = None) -> PatchPersonResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: PatchPersonResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchPersonResponse)
        response.raw = resp

        return response
