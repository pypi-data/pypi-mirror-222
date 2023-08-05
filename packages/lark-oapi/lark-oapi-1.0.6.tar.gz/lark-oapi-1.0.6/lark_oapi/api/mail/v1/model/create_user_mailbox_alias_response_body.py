# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .email_alias import EmailAlias


class CreateUserMailboxAliasResponseBody(object):
    _types = {
        "user_mailbox_alias": EmailAlias,
    }

    def __init__(self, d=None):
        self.user_mailbox_alias: Optional[EmailAlias] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateUserMailboxAliasResponseBodyBuilder":
        return CreateUserMailboxAliasResponseBodyBuilder()


class CreateUserMailboxAliasResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_user_mailbox_alias_response_body = CreateUserMailboxAliasResponseBody()

    def user_mailbox_alias(self, user_mailbox_alias: EmailAlias) -> "CreateUserMailboxAliasResponseBodyBuilder":
        self._create_user_mailbox_alias_response_body.user_mailbox_alias = user_mailbox_alias
        return self

    def build(self) -> "CreateUserMailboxAliasResponseBody":
        return self._create_user_mailbox_alias_response_body
