import json
from pathlib import Path
import re


class BotCore():
    def __init__(self):
        pass

    def handle_message(self, message):
        raise NotImplemented()

    # @classmethod
    # def strip_name(name):
    #     return re.sub(r' \(.*\)$', name, )

    # Printer methods
    @staticmethod
    def name_to_icon(name):
        raise NotImplemented()

    @staticmethod
    def bold(text):
        raise NotImplemented()

    @staticmethod
    def italics(text):
        raise NotImplemented()

    @staticmethod
    def convert_html(text):
        return text

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
