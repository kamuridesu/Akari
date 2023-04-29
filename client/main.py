import asyncio
from src.handlers import setup


async def main():
    poller = setup()
    await poller.start(0.1)


if __name__ == "__main__":
    asyncio.run(main())
