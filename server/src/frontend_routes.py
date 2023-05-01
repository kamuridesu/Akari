from .server import app

from .frontend_resources import *

@app.route("/Items", methods=["GET"])
async def Items():
    return (await handle_Items())
 