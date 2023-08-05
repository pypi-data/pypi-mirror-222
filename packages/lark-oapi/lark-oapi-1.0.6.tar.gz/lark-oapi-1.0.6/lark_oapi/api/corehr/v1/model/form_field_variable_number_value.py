# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class FormFieldVariableNumberValue(object):
    _types = {
        "value": str,
    }

    def __init__(self, d=None):
        self.value: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FormFieldVariableNumberValueBuilder":
        return FormFieldVariableNumberValueBuilder()


class FormFieldVariableNumberValueBuilder(object):
    def __init__(self) -> None:
        self._form_field_variable_number_value = FormFieldVariableNumberValue()

    def value(self, value: str) -> "FormFieldVariableNumberValueBuilder":
        self._form_field_variable_number_value.value = value
        return self

    def build(self) -> "FormFieldVariableNumberValue":
        return self._form_field_variable_number_value
