import re
import unicodedata

from r2d7.core import BotCore


class CardLookup(BotCore):
    _lookup_data = None

    def lookup(self, lookup):
        if self._lookup_data is None:
            self._lookup_data = {}
            for group, cards in self.data.items():
                for name, card in cards.items():
                    if 'slot' not in card:
                        if group == 'conditions':
                            card['slot'] = 'condition'
                        elif group == 'ships':
                            card['slot'] = card['xws']
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

    def ship_stats(self, ship, pilot=None):
        line = []
        #TODO pilot faction

        stats = ''
        if pilot:
            stats += self.name_to_icon(f"skill{pilot['skill']}")
        for stat in ('attack', 'energy', 'agility', 'hull', 'shields'):
            if stat in ship:
                # legacy naming
                icon_name = 'shield' if stat == 'shields' else stat
                stats += self.name_to_icon(f"{icon_name}{ship[stat]}")
        line.append(stats)

        #TODO attack icon - missing from guidos data

        if 'actions' in ship:
            line.append(' '.join(
                self.name_to_icon(action) for action in ship['actions']))

        #TODO slots

        #TODO epic_points

        return ' | '.join(line)

    difficulties = {
        0: 'blank',
        1: '', # Default black icons are white for our purposes
        2: 'green',
        3: 'red',
    }

    bearings = {
        0: 'turnleft',
        1: 'bankleft',
        2: 'straight',
        3: 'bankright',
        4: 'turnright',
        5: 'kturn',
        6: 'sloopleft',
        7: 'sloopright',
        8: 'trollleft',
        9: 'trollright',
        10: 'reversebankleft',
        11: 'reversestraight',
        12: 'reversebankright',
    }


    def maneuvers(self, card):
        # Check for blank columns so we can skip them
        # (eg. a ship with sloops but no k-turn)
        cols = []
        for bearing in range(len(card['maneuvers'][0])):
            empty = True
            for distance in card['maneuvers']:
                if distance[bearing] != 0:
                    empty = False
            if not empty:
                cols.append(bearing)

        lines = []
        for distance in reversed(range(len(card['maneuvers']))):
            line = [f"{distance} "]
            no_bearings = True
            for bearing in cols:
                difficulty = card['maneuvers'][distance][bearing]
                move = self.difficulties[difficulty]
                if difficulty != 0:
                    no_bearings = False
                    move += 'stop' if distance == 0 else self.bearings[bearing]
                line.append(self.name_to_icon(move))
            if not no_bearings:
                lines.append(''.join(line))
        return lines


    def print_card(self, card):
        text = []
        unique = ' • ' if card.get('unique', False) else ' '
        slot = self.name_to_icon(card['slot'])
        #TODO handle multi slot cards
        points = f" [{card['points']}]" if 'points' in card else ''
        #TODO handle deck
        #TODO name links
        text.append(f"{slot}{unique}{self.bold(card['name'])}{points}")

        if 'size' in card:
            text.append(self.ship_stats(card))
        if 'maneuvers' in card:
            text += self.maneuvers(card)

        #TODO pilots

        elif 'attack' in card or 'energy' in card:
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
