from itertools import groupby
import logging
import re

import dateutil.parser

from r2d7.core import DroidCore, DroidException

logger = logging.getLogger(__name__)


class WaveLister(DroidCore):
    def __init__(self):
        super().__init__()
        pattern = re.compile(r'\[\[wave +(\d+|iconic starships)\]\]', re.I)
        self.register_handler(pattern, self.handle_wave)

    def print_wave(self, wave):
        lines = []

        if wave.lower() == 'iconic starships':
            wave = 'Iconic Starships'
            title = self.bold(wave)
        else:
            wave = int(wave)
            title = self.bold(f"Wave {wave}")
        lines.append(title)

        packs = (pack for pack in self.raw_data['sources']
                 if pack['wave'] == wave)

        def keyfunc(pack):
            return pack.get('release_date', 'Unreleased')
        date_groups = [(date, list(packs)) for date, packs in
                       groupby(sorted(packs, key=keyfunc), key=keyfunc)]
        for date, packs in date_groups:
            if date != 'Unreleased':
                date = dateutil.parser.parse(date).strftime("%B %Y")

            packs = list(packs)
            if len(date_groups) == 1:
                lines[0] += f' - {date}'
            elif len(packs) > 1:
                lines.append(date)

            for pack in packs:
                ships = []
                if len(pack['contents']['ships']) == 1:
                    ship_id, qty = list(pack['contents']['ships'].items())[0]
                    ship = self.raw_data['ships'][int(ship_id)]
                    if ship['name'] not in pack['name'] or qty > 1:
                        ships.append((ship, qty))
                else:
                    ships = [(self.raw_data['ships'][int(ship_id)], qty)
                             for ship_id, qty in pack['contents']['ships'].items()]
                ships = [ship['name'] + (f" x{qty}" if qty > 1 else '')
                         for ship, qty in ships]
                ships = f" ({', '.join(ships)})" if ships else ''
                line_date = f' - {date}' if len(packs) == 1 else ''
                lines.append(
                    f"- {self.wiki_link(pack['name'])}{ships}{line_date}")

        return lines

    def handle_wave(self, message):
        logger.debug("Listing wave {message}")
        return self.print_wave(message)
