import aiohttp
from .polling import EventsHandlers, EventPolling, Event
from .jellyfin import AkarinClient

ev_handlers = EventsHandlers()
client = AkarinClient()

@ev_handlers.new(event_name="all_media")
async def get_all_media(event: Event):
    print(f"Client received {event.payload}")
    await event.reply("Hello world")
    return await client.all_media

