# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_folder_file_response_body import CreateFolderFileResponseBody


class CreateFolderFileResponse(BaseResponse):
    _types = {
        "data": CreateFolderFileResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateFolderFileResponseBody] = None
        init(self, d, self._types)
