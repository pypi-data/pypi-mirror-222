# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .move_docs_to_wiki_space_node_response_body import MoveDocsToWikiSpaceNodeResponseBody


class MoveDocsToWikiSpaceNodeResponse(BaseResponse):
    _types = {
        "data": MoveDocsToWikiSpaceNodeResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[MoveDocsToWikiSpaceNodeResponseBody] = None
        init(self, d, self._types)
