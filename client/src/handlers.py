import json

from Shimarin.client.events import EventsHandlers, Event
from .jellyfin import AkarinClient

ev_handlers = EventsHandlers()
client = AkarinClient()


@ev_handlers.new(event_name="jelly")
async def get_all_media(event: Event):
    print(event)
    params = None
    if event.payload:
        params = json.loads(event.payload)
    return await event.reply(json.dumps({"hello": "world"}))
