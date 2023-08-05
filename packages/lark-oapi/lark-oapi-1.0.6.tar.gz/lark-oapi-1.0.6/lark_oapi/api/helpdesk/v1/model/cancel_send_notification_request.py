# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .cancel_send_notification_request_body import CancelSendNotificationRequestBody


class CancelSendNotificationRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.notification_id: Optional[str] = None
        self.request_body: Optional[CancelSendNotificationRequestBody] = None

    @staticmethod
    def builder() -> "CancelSendNotificationRequestBuilder":
        return CancelSendNotificationRequestBuilder()


class CancelSendNotificationRequestBuilder(object):

    def __init__(self) -> None:
        cancel_send_notification_request = CancelSendNotificationRequest()
        cancel_send_notification_request.http_method = HttpMethod.POST
        cancel_send_notification_request.uri = "/open-apis/helpdesk/v1/notifications/:notification_id/cancel_send"
        cancel_send_notification_request.token_types = {AccessTokenType.USER}
        self._cancel_send_notification_request: CancelSendNotificationRequest = cancel_send_notification_request

    def notification_id(self, notification_id: str) -> "CancelSendNotificationRequestBuilder":
        self._cancel_send_notification_request.notification_id = notification_id
        self._cancel_send_notification_request.paths["notification_id"] = str(notification_id)
        return self

    def request_body(self, request_body: CancelSendNotificationRequestBody) -> "CancelSendNotificationRequestBuilder":
        self._cancel_send_notification_request.request_body = request_body
        self._cancel_send_notification_request.body = request_body
        return self

    def build(self) -> CancelSendNotificationRequest:
        return self._cancel_send_notification_request
