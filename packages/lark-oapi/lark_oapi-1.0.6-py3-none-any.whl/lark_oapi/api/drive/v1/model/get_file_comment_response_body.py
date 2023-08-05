# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .reply_list import ReplyList


class GetFileCommentResponseBody(object):
    _types = {
        "comment_id": str,
        "user_id": str,
        "create_time": int,
        "update_time": int,
        "is_solved": bool,
        "solved_time": int,
        "solver_user_id": str,
        "has_more": bool,
        "page_token": str,
        "is_whole": bool,
        "quote": str,
        "reply_list": ReplyList,
    }

    def __init__(self, d=None):
        self.comment_id: Optional[str] = None
        self.user_id: Optional[str] = None
        self.create_time: Optional[int] = None
        self.update_time: Optional[int] = None
        self.is_solved: Optional[bool] = None
        self.solved_time: Optional[int] = None
        self.solver_user_id: Optional[str] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        self.is_whole: Optional[bool] = None
        self.quote: Optional[str] = None
        self.reply_list: Optional[ReplyList] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetFileCommentResponseBodyBuilder":
        return GetFileCommentResponseBodyBuilder()


class GetFileCommentResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_file_comment_response_body = GetFileCommentResponseBody()

    def comment_id(self, comment_id: str) -> "GetFileCommentResponseBodyBuilder":
        self._get_file_comment_response_body.comment_id = comment_id
        return self

    def user_id(self, user_id: str) -> "GetFileCommentResponseBodyBuilder":
        self._get_file_comment_response_body.user_id = user_id
        return self

    def create_time(self, create_time: int) -> "GetFileCommentResponseBodyBuilder":
        self._get_file_comment_response_body.create_time = create_time
        return self

    def update_time(self, update_time: int) -> "GetFileCommentResponseBodyBuilder":
        self._get_file_comment_response_body.update_time = update_time
        return self

    def is_solved(self, is_solved: bool) -> "GetFileCommentResponseBodyBuilder":
        self._get_file_comment_response_body.is_solved = is_solved
        return self

    def solved_time(self, solved_time: int) -> "GetFileCommentResponseBodyBuilder":
        self._get_file_comment_response_body.solved_time = solved_time
        return self

    def solver_user_id(self, solver_user_id: str) -> "GetFileCommentResponseBodyBuilder":
        self._get_file_comment_response_body.solver_user_id = solver_user_id
        return self

    def has_more(self, has_more: bool) -> "GetFileCommentResponseBodyBuilder":
        self._get_file_comment_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "GetFileCommentResponseBodyBuilder":
        self._get_file_comment_response_body.page_token = page_token
        return self

    def is_whole(self, is_whole: bool) -> "GetFileCommentResponseBodyBuilder":
        self._get_file_comment_response_body.is_whole = is_whole
        return self

    def quote(self, quote: str) -> "GetFileCommentResponseBodyBuilder":
        self._get_file_comment_response_body.quote = quote
        return self

    def reply_list(self, reply_list: ReplyList) -> "GetFileCommentResponseBodyBuilder":
        self._get_file_comment_response_body.reply_list = reply_list
        return self

    def build(self) -> "GetFileCommentResponseBody":
        return self._get_file_comment_response_body
