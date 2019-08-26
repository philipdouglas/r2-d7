from multiprocessing import Process
import time
import logging

from r2d7.slack.__main__ import main as slack_main
from r2d7.discord.__main__ import main as discord_main

logger = logging.getLogger(__name__)


def auto_restarter(slack, discord):
    """
    If either bot crashes, start it up again. Last line of defence against crashes.
    """
    while True:
        time.sleep(60)
        if not slack.is_alive():
            logger.warning("AUTO RESTARTER: Slack bot down, restarting...")
            slack = Process(target=slack_main)
            slack.start()
        if not discord.is_alive():
            logger.warning("AUTO RESTARTER: Discord bot down, restarting...")
            discord = Process(target=discord_main)
            discord.start()


def main():
    slack = Process(target=slack_main)
    slack.start()
    discord = Process(target=discord_main)
    discord.start()

    auto_restarter(slack, discord)

if __name__ == "__main__":
    main()
