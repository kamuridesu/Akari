import threading
from typing import Callable
from flask import Flask, Response, jsonify, request
from werkzeug.serving import make_server
from .polling import EventEmitter
import logging



ev_sender = EventEmitter()


__app = Flask("server_mock")
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
__app.logger.disabled = True
log.disabled = True

callbacks: dict[Callable] = {}

@__app.route("/events", methods=["GET"])
async def events():
    last_ev = await ev_sender.fetch_last_event()
    if last_ev:
        callback = last_ev.pop('callback')
        if callback:
            callbacks[str(last_ev['index'])] = callback
        events = last_ev
        return events
    return {}


@__app.route("/callback")
async def reply():
    data = request.get_json(silent=True)
    if data:
        index = data['index']
        payload = data['payload']
        callback = callbacks[index]
        callback(payload)
    return {"ok": True}


def main():
    s = make_server("0.0.0.0", 2222, __app)
    t = threading.Thread(target=s.serve_forever, name="Server")
    t.start()
    return t

if __name__ == "__main__":
    main()
