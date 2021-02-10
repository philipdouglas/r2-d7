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
    match_base = '!meta'
    pattern_handler = re.compile('(!meta.*)', re.I)
    pattern_pilot = re.compile('pilot', re.I)
    pattern_ship = re.compile('ship', re.I)
    pattern_upgrade = re.compile('upgrade', re.I)
    pattern_meta = re.compile('meta meta', re.I)
    pattern_help = re.compile('(help)|(syntax)', re.I)
    pattern_quantity = re.compile('[0-9]+', re.I)

    _base_url = 'https://meta.listfortress.com'
    _json_suffix = '.json'
    _list_path = '/ship_combos'
    _pilot_path = '/pilots'
    _ship_path = '/ships'
    _upgrade_path = '/upgrades'

    _query_error = 'Error querying metawing. Perhaps the archives are incomplete'

    def __init__(self):
        super().__init__()
        self.register_handler(Metawing.pattern_handler, self.handler)

    def handler(self, message):
        url = self._base_url + self._list_path
        printer = self.list_printer
        if Metawing.pattern_pilot.search(message):
            url = self._base_url + self._pilot_path
            printer = self.pilot_printer
        if Metawing.pattern_ship.search(message):
            url = self._base_url + self._ship_path
            printer = self.ship_printer
        if Metawing.pattern_upgrade.search(message):
            url = self._base_url + self._upgrade_path
            printer = self.upgrade_printer
        if Metawing.pattern_help.search(message):
            return [self.meta_syntax()]
        if Metawing.pattern_meta.search(message):
            return [['Woah dude']]
        qty = 5
        qty_match = Metawing.pattern_quantity.search(message)
        if qty_match:
            qty = min(int(qty_match[0]), 25)
            qty = max(qty, 1)
        return [self.query_and_print(url, printer, qty)]

    def meta_syntax(self):
        output = []
        output.append('Type `!meta` to see the current meta lists. You may add the word `pilot`, `ship` or `upgrade` to see data for that category. You may also specify a number of results, up to 25.')
        output.append('e.g.: `!meta` shows the top 5 lists')
        output.append('e.g.: `!meta pilot 3` shows the top 3 pilots')
        output.append('')
        output.append('This command is intentionally simple and is not intended for in-depth meta analysis.')
        return output

    def query_and_print(self, url, printer, num_to_print=5):
        url = url + self._json_suffix
        try:
            result = requests.get(url)
            if not result.ok:
                logger.debug(f'Failed to get: {url}')
                return [[self._query_error]]
            json = result.json()
            output = []
            i = 1
            for item in json[0:num_to_print]:
                output.append(self.bold(f'{i}.') + ' ' + printer(item))
                i += 1
            return output
        except Exception as e:
            logger.debug(f'Exception while parsing MetaWing from {url}: {e}')
            return [[self._query_error]]

    def list_printer(self, meta_list):
        output = self.name_link_printer(meta_list) + ' '
        for ship in meta_list.get("ships", []):
            output += self.iconify(ship.get('xws', 'question'))
        output += '\n' + self.score_printer(meta_list)
        return output

    def pilot_printer(self, pilot):
        ship = pilot.get('ship', {})
        # TODO should probably use a more robust method than slapping the ship name into iconify
        output = self.name_link_printer(pilot) + ' '
        output += self.iconify(ship.get('name', 'question'))
        output += '\n' + self.score_printer(pilot)
        return output

    def ship_printer(self, ship):
        output = self.name_link_printer(ship) + ''
        output += self.iconify(ship.get('xws', 'question'))
        output += '\n' + self.score_printer(ship)
        return output

    def upgrade_printer(self, upgrade):
        output = self.name_link_printer(upgrade) + ''
        # TODO add upgrade type icon
        # use  cardlookup.lookup(upgradeName) to iterate over matching upgrades
        # then on the first one (that is an upgrade) try the slot field for some
        # iconifiable text - can possibly do same for ships?
        output += '\n' + self.score_printer(upgrade)
        return output

    @classmethod
    def name_link_printer(cls, data):
        name = data.get('name', '(unnamed)')
        if name is None or name == 'None':
            name = '(unnamed)'
        url = data.get('link', '')
        if url == '':
            return name
        url = re.sub('.json$', '', url)
        return cls.link(url, name)

    @staticmethod
    def score_printer(data):
        average = data.get('average_percentile', '?')
        weight = float(data.get('weight', '?'))*100
        return f'Average: {average:.0f}%, Weighted: {weight:.0f}%'
