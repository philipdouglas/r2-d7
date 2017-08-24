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


def main():
    log_level = os.getenv("LOG_LEVEL", "DEBUG")
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s: %(message)s',
        level=log_level
    )

    slack_token = os.getenv("SLACK_TOKEN", "")
    logging.info("token: {}".format(slack_token))

    if slack_token == "":
        logging.info("SLACK_TOKEN env var not set, expecting token to be provided by Resourcer events")
        slack_token = None
        botManager = bot_manager.BotManager(spawn_bot)
        res = resourcer.Resourcer(botManager)
        res.start()
    else:
        # only want to run a single instance of the bot in dev mode
        bot = SlackBot(slack_token)
    bot.start({}, Droid)

if __name__ == "__main__":
    main()
