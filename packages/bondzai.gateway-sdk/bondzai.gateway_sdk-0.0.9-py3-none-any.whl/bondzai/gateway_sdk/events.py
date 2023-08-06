from dataclasses import dataclass
from typing import Union

from .utils import b2b64
from .enums import EventOperationID

EVENT_DATA_IN_CSTRUCT_SIZEOF = 14


@dataclass
class EventHeader:
    mod: int
    appid: int
    timestamp: int
    payload_size: int

    def get_size(self) -> int:
        return 16

    def to_dict(self) -> dict:
        return {
            "mod": self.mod,
            "appid": self.appid,
            "timestamp": self.timestamp,
            "payload_size": self.payload_size
        }

    def to_array(self) -> list:
        return [
            self.mod,
            self.appid,
            self.timestamp,
            self.payload_size
        ]


@dataclass
class EventDataIn:
    datasource: int
    datatype: str
    buffer: bytes

    def get_size(self) -> int:
        # FIXME: size must depend on datatype
        # JDE: consider that data is float
        return EVENT_DATA_IN_CSTRUCT_SIZEOF + len(self.buffer) * 4

    def to_dict(self) -> dict:
        return {
            "datasource": self.datasource,
            "datatype": self.datatype,
            "buffer": self.buffer
        }

    def to_array(self) -> list:
        return [
            self.datasource,
            self.datatype,
            self.buffer
        ]


@dataclass
class EventException:
    error: int
    msg: str

    def get_size(self) -> int:
        return 4 + len(self.msg)

    def to_dict(self) -> dict:
        return {
            "error": self.error,
            "msg": self.msg
        }

    def to_array(self) -> list:
        return [
            self.error,
            self.msg
        ]


@dataclass
class EventCMDStatus:
    mod: int
    op: int
    status: int

    def get_size(self) -> int:
        return 12

    def to_dict(self) -> dict:
        return {
            "mod": self.mod,
            "op": self.op,
            "status": self.status
        }

    def to_array(self) -> list:
        return [
            self.mod,
            self.op,
            self.status
        ]


@dataclass
class EventLog:
    appid: int
    mod: int
    timestamp: int
    level: int
    msg: str

    def get_size(self) -> int:
        return 4 * 4 + len(self.msg)

    def to_dict(self) -> dict:
        return {
            "appid": self.appid,
            "mod": self.mod,
            "timestamp": self.timestamp,
            "level": self.level,
            "msg": self.msg
        }

    def to_array(self) -> list:
        return [
            self.appid,
            self.mod,
            self.timestamp,
            self.level,
            self.msg
        ]


@dataclass
class EventAslResult:
    label_type: int
    confidence: float
    result: list

    def get_size(self) -> int:
        return 2 * 4 + len(self.result) * 4

    def to_dict(self) -> dict:
        return {
            "label_type": self.label_type,
            "confidence": self.confidence,
            "result": self.result
        }

    def to_array(self) -> list:
        return [
            self.label_type,
            self.confidence,
            self.result
        ]


@dataclass
class EventInferResult:
    ai_type: int
    label_type: int
    step: int
    result: list

    def get_size(self) -> int:
        return 3 * 4 + len(self.result) * 4

    def to_dict(self) -> dict:
        return {
            "ai_type": self.ai_type,
            "label_type": self.label_type,
            "step": self.step,
            "result": self.result
        }

    def to_array(self) -> list:
        return [
            self.ai_type,
            self.label_type,
            self.step,
            self.result
        ]


@dataclass
class EventSetMode:
    ai_mode: int
    ai_type: int
    data: list

    def get_size(self) -> int:
        return 2 * 4 + len(self.data) * 4

    def to_dict(self) -> dict:
        return {
            "ai_mode": self.ai_mode,
            "ai_type": self.ai_type,
            "data": self.data
        }

    def to_array(self) -> list:
        return [
            self.ai_mode,
            self.ai_type,
            self.data
        ]


