# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CreateAgentSkillResponseBody(object):
    _types = {
        "agent_skill_id": str,
    }

    def __init__(self, d=None):
        self.agent_skill_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateAgentSkillResponseBodyBuilder":
        return CreateAgentSkillResponseBodyBuilder()


class CreateAgentSkillResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_agent_skill_response_body = CreateAgentSkillResponseBody()

    def agent_skill_id(self, agent_skill_id: str) -> "CreateAgentSkillResponseBodyBuilder":
        self._create_agent_skill_response_body.agent_skill_id = agent_skill_id
        return self

    def build(self) -> "CreateAgentSkillResponseBody":
        return self._create_agent_skill_response_body
