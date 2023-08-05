# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class OfferApplyFormPreObjectConfigInfo(object):
    _types = {
        "id": str,
        "operator": int,
        "value": List[str],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.operator: Optional[int] = None
        self.value: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OfferApplyFormPreObjectConfigInfoBuilder":
        return OfferApplyFormPreObjectConfigInfoBuilder()


class OfferApplyFormPreObjectConfigInfoBuilder(object):
    def __init__(self) -> None:
        self._offer_apply_form_pre_object_config_info = OfferApplyFormPreObjectConfigInfo()

    def id(self, id: str) -> "OfferApplyFormPreObjectConfigInfoBuilder":
        self._offer_apply_form_pre_object_config_info.id = id
        return self

    def operator(self, operator: int) -> "OfferApplyFormPreObjectConfigInfoBuilder":
        self._offer_apply_form_pre_object_config_info.operator = operator
        return self

    def value(self, value: List[str]) -> "OfferApplyFormPreObjectConfigInfoBuilder":
        self._offer_apply_form_pre_object_config_info.value = value
        return self

    def build(self) -> "OfferApplyFormPreObjectConfigInfo":
        return self._offer_apply_form_pre_object_config_info
