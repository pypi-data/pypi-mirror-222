# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .mailgroup_manager import MailgroupManager


class BatchCreateMailgroupManagerRequestBody(object):
    _types = {
        "mailgroup_manager_list": List[MailgroupManager],
    }

    def __init__(self, d=None):
        self.mailgroup_manager_list: Optional[List[MailgroupManager]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchCreateMailgroupManagerRequestBodyBuilder":
        return BatchCreateMailgroupManagerRequestBodyBuilder()


class BatchCreateMailgroupManagerRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._batch_create_mailgroup_manager_request_body = BatchCreateMailgroupManagerRequestBody()

    def mailgroup_manager_list(self, mailgroup_manager_list: List[
        MailgroupManager]) -> "BatchCreateMailgroupManagerRequestBodyBuilder":
        self._batch_create_mailgroup_manager_request_body.mailgroup_manager_list = mailgroup_manager_list
        return self

    def build(self) -> "BatchCreateMailgroupManagerRequestBody":
        return self._batch_create_mailgroup_manager_request_body
