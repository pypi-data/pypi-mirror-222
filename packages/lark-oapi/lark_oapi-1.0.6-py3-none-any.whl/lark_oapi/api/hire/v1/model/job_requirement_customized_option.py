# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n


class JobRequirementCustomizedOption(object):
    _types = {
        "key": str,
        "name": I18n,
    }

    def __init__(self, d=None):
        self.key: Optional[str] = None
        self.name: Optional[I18n] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobRequirementCustomizedOptionBuilder":
        return JobRequirementCustomizedOptionBuilder()


class JobRequirementCustomizedOptionBuilder(object):
    def __init__(self) -> None:
        self._job_requirement_customized_option = JobRequirementCustomizedOption()

    def key(self, key: str) -> "JobRequirementCustomizedOptionBuilder":
        self._job_requirement_customized_option.key = key
        return self

    def name(self, name: I18n) -> "JobRequirementCustomizedOptionBuilder":
        self._job_requirement_customized_option.name = name
        return self

    def build(self) -> "JobRequirementCustomizedOption":
        return self._job_requirement_customized_option
