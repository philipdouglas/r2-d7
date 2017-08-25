import logging
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
        self._handlers[re.compile(pattern)] = method

    def register_dm_handler(self, pattern, method):
        self._dm_handlers[re.compile(pattern)] = method

    def handle_message(self, message):
        raise NotImplementedError()

    # Printer methods
    @staticmethod
    def name_to_icon(name):
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
    BASE_URL = 'https://unpkg.com/xwing-data@latest/data/'
    DATA_FILES = (
        'pilots',
        'ships',
        'upgrades',
        'conditions',
    )
    VERSION_RE = re.compile(r'xwing-data@([\d\.]+)')
    check_frequency = 900  # 15 minutes

    def load_data(self):
        self._data = {}
        self.data_version = None
        for filename in self.DATA_FILES:
            #TODO damage cards
            #TODO reference cards
            file_url = f"{self.BASE_URL}{filename}.js"
            res = requests.get(file_url)
            if res.status_code != 200:
                raise DroidException(
                    f"Got {res.status_code} GETing {file_url}.")

            if self.data_version is None:
                match = self.VERSION_RE.search(res.url)
                self.data_version = match.group(1)
                self._last_checked_version = time.time()
                logger.info(f"Loaded xwing-data version {self.data_version}")

            self._data[filename] = group = {}
            for datum in res.json():
                group.setdefault(datum['xws'], []).append(datum)

    _last_checked_version = None

    def needs_update(self):
        if (time.time() - self._last_checked_version) < self.check_frequency:
            logger.debug("Checked version recently.")
            return False

        res = requests.head(self.BASE_URL)
        if res.status_code != 302:
            logger.warning(f"Got {res.status_code} checking data version.")
            return False

        current_version = self.VERSION_RE.search(res.headers['Location'])[1]
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
