import copy
from html import unescape
from itertools import chain
import logging
import re

import dateutil.parser

from r2d7.core import DroidCore, DroidException

logger = logging.getLogger(__name__)


class WaveLister(DroidCore):
    def __init__(self):
        super().__init__()
        self.register_handler(
            r'\[\[[Ww][Aa][Vv][Ee] +(\d+|[Ii]conic [Ss]tarships)\]\]', self.handle_wave)


    def print_wave(self, wave):
        lines = []

        if wave.lower() == 'iconic starships':
            wave = 'Iconic Starships'
            title = self.bold(wave)
        else:
            wave = int(wave)
            title = self.bold(f"Wave {wave}")


        packs = [pack for pack in self._raw_data['sources']
                 if pack['wave'] == wave]
        dates = sorted({pack['release_date'] for pack in packs
                       if 'release_date' in pack})
        dates = [dateutil.parser.parse(date).strftime("%B %Y")
                 for date in dates]
        if not dates:
            dates = ['Unreleased']

        lines.append(f"{title} - {', '.join(dates)}")

        for pack in packs:
            ships = []
            if len(pack['contents']['ships']) == 1:
                ship_id, qty = list(pack['contents']['ships'].items())[0]
                ship = self._raw_data['ships'][int(ship_id)]
                if ship['name'] not in pack['name']:
                    ships.append((ship, qty))
            else:
                ships = [(self._raw_data['ships'][int(ship_id)], qty)
                         for ship_id, qty in pack['contents']['ships'].items()]
            ships = [ship['name'] + (f" x{qty}" if qty > 1 else '')
                     for ship, qty in ships]
            ships = f" ({', '.join(ships)})" if ships else ''
            lines.append(
                f"- {self.wiki_link(pack['name'])}{ships}")

        return lines

    def handle_wave(self, message):
        logger.debug("Listing wave {message}")
        return self.print_wave(message)
