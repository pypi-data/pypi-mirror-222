# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .management_scope import ManagementScope


class SearchAssignedUserRequestBody(object):
    _types = {
        "role_id": str,
        "management_scope_list": List[ManagementScope],
        "search_method": str,
        "page_token": str,
        "page_size": str,
    }

    def __init__(self, d=None):
        self.role_id: Optional[str] = None
        self.management_scope_list: Optional[List[ManagementScope]] = None
        self.search_method: Optional[str] = None
        self.page_token: Optional[str] = None
        self.page_size: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchAssignedUserRequestBodyBuilder":
        return SearchAssignedUserRequestBodyBuilder()


class SearchAssignedUserRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._search_assigned_user_request_body = SearchAssignedUserRequestBody()

    def role_id(self, role_id: str) -> "SearchAssignedUserRequestBodyBuilder":
        self._search_assigned_user_request_body.role_id = role_id
        return self

    def management_scope_list(self,
                              management_scope_list: List[ManagementScope]) -> "SearchAssignedUserRequestBodyBuilder":
        self._search_assigned_user_request_body.management_scope_list = management_scope_list
        return self

    def search_method(self, search_method: str) -> "SearchAssignedUserRequestBodyBuilder":
        self._search_assigned_user_request_body.search_method = search_method
        return self

    def page_token(self, page_token: str) -> "SearchAssignedUserRequestBodyBuilder":
        self._search_assigned_user_request_body.page_token = page_token
        return self

    def page_size(self, page_size: str) -> "SearchAssignedUserRequestBodyBuilder":
        self._search_assigned_user_request_body.page_size = page_size
        return self

    def build(self) -> "SearchAssignedUserRequestBody":
        return self._search_assigned_user_request_body
