# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .text_element_style import TextElementStyle


class Reminder(object):
    _types = {
        "create_user_id": str,
        "is_notify": bool,
        "is_whole_day": bool,
        "expire_time": int,
        "notify_time": int,
        "text_element_style": TextElementStyle,
    }

    def __init__(self, d=None):
        self.create_user_id: Optional[str] = None
        self.is_notify: Optional[bool] = None
        self.is_whole_day: Optional[bool] = None
        self.expire_time: Optional[int] = None
        self.notify_time: Optional[int] = None
        self.text_element_style: Optional[TextElementStyle] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ReminderBuilder":
        return ReminderBuilder()


class ReminderBuilder(object):
    def __init__(self) -> None:
        self._reminder = Reminder()

    def create_user_id(self, create_user_id: str) -> "ReminderBuilder":
        self._reminder.create_user_id = create_user_id
        return self

    def is_notify(self, is_notify: bool) -> "ReminderBuilder":
        self._reminder.is_notify = is_notify
        return self

    def is_whole_day(self, is_whole_day: bool) -> "ReminderBuilder":
        self._reminder.is_whole_day = is_whole_day
        return self

    def expire_time(self, expire_time: int) -> "ReminderBuilder":
        self._reminder.expire_time = expire_time
        return self

    def notify_time(self, notify_time: int) -> "ReminderBuilder":
        self._reminder.notify_time = notify_time
        return self

    def text_element_style(self, text_element_style: TextElementStyle) -> "ReminderBuilder":
        self._reminder.text_element_style = text_element_style
        return self

    def build(self) -> "Reminder":
        return self._reminder
