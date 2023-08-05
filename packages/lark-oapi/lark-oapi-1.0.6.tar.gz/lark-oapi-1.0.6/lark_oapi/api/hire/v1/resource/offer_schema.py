# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.get_offer_schema_request import GetOfferSchemaRequest
from ..model.get_offer_schema_response import GetOfferSchemaResponse


class OfferSchema(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def get(self, request: GetOfferSchemaRequest, option: Optional[RequestOption] = None) -> GetOfferSchemaResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetOfferSchemaResponse = JSON.unmarshal(str(resp.content, UTF_8), GetOfferSchemaResponse)
        response.raw = resp

        return response
