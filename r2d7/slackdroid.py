import logging
import re

from r2d7.core import DroidCore


logger = logging.getLogger(__name__)


HELP_TEXT = """\
I am R2-D7, xwingtmg.slack.com's bot.
*List Printing:* If you paste a (Yet Another) Squad Builder, Fab's or xwing-builder.co.uk permalink into a channel I'm in (or direct
message me one), I will print a summary of the list.
*Card Lookup:* Say something to me (_<@{0}>: something_) and I will describe any upgrades, ships or pilots that match what you said.
You can also lookup a card by enclosing its name in double square brackets. (Eg. Why not try [[Engine Upgrade]])
If you only want cards in a particular slot or ship, begin your lookup with the emoji for that ship or slot. (eg. _<@{0}>: :crew: rey_)
You can also search for cards by points value in a particular slot. Eg. _<@{0}> :crew: <=3_. =, <, >, <= and >= are supported.
"""


class SlackDroid(DroidCore):
    def __init__(self, slack_clients=None):
        self.clients = slack_clients

    def send_message(self, channel_id, msg):
        # in the case of Group and Private channels, RTM channel payload is a complex dictionary
        if isinstance(channel_id, dict):
            channel_id = channel_id['id']
        logger.debug('Sending msg: %s to channel: %s' % (msg, channel_id))
        channel = self.clients.rtm.server.channels.find(channel_id)
        channel.send_message(msg)

    def write_help_message(self, channel_id):
        bot_uid = self.clients.bot_user_id()
        self.send_message(channel_id, HELP_TEXT.format(bot_uid))

    def write_error(self, channel_id, err_msg):
        self.send_message(channel_id, ':alarm: ' + err_msg)

    @staticmethod
    def iconify(name, hypens=False):
        name = name.lower()
        if hypens:
            name = re.sub(r'[^a-zA-Z0-9\-]', '', name)
        else:
            name = re.sub(r'[^a-zA-Z0-9]', '', name)
        name = name.replace('+', 'plus')
        if name in ['bomb', 'shield']:
            name = 'x' + name
        elif name == 'rebelalliance':
            name = 'rebel'
        elif name == 'scumandvillainy':
            name = 'scum'
        elif name == 'galacticempire':
            name = 'empire'
        return f":{name}:"

    @staticmethod
    def bold(text):
        return f"*{text}*"

    @staticmethod
    def italics(text):
        return f"_{text}_"

    @staticmethod
    def convert_html(text):
        """
        The data has HTML formatting tags, convert them to slack formatting.
        """
        text = re.sub(r'<\/?strong>', '*', text)
        text = re.sub(r'(<br \/>)+', '\n', text)
        text = re.sub(r'\[Koiogran Turn\]', ':kturn:', text)
        text = re.sub(r'\[Bomb\]', ':xbomb:', text)
        text = re.sub(r'\[([^\]]+)\]', ':\\1:', text)
        return text
