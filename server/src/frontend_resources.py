import json
from .polling import Event
from .client_routes import ev_sender


async def handle_Items():
    event = Event.new("Items", None, json.loads)
    await ev_sender.send(event)
    answer = await event.get_answer()
    return answer
