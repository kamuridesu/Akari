from src.server import start, ev_sender

import asyncio

async def main():
    server_thread = start()
    while True:
        user_input = input(">>> ")
        await ev_sender.send("all_media", user_input, lambda x: print(f"Server received {x}"))
    server_thread.join()


if __name__ == "__main__":
    asyncio.run(main())
