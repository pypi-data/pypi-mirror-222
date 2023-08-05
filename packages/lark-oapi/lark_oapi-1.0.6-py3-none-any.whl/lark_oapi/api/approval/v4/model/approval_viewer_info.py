# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ApprovalViewerInfo(object):
    _types = {
        "type": str,
        "id": str,
        "user_id": str,
    }

    def __init__(self, d=None):
        self.type: Optional[str] = None
        self.id: Optional[str] = None
        self.user_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApprovalViewerInfoBuilder":
        return ApprovalViewerInfoBuilder()


class ApprovalViewerInfoBuilder(object):
    def __init__(self) -> None:
        self._approval_viewer_info = ApprovalViewerInfo()

    def type(self, type: str) -> "ApprovalViewerInfoBuilder":
        self._approval_viewer_info.type = type
        return self

    def id(self, id: str) -> "ApprovalViewerInfoBuilder":
        self._approval_viewer_info.id = id
        return self

    def user_id(self, user_id: str) -> "ApprovalViewerInfoBuilder":
        self._approval_viewer_info.user_id = user_id
        return self

    def build(self) -> "ApprovalViewerInfo":
        return self._approval_viewer_info
