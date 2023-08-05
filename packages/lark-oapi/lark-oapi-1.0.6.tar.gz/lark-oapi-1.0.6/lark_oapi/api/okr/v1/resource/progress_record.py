# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_progress_record_request import CreateProgressRecordRequest
from ..model.create_progress_record_response import CreateProgressRecordResponse
from ..model.delete_progress_record_request import DeleteProgressRecordRequest
from ..model.delete_progress_record_response import DeleteProgressRecordResponse
from ..model.get_progress_record_request import GetProgressRecordRequest
from ..model.get_progress_record_response import GetProgressRecordResponse
from ..model.update_progress_record_request import UpdateProgressRecordRequest
from ..model.update_progress_record_response import UpdateProgressRecordResponse


class ProgressRecord(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateProgressRecordRequest,
               option: Optional[RequestOption] = None) -> CreateProgressRecordResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateProgressRecordResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateProgressRecordResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteProgressRecordRequest,
               option: Optional[RequestOption] = None) -> DeleteProgressRecordResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteProgressRecordResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteProgressRecordResponse)
        response.raw = resp

        return response

    def get(self, request: GetProgressRecordRequest,
            option: Optional[RequestOption] = None) -> GetProgressRecordResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetProgressRecordResponse = JSON.unmarshal(str(resp.content, UTF_8), GetProgressRecordResponse)
        response.raw = resp

        return response

    def update(self, request: UpdateProgressRecordRequest,
               option: Optional[RequestOption] = None) -> UpdateProgressRecordResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: UpdateProgressRecordResponse = JSON.unmarshal(str(resp.content, UTF_8), UpdateProgressRecordResponse)
        response.raw = resp

        return response
