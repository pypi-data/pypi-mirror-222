# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListFileCommentRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.file_type: Optional[str] = None
        self.is_whole: Optional[bool] = None
        self.is_solved: Optional[bool] = None
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None
        self.user_id_type: Optional[str] = None
        self.file_token: Optional[str] = None

    @staticmethod
    def builder() -> "ListFileCommentRequestBuilder":
        return ListFileCommentRequestBuilder()


class ListFileCommentRequestBuilder(object):

    def __init__(self) -> None:
        list_file_comment_request = ListFileCommentRequest()
        list_file_comment_request.http_method = HttpMethod.GET
        list_file_comment_request.uri = "/open-apis/drive/v1/files/:file_token/comments"
        list_file_comment_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._list_file_comment_request: ListFileCommentRequest = list_file_comment_request

    def file_type(self, file_type: str) -> "ListFileCommentRequestBuilder":
        self._list_file_comment_request.file_type = file_type
        self._list_file_comment_request.add_query("file_type", file_type)
        return self

    def is_whole(self, is_whole: bool) -> "ListFileCommentRequestBuilder":
        self._list_file_comment_request.is_whole = is_whole
        self._list_file_comment_request.add_query("is_whole", is_whole)
        return self

    def is_solved(self, is_solved: bool) -> "ListFileCommentRequestBuilder":
        self._list_file_comment_request.is_solved = is_solved
        self._list_file_comment_request.add_query("is_solved", is_solved)
        return self

    def page_token(self, page_token: str) -> "ListFileCommentRequestBuilder":
        self._list_file_comment_request.page_token = page_token
        self._list_file_comment_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: int) -> "ListFileCommentRequestBuilder":
        self._list_file_comment_request.page_size = page_size
        self._list_file_comment_request.add_query("page_size", page_size)
        return self

    def user_id_type(self, user_id_type: str) -> "ListFileCommentRequestBuilder":
        self._list_file_comment_request.user_id_type = user_id_type
        self._list_file_comment_request.add_query("user_id_type", user_id_type)
        return self

    def file_token(self, file_token: str) -> "ListFileCommentRequestBuilder":
        self._list_file_comment_request.file_token = file_token
        self._list_file_comment_request.paths["file_token"] = str(file_token)
        return self

    def build(self) -> ListFileCommentRequest:
        return self._list_file_comment_request
