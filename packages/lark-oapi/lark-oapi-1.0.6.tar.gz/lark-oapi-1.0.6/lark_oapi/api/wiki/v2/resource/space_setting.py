# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.update_space_setting_request import UpdateSpaceSettingRequest
from ..model.update_space_setting_response import UpdateSpaceSettingResponse


class SpaceSetting(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def update(self, request: UpdateSpaceSettingRequest,
               option: Optional[RequestOption] = None) -> UpdateSpaceSettingResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: UpdateSpaceSettingResponse = JSON.unmarshal(str(resp.content, UTF_8), UpdateSpaceSettingResponse)
        response.raw = resp

        return response
