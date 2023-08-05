# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .application import Application


class PatchApplicationRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.lang: Optional[str] = None
        self.app_id: Optional[str] = None
        self.request_body: Optional[Application] = None

    @staticmethod
    def builder() -> "PatchApplicationRequestBuilder":
        return PatchApplicationRequestBuilder()


class PatchApplicationRequestBuilder(object):

    def __init__(self) -> None:
        patch_application_request = PatchApplicationRequest()
        patch_application_request.http_method = HttpMethod.PATCH
        patch_application_request.uri = "/open-apis/application/v6/applications/:app_id"
        patch_application_request.token_types = {AccessTokenType.TENANT}
        self._patch_application_request: PatchApplicationRequest = patch_application_request

    def lang(self, lang: str) -> "PatchApplicationRequestBuilder":
        self._patch_application_request.lang = lang
        self._patch_application_request.add_query("lang", lang)
        return self

    def app_id(self, app_id: str) -> "PatchApplicationRequestBuilder":
        self._patch_application_request.app_id = app_id
        self._patch_application_request.paths["app_id"] = str(app_id)
        return self

    def request_body(self, request_body: Application) -> "PatchApplicationRequestBuilder":
        self._patch_application_request.request_body = request_body
        self._patch_application_request.body = request_body
        return self

    def build(self) -> PatchApplicationRequest:
        return self._patch_application_request
