from importlib.metadata import version
import click
from .app import App
import pathlib
import logging
import datetime

__path__ = pathlib.Path().absolute()
__version__  = version("PROJECT-DEFIANT")
__time__  = datetime.datetime.now()

logger = logging.getLogger(__name__)
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.INFO)
f_handler.setLevel(logging.INFO)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.error('This is an error')
# print(logger.level)

# Here we describe a cli application that the host will run on the fastapi server
@click.version_option(__version__)
@click.group()
def cli() -> None:
    """
    ============== PROJECT DEFIANT ============ \n
    Cli for PROJECT-DEFIANT blog application \n                                                                  
    """


@cli.command("start", help="Start application")
@click.argument("port", type=click.INT, default=5050, required=False)
@click.argument("host", type=click.STRING, default="localhost", required=False)
def start_server(port: int, host: str) -> None:
    App(port, host)
