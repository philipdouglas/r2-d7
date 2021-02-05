from enum import Enum
import logging
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

    _data_url = 'https://github.com/guidokessels/xwing-data2'
    _r2d7_url = 'https://github.com/FreakyDug/r2-d7'

    def __init__(self):
        super().__init__()
        self.register_handler(Talkback.pattern_fix, self.fixHandler)
        self.register_handler(Talkback.pattern_typo, self.fixHandler)
        self.register_handler(Talkback.pattern_data, self.dataHandler)

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

