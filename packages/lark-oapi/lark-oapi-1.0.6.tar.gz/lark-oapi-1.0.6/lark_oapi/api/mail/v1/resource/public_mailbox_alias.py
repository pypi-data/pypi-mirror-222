# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_public_mailbox_alias_request import CreatePublicMailboxAliasRequest
from ..model.create_public_mailbox_alias_response import CreatePublicMailboxAliasResponse
from ..model.delete_public_mailbox_alias_request import DeletePublicMailboxAliasRequest
from ..model.delete_public_mailbox_alias_response import DeletePublicMailboxAliasResponse
from ..model.list_public_mailbox_alias_request import ListPublicMailboxAliasRequest
from ..model.list_public_mailbox_alias_response import ListPublicMailboxAliasResponse


class PublicMailboxAlias(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreatePublicMailboxAliasRequest,
               option: Optional[RequestOption] = None) -> CreatePublicMailboxAliasResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreatePublicMailboxAliasResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                    CreatePublicMailboxAliasResponse)
        response.raw = resp

        return response

    def delete(self, request: DeletePublicMailboxAliasRequest,
               option: Optional[RequestOption] = None) -> DeletePublicMailboxAliasResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeletePublicMailboxAliasResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                    DeletePublicMailboxAliasResponse)
        response.raw = resp

        return response

    def list(self, request: ListPublicMailboxAliasRequest,
             option: Optional[RequestOption] = None) -> ListPublicMailboxAliasResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListPublicMailboxAliasResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                  ListPublicMailboxAliasResponse)
        response.raw = resp

        return response
