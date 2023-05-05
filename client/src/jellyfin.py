import json
import os
from jellyfin_apiclient_python import JellyfinClient

from . import config


class AkarinClient(JellyfinClient):
    def __init__(self):
        super().__init__()

        # Configure the application name and version
        self.config.app("Akari", "0.0.1", "Akari", "1")

        # Set SSL to True
        self.config.data["auth.ssl"] = True

        # Connect to the Jellyfin server
        self.auth.connect_to_address(config.JELLYFIN_ENDPOINT)

        # Check if a token is set, if not, generate a new one
        if config.JELLYFIN_TOKEN is None:
            self.generate_token()

        # Authenticate with the Jellyfin server using the token
        self.authenticate(json.loads(os.getenv("JELLYFIN_TOKEN")), discover=False)
        print(self.config.data)
        self.jellyfin.user_items(
            params={
                "recursive": True,
                "mediaTypes": ["Video"],
                "collapseBoxSetItems": False,
                "fields": "Path",
            }
        )

    def generate_token(self):
        print(
            "[!] JELLYFIN_TOKEN is not set. Falling back to username/password authentication"
        )

        # Login using the username and password
        self.auth.login(
            config.JELLYFIN_ENDPOINT, config.JELLYFIN_USERNAME, config.JELLYFIN_PASSWORD
        )

        # Get the server credentials
        credentials = self.auth.credentials.get_credentials()
        server = credentials["Servers"][0]
        server["username"] = config.JELLYFIN_USERNAME
        tokens = {"Servers": [server]}

        # Save the token in the environment variable
        tokens = json.dumps(tokens, ensure_ascii=False)
        os.environ.setdefault("JELLYFIN_TOKEN", tokens)

        print("[*] Token generated! Please, make sure to save it!")
        print(tokens)
