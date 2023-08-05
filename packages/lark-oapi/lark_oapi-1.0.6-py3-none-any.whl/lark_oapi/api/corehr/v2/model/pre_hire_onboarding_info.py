# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .onboarding_task import OnboardingTask


class PreHireOnboardingInfo(object):
    _types = {
        "offer_id": str,
        "offer_hr_id": str,
        "entry_mode": str,
        "onboarding_date": str,
        "ats_application_id": str,
        "recruitment_type": str,
        "onboarding_location_id": str,
        "company_sponsored_visa": bool,
        "onboarding_status": bool,
        "onboarding_task_list": List[OnboardingTask],
    }

    def __init__(self, d=None):
        self.offer_id: Optional[str] = None
        self.offer_hr_id: Optional[str] = None
        self.entry_mode: Optional[str] = None
        self.onboarding_date: Optional[str] = None
        self.ats_application_id: Optional[str] = None
        self.recruitment_type: Optional[str] = None
        self.onboarding_location_id: Optional[str] = None
        self.company_sponsored_visa: Optional[bool] = None
        self.onboarding_status: Optional[bool] = None
        self.onboarding_task_list: Optional[List[OnboardingTask]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PreHireOnboardingInfoBuilder":
        return PreHireOnboardingInfoBuilder()


class PreHireOnboardingInfoBuilder(object):
    def __init__(self) -> None:
        self._pre_hire_onboarding_info = PreHireOnboardingInfo()

    def offer_id(self, offer_id: str) -> "PreHireOnboardingInfoBuilder":
        self._pre_hire_onboarding_info.offer_id = offer_id
        return self

    def offer_hr_id(self, offer_hr_id: str) -> "PreHireOnboardingInfoBuilder":
        self._pre_hire_onboarding_info.offer_hr_id = offer_hr_id
        return self

    def entry_mode(self, entry_mode: str) -> "PreHireOnboardingInfoBuilder":
        self._pre_hire_onboarding_info.entry_mode = entry_mode
        return self

    def onboarding_date(self, onboarding_date: str) -> "PreHireOnboardingInfoBuilder":
        self._pre_hire_onboarding_info.onboarding_date = onboarding_date
        return self

    def ats_application_id(self, ats_application_id: str) -> "PreHireOnboardingInfoBuilder":
        self._pre_hire_onboarding_info.ats_application_id = ats_application_id
        return self

    def recruitment_type(self, recruitment_type: str) -> "PreHireOnboardingInfoBuilder":
        self._pre_hire_onboarding_info.recruitment_type = recruitment_type
        return self

    def onboarding_location_id(self, onboarding_location_id: str) -> "PreHireOnboardingInfoBuilder":
        self._pre_hire_onboarding_info.onboarding_location_id = onboarding_location_id
        return self

    def company_sponsored_visa(self, company_sponsored_visa: bool) -> "PreHireOnboardingInfoBuilder":
        self._pre_hire_onboarding_info.company_sponsored_visa = company_sponsored_visa
        return self

    def onboarding_status(self, onboarding_status: bool) -> "PreHireOnboardingInfoBuilder":
        self._pre_hire_onboarding_info.onboarding_status = onboarding_status
        return self

    def onboarding_task_list(self, onboarding_task_list: List[OnboardingTask]) -> "PreHireOnboardingInfoBuilder":
        self._pre_hire_onboarding_info.onboarding_task_list = onboarding_task_list
        return self

    def build(self) -> "PreHireOnboardingInfo":
        return self._pre_hire_onboarding_info
