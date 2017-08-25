from pathlib import Path
import re
import unicodedata

import requests


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

    def load_data(self):
        self._data = {}
        self.data_version = None
        for filename in self.DATA_FILES:
            #TODO damage cards
            #TODO reference cards
            file_url = f"{self.BASE_URL}{filename}.js"
            response = requests.get(file_url)
            if response.status_code != 200:
                raise DroidException(
                    f"Got {response.status_code} GETing {file_url}.")

            if self.data_version is None:
                match = re.search(r'xwing-data@([\d\.]+)\/', response.url)
                self.data_version = match.group(1)

            self._data[filename] = group = {}
            for datum in response.json():
                group.setdefault(datum['xws'], []).append(datum)

    @property
    def data(self):
        if self._data is None:
            #TODO load from the internet!
            self.load_data()
        return self._data

    @staticmethod
    def partial_canonicalize(string):
        #TODO handle special cases https://github.com/elistevens/xws-spec
        string = string.lower()
        string = unicodedata.normalize('NFKD', string)
        string = re.sub(r'[^a-zA-Z0-9]', '', string)
        return string
