from html import unescape
import logging
import re
import json

import requests

from r2d7.core import DroidCore, DroidException

logger = logging.getLogger(__name__)


class ListFormatter(DroidCore):
    _hyperspace_check_url = 'https://launchbaynext.app/api/hyperspace'

    def __init__(self):
        super().__init__()
        # The leading and trailing < and > are for Slack
        self.register_handler(r'<?(https?://[^>]+)>?', self.handle_url)

    _regexes = (
        re.compile(r'(https?://(raithos)\.github\.io/\?(.*))'),
        re.compile(r'(https?://(danrs)\.github\.io/xwing/\?(.*))'),
        re.compile(
            r'(https://(squadbuilder)\.fantasyflightgames\.com/squad-preview/([a-zA-Z0-9\-]+))'),
        re.compile(
            r'(https://devjonny\.github\.io/(xwing2estopgap)/[a-z]+\?id=([a-zA-Z0-9\-]+))'),
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
        if match[2] == 'raithos':
            xws_url = f"http://squad2xws.herokuapp.com/yasb/xws/?{match[3]}"
        if match[2] == 'danrs':
            xws_url = f"http://squad2xws.herokuapp.com/yasb/xws/?{match[3]}"
        if match[2] == 'squadbuilder':
            xws_url = f"http://squad2xws.herokuapp.com/translate/{match[3]}"
        if match[2] == 'launchbaynext':
            xws_url = f"https://launchbaynext.app/api/xws?lbx={match[3]}"
        if match[2] == 'launch-bay-next': # legacy LBN app
            xws_url = f"https://launch-bay-next.herokuapp.com/xws?lbx={match[3]}"

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

    def check_hyperspace_legal(self, xws):
        r = requests.post(self._hyperspace_check_url, json=xws)
        if r.status_code == 200:
            return True
        if r.status_code != 400:
            # 400 means query succeeded but list was not hyperspace legal, other response codes indicate error
            logger.warning(f"HTTP Error {r.status_code} while checking hyperspace, reason: {r.reason}, xws: {xws}")
        return False

    def get_pilot_cards(self, pilot):
        cards = []
        if 'upgrades' in pilot:
            for slot, upgrades in pilot['upgrades'].items():
                # Hardpoint is a fake slot used to implement the scyk ship ability
                if slot == 'hardpoint':
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

    def print_xws(self, xws, hyperspace=False, url=None):
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
        total_points = 0

        for pilot in xws['pilots']:
            points = 0
            try:
                pilot_name = pilot['id']
            except KeyError:
                pilot_name = pilot['name']
            try:
                pilot_card = self.data['pilot'][pilot_name]
            except KeyError:
                # Unrecognised pilot
                output.append(self.iconify('question') * 2 + ' ' +
                              self.italics('Unknown Pilot'))
                continue
            points += pilot_card.get('cost', 0)
            initiative = pilot_card['initiative']

            cards = self.get_pilot_cards(pilot)

            upgrades = []
            for upgrade in cards:
                if upgrade is None:
                    upgrades.append(self.bold('Unrecognised Upgrade'))
                    continue

                upgrade_text = self.wiki_link(upgrade['name'])
                upgrades.append(upgrade_text)
                points += self.get_upgrade_cost(pilot_card, upgrade)

            ship_line = (
                self.iconify(pilot_card['ship']['name']) +
                self.iconify(f"initiative{initiative}") +
                f" {self.italics(self.wiki_link(pilot_card['name']))}"
            )
            if upgrades:
                ship_line += ':' + f" {', '.join(upgrades)}"
            ship_line += ' ' + self.bold(f"[{points}]")

            output.append(ship_line)
            total_points += points

        output[0] += self.bold(f"[{total_points}]")
        if hyperspace:
            output[0] += " " + self.bold(f"[Hyperspace]")
        return [output]

    def handle_url(self, message):
        match = self.formatted_link_regex.match(message)
        if match:
            message = match['url']
        xws = self.get_xws(message)
        hyperspace = self.check_hyperspace_legal(xws)
        logger.debug(xws)
        if xws:
            return self.print_xws(xws, hyperspace, url=message)
        return []
