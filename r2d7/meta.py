from enum import Enum
import logging
import re
import requests
from r2d7.core import DroidCore

logger = logging.getLogger(__name__)

class Metawing(DroidCore):
    """
    Handler class, contains slack chat logic
    """
    match_base = '!(hyper)?meta'
    list_handler = re.compile(match_base + '.*', re.I)
    pilot_handler = re.compile(match_base + '\s*pilot.*', re.I)
    ship_handler = re.compile(match_base + '\s*ship.*', re.I)
    upgrade_handler = re.compile(match_base + '\s*upgrade.*', re.I)
    meta_handler = re.compile(match_base + '\s*meta.*', re.I)

    _base_url = 'https://meta.listfortress.com'
    _list_path = '/ship_combos'
    _pilot_path = '/pilots'
    _ship_path = '/ships'
    _upgrade_path = '/upgrades'

    _query_error = 'Error querying metawing. Perhaps the archives are incomplete'

    def __init__(self):
        super().__init__()
        self.register_handler(Metawing.list_handler, self.lists)
        self.register_handler(Metawing.pilot_handler, self.pilots)
        self.register_handler(Metawing.ship_handler, self.ships)
        self.register_handler(Metawing.upgrade_handler, self.upgrades)
        self.register_handler(Metawing.meta_handler, self.meta)

    def query_and_print(self, url, printer, num_to_print=5):
        try:
            result = requests.get(url)
            if !result.ok
                return [self._query_error]
            json = result.json()
            output = []
            # TODO maybe add numbers here?
            for item in json[0:num_to_print]:
                output += printer(item)
            return output
        except:
            return [self._query_error]

    def lists(self, message):
        url = self._base_url + self._list_path
        return self.query_and_print(url, list_printer, 3)

    def pilots(self, message):
        url = self._base_url + self._pilot_path
        return self.query_and_print(url, pilot_printer)

    def ships(self, message):
        url = self._base_url + self._ship_path
        return self.query_and_print(url, ship_printer)

    def upgrades(self, message):
        url = self._base_url + self._upgrade_path
        return self.query_and_print(url, upgrade_printer)

    def meta(self, message):
        return ['Woah dude']

    def list_printer(self, meta_list):
        output = name_link_printer(meta_list) + ''
        for ship in meta_list.get("ships", []):
            icon
            output += self.iconify(ship.get('xws', 'question'))
        output += '\n' + score_printer(meta_list)
        return output

    def pilot_printer(self, pilot):
        ship = pilot.get('ship', {})
        # TODO should probably use a more robust method than slapping the ship name into iconify
        output = self.iconify(ship.get('name', 'question'), True)
        output += ' ' + name_link_printer(pilot)
        output += '\n' + score_printer(pilot)
        return output

    def ship_printer(self, ship):
        output = name_link_printer(ship) + ''
        output += self.iconify(ship.get('xws', 'question'))
        output += '\n' + score_printer(ship)
        return output

    def upgrade_printer(self, upgrade):
        output = name_link_printer(upgrade) + ''
        # TODO add upgrade type icon
        # TODO put icon before name
        output += '\n' + score_printer(upgrade)
        return output

    def name_link_printer(self, data):
        listName = meta_list.get('name', '(unnamed)')
        listUrl = meta_list.get('link', '')
        if listUrl == '':
            return listName
        return self.link(listUrl, listName)

    def score_printer(self, data):
        average = data.get('average_percentile', '?')
        weight = data.get('weight', '?')
        return f'Average: {average}, Weighted: {weight}'
