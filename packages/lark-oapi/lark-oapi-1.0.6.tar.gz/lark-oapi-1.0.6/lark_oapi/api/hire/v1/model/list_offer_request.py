# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListOfferRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None
        self.talent_id: Optional[str] = None
        self.user_id_type: Optional[str] = None

    @staticmethod
    def builder() -> "ListOfferRequestBuilder":
        return ListOfferRequestBuilder()


class ListOfferRequestBuilder(object):

    def __init__(self) -> None:
        list_offer_request = ListOfferRequest()
        list_offer_request.http_method = HttpMethod.GET
        list_offer_request.uri = "/open-apis/hire/v1/offers"
        list_offer_request.token_types = {AccessTokenType.TENANT}
        self._list_offer_request: ListOfferRequest = list_offer_request

    def page_token(self, page_token: str) -> "ListOfferRequestBuilder":
        self._list_offer_request.page_token = page_token
        self._list_offer_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: int) -> "ListOfferRequestBuilder":
        self._list_offer_request.page_size = page_size
        self._list_offer_request.add_query("page_size", page_size)
        return self

    def talent_id(self, talent_id: str) -> "ListOfferRequestBuilder":
        self._list_offer_request.talent_id = talent_id
        self._list_offer_request.add_query("talent_id", talent_id)
        return self

    def user_id_type(self, user_id_type: str) -> "ListOfferRequestBuilder":
        self._list_offer_request.user_id_type = user_id_type
        self._list_offer_request.add_query("user_id_type", user_id_type)
        return self

    def build(self) -> ListOfferRequest:
        return self._list_offer_request
