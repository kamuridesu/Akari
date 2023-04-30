from .server import request, app
from .polling import EventEmitter, CallbacksHandlers

ev_sender = EventEmitter()
cb_handler = CallbacksHandlers()


@app.route("/events", methods=["GET"])
async def events():
    fetch = request.args.get('fetch')
    events_to_send = 1
    if fetch:
        events_to_send = int(fetch)
    events = []
    for _ in range(events_to_send):
        last_ev = await ev_sender.fetch_last_event()
        if last_ev.event_type:
            await cb_handler.register(last_ev)
            events.append(last_ev.json())
    return events


@app.route("/callback")
async def reply():
    data = request.get_json(silent=True)
    if data:
        identifier = data['identifier']
        payload = data['payload']
        await cb_handler.handle(identifier, payload)
    return {"ok": True}
