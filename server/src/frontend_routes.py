import asyncio
from flask import render_template

from .server import app

from .frontend_resources import *

@app.route("/", methods=["GET"])
async def index():
    return render_template("index.html", media=(await handle_all_items()))
