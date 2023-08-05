# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .custom_field_data import CustomFieldData
from .enum import Enum
from .i18n import I18n


class Education(object):
    _types = {
        "school": List[I18n],
        "level_of_education": Enum,
        "start_date": str,
        "end_date": str,
        "field_of_study": List[I18n],
        "degree": Enum,
        "school_name": Enum,
        "field_of_study_name": Enum,
        "country_region_id": str,
        "expected_end_date": str,
        "custom_fields": List[CustomFieldData],
    }

    def __init__(self, d=None):
        self.school: Optional[List[I18n]] = None
        self.level_of_education: Optional[Enum] = None
        self.start_date: Optional[str] = None
        self.end_date: Optional[str] = None
        self.field_of_study: Optional[List[I18n]] = None
        self.degree: Optional[Enum] = None
        self.school_name: Optional[Enum] = None
        self.field_of_study_name: Optional[Enum] = None
        self.country_region_id: Optional[str] = None
        self.expected_end_date: Optional[str] = None
        self.custom_fields: Optional[List[CustomFieldData]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EducationBuilder":
        return EducationBuilder()


class EducationBuilder(object):
    def __init__(self) -> None:
        self._education = Education()

    def school(self, school: List[I18n]) -> "EducationBuilder":
        self._education.school = school
        return self

    def level_of_education(self, level_of_education: Enum) -> "EducationBuilder":
        self._education.level_of_education = level_of_education
        return self

    def start_date(self, start_date: str) -> "EducationBuilder":
        self._education.start_date = start_date
        return self

    def end_date(self, end_date: str) -> "EducationBuilder":
        self._education.end_date = end_date
        return self

    def field_of_study(self, field_of_study: List[I18n]) -> "EducationBuilder":
        self._education.field_of_study = field_of_study
        return self

    def degree(self, degree: Enum) -> "EducationBuilder":
        self._education.degree = degree
        return self

    def school_name(self, school_name: Enum) -> "EducationBuilder":
        self._education.school_name = school_name
        return self

    def field_of_study_name(self, field_of_study_name: Enum) -> "EducationBuilder":
        self._education.field_of_study_name = field_of_study_name
        return self

    def country_region_id(self, country_region_id: str) -> "EducationBuilder":
        self._education.country_region_id = country_region_id
        return self

    def expected_end_date(self, expected_end_date: str) -> "EducationBuilder":
        self._education.expected_end_date = expected_end_date
        return self

    def custom_fields(self, custom_fields: List[CustomFieldData]) -> "EducationBuilder":
        self._education.custom_fields = custom_fields
        return self

    def build(self) -> "Education":
        return self._education
