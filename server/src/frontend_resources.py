import json
from Shimarin.server.events import Event
from .client_routes import ev_sender


async def handle_Items(params: dict = {}):
    event = Event.new("jelly", json.dumps(params), json.loads)
    await ev_sender.send(event)
    answer = await event.get_answer()
    return answer
