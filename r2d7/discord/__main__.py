#!/usr/bin/env python
import logging
import os
import re
import asyncio

import discord

from r2d7.listformatter import ListFormatter
from r2d7.cardlookup import CardLookup
from r2d7.factionlister import FactionLister
from r2d7.meta import Metawing
from r2d7.roller import Roller
from r2d7.talkback import Talkback
from r2d7.discorddroid import DiscordDroid

logger = logging.getLogger(__name__)


class Droid(
        DiscordDroid,
        ListFormatter,
        CardLookup,
        FactionLister,
        Metawing,
        Roller,
        Talkback):
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

        logger.debug(f"Message: {message}\nContent: {message.clean_content}")

        # Check for new data
        if self.droid.needs_update():
            self.droid.load_data()

        responses = None

        if isinstance(message.channel, discord.DMChannel):
            for regex, handle_method in self.droid._dm_handlers.items():
                match = regex.search(message.clean_content)
                if match:
                    responses = handle_method(match[1])
                    if responses:
                        break

        if not responses:
            for regex, handle_method in self.droid._handlers.items():
                logger.debug(f"Checking {regex}")
                match = regex.search(message.clean_content)
                if match:
                    responses = handle_method(match[1])
                    if responses:
                        break

        if responses:
            for response in responses:
                emoji_map = {f":{emoji.name}:": str(emoji) for emoji in self.emojis}

                current_message = ''
                for line in response:
                    fixed_line = line
                    for slack_style, discord_style in emoji_map.items():
                        fixed_line = fixed_line.replace(
                            slack_style, discord_style)
                    if len(current_message) + 2 + len(fixed_line) < 2048:
                        current_message += f"\n{fixed_line}"
                    else:
                        embed=discord.Embed(description=current_message)
                        embed.set_footer(text=f"*Requested by {message.author.mention}*")
                        await message.channel.send(embed=embed)
                        current_message = fixed_line
                await message.channel.send(
                    embed=discord.Embed(description=current_message))
            
            if message.guild.me.permissions_in(message.channel).manage_messages:
                prompt_delete_previous_message = await message.channel.send("Delete your message?")
                await prompt_delete_previous_message.add_reaction("✅")
                await prompt_delete_previous_message.add_reaction("❌")

                try:
                    reaction, user = await self.wait_for(
                        event="reaction_add",
                        timeout=10,
                        check=lambda reaction, user: user == message.author
                    )
                    if str(reaction.emoji) == "✅":
                        await message.delete()
                        await prompt_delete_previous_message.delete()
                        return
                    if str(reaction.emoji) == "❌":
                        await prompt_delete_previous_message.delete()
                        return
                except asyncio.TimeoutError:
                    await prompt_delete_previous_message.delete()
                    return


def main():
    debug = os.getenv('DEBUG', False)
    log_level = 'DEBUG' if debug else 'INFO'
    logging.basicConfig(
        format='%(asctime)s [%(process)d] Discord - %(levelname)s: %(message)s',
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
