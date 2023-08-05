# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CombinedJobObjectValueMap(object):
    _types = {
        "object_id": str,
        "value": str,
    }

    def __init__(self, d=None):
        self.object_id: Optional[str] = None
        self.value: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CombinedJobObjectValueMapBuilder":
        return CombinedJobObjectValueMapBuilder()


class CombinedJobObjectValueMapBuilder(object):
    def __init__(self) -> None:
        self._combined_job_object_value_map = CombinedJobObjectValueMap()

    def object_id(self, object_id: str) -> "CombinedJobObjectValueMapBuilder":
        self._combined_job_object_value_map.object_id = object_id
        return self

    def value(self, value: str) -> "CombinedJobObjectValueMapBuilder":
        self._combined_job_object_value_map.value = value
        return self

    def build(self) -> "CombinedJobObjectValueMap":
        return self._combined_job_object_value_map
