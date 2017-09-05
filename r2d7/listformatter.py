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
        self.register_handler(r'<(https?://[^>]+)>', self.handle_url)
        self.register_handler(r'({.*})', self.handle_json)

    _regexes = (
        re.compile(r'(https?://(geordanr)\.github\.io/xwing/\?(.*))'),
        re.compile(r'(https?://(xwing-builder)\.co\.uk/view/(\d+)[^>|]*)'),
        re.compile(r'(https?://x-wing\.(fabpsb)\.net/permalink\.php\?sq=([a-z0-9]+))'),
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
        if match[2] == 'geordanr':
            xws_url = f"https://yasb-xws.herokuapp.com/?{match[3]}"
        elif match[2] == 'xwing-builder':
            xws_url = f"http://xwing-builder.co.uk/xws/{match[3]}?dl=1"
        elif match[2] == 'fabpsb':
            xws_url = f"http://x-wing.fabpsb.net/permalink.php?sq={match[3]}&xws=1"

        if xws_url:
            xws_url = unescape(xws_url)
            logging.info(f"Requesting {xws_url}")
            response = requests.get(xws_url)
            if response.status_code != 200:
                raise DroidException(
                    f"Got {response.status_code} GETing {xws_url}.")
            data = response.json()
            if 'message' in data:
                raise DroidException(f"YASB error: ({data['message']}")
            return data

    def print_xws(self, xws):
        name = xws.get('name', 'Nameless Squadron')
        if 'vendor' in xws:
            if len(list(xws['vendor'].keys())) > 1:
                logger.warning(f"More than one vendor found! {xws['vendor']}")
            vendor = list(xws['vendor'].values())[0]
            if 'link' in vendor:
                name = self.link(vendor['link'], name)
        name = self.bold(name)
        output = [f"{self.iconify(xws['faction'])} {name} "]
        total_points = 0

        for pilot in xws['pilots']:
            points = 0
            pilot_card = None
            for pilot_card in self.data['pilots'][pilot['name']]:
                canon_ship = self.partial_canonicalize(pilot_card['ship'])
                if canon_ship == pilot['ship']:
                    break
            points += pilot_card['points']
            skill = pilot_card['skill']

            cards = []
            tiex1 = False
            vaksai = False
            if 'upgrades' in pilot:
                for slot, upgrades in pilot['upgrades'].items():
                    for upgrade in upgrades:
                        try:
                            cards.append(self.data['upgrades'][upgrade][0])
                        except KeyError:
                            cards.append(None)
                        tiex1 = tiex1 or upgrade == 'tiex1'
                        vaksai = vaksai or upgrade == 'vaksai'

            upgrades = []
            for upgrade in cards:
                if upgrade is None:
                    upgrades.append(self.bold('Unrecognised Upgrade'))
                    continue

                if upgrade['name'] == 'Veteran Instincts':
                    skill += 2
                if tiex1 and upgrade['slot'] == 'System':
                    points -= min(4, upgrade['points'])
                upgrade_name = upgrade['name']
                if upgrade['xws'] == 'adaptability':
                    upgrade_name = 'Adaptability'
                upgrade_text = self.wiki_link(
                    upgrade_name,
                    (
                        upgrade['slot'] == 'Crew' and (
                            upgrade['xws'] in self.data['pilots'] or
                            upgrade['xws'] == 'r2d2-swx22'
                        )
                    )
                )
                if upgrade_name == 'Adaptability':
                    upgrade_text += self.iconify('skill_1', special_chars=True)
                upgrades.append(upgrade_text)
                cost = upgrade['points']
                if vaksai and cost >= 1:
                    cost -= 1
                points += cost

            ship_line = (
                self.iconify(pilot_card['ship']) +
                self.iconify(f"skill{skill}") +
                f" {self.italics(self.wiki_link(pilot_card['name']))}"
            )
            if upgrades:
                ship_line += ':' + f" {', '.join(upgrades)}"
            ship_line += ' ' + self.bold(f"[{points}]")

            output.append(ship_line)
            total_points += points

        output[0] += self.bold(f"[{total_points}]")
        return output

    def handle_json(self, message):
        try:
            logging.debug("Parsing raw JSON")
            return self.print_xws(json.loads(message))
        except json.JSONDecodeError:
            logging.debug("Invalid JSON")
            return []

    def handle_url(self, message):
        xws = self.get_xws(message)
        logger.debug(xws)
        if xws:
            return self.print_xws(xws)
        return []
