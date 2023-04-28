from src.server import main, ev_sender

import asyncio

async def a():
    t = main()
    while True:
        a = input(">>> ")
        await ev_sender.send("all_media", a, lambda x: print(f"Server received {x}"))
    t.join()


if __name__ == "__main__":
    asyncio.run(a())
