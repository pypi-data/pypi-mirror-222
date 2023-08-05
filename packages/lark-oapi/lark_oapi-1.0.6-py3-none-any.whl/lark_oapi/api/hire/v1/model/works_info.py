# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class WorksInfo(object):
    _types = {
        "attachment_id": str,
        "desc": str,
        "link": str,
    }

    def __init__(self, d=None):
        self.attachment_id: Optional[str] = None
        self.desc: Optional[str] = None
        self.link: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WorksInfoBuilder":
        return WorksInfoBuilder()


class WorksInfoBuilder(object):
    def __init__(self) -> None:
        self._works_info = WorksInfo()

    def attachment_id(self, attachment_id: str) -> "WorksInfoBuilder":
        self._works_info.attachment_id = attachment_id
        return self

    def desc(self, desc: str) -> "WorksInfoBuilder":
        self._works_info.desc = desc
        return self

    def link(self, link: str) -> "WorksInfoBuilder":
        self._works_info.link = link
        return self

    def build(self) -> "WorksInfo":
        return self._works_info
