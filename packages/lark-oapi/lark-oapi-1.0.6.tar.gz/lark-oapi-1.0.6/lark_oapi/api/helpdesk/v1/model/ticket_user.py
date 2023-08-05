# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class TicketUser(object):
    _types = {
        "id": str,
        "avatar_url": str,
        "name": str,
        "email": str,
        "department": str,
        "city": str,
        "country": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.avatar_url: Optional[str] = None
        self.name: Optional[str] = None
        self.email: Optional[str] = None
        self.department: Optional[str] = None
        self.city: Optional[str] = None
        self.country: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TicketUserBuilder":
        return TicketUserBuilder()


class TicketUserBuilder(object):
    def __init__(self) -> None:
        self._ticket_user = TicketUser()

    def id(self, id: str) -> "TicketUserBuilder":
        self._ticket_user.id = id
        return self

    def avatar_url(self, avatar_url: str) -> "TicketUserBuilder":
        self._ticket_user.avatar_url = avatar_url
        return self

    def name(self, name: str) -> "TicketUserBuilder":
        self._ticket_user.name = name
        return self

    def email(self, email: str) -> "TicketUserBuilder":
        self._ticket_user.email = email
        return self

    def department(self, department: str) -> "TicketUserBuilder":
        self._ticket_user.department = department
        return self

    def city(self, city: str) -> "TicketUserBuilder":
        self._ticket_user.city = city
        return self

    def country(self, country: str) -> "TicketUserBuilder":
        self._ticket_user.country = country
        return self

    def build(self) -> "TicketUser":
        return self._ticket_user
