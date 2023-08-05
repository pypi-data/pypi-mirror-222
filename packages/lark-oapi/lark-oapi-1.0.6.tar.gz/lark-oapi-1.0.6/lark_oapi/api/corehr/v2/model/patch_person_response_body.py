# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .person_info import PersonInfo


class PatchPersonResponseBody(object):
    _types = {
        "person": PersonInfo,
    }

    def __init__(self, d=None):
        self.person: Optional[PersonInfo] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchPersonResponseBodyBuilder":
        return PatchPersonResponseBodyBuilder()


class PatchPersonResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._patch_person_response_body = PatchPersonResponseBody()

    def person(self, person: PersonInfo) -> "PatchPersonResponseBodyBuilder":
        self._patch_person_response_body.person = person
        return self

    def build(self) -> "PatchPersonResponseBody":
        return self._patch_person_response_body
