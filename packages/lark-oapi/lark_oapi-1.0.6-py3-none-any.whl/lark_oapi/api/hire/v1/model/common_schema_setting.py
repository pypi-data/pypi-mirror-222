# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .common_schema_config import CommonSchemaConfig


class CommonSchemaSetting(object):
    _types = {
        "object_type": int,
        "config": CommonSchemaConfig,
    }

    def __init__(self, d=None):
        self.object_type: Optional[int] = None
        self.config: Optional[CommonSchemaConfig] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CommonSchemaSettingBuilder":
        return CommonSchemaSettingBuilder()


class CommonSchemaSettingBuilder(object):
    def __init__(self) -> None:
        self._common_schema_setting = CommonSchemaSetting()

    def object_type(self, object_type: int) -> "CommonSchemaSettingBuilder":
        self._common_schema_setting.object_type = object_type
        return self

    def config(self, config: CommonSchemaConfig) -> "CommonSchemaSettingBuilder":
        self._common_schema_setting.config = config
        return self

    def build(self) -> "CommonSchemaSetting":
        return self._common_schema_setting
