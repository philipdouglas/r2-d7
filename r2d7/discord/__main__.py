#!/usr/bin/env python
import logging
import os
import re

import discord

from r2d7.listformatter import ListFormatter
from r2d7.cardlookup import CardLookup
from r2d7.factionlister import FactionLister
from r2d7.discorddroid import DiscordDroid

logger = logging.getLogger(__name__)


class Droid(
        DiscordDroid,
        ListFormatter,
        CardLookup,
        FactionLister):
    pass


class DiscordClient(discord.Client):
    def __init__(self, droid):
        super().__init__()
        self.droid = droid

    async def on_ready(self):
        logger.info(f"Bot online as {self.user}")

    async def on_message(self, message):
        if message.author == self.user:
            return

        logger.debug(f"Message: {message.clean_content}")

        # Check for new data
        if self.droid.needs_update():
            self.droid.load_data()

        response = None

        for regex, handle_method in self.droid._handlers.items():
            logger.debug(f"Checking {regex}")
            match = regex.search(message.clean_content)
            if match:
                response = handle_method(match[1])
                if response:
                    break

        if response:
            response = '\n'.join(response)
            for match in re.finditer(r'\:([^:]*)\:', response):
                for emoji in message.guild.emojis:
                    if emoji.name == match.group(1):
                        response = response.replace(match.group(0), str(emoji))

            await message.channel.send(response)


def main():
    debug = os.getenv('DEBUG', False)
    log_level = 'DEBUG' if debug else 'INFO'
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s: %(message)s',
        level=log_level
    )

    discord_token = os.getenv("DISCORD_TOKEN", None)
    logging.info("discord token: {}".format(discord_token))

    droid = Droid()
    if discord_token:
        logging.info("DISCORD_TOKEN env var set")
        bot = DiscordClient(droid)
        bot.run(discord_token)
    else:
        logging.error("No discord token found, exiting.")
        return()


if __name__ == "__main__":
    main()
