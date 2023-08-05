# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .objective_id_with_kr_id import ObjectiveIdWithKrId
from .okr_visible_setting import OkrVisibleSetting


class Okr(object):
    _types = {
        "okr_id": int,
        "objectives": List[ObjectiveIdWithKrId],
        "period_display_status": str,
        "period_name_zh": str,
        "period_name_en": str,
        "user_id": str,
        "visible_setting": OkrVisibleSetting,
    }

    def __init__(self, d=None):
        self.okr_id: Optional[int] = None
        self.objectives: Optional[List[ObjectiveIdWithKrId]] = None
        self.period_display_status: Optional[str] = None
        self.period_name_zh: Optional[str] = None
        self.period_name_en: Optional[str] = None
        self.user_id: Optional[str] = None
        self.visible_setting: Optional[OkrVisibleSetting] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OkrBuilder":
        return OkrBuilder()


class OkrBuilder(object):
    def __init__(self) -> None:
        self._okr = Okr()

    def okr_id(self, okr_id: int) -> "OkrBuilder":
        self._okr.okr_id = okr_id
        return self

    def objectives(self, objectives: List[ObjectiveIdWithKrId]) -> "OkrBuilder":
        self._okr.objectives = objectives
        return self

    def period_display_status(self, period_display_status: str) -> "OkrBuilder":
        self._okr.period_display_status = period_display_status
        return self

    def period_name_zh(self, period_name_zh: str) -> "OkrBuilder":
        self._okr.period_name_zh = period_name_zh
        return self

    def period_name_en(self, period_name_en: str) -> "OkrBuilder":
        self._okr.period_name_en = period_name_en
        return self

    def user_id(self, user_id: str) -> "OkrBuilder":
        self._okr.user_id = user_id
        return self

    def visible_setting(self, visible_setting: OkrVisibleSetting) -> "OkrBuilder":
        self._okr.visible_setting = visible_setting
        return self

    def build(self) -> "Okr":
        return self._okr
