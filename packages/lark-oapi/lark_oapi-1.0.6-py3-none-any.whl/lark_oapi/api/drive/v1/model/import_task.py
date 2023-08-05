# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .import_task_mount_point import ImportTaskMountPoint


class ImportTask(object):
    _types = {
        "ticket": str,
        "file_extension": str,
        "file_token": str,
        "type": str,
        "file_name": str,
        "point": ImportTaskMountPoint,
        "job_status": int,
        "job_error_msg": str,
        "token": str,
        "url": str,
        "extra": List[str],
    }

    def __init__(self, d=None):
        self.ticket: Optional[str] = None
        self.file_extension: Optional[str] = None
        self.file_token: Optional[str] = None
        self.type: Optional[str] = None
        self.file_name: Optional[str] = None
        self.point: Optional[ImportTaskMountPoint] = None
        self.job_status: Optional[int] = None
        self.job_error_msg: Optional[str] = None
        self.token: Optional[str] = None
        self.url: Optional[str] = None
        self.extra: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ImportTaskBuilder":
        return ImportTaskBuilder()


class ImportTaskBuilder(object):
    def __init__(self) -> None:
        self._import_task = ImportTask()

    def ticket(self, ticket: str) -> "ImportTaskBuilder":
        self._import_task.ticket = ticket
        return self

    def file_extension(self, file_extension: str) -> "ImportTaskBuilder":
        self._import_task.file_extension = file_extension
        return self

    def file_token(self, file_token: str) -> "ImportTaskBuilder":
        self._import_task.file_token = file_token
        return self

    def type(self, type: str) -> "ImportTaskBuilder":
        self._import_task.type = type
        return self

    def file_name(self, file_name: str) -> "ImportTaskBuilder":
        self._import_task.file_name = file_name
        return self

    def point(self, point: ImportTaskMountPoint) -> "ImportTaskBuilder":
        self._import_task.point = point
        return self

    def job_status(self, job_status: int) -> "ImportTaskBuilder":
        self._import_task.job_status = job_status
        return self

    def job_error_msg(self, job_error_msg: str) -> "ImportTaskBuilder":
        self._import_task.job_error_msg = job_error_msg
        return self

    def token(self, token: str) -> "ImportTaskBuilder":
        self._import_task.token = token
        return self

    def url(self, url: str) -> "ImportTaskBuilder":
        self._import_task.url = url
        return self

    def extra(self, extra: List[str]) -> "ImportTaskBuilder":
        self._import_task.extra = extra
        return self

    def build(self) -> "ImportTask":
        return self._import_task
