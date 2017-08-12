import re
import unicodedata

from r2d7.core import BotCore


class CardLookup(BotCore):
    _lookup_data = None

    def lookup(self, lookup):
        if self._lookup_data is None:
            self._lookup_data = {}
            for cards in self.data.values():
                for name, card in cards.items():
                    self._lookup_data[name] = card

        for name, card in self._lookup_data.items():
            if lookup in name:
                yield card

    @staticmethod
    def partial_canonicalize(string):
        #TODO handle special cases https://github.com/elistevens/xws-spec
        string = string.lower()
        string = unicodedata.normalize('NFKD', string)
        string = re.sub(r'[^a-zA-Z0-9]', '', string)
        return string

    def print_card(self, card):
        text = []
        unique = ' • ' if card.get('unique', False) else ' '
        slot = self.name_to_icon(card['slot'])
        #TODO handle multi slot cards
        points = f"[{card['points']}]" if 'points' in card else ''
        #TODO handle deck
        #TODO name links
        text.append(f"{slot}{unique}{self.bold(card['name'])} {points}")

        #TODO ship stats

        #TODO pilots

        #TODO secondary weapon/energy
        if 'attack' in card or 'energy' in card:
            line = []
            if 'attack' in card:
                attack_size = self.name_to_icon(f"attack{card['attack']}")
                line.append(f"{self.name_to_icon('attack')}{attack_size}")
            if 'range' in card:
                line.append(f"Range: {card['range']}")
            if 'energy' in card:
                attack_size = self.name_to_icon(f"energy{card['energy']}")
                line.append(f"{self.name_to_icon('energy')}{attack_size}")
            text.append(' | '.join(line))

        if 'ship' in card:
            for ship in card['ship']:
                text.append(self.italics(f"{ship} only."))

        if card.get('limited', False):
            text.append(self.italics('Limited.'))

        #TODO damage card type

        if 'text' in card:
            #TODO emoji in text
            text.append(self.convert_html(card['text']))

        return text

    def handle_message(self, message):
        output = []
        for card in self.lookup(self.partial_canonicalize(message)):
            output += self.print_card(card)
        return output
