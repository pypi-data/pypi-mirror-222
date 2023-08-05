# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .website_delivery_customized_data import WebsiteDeliveryCustomizedData


class WebsiteDeliverySelfEvaluation(object):
    _types = {
        "content": str,
        "customized_data": List[WebsiteDeliveryCustomizedData],
    }

    def __init__(self, d=None):
        self.content: Optional[str] = None
        self.customized_data: Optional[List[WebsiteDeliveryCustomizedData]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WebsiteDeliverySelfEvaluationBuilder":
        return WebsiteDeliverySelfEvaluationBuilder()


class WebsiteDeliverySelfEvaluationBuilder(object):
    def __init__(self) -> None:
        self._website_delivery_self_evaluation = WebsiteDeliverySelfEvaluation()

    def content(self, content: str) -> "WebsiteDeliverySelfEvaluationBuilder":
        self._website_delivery_self_evaluation.content = content
        return self

    def customized_data(self,
                        customized_data: List[WebsiteDeliveryCustomizedData]) -> "WebsiteDeliverySelfEvaluationBuilder":
        self._website_delivery_self_evaluation.customized_data = customized_data
        return self

    def build(self) -> "WebsiteDeliverySelfEvaluation":
        return self._website_delivery_self_evaluation
