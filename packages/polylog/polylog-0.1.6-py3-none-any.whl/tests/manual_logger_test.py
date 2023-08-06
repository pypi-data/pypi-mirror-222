import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from polylog import setup_logger

os.environ["LOGGING"] = "True"

logger = setup_logger(__name__, useFileHandler=True)

logger.info("test")
logger.warning("test")
logger.error("test")
logger.critical("test")
