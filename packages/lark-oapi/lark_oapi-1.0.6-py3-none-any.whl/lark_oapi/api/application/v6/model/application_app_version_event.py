# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .app_ability import AppAbility
from .app_i18n_info import AppI18nInfo
from .app_scope import AppScope
from .app_version_remark_event import AppVersionRemarkEvent


class ApplicationAppVersionEvent(object):
    _types = {
        "app_id": str,
        "version": str,
        "version_id": str,
        "app_name": str,
        "avatar_url": str,
        "description": str,
        "scopes": List[AppScope],
        "back_home_url": str,
        "i18n": List[AppI18nInfo],
        "common_categories": List[str],
        "events": List[str],
        "status": int,
        "create_time": int,
        "publish_time": int,
        "ability": AppAbility,
        "remark": AppVersionRemarkEvent,
    }

    def __init__(self, d=None):
        self.app_id: Optional[str] = None
        self.version: Optional[str] = None
        self.version_id: Optional[str] = None
        self.app_name: Optional[str] = None
        self.avatar_url: Optional[str] = None
        self.description: Optional[str] = None
        self.scopes: Optional[List[AppScope]] = None
        self.back_home_url: Optional[str] = None
        self.i18n: Optional[List[AppI18nInfo]] = None
        self.common_categories: Optional[List[str]] = None
        self.events: Optional[List[str]] = None
        self.status: Optional[int] = None
        self.create_time: Optional[int] = None
        self.publish_time: Optional[int] = None
        self.ability: Optional[AppAbility] = None
        self.remark: Optional[AppVersionRemarkEvent] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApplicationAppVersionEventBuilder":
        return ApplicationAppVersionEventBuilder()


class ApplicationAppVersionEventBuilder(object):
    def __init__(self) -> None:
        self._application_app_version_event = ApplicationAppVersionEvent()

    def app_id(self, app_id: str) -> "ApplicationAppVersionEventBuilder":
        self._application_app_version_event.app_id = app_id
        return self

    def version(self, version: str) -> "ApplicationAppVersionEventBuilder":
        self._application_app_version_event.version = version
        return self

    def version_id(self, version_id: str) -> "ApplicationAppVersionEventBuilder":
        self._application_app_version_event.version_id = version_id
        return self

    def app_name(self, app_name: str) -> "ApplicationAppVersionEventBuilder":
        self._application_app_version_event.app_name = app_name
        return self

    def avatar_url(self, avatar_url: str) -> "ApplicationAppVersionEventBuilder":
        self._application_app_version_event.avatar_url = avatar_url
        return self

    def description(self, description: str) -> "ApplicationAppVersionEventBuilder":
        self._application_app_version_event.description = description
        return self

    def scopes(self, scopes: List[AppScope]) -> "ApplicationAppVersionEventBuilder":
        self._application_app_version_event.scopes = scopes
        return self

    def back_home_url(self, back_home_url: str) -> "ApplicationAppVersionEventBuilder":
        self._application_app_version_event.back_home_url = back_home_url
        return self

    def i18n(self, i18n: List[AppI18nInfo]) -> "ApplicationAppVersionEventBuilder":
        self._application_app_version_event.i18n = i18n
        return self

    def common_categories(self, common_categories: List[str]) -> "ApplicationAppVersionEventBuilder":
        self._application_app_version_event.common_categories = common_categories
        return self

    def events(self, events: List[str]) -> "ApplicationAppVersionEventBuilder":
        self._application_app_version_event.events = events
        return self

    def status(self, status: int) -> "ApplicationAppVersionEventBuilder":
        self._application_app_version_event.status = status
        return self

    def create_time(self, create_time: int) -> "ApplicationAppVersionEventBuilder":
        self._application_app_version_event.create_time = create_time
        return self

    def publish_time(self, publish_time: int) -> "ApplicationAppVersionEventBuilder":
        self._application_app_version_event.publish_time = publish_time
        return self

    def ability(self, ability: AppAbility) -> "ApplicationAppVersionEventBuilder":
        self._application_app_version_event.ability = ability
        return self

    def remark(self, remark: AppVersionRemarkEvent) -> "ApplicationAppVersionEventBuilder":
        self._application_app_version_event.remark = remark
        return self

    def build(self) -> "ApplicationAppVersionEvent":
        return self._application_app_version_event