@dataclass
class EventCorrection:
    position: int
    ai_type: int
    data: list  # classification.label_type & classification.label OR regression

    def get_size(self) -> int:
        return 2 * 4 + len(self.data) * 4

    def to_dict(self) -> dict:
        return {
            "position": self.position,
            "ai_type": self.ai_type,
            "data": self.data
        }

    def to_array(self) -> list:
        return [
            self.position,
            self.ai_type,
            self.data
        ]


@dataclass
class EventTrigger:
    trigger_type: int
    trigger_value: int

    def get_size(self) -> int:
        return 8

    def to_dict(self) -> dict:
        return {
            "trigger_type": self.trigger_type,
            "trigger_value": self.trigger_value,
        }

    def to_array(self) -> list:
        return [
            self.trigger_type,
            self.trigger_value
        ]


@dataclass
class EventCustom:
    data: bytearray

    def __init__(self, data) -> None:
        self.data = bytearray(data)

    def get_size(self) -> int:
        return len(self.data)

    def to_dict(self) -> dict:
        return {"data": b2b64(self.data)}

    def to_array(self) -> list:
        return [self.data]

    @classmethod
    def from_dict(cls, data: dict) -> "EventCustom":
        return EventCustom(data.get("data"))

@dataclass
class EventProcessAck:
    evt_id: int
    process_state: int
    step: int
    app_id: int
    meta: bytes

    def to_dict(self) -> str:
        return {
            "evt_id": self.evt_id,
            "process_state": self.process_state,
            "step": self.step,
            "app_id": self.app_id,
            "meta": self.meta
        }

    def to_array(self) -> list:
        return [
            self.evt_id,
            self.process_state,
            self.step,
            self.app_id,
            self.meta
        ]


EventPayloadType = Union[
    EventCMDStatus,
    EventCustom,
    EventDataIn,
    EventException,
    EventLog,
    EventAslResult,
    EventInferResult,
    EventSetMode,
    EventCorrection,
    EventTrigger,
    EventProcessAck
]

OP_TO_EVENT_TYPES = {
    EventOperationID.EVT_EXT_EXCEPTION.value: EventException,
    EventOperationID.EVT_EXT_DATA_IN.value: EventDataIn,
    EventOperationID.EVT_EXT_CMD_STATUS.value: EventCMDStatus,
    EventOperationID.EVT_EXT_LOG.value: EventLog,
    EventOperationID.EVT_EXT_ASL_RESULT.value: EventAslResult,
    EventOperationID.EVT_EXT_VM_RESULT.value: EventInferResult,
    EventOperationID.EVT_EXT_SET_MODE.value: EventSetMode,
    EventOperationID.EVT_EXT_CORRECTION.value: EventCorrection,
    EventOperationID.EVT_EXT_TRIGGER.value: EventTrigger,
    EventOperationID.EVT_EXT_CUSTOM_1.value: EventCustom,
    EventOperationID.EVT_EXT_CUSTOM_2.value: EventCustom,
    EventOperationID.EVT_EXT_CUSTOM_3.value: EventCustom,
    EventOperationID.EVT_EXT_CUSTOM_4.value: EventCustom,
    EventOperationID.EVT_EXT_CUSTOM_5.value: EventCustom,
    EventOperationID.EVT_EXT_CUSTOM_6.value: EventCustom,
    EventOperationID.EVT_EXT_CUSTOM_7.value: EventCustom,
    EventOperationID.EVT_EXT_CUSTOM_8.value: EventCustom,
    EventOperationID.EVT_EXT_CUSTOM_9.value: EventCustom,
    EventOperationID.EVT_EXT_CUSTOM_10.value: EventCustom,
    EventOperationID.EVT_EXT_PROCESS_ACK.value: EventProcessAck,
}


def get_event_class(event_type_id: EventOperationID):
    return OP_TO_EVENT_TYPES.get(event_type_id.value, None)
