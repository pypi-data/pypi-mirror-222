from abc import ABC
from dataclasses import dataclass, field
from enum import StrEnum
from typing import Optional, Mapping, Dict, Any, Set

from multidict import MultiDict

from .base import (
    BaseObject,
    BaseCallSession,
    ObjectWithSnapshot,
    ObjectWithVideo,
    ObjectWithUnlocker,
    ObjectWithSIP,
)


@dataclass(slots=True)
class IcmBuilding(BaseObject):
    building: Optional[str] = None
    district_id: Optional[int] = None
    entrances_count: Optional[int] = None
    house: Optional[str] = None
    housing: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    street: Optional[str] = None

    @property
    def address(self) -> Optional[str]:
        parts = []
        if part := self.street:
            parts.append(part)
        if part := self.house:
            parts.append(f"д. {part}")
        if part := self.building:
            parts.append(f"ст. {part}")
        return ", ".join(parts) if parts else None

    def update_from_dict(self, data: Mapping[str, Any]) -> None:
        BaseObject.update_from_dict(self, data)

        self.district_id = data.get("district_id") or None
        self.entrances_count = data.get("entrances_count") or None
        self.house = data.get("house") or None
        self.housing = data.get("housing") or None
        self.street = data.get("street") or None

        try:
            self.latitude, self.longitude = map(float, data["location"])
        except (TypeError, ValueError, LookupError):
            pass


@dataclass(slots=True)
class ObjectWithBuilding(BaseObject, ABC):
    building_id: Optional[int] = None

    def update_from_dict(self, data: Mapping[str, Any]) -> None:
        BaseObject.update_from_dict(self, data)

        self.building_id = (
            int(data["building_id"]) if data.get("building_id") else None
        )

    @property
    def building(self) -> Optional[IcmBuilding]:
        return self.api.icm_buildings.get(self.building_id)


class IcmPropertyCategory(StrEnum):
    APARTMENT = "apartment"
    PARKING_PLACE = "parking_place"
    STOREROOM = "storeroom"
    BKFN = "bkfn"


@dataclass(slots=True)
class IcmProperty(ObjectWithBuilding):
    scheme_id: Optional[int] = None
    number: Optional[str] = None
    section: Optional[int] = None
    district_id: Optional[int] = None
    account_number: Optional[str] = None

    # Externally set properties
    category: Optional[IcmPropertyCategory] = None

    @property
    def address(self) -> Optional[str]:
        if not (category := self.category):
            return
        if not (building := self.building):
            return
        if not (address := building.address):
            return
        address += ","
        if category == IcmPropertyCategory.APARTMENT:
            address += " кв."
        elif category == IcmPropertyCategory.STOREROOM:
            address += " кл."
        elif category == IcmPropertyCategory.PARKING_PLACE:
            address += " мм."
        elif category == IcmPropertyCategory.BKFN:
            address += " БКФН."
        if number := self.number:
            address += " " + str(number)
        return address

    def update_from_dict(self, data: Mapping[str, Any]) -> None:
        ObjectWithBuilding.update_from_dict(self, data)

        self.scheme_id = data.get("scheme_id") or None
        self.number = data.get("number") or None
        self.section = data.get("section") or None
        self.district_id = data.get("district_id") or None
        self.account_number = data.get("account_number") or None

    @property
    def intercoms(self) -> Mapping[int, "IcmIntercom"]:
        return {
            intercom_id: intercom_device
            for intercom_id, intercom_device in self.api.icm_intercoms.items()
            if self.id in intercom_device.property_ids
        }

    async def update_intercoms(self) -> None:
        await self.api.icm_update_intercoms(self.id)


@dataclass(slots=True)
class BaseIcmCallSession(BaseCallSession):
    intercom_name: Optional[str] = None
    snapshot_url: Optional[str] = None

    def update_from_dict(self, data: Mapping[str, Any]) -> None:
        BaseCallSession.update_from_dict(self, data)
        self.intercom_name = data.get("intercom_name") or None
        self.snapshot_url = data.get("photo_url") or None

    async def unlock(self, mode: Optional[str] = None) -> None:
        await self.api.icm_intercoms[self.intercom_id].unlock()


