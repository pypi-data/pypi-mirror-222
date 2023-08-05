# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .enum import Enum
from .object_field_data import ObjectFieldData
from .person_name import PersonName
from .phone import Phone


class EmergencyContact(object):
    _types = {
        "name": PersonName,
        "relationship": Enum,
        "phone_ist": List[Phone],
        "custom_fields": List[ObjectFieldData],
        "legal_name": str,
    }

    def __init__(self, d=None):
        self.name: Optional[PersonName] = None
        self.relationship: Optional[Enum] = None
        self.phone_ist: Optional[List[Phone]] = None
        self.custom_fields: Optional[List[ObjectFieldData]] = None
        self.legal_name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EmergencyContactBuilder":
        return EmergencyContactBuilder()


class EmergencyContactBuilder(object):
    def __init__(self) -> None:
        self._emergency_contact = EmergencyContact()

    def name(self, name: PersonName) -> "EmergencyContactBuilder":
        self._emergency_contact.name = name
        return self

    def relationship(self, relationship: Enum) -> "EmergencyContactBuilder":
        self._emergency_contact.relationship = relationship
        return self

    def phone_ist(self, phone_ist: List[Phone]) -> "EmergencyContactBuilder":
        self._emergency_contact.phone_ist = phone_ist
        return self

    def custom_fields(self, custom_fields: List[ObjectFieldData]) -> "EmergencyContactBuilder":
        self._emergency_contact.custom_fields = custom_fields
        return self

    def legal_name(self, legal_name: str) -> "EmergencyContactBuilder":
        self._emergency_contact.legal_name = legal_name
        return self

    def build(self) -> "EmergencyContact":
        return self._emergency_contact
