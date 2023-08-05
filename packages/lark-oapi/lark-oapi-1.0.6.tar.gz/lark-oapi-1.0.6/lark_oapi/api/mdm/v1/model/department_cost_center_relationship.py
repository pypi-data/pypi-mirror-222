# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class DepartmentCostCenterRelationship(object):
    _types = {
        "department_cost_center_relationship_uid": str,
        "company_code": str,
        "open_department_id": str,
        "cost_center_code": str,
        "department_id": str,
    }

    def __init__(self, d=None):
        self.department_cost_center_relationship_uid: Optional[str] = None
        self.company_code: Optional[str] = None
        self.open_department_id: Optional[str] = None
        self.cost_center_code: Optional[str] = None
        self.department_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DepartmentCostCenterRelationshipBuilder":
        return DepartmentCostCenterRelationshipBuilder()


class DepartmentCostCenterRelationshipBuilder(object):
    def __init__(self) -> None:
        self._department_cost_center_relationship = DepartmentCostCenterRelationship()

    def department_cost_center_relationship_uid(self,
                                                department_cost_center_relationship_uid: str) -> "DepartmentCostCenterRelationshipBuilder":
        self._department_cost_center_relationship.department_cost_center_relationship_uid = department_cost_center_relationship_uid
        return self

    def company_code(self, company_code: str) -> "DepartmentCostCenterRelationshipBuilder":
        self._department_cost_center_relationship.company_code = company_code
        return self

    def open_department_id(self, open_department_id: str) -> "DepartmentCostCenterRelationshipBuilder":
        self._department_cost_center_relationship.open_department_id = open_department_id
        return self

    def cost_center_code(self, cost_center_code: str) -> "DepartmentCostCenterRelationshipBuilder":
        self._department_cost_center_relationship.cost_center_code = cost_center_code
        return self

    def department_id(self, department_id: str) -> "DepartmentCostCenterRelationshipBuilder":
        self._department_cost_center_relationship.department_id = department_id
        return self

    def build(self) -> "DepartmentCostCenterRelationship":
        return self._department_cost_center_relationship
