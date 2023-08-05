# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .app_visible_list import AppVisibleList


class ApplicationAppContactsRange(object):
    _types = {
        "contacts_scope_type": str,
        "visible_list": AppVisibleList,
    }

    def __init__(self, d=None):
        self.contacts_scope_type: Optional[str] = None
        self.visible_list: Optional[AppVisibleList] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApplicationAppContactsRangeBuilder":
        return ApplicationAppContactsRangeBuilder()


class ApplicationAppContactsRangeBuilder(object):
    def __init__(self) -> None:
        self._application_app_contacts_range = ApplicationAppContactsRange()

    def contacts_scope_type(self, contacts_scope_type: str) -> "ApplicationAppContactsRangeBuilder":
        self._application_app_contacts_range.contacts_scope_type = contacts_scope_type
        return self

    def visible_list(self, visible_list: AppVisibleList) -> "ApplicationAppContactsRangeBuilder":
        self._application_app_contacts_range.visible_list = visible_list
        return self

    def build(self) -> "ApplicationAppContactsRange":
        return self._application_app_contacts_range
