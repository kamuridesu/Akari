import asyncio
# from Shimarin.client.events import EventPolling
# from src.handlers import ev_handlers
from src.kirika import Kirika


async def main():
    async with Kirika() as k:
        await k.login()
    # async with EventPolling(ev_handlers) as poller:
    #     print("Poller started!")
    #     await poller.start(0.01)


if __name__ == "__main__":
    asyncio.run(main())
    # from client.src.jellyfin import AkarinClient

    # client = AkarinClient()
    # client.jellyfin.user_items(
    #     params={
    #         "recursive": True,
    #         "mediaTypes": ["Video"],
    #         "collapseBoxSetItems": False,
    #         "fields": "Path",
    #     }
    # )
