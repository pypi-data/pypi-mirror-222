# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Participant(object):
    _types = {
        "participant_name": str,
        "department": str,
        "user_id": str,
        "employee_id": str,
        "phone": str,
        "email": str,
        "device": str,
        "app_version": str,
        "public_ip": str,
        "internal_ip": str,
        "use_rtc_proxy": bool,
        "location": str,
        "network_type": str,
        "protocol": str,
        "microphone": str,
        "speaker": str,
        "camera": str,
        "audio": bool,
        "video": bool,
        "sharing": bool,
        "join_time": str,
        "leave_time": str,
        "time_in_meeting": str,
        "leave_reason": str,
    }

    def __init__(self, d=None):
        self.participant_name: Optional[str] = None
        self.department: Optional[str] = None
        self.user_id: Optional[str] = None
        self.employee_id: Optional[str] = None
        self.phone: Optional[str] = None
        self.email: Optional[str] = None
        self.device: Optional[str] = None
        self.app_version: Optional[str] = None
        self.public_ip: Optional[str] = None
        self.internal_ip: Optional[str] = None
        self.use_rtc_proxy: Optional[bool] = None
        self.location: Optional[str] = None
        self.network_type: Optional[str] = None
        self.protocol: Optional[str] = None
        self.microphone: Optional[str] = None
        self.speaker: Optional[str] = None
        self.camera: Optional[str] = None
        self.audio: Optional[bool] = None
        self.video: Optional[bool] = None
        self.sharing: Optional[bool] = None
        self.join_time: Optional[str] = None
        self.leave_time: Optional[str] = None
        self.time_in_meeting: Optional[str] = None
        self.leave_reason: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ParticipantBuilder":
        return ParticipantBuilder()


class ParticipantBuilder(object):
    def __init__(self) -> None:
        self._participant = Participant()

    def participant_name(self, participant_name: str) -> "ParticipantBuilder":
        self._participant.participant_name = participant_name
        return self

    def department(self, department: str) -> "ParticipantBuilder":
        self._participant.department = department
        return self

    def user_id(self, user_id: str) -> "ParticipantBuilder":
        self._participant.user_id = user_id
        return self

    def employee_id(self, employee_id: str) -> "ParticipantBuilder":
        self._participant.employee_id = employee_id
        return self

    def phone(self, phone: str) -> "ParticipantBuilder":
        self._participant.phone = phone
        return self

    def email(self, email: str) -> "ParticipantBuilder":
        self._participant.email = email
        return self

    def device(self, device: str) -> "ParticipantBuilder":
        self._participant.device = device
        return self

    def app_version(self, app_version: str) -> "ParticipantBuilder":
        self._participant.app_version = app_version
        return self

    def public_ip(self, public_ip: str) -> "ParticipantBuilder":
        self._participant.public_ip = public_ip
        return self

    def internal_ip(self, internal_ip: str) -> "ParticipantBuilder":
        self._participant.internal_ip = internal_ip
        return self

    def use_rtc_proxy(self, use_rtc_proxy: bool) -> "ParticipantBuilder":
        self._participant.use_rtc_proxy = use_rtc_proxy
        return self

    def location(self, location: str) -> "ParticipantBuilder":
        self._participant.location = location
        return self

    def network_type(self, network_type: str) -> "ParticipantBuilder":
        self._participant.network_type = network_type
        return self

    def protocol(self, protocol: str) -> "ParticipantBuilder":
        self._participant.protocol = protocol
        return self

    def microphone(self, microphone: str) -> "ParticipantBuilder":
        self._participant.microphone = microphone
        return self

    def speaker(self, speaker: str) -> "ParticipantBuilder":
        self._participant.speaker = speaker
        return self

    def camera(self, camera: str) -> "ParticipantBuilder":
        self._participant.camera = camera
        return self

    def audio(self, audio: bool) -> "ParticipantBuilder":
        self._participant.audio = audio
        return self

    def video(self, video: bool) -> "ParticipantBuilder":
        self._participant.video = video
        return self

    def sharing(self, sharing: bool) -> "ParticipantBuilder":
        self._participant.sharing = sharing
        return self

    def join_time(self, join_time: str) -> "ParticipantBuilder":
        self._participant.join_time = join_time
        return self

    def leave_time(self, leave_time: str) -> "ParticipantBuilder":
        self._participant.leave_time = leave_time
        return self

    def time_in_meeting(self, time_in_meeting: str) -> "ParticipantBuilder":
        self._participant.time_in_meeting = time_in_meeting
        return self

    def leave_reason(self, leave_reason: str) -> "ParticipantBuilder":
        self._participant.leave_reason = leave_reason
        return self

    def build(self) -> "Participant":
        return self._participant
