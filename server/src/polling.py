from typing import Callable, Any
import uuid


class EventEmitter:
    def __init__(self):
        self.events = []

    async def fetch_last_event(self):
        try:
            return self.events.pop()
        except IndexError:
            return {}
        
    async def send(self, event_type: str, payload: str = None, callback: Callable |  None = None) -> None:
        self.events.append({
            "event_type": event_type,
            "payload": payload,
            "callback": callback,
            "identifier": str(uuid.uuid1())
        })


class CallbacksHandlers:
    def __init__(self):
        self.callbacks: dict[str, Callable] = {}

    async def register(self, unique_identifier: str, callback: Callable):
        self.callbacks[unique_identifier] = callback

    async def trigger(self, unique_identifier: str, payload: Any):
        return await self.callbacks[unique_identifier](payload)
