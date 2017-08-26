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
from r2d7.slack.bot import spawn_bot

from r2d7.listformatter import ListFormatter
from r2d7.cardlookup import CardLookup
from r2d7.slackdroid import SlackDroid

logger = logging.getLogger(__name__)


class Droid(SlackDroid, ListFormatter, CardLookup): pass


def on_message(ws, message):

    # Access the message type
    logger.info(message['type'])
    logger.info(message)


# Fires when an error occurred in the connection with the Beep Boop Resourcer server.
def on_error(ws, error):
    logger.info ('Error: ' + str(error))

# Fires the connection with the Beep Boop resourcer has closed.
def on_close(ws):
    logger.info ('Closed')

# Fires when the connection with the Beep Boop resourcer has opened.
def on_open(ws):
    logger.info('Opened')


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

    slack_token = os.getenv("SLACK_TOKEN", "")
    logging.info("token: {}".format(slack_token))

    droid = Droid()

    if slack_token == "":
        logging.info("SLACK_TOKEN env var not set, expecting token to be provided by Resourcer events")
        slack_token = None
        bot = SlackBot(droid)
        botManager = bot_manager.BotManager(lambda: bot)
        res = resourcer.Resourcer(botManager)
        res.handlers(handler_funcs)
        res.start()
    else:
        # only want to run a single instance of the bot in dev mode
        bot = SlackBot(droid, slack_token, debug)
    bot.start({})

if __name__ == "__main__":
    main()
