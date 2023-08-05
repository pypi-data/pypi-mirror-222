# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class MsgActionI18nInfo(object):
    _types = {
        "i18n_key": str,
        "name": str,
    }

    def __init__(self, d=None):
        self.i18n_key: Optional[str] = None
        self.name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MsgActionI18nInfoBuilder":
        return MsgActionI18nInfoBuilder()


class MsgActionI18nInfoBuilder(object):
    def __init__(self) -> None:
        self._msg_action_i18n_info = MsgActionI18nInfo()

    def i18n_key(self, i18n_key: str) -> "MsgActionI18nInfoBuilder":
        self._msg_action_i18n_info.i18n_key = i18n_key
        return self

    def name(self, name: str) -> "MsgActionI18nInfoBuilder":
        self._msg_action_i18n_info.name = name
        return self

    def build(self) -> "MsgActionI18nInfo":
        return self._msg_action_i18n_info
