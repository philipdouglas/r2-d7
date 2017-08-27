#!/usr/bin/env python
"""
Stolen from https://github.com/BeepBoopHQ/starter-python-bot/

MIT Licensed
"""
import logging
import os

from beepboop import resourcer
from beepboop import bot_manager

from r2d7.slack.bot import SlackBot
from r2d7.slack.bot import BotSpawner

from r2d7.listformatter import ListFormatter
from r2d7.cardlookup import CardLookup
from r2d7.slackdroid import SlackDroid

logger = logging.getLogger(__name__)


class Droid(SlackDroid, ListFormatter, CardLookup):
    pass


def on_message(ws, message):
    logger.debug(f"Resource message ({message['type']}):\n{message}")


def on_error(ws, error):
    logger.error(f'Resourcer error: {error}')


def on_close(ws):
    logger.info ('Resourcer connection closed.')


def on_open(ws):
    logger.info('Resourcer connection opened')


handler_funcs = {
    'on_open': on_open,
    'on_message': on_message,
    'on_error': on_error,
    'on_close': on_close,
}


def main():
    debug = os.getenv('DEBUG', False)
    log_level = 'DEBUG' if debug else 'INFO'
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s: %(message)s',
        level=log_level
    )

    slack_token = os.getenv("SLACK_TOKEN", None)
    logging.info("token: {}".format(slack_token))

    droid = Droid()
    if not slack_token:
        logging.info("SLACK_TOKEN env var not set, connecting to Resourcer")
        botManager = bot_manager.BotManager(lambda: SlackBot(droid))
        res = resourcer.Resourcer(botManager)
        res.handlers(handler_funcs)
        res.start()
    else:
        # Run a single instance of the bot in dev mode
        bot = SlackBot(droid, slack_token, debug)
        bot.start({})

if __name__ == "__main__":
    main()
