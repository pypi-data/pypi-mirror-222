# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .application_offer_custom_value import ApplicationOfferCustomValue
from .base_address import BaseAddress
from .base_bilingual_with_id import BaseBilingualWithId


class ApplicationOfferBasicInfo(object):
    _types = {
        "offer_type": int,
        "remark": str,
        "expire_time": int,
        "owner_user_id": str,
        "creator_user_id": str,
        "employee_type": BaseBilingualWithId,
        "create_time": str,
        "leader_user_id": str,
        "onboard_date": str,
        "department_id": str,
        "probation_month": int,
        "contract_year": int,
        "recruitment_type": BaseBilingualWithId,
        "sequence": BaseBilingualWithId,
        "level": BaseBilingualWithId,
        "onboard_address": BaseAddress,
        "work_address": BaseAddress,
        "customize_info_list": List[ApplicationOfferCustomValue],
    }

    def __init__(self, d=None):
        self.offer_type: Optional[int] = None
        self.remark: Optional[str] = None
        self.expire_time: Optional[int] = None
        self.owner_user_id: Optional[str] = None
        self.creator_user_id: Optional[str] = None
        self.employee_type: Optional[BaseBilingualWithId] = None
        self.create_time: Optional[str] = None
        self.leader_user_id: Optional[str] = None
        self.onboard_date: Optional[str] = None
        self.department_id: Optional[str] = None
        self.probation_month: Optional[int] = None
        self.contract_year: Optional[int] = None
        self.recruitment_type: Optional[BaseBilingualWithId] = None
        self.sequence: Optional[BaseBilingualWithId] = None
        self.level: Optional[BaseBilingualWithId] = None
        self.onboard_address: Optional[BaseAddress] = None
        self.work_address: Optional[BaseAddress] = None
        self.customize_info_list: Optional[List[ApplicationOfferCustomValue]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApplicationOfferBasicInfoBuilder":
        return ApplicationOfferBasicInfoBuilder()


class ApplicationOfferBasicInfoBuilder(object):
    def __init__(self) -> None:
        self._application_offer_basic_info = ApplicationOfferBasicInfo()

    def offer_type(self, offer_type: int) -> "ApplicationOfferBasicInfoBuilder":
        self._application_offer_basic_info.offer_type = offer_type
        return self

    def remark(self, remark: str) -> "ApplicationOfferBasicInfoBuilder":
        self._application_offer_basic_info.remark = remark
        return self

    def expire_time(self, expire_time: int) -> "ApplicationOfferBasicInfoBuilder":
        self._application_offer_basic_info.expire_time = expire_time
        return self

    def owner_user_id(self, owner_user_id: str) -> "ApplicationOfferBasicInfoBuilder":
        self._application_offer_basic_info.owner_user_id = owner_user_id
        return self

    def creator_user_id(self, creator_user_id: str) -> "ApplicationOfferBasicInfoBuilder":
        self._application_offer_basic_info.creator_user_id = creator_user_id
        return self

    def employee_type(self, employee_type: BaseBilingualWithId) -> "ApplicationOfferBasicInfoBuilder":
        self._application_offer_basic_info.employee_type = employee_type
        return self

    def create_time(self, create_time: str) -> "ApplicationOfferBasicInfoBuilder":
        self._application_offer_basic_info.create_time = create_time
        return self

    def leader_user_id(self, leader_user_id: str) -> "ApplicationOfferBasicInfoBuilder":
        self._application_offer_basic_info.leader_user_id = leader_user_id
        return self

    def onboard_date(self, onboard_date: str) -> "ApplicationOfferBasicInfoBuilder":
        self._application_offer_basic_info.onboard_date = onboard_date
        return self

    def department_id(self, department_id: str) -> "ApplicationOfferBasicInfoBuilder":
        self._application_offer_basic_info.department_id = department_id
        return self

    def probation_month(self, probation_month: int) -> "ApplicationOfferBasicInfoBuilder":
        self._application_offer_basic_info.probation_month = probation_month
        return self

    def contract_year(self, contract_year: int) -> "ApplicationOfferBasicInfoBuilder":
        self._application_offer_basic_info.contract_year = contract_year
        return self

    def recruitment_type(self, recruitment_type: BaseBilingualWithId) -> "ApplicationOfferBasicInfoBuilder":
        self._application_offer_basic_info.recruitment_type = recruitment_type
        return self

    def sequence(self, sequence: BaseBilingualWithId) -> "ApplicationOfferBasicInfoBuilder":
        self._application_offer_basic_info.sequence = sequence
        return self

    def level(self, level: BaseBilingualWithId) -> "ApplicationOfferBasicInfoBuilder":
        self._application_offer_basic_info.level = level
        return self

    def onboard_address(self, onboard_address: BaseAddress) -> "ApplicationOfferBasicInfoBuilder":
        self._application_offer_basic_info.onboard_address = onboard_address
        return self

    def work_address(self, work_address: BaseAddress) -> "ApplicationOfferBasicInfoBuilder":
        self._application_offer_basic_info.work_address = work_address
        return self

    def customize_info_list(self, customize_info_list: List[
        ApplicationOfferCustomValue]) -> "ApplicationOfferBasicInfoBuilder":
        self._application_offer_basic_info.customize_info_list = customize_info_list
        return self

    def build(self) -> "ApplicationOfferBasicInfo":
        return self._application_offer_basic_info
