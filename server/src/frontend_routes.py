from flask import request
from .server import app

from .frontend_resources import *


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
async def main(*args, **kwargs):
    return await handle_Items({"args": args, "kwargs": kwargs})
