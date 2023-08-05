# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .appli_offer_basic_info_user import AppliOfferBasicInfoUser


class ApplicationPrehireOfferBasic(object):
    _types = {
        "offer_id": str,
        "application_id": str,
        "talent_id": str,
        "job_id": str,
        "remark": str,
        "expire_time": int,
        "onboard_time": int,
        "time_zone": str,
        "offer_type": int,
        "offer_status": int,
        "owner": AppliOfferBasicInfoUser,
        "offer_job_title": str,
    }

    def __init__(self, d=None):
        self.offer_id: Optional[str] = None
        self.application_id: Optional[str] = None
        self.talent_id: Optional[str] = None
        self.job_id: Optional[str] = None
        self.remark: Optional[str] = None
        self.expire_time: Optional[int] = None
        self.onboard_time: Optional[int] = None
        self.time_zone: Optional[str] = None
        self.offer_type: Optional[int] = None
        self.offer_status: Optional[int] = None
        self.owner: Optional[AppliOfferBasicInfoUser] = None
        self.offer_job_title: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApplicationPrehireOfferBasicBuilder":
        return ApplicationPrehireOfferBasicBuilder()


class ApplicationPrehireOfferBasicBuilder(object):
    def __init__(self) -> None:
        self._application_prehire_offer_basic = ApplicationPrehireOfferBasic()

    def offer_id(self, offer_id: str) -> "ApplicationPrehireOfferBasicBuilder":
        self._application_prehire_offer_basic.offer_id = offer_id
        return self

    def application_id(self, application_id: str) -> "ApplicationPrehireOfferBasicBuilder":
        self._application_prehire_offer_basic.application_id = application_id
        return self

    def talent_id(self, talent_id: str) -> "ApplicationPrehireOfferBasicBuilder":
        self._application_prehire_offer_basic.talent_id = talent_id
        return self

    def job_id(self, job_id: str) -> "ApplicationPrehireOfferBasicBuilder":
        self._application_prehire_offer_basic.job_id = job_id
        return self

    def remark(self, remark: str) -> "ApplicationPrehireOfferBasicBuilder":
        self._application_prehire_offer_basic.remark = remark
        return self

    def expire_time(self, expire_time: int) -> "ApplicationPrehireOfferBasicBuilder":
        self._application_prehire_offer_basic.expire_time = expire_time
        return self

    def onboard_time(self, onboard_time: int) -> "ApplicationPrehireOfferBasicBuilder":
        self._application_prehire_offer_basic.onboard_time = onboard_time
        return self

    def time_zone(self, time_zone: str) -> "ApplicationPrehireOfferBasicBuilder":
        self._application_prehire_offer_basic.time_zone = time_zone
        return self

    def offer_type(self, offer_type: int) -> "ApplicationPrehireOfferBasicBuilder":
        self._application_prehire_offer_basic.offer_type = offer_type
        return self

    def offer_status(self, offer_status: int) -> "ApplicationPrehireOfferBasicBuilder":
        self._application_prehire_offer_basic.offer_status = offer_status
        return self

    def owner(self, owner: AppliOfferBasicInfoUser) -> "ApplicationPrehireOfferBasicBuilder":
        self._application_prehire_offer_basic.owner = owner
        return self

    def offer_job_title(self, offer_job_title: str) -> "ApplicationPrehireOfferBasicBuilder":
        self._application_prehire_offer_basic.offer_job_title = offer_job_title
        return self

    def build(self) -> "ApplicationPrehireOfferBasic":
        return self._application_prehire_offer_basic
