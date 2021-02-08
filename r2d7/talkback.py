from enum import Enum
import logging
import random
import re
import requests
from r2d7.core import DroidCore

logger = logging.getLogger(__name__)

class Talkback(DroidCore):
    """
    Chat responses unrelated to other commands
    """
    pattern_fix = re.compile('(!fix)', re.I)
    pattern_typo = re.compile('(!typo)', re.I)
    pattern_data = re.compile('(!data)', re.I)
    pattern_stitch = re.compile('(!stitch ?crew)', re.I)

    _data_url = 'https://github.com/guidokessels/xwing-data2'
    _r2d7_url = 'https://github.com/FreakyDug/r2-d7'

    def __init__(self):
        super().__init__()
        self.register_handler(Talkback.pattern_fix, self.fixHandler)
        self.register_handler(Talkback.pattern_typo, self.fixHandler)
        self.register_handler(Talkback.pattern_data, self.dataHandler)
        self.register_handler(Talkback.pattern_stitch, self.stitchCrewHandler)

    def fixHandler(self, message):
        dataErrorText = 'For issues with card data, raise an issue or pull request at '
        dataErrorText += self.link(self._data_url, self._data_url)
        squadErrorText = 'For issues with squad lists, raise an issue at '
        squadErrorText += self.link(self._r2d7_url, self._r2d7_url)
        return [[dataErrorText, squadErrorText]]

    def dataHandler(self, message):
        text = 'X-Wing card data taken from '
        text += self.link(self._data_url, self._data_url)
        return [[text]]

    def stitchCrewHandler(self, message):
        # Commented-out responses are intentionally disabled for the time being
        lines = [
                    ['Stitch who?'],
                    ['Coming soon...'],
                    #['STITCH CREW!'],
                    #[':sewing_needle::crew:'],
                    #[
                    #    f':crew::crew::crew::crew:• {self.bold("Stitch Crew")} [0]',
                    #    'Pew Pew Pew'
                    #],
                    #[
                    #    self.bold('Stitch Crew'),
                    #    '4 players, 200pts, 2 ships per player, 2 obstacles per player. First player is random and player order proceeds clockwise.',
                    #    f'{self.bold("Setup:")} Players place obstacles in player order until 6 obstacles have been placed. Players deploy ships within range 3 of their assigned table corner and range 1 of the table edge.',
                    #    f'{self.bold("Rules:")} The last surviving player wins the game. Alliances are forbidden, but table talk is encouraged. When a ship engages, if it has one or more valid enemy targets, it must shoot.'
                    #]
                ]
        return [random.choice(lines)]

