import logging


def logger():
    logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',
    )

    logger = logging.getLogger(__name__)

    return logger