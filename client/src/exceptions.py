class ClientException(Exception):
    def __init__(self, message: str = "Client could not communicate with server!"):
        super().__init__(message)


class ServerException(Exception):
    def __init__(self, message: str = "Server is not available!"):
        super().__init__(message)