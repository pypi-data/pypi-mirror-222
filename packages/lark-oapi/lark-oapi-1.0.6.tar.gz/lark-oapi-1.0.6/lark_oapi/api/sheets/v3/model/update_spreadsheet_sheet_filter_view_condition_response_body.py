# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .filter_view_condition import FilterViewCondition


class UpdateSpreadsheetSheetFilterViewConditionResponseBody(object):
    _types = {
        "condition": FilterViewCondition,
    }

    def __init__(self, d=None):
        self.condition: Optional[FilterViewCondition] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateSpreadsheetSheetFilterViewConditionResponseBodyBuilder":
        return UpdateSpreadsheetSheetFilterViewConditionResponseBodyBuilder()


class UpdateSpreadsheetSheetFilterViewConditionResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._update_spreadsheet_sheet_filter_view_condition_response_body = UpdateSpreadsheetSheetFilterViewConditionResponseBody()

    def condition(self,
                  condition: FilterViewCondition) -> "UpdateSpreadsheetSheetFilterViewConditionResponseBodyBuilder":
        self._update_spreadsheet_sheet_filter_view_condition_response_body.condition = condition
        return self

    def build(self) -> "UpdateSpreadsheetSheetFilterViewConditionResponseBody":
        return self._update_spreadsheet_sheet_filter_view_condition_response_body
