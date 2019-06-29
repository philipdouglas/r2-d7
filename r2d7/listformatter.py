from html import unescape
import logging
import re
import json

import requests

from r2d7.core import DroidCore, DroidException

logger = logging.getLogger(__name__)


class ListFormatter(DroidCore):
    def __init__(self):
        super().__init__()
        # The leading and trailing < and > are for Slack
        self.register_handler(r'<?(https?://[^>]+)>?', self.handle_url)

    _regexes = (
        re.compile(r'(https?://(raithos)\.github\.io/\?(.*))'),
        re.compile(
            r'(https://(squadbuilder)\.fantasyflightgames\.com/squad-preview/([a-zA-Z0-9\-]+))'),
        re.compile(
            r'(https://devjonny\.github\.io/(xwing2estopgap)/[a-z]+\?id=([a-zA-Z0-9\-]+))'),
        re.compile(
            r'(https://(launch-bay-next)\.herokuapp\.com/[a-z]+\?lbx=([^&]+)(?:&mode=[a-z]+)?)'),
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
            xws_url = f"https://yasb2-xws.herokuapp.com/?{match[3]}"
        if match[2] == 'squadbuilder':
            xws_url = f"http://sb2xws.herokuapp.com/translate/{match[3]}"
        if match[2] == 'xwing2estopgap':
            xws_url = f"https://o8l90u2pyd.execute-api.eu-west-2.amazonaws.com/live/idtoxws?id={match[3]}"
        if match[2] == 'launch-bay-next':
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

    def print_xws(self, xws, url=None):
        name = xws.get('name', 'Nameless Squadron')
        if 'vendor' in xws:
            if len(list(xws['vendor'].keys())) > 1:
                logger.warning(f"More than one vendor found! {xws['vendor']}")
            vendor = list(xws['vendor'].values())[0]
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

            upgrades = []
            for upgrade in cards:
                if upgrade is None:
                    upgrades.append(self.bold('Unrecognised Upgrade'))
                    continue

                upgrade_text = self.wiki_link(upgrade['name'])
                upgrades.append(upgrade_text)
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
                    points += cost['values'][str(stat)]
                else:
                    points += cost.get('value', 0)

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
        return [output]

    def handle_url(self, message):
        xws = self.get_xws(message)
        logger.debug(xws)
        if xws:
            return self.print_xws(xws, url=message)
        return []
