from typing import Callable


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
            "index": len(self.events)
        })
