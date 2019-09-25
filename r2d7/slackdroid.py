import html
import logging
import re
from urllib.parse import quote

from r2d7.core import DroidCore


logger = logging.getLogger(__name__)


class SlackDroid(DroidCore):
    def __init__(self):
        super().__init__()
        self.load_data()

    def load_data(self):
        super().load_data()

        # References to conditions and ship abilities are highlighted
        self._ref_names = set()
        for card in self.data['condition'].values():
            self._ref_names.add(card['name'])
        for card in self.data['pilot'].values():
            if 'shipAbility' in card:
                self._ref_names.add(card['shipAbility']['name'])

        # Convert text now to save time later
        for category, names in self.data.items():
            for card in names.values():
                if 'sides' in card:
                    for side in card['sides']:
                        if 'ability' in side:
                            side['ability'] = self.convert_text(
                                side['ability'])
                        if 'device' in side:
                            side['device']['effect'] = self.convert_text(
                                side['device']['effect'])
                if 'ability' in card:
                    card['ability'] = self.convert_text(card['ability'])
                if 'shipAbility' in card:
                    card['shipAbility']['text'] = self.convert_text(
                        card['shipAbility']['text'])
                if category == 'damage':
                    card['text'] = self.convert_text(card['text'])

    help = """\
I am R2-D7, xwingtmg.slack.com's bot.
*List Printing:* If you paste a (Yet Another) Squad Builder, Official FFG or X-Wing 2E Stop Gapp permalink into a channel I'm in (or direct message me one), I will print a summary of the list.
*Card Lookup:* Type something surrounded by square brackets and I will describe any upgrades, ships or pilots that match what you said. (Eg. Why not try [[Engine Upgrade]])
If you only want cards in a particular slot or ship, begin your lookup with the emoji for that ship or slot. (eg. _[[:crew: rey]]_)
You can also search for cards by points value in a particular slot. Eg. _[[:crew: <=3]]_. =, <, >, <= and >= are supported.
*Dice Rolling:* If you type `!roll` followed by a number and a dice color, I'll roll dice for you. Type `!roll syntax` for full syntax.
"""

    filter_pattern = re.compile(
        r' *(?:(:[^:]+:))? *(?:([^=><:]*[^=><: ][^=><:]*)|([=><][=><]?)'
        r' *(\d+)) *(?:(:[^:]+:))? *'
    )
    faction_icon_pattern = r':(rebel|resistance|scum|imperial|first_order):'

    @staticmethod
    def iconify(name, special_chars=False):
        name = name.lower()
        if special_chars:
            name = re.sub(r'[^a-zA-Z0-9\-\_]', '', name)
        else:
            name = re.sub(r'[^a-zA-Z0-9]', '', name)
        name = name.replace('+', 'plus')
        if name in ['bomb', 'shield']:
            name = 'x' + name
        # Lock is a standard emoji, so we'll stick with targetlock for 2.0
        elif name == 'lock':
            name = 'targetlock'
        elif name == 'rebelalliance':
            name = 'rebel'
        elif name == 'scumandvillainy':
            name = 'scum'
        elif name == 'galacticempire':
            name = 'imperial'
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
        re.compile(r'\[Stationary\]'): ':stop:',
        re.compile(r'\[Critical Hit\]'): ':crit:',
        re.compile(r'\[Bomb\]'): ':xbomb:',
        re.compile(r'\[Barrel Roll\]'): ':barrelroll:',
        # :lock: is a default Slack emoji, so we'll stick with targetlock for 2.0
        re.compile(r'\[Lock\]'): ':targetlock:',
        re.compile(r'\[Force\]'): ':forcecharge:',
        re.compile(r'\[Rear Arc\]'): ':reararc:',
        re.compile(r'\[Front Arc\]'): ':frontarc:',
        re.compile(r'\[Left Arc\]'): ':leftarc:',
        re.compile(r'\[Right Arc\]'): ':rightarc:',
        re.compile(r'\[Bullseye Arc\]'): ':bullseyearc:',
        re.compile(r'\[Single Turret Arc\]'): ':singleturretarc:',
        re.compile(r'\[Double Turret Arc\]'): ':doubleturretarc:',
        re.compile(r'\[Rotate Arc\]'): ':rotatearc:',
        re.compile(r'(Ship|Pilot) damage card'): '_*\\1*_ damage card',
        re.compile(r'^(Bomb|Mine)'): '_*\\1:*_',
    }

    _bold_words = [
        'must',
    ]

    def convert_text(self, text):
        """
        The data has HTML formatting tags, convert them to slack formatting.
        """
        if text == 'Attack':
            return [self.bold('Attack')]
        text = re.sub(r'\b([A-Z][A-Za-z ]+:)', '__BREAK__*\\1*', text)
        for regex, sub in self._data_to_emoji.items():
            text = regex.sub(sub, text)
        for card_name in self._ref_names:
            text = text.replace(card_name, self.italics(self.bold(card_name)))
        text = re.sub(f"\\b({'|'.join(self._bold_words)})\\b", '*\\1*', text)
        text = re.sub(r'\[([^\[\]:]+)\]', lambda pat: f":{pat.group(1).lower()}:", text)
        lines = text.split('__BREAK__')
        return [line.strip() for line in lines if line != '']

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
        fudged_name = quote(fudged_name)
        url = f"http://xwing-miniatures-second-edition.wikia.com/wiki/{fudged_name}"
        return cls.link(url, card_name)

    @staticmethod
    def link(url, name):
        return f"<{url}|{name}>"
