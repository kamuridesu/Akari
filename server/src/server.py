import threading
from flask import Flask, Response, jsonify, request
from werkzeug.serving import make_server
import logging


app = Flask("server_mock")
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app.logger.disabled = True
log.disabled = True


def start():
    s = make_server("0.0.0.0", 2222, app)
    t = threading.Thread(target=s.serve_forever, name="Server")
    t.start()
    print("Server started")
    return t

if __name__ == "__main__":
    start()
