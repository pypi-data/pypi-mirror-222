# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .address import Address
from .custom_field_data import CustomFieldData
from .enum import Enum
from .file import File
from .national_id import NationalId
from .person_name import PersonName
from .phone import Phone


class Dependent(object):
    _types = {
        "name": PersonName,
        "relationship": Enum,
        "gender": Enum,
        "date_of_birth": str,
        "national_id_list": List[NationalId],
        "spouses_working_status": Enum,
        "is_this_person_covered_by_health_insurance": bool,
        "is_this_person_allowed_for_tax_deduction": bool,
        "custom_fields": List[CustomFieldData],
        "dependent_name": str,
        "employer": str,
        "job": str,
        "phone": Phone,
        "address": Address,
        "birth_certificate_of_child": List[File],
    }

    def __init__(self, d=None):
        self.name: Optional[PersonName] = None
        self.relationship: Optional[Enum] = None
        self.gender: Optional[Enum] = None
        self.date_of_birth: Optional[str] = None
        self.national_id_list: Optional[List[NationalId]] = None
        self.spouses_working_status: Optional[Enum] = None
        self.is_this_person_covered_by_health_insurance: Optional[bool] = None
        self.is_this_person_allowed_for_tax_deduction: Optional[bool] = None
        self.custom_fields: Optional[List[CustomFieldData]] = None
        self.dependent_name: Optional[str] = None
        self.employer: Optional[str] = None
        self.job: Optional[str] = None
        self.phone: Optional[Phone] = None
        self.address: Optional[Address] = None
        self.birth_certificate_of_child: Optional[List[File]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DependentBuilder":
        return DependentBuilder()


class DependentBuilder(object):
    def __init__(self) -> None:
        self._dependent = Dependent()

    def name(self, name: PersonName) -> "DependentBuilder":
        self._dependent.name = name
        return self

    def relationship(self, relationship: Enum) -> "DependentBuilder":
        self._dependent.relationship = relationship
        return self

    def gender(self, gender: Enum) -> "DependentBuilder":
        self._dependent.gender = gender
        return self

    def date_of_birth(self, date_of_birth: str) -> "DependentBuilder":
        self._dependent.date_of_birth = date_of_birth
        return self

    def national_id_list(self, national_id_list: List[NationalId]) -> "DependentBuilder":
        self._dependent.national_id_list = national_id_list
        return self

    def spouses_working_status(self, spouses_working_status: Enum) -> "DependentBuilder":
        self._dependent.spouses_working_status = spouses_working_status
        return self

    def is_this_person_covered_by_health_insurance(self,
                                                   is_this_person_covered_by_health_insurance: bool) -> "DependentBuilder":
        self._dependent.is_this_person_covered_by_health_insurance = is_this_person_covered_by_health_insurance
        return self

    def is_this_person_allowed_for_tax_deduction(self,
                                                 is_this_person_allowed_for_tax_deduction: bool) -> "DependentBuilder":
        self._dependent.is_this_person_allowed_for_tax_deduction = is_this_person_allowed_for_tax_deduction
        return self

    def custom_fields(self, custom_fields: List[CustomFieldData]) -> "DependentBuilder":
        self._dependent.custom_fields = custom_fields
        return self

    def dependent_name(self, dependent_name: str) -> "DependentBuilder":
        self._dependent.dependent_name = dependent_name
        return self

    def employer(self, employer: str) -> "DependentBuilder":
        self._dependent.employer = employer
        return self

    def job(self, job: str) -> "DependentBuilder":
        self._dependent.job = job
        return self

    def phone(self, phone: Phone) -> "DependentBuilder":
        self._dependent.phone = phone
        return self

    def address(self, address: Address) -> "DependentBuilder":
        self._dependent.address = address
        return self

    def birth_certificate_of_child(self, birth_certificate_of_child: List[File]) -> "DependentBuilder":
        self._dependent.birth_certificate_of_child = birth_certificate_of_child
        return self

    def build(self) -> "Dependent":
        return self._dependent
