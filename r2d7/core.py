import json
from pathlib import Path
import re
import unicodedata


class DroidException(Exception):
    pass


class DroidCore():
    def __init__(self):
        self._handlers = {}

    def register_handler(self, pattern, method):
        self._handlers[re.compile(pattern)] = method

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

    @property
    def data(self):
        if self._data is None:
            self._data = {}
            #TODO load from the internet!
            for path in Path('xwing-data/data').glob('*.js'):
                if 'sources' in path.name:
                    continue
                #TODO canonicalise names for damage cards
                #TODO reference cards
                if 'damage-deck' in path.name or 'reference' in path.name:
                    continue

                with path.open(encoding='utf-8') as json_file:
                    self._data[path.name.split('.')[0]] = group = {}
                    for datum in json.load(json_file):
                        group.setdefault(datum['xws'], []).append(datum)
        return self._data

    @staticmethod
    def partial_canonicalize(string):
        #TODO handle special cases https://github.com/elistevens/xws-spec
        string = string.lower()
        string = unicodedata.normalize('NFKD', string)
        string = re.sub(r'[^a-zA-Z0-9]', '', string)
        return string
