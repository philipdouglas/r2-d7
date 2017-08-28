import html
import logging
import re

from r2d7.core import DroidCore


logger = logging.getLogger(__name__)


HELP_TEXT = """\
I am R2-D7, xwingtmg.slack.com's bot.
*List Printing:* If you paste a (Yet Another) Squad Builder, Fab's or xwing-builder.co.uk permalink into a channel I'm in (or direct message me one), I will print a summary of the list.
*Card Lookup:* Type something surrounded by square brackets and I will describe any upgrades, ships or pilots that match what you said. (Eg. Why not try [[Engine Upgrade]])
If you only want cards in a particular slot or ship, begin your lookup with the emoji for that ship or slot. (eg. _[[:crew: rey]]_)
You can also search for cards by points value in a particular slot. Eg. _[[:crew: <=3]]_. =, <, >, <= and >= are supported.
You can list the contents of each wave by saying [[Wave X]]. Eg. [[Wave 1]].
"""


class SlackDroid(DroidCore):
    def __init__(self):
        super().__init__()
        self.load_data()

    filter_pattern = re.compile(
        r' *(?:(:[^:]+:))? *(?:([^=><:]*[^=><: ][^=><:]*)|([=><][=><]?)'
        r' *(\d+)) *(?:(:[^:]+:))? *'
    )
    faction_icon_pattern = r':(rebel|resistance|scum|imperial|first_order):'

    @staticmethod
    def iconify(name, hyphens=False):
        name = name.lower()
        if hyphens:
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
        elif name == 'firstorder':
            name = 'first_order'
        return f":{name}:"

    @staticmethod
    def bold(text):
        return f"*{text}*"

    @staticmethod
    def italics(text):
        return f"_{text}_"

    _data_to_emoji = {
        re.compile(r'\[Koiogran Turn\]'): ':kturn:',
        re.compile(r'\[Turn Right\]'): ':turnright:',
        re.compile(r'\[Turn Left\]'): ':turnleft:',
        re.compile(r'\[Bank Right\]'): ':bankright:',
        re.compile(r'\[Bank Left\]'): ':bankleft:',
        re.compile(r'\[Segnor\'s Loop Left\]'): ':sloopleft:',
        re.compile(r'\[Segnor\'s Loop Right\]'): ':sloopright:',
        re.compile(r'\[Tallon Roll Left\]'): ':trollleft:',
        re.compile(r'\[Tallon Roll Right\]'): ':trollright:',
        re.compile(r'\[Critical Hit\]'): ':crit:',
        re.compile(r'\[Bomb\]'): ':xbomb:',
    }

    @classmethod
    def convert_html(cls, text):
        """
        The data has HTML formatting tags, convert them to slack formatting.
        """
        for regex, sub in cls._data_to_emoji.items():
            text = regex.sub(sub, text)
        text = re.sub(r'<\/?strong>', '*', text)
        text = re.sub(r'<\/?em>', '_', text)
        text = re.sub(r'\[([^\]]+)\]', ':\\1:', text)
        lines = re.split(r'(?:<br \/>)+', text)
        return [line for line in lines if line != '']

    @classmethod
    def wiki_link(cls, card_name, crew_of_pilot=False, wiki_name=False):
        if not wiki_name:
            wiki_name = card_name
        fudged_name = re.sub(r' ', '_', wiki_name)
        # Data and the wiki use different name conventions
        #TODO work out the fudges for xwing-data
        # fudged_name = re.sub(r'\(Scum\)', '(S&V)', fudged_name)
        # fudged_name = re.sub(r'\((PS9|TFA)\)', '(HOR)', fudged_name)
        if 'Core Set' in card_name:
            fudged_name = 'X-Wing_' + fudged_name
        fudged_name = re.sub(r'-wing', '-Wing', fudged_name)
        fudged_name = re.sub(r'\/V', '/v', fudged_name)
        fudged_name = re.sub(r'\/X', '/x', fudged_name)
        fudged_name = re.sub(r'_\([-+]1\)', '', fudged_name)
        if crew_of_pilot:
            fudged_name += '_(Crew)'
        # Stupid Nien Nunb is a stupid special case
        elif fudged_name == 'Nien_Nunb':
            fudged_name += '_(T-70_X-Wing)'
        # All Hera's are suffixed on the wiki
        elif fudged_name == 'Hera_Syndulla':
            fudged_name += '_(VCX-100)'
        elif re.match(r'"Heavy_Scyk"_Interceptor', fudged_name):
            fudged_name = '"Heavy_Scyk"_Interceptor'
        url = f"http://xwing-miniatures.wikia.com/wiki/{fudged_name}"
        return cls.link(url, card_name)

    @staticmethod
    def link(url, name):
        return f"<{url}|{name}>"
