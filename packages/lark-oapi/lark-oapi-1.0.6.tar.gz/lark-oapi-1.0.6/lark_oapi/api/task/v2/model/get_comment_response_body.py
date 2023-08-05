# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .comment import Comment


class GetCommentResponseBody(object):
    _types = {
        "comment": Comment,
    }

    def __init__(self, d=None):
        self.comment: Optional[Comment] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetCommentResponseBodyBuilder":
        return GetCommentResponseBodyBuilder()


class GetCommentResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_comment_response_body = GetCommentResponseBody()

    def comment(self, comment: Comment) -> "GetCommentResponseBodyBuilder":
        self._get_comment_response_body.comment = comment
        return self

    def build(self) -> "GetCommentResponseBody":
        return self._get_comment_response_body
