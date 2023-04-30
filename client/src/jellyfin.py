import os
import json
import time

from jellyfin_apiclient_python import JellyfinClient

from . import config

class AkarinClient(JellyfinClient):
    def __init__(self):
        super().__init__()

        self.config.app('Akari', '0.0.1', 'Akari', '1')
        self.config.data["auth.ssl"] = True

        self.auth.connect_to_address(config.JELLYFIN_ENDPOINT)
        if config.JELYFIN_TOKEN is None:
            self.generate_token()

        self.authenticate(json.loads(os.getenv("JELLYFIN_TOKEN")), discover=False)
    
    def generate_token(self):
        print("[!] JELLYFIN_TOKEN is not set. Falling back to username/password authentication")
        self.auth.login(config.JELLYFIN_ENDPOINT, config.JELLYFIN_USERNAME, config.JELLYFIN_PASSWORD)
        credentials = self.auth.credentials.get_credentials()
        server = credentials["Servers"][0]
        server["username"] = config.JELLYFIN_USERNAME
        tokens = {"Servers": [server]}
        tokens = json.dumps(tokens, ensure_ascii=False)
        os.environ.setdefault("JELLYFIN_TOKEN", tokens)
        print("[*] Token generated! Please, make sure to save it!")
        print(tokens)

    @property
    async def all_media(self) -> list[dict]:
        start = time.perf_counter()
        response = self.jellyfin.user_items(params={
                    'recursive': True,
                    'mediaTypes': [ 'Video' ],
                    'collapseBoxSetItems': False,
                    'fields': 'Path',
                    })
        print(f"Jellyfin took {time.perf_counter() - start} to answer")
        return [file for file in response['Items']]
