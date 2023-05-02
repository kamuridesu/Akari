from flask import request
from .server import app

from .frontend_resources import *

@app.route("/User/Items", methods=["GET"])
async def Items():
    args = request.get_json(force=True, silent=True)
    if args is None:
        args = {}
    return (await handle_Items(args))
 