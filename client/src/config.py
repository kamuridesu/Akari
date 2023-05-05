import os
import sys

import requests

JELLYFIN_ENDPOINT = os.getenv("JELLYFIN_ENDPOINT", "http://localhost:8096")
JELLYFIN_TOKEN = os.getenv("JELLYFIN_TOKEN")
JELLYFIN_USERNAME = os.getenv("JELLYFIN_USERNAME")
JELLYFIN_PASSWORD = os.getenv("JELLYFIN_PASSWORD")
JELLYFIN_HEADERS = {"Authorization": JELLYFIN_TOKEN}

SERVER_ENDPOINT = os.getenv("SERVER_ENDPOINT", "http://localhost:2222")

SSL_ENABLED = "--insecure" not in sys.argv


# response = requests.get(JELLYFIN_ENDPOINT)
# if response.status_code != 200:
#     raise requests.exceptions.ConnectionError("Could not connect to JellyFin endpoint!")
