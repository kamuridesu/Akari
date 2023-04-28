import client
from client.src.handlers import setup
from client.src.jellyfin import AkarinClient
# from localServer.src.websocket import main
import asyncio



async def main():
#     # await ev_handlers.register(list_handler)
    # try:
    #     ev = await events.start()
    # except KeyboardInterrupt:
    #     events.stop()
    polling = setup()
    await polling.start()
#     ...


if __name__ == "__main__":
    asyncio.run(main())
