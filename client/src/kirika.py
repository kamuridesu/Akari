from aiohttp import ClientSession

from . import config
from .networking import sendGetRequest, sendPostRequest, Response


class Kirika:
    def __init__(self):
        self.name = "Kirika"
        self.version = "0.0.1"
        self.device_id = 1
        self.user_id = ""
        self.token = ""
        self.headers = {
            "headers": {
                "Content-type": "application/json",
                "Accept-Charset": "UTF-8,*",
                "Accept-encoding": "gzip",
                "User-Agent": "Akari/0.0.1",
            }
        }
        self.session = ClientSession()

    async def __aenter__(self):
        await self.session.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_val, tb):
        if self.session:
            await self.session.__aexit__(exc_type, exc_val, tb)

    async def login(self):
        auth_data = {
            "Username": config.JELLYFIN_USERNAME,
            "Pw": config.JELLYFIN_PASSWORD,
        }

        self.headers['UserId'] = 

        response = await sendPostRequest(
            self.session, f"{config.JELLYFIN_ENDPOINT}/Users/AuthenticateByName"
        )

        print(response.content)

        if response.status == 200:
            print(await response.json())
