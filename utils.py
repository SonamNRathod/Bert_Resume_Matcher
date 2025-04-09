# bert_resume_matcher/app/utils.py

import logging

def configure_logger(name: str = "resume_matcher") -> logging.Logger:
    """
    Configures and returns a logger.

    Args:
        name (str): Name of the logger.

    Returns:
        Logger object.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] - %(message)s", "%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger
