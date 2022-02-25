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
    pattern_fix = re.compile('^!((fix)|(typo))', re.I)
    pattern_data = re.compile('^!(data)', re.I)
    pattern_help = re.compile('^!(help)', re.I)
    pattern_stitchCrew = re.compile('^!(stitch ?crew)', re.I)
    pattern_egg = re.compile('^!((egg)|(sooga))', re.I)

    _data_url = 'https://github.com/guidokessels/xwing-data2'
    _r2d7_url = 'https://github.com/FreakyDug/r2-d7'

    def __init__(self):
        super().__init__()
        self.register_handler(Talkback.pattern_fix, self.fixHandler)
        self.register_handler(Talkback.pattern_data, self.dataHandler)
        self.register_handler(Talkback.pattern_help, self.helpHandler)
        self.register_handler(Talkback.pattern_stitchCrew, self.stitchCrewHandler)
        self.register_handler(Talkback.pattern_egg, self.eggHandler)

    def fixHandler(self, message):
        dataErrorText = 'For issues with card data, raise an issue or pull request at '
        dataErrorText += self.link(self._data_url, self._data_url)
        squadErrorText = 'For issues with bot behaviour or squad lists, raise an issue or pull request at '
        squadErrorText += self.link(self._r2d7_url, self._r2d7_url)
        return [[dataErrorText, squadErrorText]]

    def dataHandler(self, message):
        text = 'X-Wing card data taken from '
        text += self.link(self._data_url, self._data_url)
        return [[text]]

    def helpHandler(self, message):
        return [[self.helpMessage()]]

    def stitchCrewHandler(self, message):
        lines = [
                    ['Stitch who?'],
                    ['STITCH CREW!'],
                    [':sewing_needle::crew:'],
                    [
                        self.bold('Stitch Crew'),
                        '4 players, 200pts, 2 ships per player, 2 obstacles per player. First player is random and player order proceeds clockwise.',
                        f'{self.bold("Setup:")} Players place obstacles in player order until 6 obstacles have been placed. Players deploy ships within range 3 of their assigned table corner and range 1 of the table edge.',
                        f'{self.bold("Rules:")} The last surviving player wins the game. Alliances are forbidden, but table talk is encouraged. When a ship engages, if it has one or more valid enemy targets, it must shoot.'
                    ]
                ]
        return [random.choice(lines)]

    def eggHandler(self, message):
        lines = [
                    ['Sooga! Sooga! Sooga!'],
                    ['Utinni!'],
                    [':egg:'],
                    ['Maclunkey!'],
                ]
        return [random.choice(lines)]

