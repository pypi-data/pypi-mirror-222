# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_chat_members_request import CreateChatMembersRequest
from ..model.create_chat_members_response import CreateChatMembersResponse
from ..model.delete_chat_members_request import DeleteChatMembersRequest
from ..model.delete_chat_members_response import DeleteChatMembersResponse
from ..model.get_chat_members_request import GetChatMembersRequest
from ..model.get_chat_members_response import GetChatMembersResponse
from ..model.is_in_chat_chat_members_request import IsInChatChatMembersRequest
from ..model.is_in_chat_chat_members_response import IsInChatChatMembersResponse
from ..model.me_join_chat_members_request import MeJoinChatMembersRequest
from ..model.me_join_chat_members_response import MeJoinChatMembersResponse


class ChatMembers(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateChatMembersRequest,
               option: Optional[RequestOption] = None) -> CreateChatMembersResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateChatMembersResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateChatMembersResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteChatMembersRequest,
               option: Optional[RequestOption] = None) -> DeleteChatMembersResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteChatMembersResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteChatMembersResponse)
        response.raw = resp

        return response

    def get(self, request: GetChatMembersRequest, option: Optional[RequestOption] = None) -> GetChatMembersResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetChatMembersResponse = JSON.unmarshal(str(resp.content, UTF_8), GetChatMembersResponse)
        response.raw = resp

        return response

    def is_in_chat(self, request: IsInChatChatMembersRequest,
                   option: Optional[RequestOption] = None) -> IsInChatChatMembersResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: IsInChatChatMembersResponse = JSON.unmarshal(str(resp.content, UTF_8), IsInChatChatMembersResponse)
        response.raw = resp

        return response

    def me_join(self, request: MeJoinChatMembersRequest,
                option: Optional[RequestOption] = None) -> MeJoinChatMembersResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: MeJoinChatMembersResponse = JSON.unmarshal(str(resp.content, UTF_8), MeJoinChatMembersResponse)
        response.raw = resp

        return response
