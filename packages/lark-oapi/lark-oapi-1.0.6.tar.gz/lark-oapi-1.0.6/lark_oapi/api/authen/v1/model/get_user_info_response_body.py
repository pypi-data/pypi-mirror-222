# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class GetUserInfoResponseBody(object):
    _types = {
        "name": str,
        "en_name": str,
        "avatar_url": str,
        "avatar_thumb": str,
        "avatar_middle": str,
        "avatar_big": str,
        "open_id": str,
        "union_id": str,
        "email": str,
        "enterprise_email": str,
        "user_id": str,
        "mobile": str,
        "tenant_key": str,
        "employee_no": str,
    }

    def __init__(self, d=None):
        self.name: Optional[str] = None
        self.en_name: Optional[str] = None
        self.avatar_url: Optional[str] = None
        self.avatar_thumb: Optional[str] = None
        self.avatar_middle: Optional[str] = None
        self.avatar_big: Optional[str] = None
        self.open_id: Optional[str] = None
        self.union_id: Optional[str] = None
        self.email: Optional[str] = None
        self.enterprise_email: Optional[str] = None
        self.user_id: Optional[str] = None
        self.mobile: Optional[str] = None
        self.tenant_key: Optional[str] = None
        self.employee_no: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetUserInfoResponseBodyBuilder":
        return GetUserInfoResponseBodyBuilder()


class GetUserInfoResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_user_info_response_body = GetUserInfoResponseBody()

    def name(self, name: str) -> "GetUserInfoResponseBodyBuilder":
        self._get_user_info_response_body.name = name
        return self

    def en_name(self, en_name: str) -> "GetUserInfoResponseBodyBuilder":
        self._get_user_info_response_body.en_name = en_name
        return self

    def avatar_url(self, avatar_url: str) -> "GetUserInfoResponseBodyBuilder":
        self._get_user_info_response_body.avatar_url = avatar_url
        return self

    def avatar_thumb(self, avatar_thumb: str) -> "GetUserInfoResponseBodyBuilder":
        self._get_user_info_response_body.avatar_thumb = avatar_thumb
        return self

    def avatar_middle(self, avatar_middle: str) -> "GetUserInfoResponseBodyBuilder":
        self._get_user_info_response_body.avatar_middle = avatar_middle
        return self

    def avatar_big(self, avatar_big: str) -> "GetUserInfoResponseBodyBuilder":
        self._get_user_info_response_body.avatar_big = avatar_big
        return self

    def open_id(self, open_id: str) -> "GetUserInfoResponseBodyBuilder":
        self._get_user_info_response_body.open_id = open_id
        return self

    def union_id(self, union_id: str) -> "GetUserInfoResponseBodyBuilder":
        self._get_user_info_response_body.union_id = union_id
        return self

    def email(self, email: str) -> "GetUserInfoResponseBodyBuilder":
        self._get_user_info_response_body.email = email
        return self

    def enterprise_email(self, enterprise_email: str) -> "GetUserInfoResponseBodyBuilder":
        self._get_user_info_response_body.enterprise_email = enterprise_email
        return self

    def user_id(self, user_id: str) -> "GetUserInfoResponseBodyBuilder":
        self._get_user_info_response_body.user_id = user_id
        return self

    def mobile(self, mobile: str) -> "GetUserInfoResponseBodyBuilder":
        self._get_user_info_response_body.mobile = mobile
        return self

    def tenant_key(self, tenant_key: str) -> "GetUserInfoResponseBodyBuilder":
        self._get_user_info_response_body.tenant_key = tenant_key
        return self

    def employee_no(self, employee_no: str) -> "GetUserInfoResponseBodyBuilder":
        self._get_user_info_response_body.employee_no = employee_no
        return self

    def build(self) -> "GetUserInfoResponseBody":
        return self._get_user_info_response_body
