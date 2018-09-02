import asyncio
import logging
import json
from pathlib import Path
import re
import time
import unicodedata

import requests

logger = logging.getLogger(__name__)


class DroidException(Exception):
    pass


class DroidCore():
    def __init__(self):
        self._handlers = {}
        self._dm_handlers = {}

    def register_handler(self, pattern, method):
        if not isinstance(pattern, re._pattern_type):
            pattern = re.compile(pattern)
        self._handlers[pattern] = method

    def register_dm_handler(self, pattern, method):
        if not isinstance(pattern, re._pattern_type):
            pattern = re.compile(pattern)
        self._dm_handlers[pattern] = method

    def handle_message(self, message):
        raise NotImplementedError()

    # Printer methods
    @staticmethod
    def iconify(name):
        raise NotImplementedError()

    @staticmethod
    def bold(text):
        raise NotImplementedError()

    @staticmethod
    def italics(text):
        raise NotImplementedError()

    @staticmethod
    def convert_html(text):
        return text

    @classmethod
    def wiki_link(cls, card_name, crew_of_pilot, wiki_name=False):
        raise NotImplementedError()

    @staticmethod
    def link(url, name):
        raise NotImplementedError()

    _data = None
    BASE_URL = 'https://raw.githubusercontent.com/andrelind/xwing-data2/restrictions/'
    MANIFEST = 'data/manifest.json'
    # VERSION_RE = re.compile(r'xwing-data/releases/tag/([\d\.]+)')
    check_frequency = 900  # 15 minutes

    @classmethod
    def get_file(cls, filepath):
        return filepath, requests.get(cls.BASE_URL + filepath)

    @classmethod
    def get_version(cls):
        res = requests.get(
            'https://api.github.com/repos/andrelind/xwing-data2/branches/restrictions')
        if res.status_code != 200:
            logger.warning(f"Got {res.status_code} checking data version.")
            return False
        return res.json()['commit']['sha']

    async def _load_data(self):
        res = requests.get(self.BASE_URL + self.MANIFEST)
        if res.status_code != 200:
            raise DroidException( f"Got {res.status_code} GETing {res.url}.")
        manifest = res.json()

        files = (
            manifest['damagedecks'] +
            manifest['upgrades'] +
            [manifest['conditions']] +
            [ship for faction in manifest['pilots']
                for ship in faction['ships']]
        )

        self._data = {}
        self.data_version = None
        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(
                None,
                self.get_file,
                filename,
            )
            for filename in files
        ]

        self.data_version = self.get_version()
        self._last_checked_version = time.time()

        for filepath, res in await asyncio.gather(*futures):
            if res.status_code != 200:
                raise DroidException(
                    f"Got {res.status_code} GETing {res.url}.")

            _, category, remaining = filepath.split('/', maxsplit=2)

            raw_data = res.json()

            if category == 'upgrades':
                for card in raw_data:
                    self.add_card('upgrade', card,
                                  subcat=remaining.split('.')[0])

            elif category == 'pilots':
                ship = raw_data
                ship['xws'] = remaining.split('/')[1][:-5].replace('-', '')
                for pilot in ship['pilots']:
                    pilot['ship'] = ship
                    self.add_card('pilot', pilot)
                self.add_card('ship', ship)

            elif category == 'damage-decks':
                for card in raw_data['cards']:
                    card['name'] = card['title']
                    card['xws'] = self.partial_canonicalize(card['name'])
                    card['deck'] = remaining[:-5]
                    self.add_card('damage', card)

            elif category == 'conditions':
                for card in raw_data:
                    self.add_card('condition', card)


    def add_card(self, category, card, subcat=None):
        card['category'] = subcat or category
        category = self._data.setdefault(category, {})
        category.setdefault(card['xws'], []).append(card)

    def load_data(self):
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            # If we don't run in the main Thread, there won't be an event loop
            # yet, so make one
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        loop.run_until_complete(self._load_data())

    _last_checked_version = None

    def needs_update(self):
        if (time.time() - self._last_checked_version) < self.check_frequency:
            logger.debug("Checked version recently.")
            return False

        current_version = self.get_version()
        logger.debug(f"Current xwing-data version: {current_version}")
        self._last_checked_version = time.time()
        return self.data_version != current_version

    @property
    def data(self):
        if self._data is None:
            self.load_data()
        return self._data

    @staticmethod
    def partial_canonicalize(string):
        #TODO handle special cases https://github.com/elistevens/xws-spec
        string = string.lower()
        string = unicodedata.normalize('NFKD', string)
        string = re.sub(r'[^a-zA-Z0-9]', '', string)
        return string


def long_substr(data):
    """
    From: https://stackoverflow.com/a/2894073/1424112
    """
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and all(data[0][i:i+j] in x for x in data):
                    substr = data[0][i:i+j]
    return substr
