import logging

class App:
    def __init__(self, port:int = 5050, host: str = "localhost") -> None:
        self.port = port
        self.host = host
        self.url = f"http://{host}:{port}"
        logger = logging.getLogger(__name__)        
        logger.info("App configurated with {self.url}")