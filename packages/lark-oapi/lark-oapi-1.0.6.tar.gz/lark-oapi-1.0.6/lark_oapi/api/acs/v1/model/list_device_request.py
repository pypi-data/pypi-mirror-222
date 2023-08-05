# Code generated by Lark OpenAPI.

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListDeviceRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def builder() -> "ListDeviceRequestBuilder":
        return ListDeviceRequestBuilder()


class ListDeviceRequestBuilder(object):

    def __init__(self) -> None:
        list_device_request = ListDeviceRequest()
        list_device_request.http_method = HttpMethod.GET
        list_device_request.uri = "/open-apis/acs/v1/devices"
        list_device_request.token_types = {AccessTokenType.TENANT}
        self._list_device_request: ListDeviceRequest = list_device_request

    def build(self) -> ListDeviceRequest:
        return self._list_device_request
