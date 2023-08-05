# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .generate_caldav_conf_setting_request_body import GenerateCaldavConfSettingRequestBody


class GenerateCaldavConfSettingRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[GenerateCaldavConfSettingRequestBody] = None

    @staticmethod
    def builder() -> "GenerateCaldavConfSettingRequestBuilder":
        return GenerateCaldavConfSettingRequestBuilder()


class GenerateCaldavConfSettingRequestBuilder(object):

    def __init__(self) -> None:
        generate_caldav_conf_setting_request = GenerateCaldavConfSettingRequest()
        generate_caldav_conf_setting_request.http_method = HttpMethod.POST
        generate_caldav_conf_setting_request.uri = "/open-apis/calendar/v4/settings/generate_caldav_conf"
        generate_caldav_conf_setting_request.token_types = {AccessTokenType.USER}
        self._generate_caldav_conf_setting_request: GenerateCaldavConfSettingRequest = generate_caldav_conf_setting_request

    def request_body(self,
                     request_body: GenerateCaldavConfSettingRequestBody) -> "GenerateCaldavConfSettingRequestBuilder":
        self._generate_caldav_conf_setting_request.request_body = request_body
        self._generate_caldav_conf_setting_request.body = request_body
        return self

    def build(self) -> GenerateCaldavConfSettingRequest:
        return self._generate_caldav_conf_setting_request
