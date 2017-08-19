import re

import requests

from r2d7.core import BotCore, BotException


class ListFormatter(BotCore):
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
            raise ValueError(f"Unrecognised URL: {message}")

        xws_url = None
        if match[2] == 'geordanr':
            xws_url = f"https://yasb-xws.herokuapp.com/?{match[3]}"
        elif match[2] == 'xwing-builder':
            xws_url = f"http://xwing-builder.co.uk/xws/{match[3]}?dl=1"
        elif match[2] == 'fabpsb':
            xws_url = f"http://x-wing.fabpsb.net/permalink.php?sq={match[3]}&xws=1"

        #TODO other builders

        if xws_url:
            response = requests.get(xws_url)
            if response.status_code != 200:
                raise BotException(
                    f"Got {response.status_code} GETing f{xws_url}.")
            return response.json()

        #TODO handle raw XWS

    def print(self, xws):
        #TODO list url
        name = self.bold(xws.get('name', 'Nameless Squadron'))
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
            for slot, upgrades in pilot['upgrades'].items():
                for upgrade in upgrades:
                    #TODO heavy scyk
                    try:
                        cards.append(self.data['upgrades'][upgrade][0])
                    except KeyError:
                        cards.append(None)
                    tiex1 = tiex1 or upgrade == 'tiex1'
                    vaksai = vaksai or upgrade == 'vaksai'

            upgrades = []
            for upgrade in cards:
                if upgrade is None:
                    #TODO test this
                    upgrades.append(self.bold('Unrecognised Upgrade'))
                    continue

                if upgrade['name'] == 'Veteran Instincts':
                    skill += 2
                if tiex1 and upgrade['slot'] == 'System':
                    points -= min(4, upgrade['points'])
                #TODO upgrade links
                upgrade_text = upgrade['name']
                if upgrade['name'] == 'Adaptability':
                    upgrade_text += self.iconify('skill_1')
                upgrades.append(upgrade_text)
                cost = upgrade['points']
                if vaksai and cost >= 1:
                    cost -= 1
                points += cost

            output.append(
                self.iconify(pilot_card['ship']) +
                self.iconify(f"skill{skill}") +
                f" {self.italics(pilot_card['name'])}:" +
                f" {', '.join(upgrades)}" +
                ' ' + self.bold(f"[{points}]")
            )
            total_points += points

        output[0] += self.bold(f"[{total_points}]")
        return output

    def handle_message(self, message):
        xws = self.get_xws(message)
        return self.print(xws)
