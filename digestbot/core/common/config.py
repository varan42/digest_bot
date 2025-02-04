"""
Parse configuration variables from env vars and raise Exceptions if needed
"""

import os
import logging
from digestbot.core.common import LoggerFactory as _log_factory


_logger = _log_factory.create_logger(__name__, logging.WARNING)


# User token for message access
SLACK_USER_TOKEN = os.getenv("SLACK_USER_TOKEN", None)
if SLACK_USER_TOKEN is None:
    raise Exception("SLACK_USER_TOKEN is not provided.")


# Bot token for bot access (post to channels etc)
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN", None)
if SLACK_BOT_TOKEN is None:
    raise Exception("SLACK_BOT_TOKEN is not provided.")


# How often to crawl messages from chats
CRAWL_INTERVAL = os.getenv("CRAWL_INTERVAL", "900")
try:
    CRAWL_INTERVAL = int(CRAWL_INTERVAL)
except ValueError:
    _logger.warning(
        f"Could not parse crawl interval: f{CRAWL_INTERVAL}, default value 900 is used."
    )
    CRAWL_INTERVAL = 900


# App name in slack (important for not answering own messages)
BOT_NAME = os.getenv("BOT_NAME", "digest-bot")


# Database settings
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "postgres")
DB_NAME = os.getenv("DB_NAME", "postgres")
DB_HOST = os.getenv("DB_HOST", "postgres")
DB_PORT = os.getenv("DB_PORT", 5432)


# Log level
__available_log_levels = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warn": logging.WARNING,
    "warning": logging.WARNING,
    "error": logging.ERROR,
}
LOG_LEVEL = os.getenv("LOG_LEVEL", "info").lower()
if LOG_LEVEL not in __available_log_levels:
    _logger.warning(
        f"Could not parse log level: f{LOG_LEVEL}, default value 'info' is used."
    )
    LOG_LEVEL = "info"
LOG_LEVEL = __available_log_levels[LOG_LEVEL]