@dataclass(slots=True)
class IcmCallSession(BaseIcmCallSession):
    # From call session
    call_number: Optional[str] = None

    # From root
    answered_customer_device_ids: tuple[int, ...] = ()
    hangup: bool = False

    @classmethod
    def get_id_from_data(cls, data: Mapping[str, Any]) -> int:
        """Call session identifier is embedded in a sub-dict."""
        return int(data["call_session"]["id"])

    def update_from_dict(self, data: Mapping[str, Any]) -> None:
        # This call session type holds call session data in a sub-dict
        call_session_data = data.get("call_session") or {}
        BaseIcmCallSession.update_from_dict(self, call_session_data)

        self.call_number = call_session_data.get("call_number")
        self.answered_customer_device_ids = tuple(
            map(int, data.get("answered_customer_device_ids") or ())
        )
        self.hangup = bool(data.get("hangup"))


@dataclass(slots=True)
class IcmActiveCallSession(BaseIcmCallSession):
    call_duration: Optional[int] = None
    call_id: Optional[str] = None
    call_from: Optional[int] = None
    mode: Optional[str] = None
    session_id: Optional[int] = None
    sip_proxy: Optional[str] = None
    property_id: Optional[int] = None

    def update_from_dict(self, data: Mapping[str, Any]) -> None:
        BaseIcmCallSession.update_from_dict(self, data)

        self.call_duration = data.get("call_duration") or None
        self.call_id = data.get("call_id") or None
        self.call_from = data.get("from") or None
        self.mode = data.get("mode") or None
        self.session_id = data.get("session_id") or None
        self.sip_proxy = data.get("proxy") or None
        self.property_id = data.get("property_id") or None


class VideoQualityTypes(StrEnum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


@dataclass(slots=True)
class IcmIntercom(
    ObjectWithSnapshot,
    ObjectWithVideo,
    ObjectWithUnlocker,
    ObjectWithSIP,
    ObjectWithBuilding,
):
    scheme_id: Optional[int] = None
    kind: Optional[str] = None
    device_category: Optional[str] = None
    mode: Optional[str] = None
    name: Optional[str] = None
    human_name: Optional[str] = None
    renamed_name: Optional[str] = None
    relays: Optional[Dict[str, str]] = None
    checkpoint_relay_index: Optional[int] = None
    entrance: Optional[int] = None
    can_address: Optional[Any] = None
    face_detection: Optional[bool] = None
    video: Optional[MultiDict[str]] = None
    photo_url: Optional[str] = None
    ip_address: Optional[str] = None

    # From sip_account parameter
    sip_account_proxy: Optional[str] = None
    sip_account_ex_user: Optional[str] = None

    # Non-standard attribute
    property_ids: Set[int] = field(default_factory=set)

    def update_from_dict(self, data: Mapping[str, Any]) -> None:
        ObjectWithSnapshot.update_from_dict(self, data)
        ObjectWithVideo.update_from_dict(self, data)
        ObjectWithUnlocker.update_from_dict(self, data)
        ObjectWithSIP.update_from_dict(self, data)
        ObjectWithBuilding.update_from_dict(self, data)

        self.scheme_id = data.get("scheme_id") or None
        self.kind = data.get("kind") or None
        self.device_category = data.get("device_category") or None
        self.mode = data.get("mode") or None
        self.name = data.get("name") or None
        self.human_name = data.get("human_name") or None
        self.renamed_name = data.get("renamed_name") or None
        self.checkpoint_relay_index = data.get("checkpoint_relay_index")
        self.relays = data.get("relays") or None
        self.entrance = data.get("entrance")
        self.can_address = data.get("can_address")
        self.face_detection = data.get("face_detection")
        self.video = (
            MultiDict([(v["quality"], v["source"]) for v in video_data])
            if (video_data := data.get("video"))
            else None
        )
        self.photo_url = data.get("photo_url") or None
        self.ip_address = data.get("ip_address") or None

        if sip_account_data := data.get("sip_account") or None:
            self.sip_account_ex_user = sip_account_data.get("ex_user")
            self.sip_account_proxy = sip_account_data.get("proxy")

    @property
    def sip_user(self) -> Optional[str]:
        return self.sip_account_ex_user

    @property
    def stream_url(self) -> Optional[str]:
        """Return URL for video stream"""
        if not (video_streams := self.video):
            return None

        for quality in VideoQualityTypes:
            if video_stream_url := video_streams.get(quality):
                return video_stream_url

        return next(iter(video_streams.values()))

    @property
    def snapshot_url(self) -> Optional[str]:
        return self.photo_url

    async def unlock(self) -> None:
        """Unlock intercom"""
        await self.api.icm_unlock_intercom(self.id, self.mode)
