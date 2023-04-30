# ~Akarin~

Client-server application to deliver content from Jellyfin runnning on local network to a remote server.

<p align="center">
    <img src="images/akarin.png" width=300 alt="akarin">
</p>

# Server

The AkarinServer must be running on the remote server. To run it, you can run the `main.py` from the `server` folder.

# Client

First, setup the following environment variables:

```
JELLYFIN_ENDPOINT=
JELYFIN_TOKEN=
JELLYFIN_USERNAME=
JELLYFIN_PASSWORD=
SERVER_ENDPOINT=
```

If `JELYFIN_TOKEN` is set, you can leave `JELLYFIN_USERNAME` and `JELLYFIN_PASSWORD` blank. To generate a token, the first run has to be authenticated using username and password.

After all envirinoment variables are set, you can run the AkarinClient using the `main.py` from the `client` folder.


# THIS IS A WORK IN PROGRESS

not functional yet :p

# TODO

- [x] Use aiohttp instead of requests to avoid blocking connections.
- [ ] Map all endpoints used by jellyfin-web.


<p align="center">
    <img src="https://count.kamuridesu.com?username=Akarin" width=300 alt="count">
</p>
