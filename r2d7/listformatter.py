from html import unescape
import logging
import re
import json
from enum import Enum

import requests

from r2d7.core import DroidCore, DroidException

logger = logging.getLogger(__name__)

class Legality(Enum):
    standard = "Standard"
    extended = "Extended"
    epic = "Epic"
    banned = "Banned"


class ListLegality:
    def __init__(self, legality=Legality.epic):
        self.legality = legality

    def update(self, standard=False, extended=False, epic=True):
        """
        Decrease list legality Standard -> Extended -> Epic -> Banned
        This function makes the following assumptions:
        - everything legal in standard is legal in extended,
        - everything legal in extended is legal in epic
        """
        if self.legality == Legality.standard and standard == False:
            self.legality = Legality.extended
        if self.legality == Legality.extended and extended == False:
            self.legality = Legality.epic
        if self.legality == Legality.epic and epic == False:
            self.legality = Legality.banned


class ListFormatter(DroidCore):

    def __init__(self):
        super().__init__()
        # The leading and trailing < and > are for Slack
        self.register_handler(r'<?(https?://[^>]+)>?', self.handle_url)

    _regexes = (
        re.compile(r'(https?://(yasb)\.app/(?:[^?/]*/)?\?(.*))'),
        re.compile(
            r'(https://(launchbaynext)\.app/[a-z]*\?lbx=([^&]+)(?:&mode=[a-z]+)?)'),
        re.compile( # legacy LBN app links
            r'(https://(launch-bay-next)\.herokuapp\.com/[a-z]*\?lbx=([^&]+)(?:&mode=[a-z]+)?)'),
    )

    def get_xws(self, message):
        match = None
        for regex in self._regexes:
            match = regex.match(message)
            if match:
                break
        else:
            logger.debug(f"Unrecognised URL: {message}")
            return None

        xws_url = None
        if match[2] == 'yasb':
            xws_url = f"http://squad2xws.herokuapp.com/yasb/xws/?{match[3]}"
        if match[2] == 'launchbaynext':
            xws_url = f"https://launchbaynext.app/api/xws?lbx={match[3]}"

        if xws_url:
            xws_url = unescape(xws_url)
            logging.info(f"Requesting {xws_url}")
            response = requests.get(xws_url)
            if response.status_code != 200:
                raise DroidException(
                    f"Got {response.status_code} GETing {xws_url}")
            data = response.json()
            if 'message' in data:
                raise DroidException(f"YASB error: ({data['message']}")
            return data

    def get_pilot_cards(self, pilot):
        cards = []
        if 'upgrades' in pilot:
            for slot, upgrades in pilot['upgrades'].items():
                # Hardpoint is a fake slot used to implement the scyk ship ability - but needs to work for Epic ships!
                if slot == 'hardpoint' and pilot['ship'] in {'t70xwing', 'm3ainterceptor'}:
                    continue
                for upgrade in upgrades:
                    try:
                        cards.append(self.data['upgrade'][upgrade])
                    except KeyError:
                        cards.append(None)
        return cards

    def get_upgrade_cost(self, pilot_card, upgrade):
        cost = upgrade.get('cost', {})
        if 'variable' in cost:
            if cost['variable'] == 'size':
                stat = pilot_card['ship']['size']
            elif cost['variable'] in pilot_card:
                stat = pilot_card[cost['variable']]
            else:
                stat = 0
                for stat_block in pilot_card['ship']['stats']:
                    if stat_block['type'] == cost['variable']:
                        stat = stat_block['value']
                        break
            return cost['values'][str(stat)]
        else:
            return cost.get('value', 0)

    def print_xws(self, xws, url=None):
        name = xws.get('name', 'Nameless Squadron')
        if 'vendor' in xws:
            if len(list(xws['vendor'].keys())) > 1:
                logger.warning(f"More than one vendor found! {xws['vendor']}")
            vendor = list(xws['vendor'].values())
            if len(vendor) > 0:
                vendor = vendor[0]
                if 'link' in vendor:
                    url = vendor['link']
        if url:
            name = self.link(url, name)
        name = self.bold(name)
        output = [f"{self.iconify(xws['faction'])} {name} "]
        squad_points = 0
        legality = ListLegality(Legality.standard)

        for pilot in xws['pilots']:
            try:
                pilot_name = pilot['id']
            except KeyError:
                pilot_name = pilot['name']
            try:
                pilot_card = self.data['pilot'][pilot_name]
            except KeyError:
                # Unrecognised pilot
                output.append(self.iconify('question') * 2 + ' ' +
                        self.italics('Unknown Pilot: ' + pilot_name))
                continue
            pilot_points = pilot_card.get('cost', 0)
            loadout_used = 0
            loadout_total = pilot_card.get('loadout', 0)
            initiative = pilot_card['initiative']

            legality.update(pilot_card.get('standard', False), pilot_card.get('extended', False),
                    epic = pilot_card.get('epic', False))

            cards = self.get_pilot_cards(pilot)
            upgrades = []
            for upgrade in cards:
                if upgrade is None:
                    upgrades.append(self.bold('Unrecognised Upgrade'))
                    continue

                upgrade_text = self.wiki_link(upgrade['name'])
                upgrades.append(upgrade_text)
                loadout_used += self.get_upgrade_cost(pilot_card, upgrade)
                legality.update(upgrade.get('standard', False), upgrade.get('extended', False),
                        epic = upgrade.get('epic', False))

            ship_line = (
                self.iconify(pilot_card['ship']['name']) +
                self.iconify(f"initiative{initiative}") +
                f" {self.italics(self.wiki_link(pilot_card['name']))}"
            )
            if upgrades:
                ship_line += ':' + f" {', '.join(upgrades)}"
            ship_line += ' ' + self.bold(f"[{pilot_points}]") + f"[{loadout_used}/{loadout_total}]"

            output.append(ship_line)
            squad_points += pilot_points

        output[0] += self.bold(f"[{squad_points}]")
        if (legality.legality != Legality.banned):
            output[0] += " " + self.bold(f"[{legality.legality.value}]")
        return [output]

    def handle_url(self, message):
        match = self.formatted_link_regex.match(message)
        if match:
            message = match['url']
        xws = self.get_xws(message)
        logger.debug(xws)
        if xws:
            return self.print_xws(xws, url=message)
        return []
