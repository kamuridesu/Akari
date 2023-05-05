from src.server import app
import src
import asyncio


async def hello(x):
    print(x)


async def main():
    from src.client_routes import ev_sender, cb_handler

    from Shimarin.server.events import Event

    event = Event("all_media", None, lambda x: x)
    await cb_handler.register(event)
    await ev_sender.send(event)
    await cb_handler.handle(
        event.identifier, __import__("json").dumps({"hello": "world"})
    )
    print(event.answered)
    while not event.answered:
        await asyncio.sleep(0)
    answer = event.answer
    print(answer)
    print(event.done)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=2222)
    # asyncio.run(main())
