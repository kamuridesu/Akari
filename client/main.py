import asyncio
from src.polling import EventPolling
from src.handlers import ev_handlers


async def main():
    async with EventPolling(ev_handlers) as poller:
        await poller.start(0.01)


if __name__ == "__main__":
    asyncio.run(main())
