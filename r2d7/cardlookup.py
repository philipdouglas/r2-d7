import copy
import re

from r2d7.core import BotCore


class CardLookup(BotCore):
    _lookup_data = None

    _processing_order = (
        'upgrades',
        'ships',
        'pilots',
        'conditions'
    )

    _action_order = (
        'Focus',
        'Recover',
        'Reinforce',
        'Target Lock',
        'Barrel Roll',
        'Boost',
        'Evade',
        'Cloak',
        'Coordinate',
        'Jam',
        'SLAM',
        'Rotate Arc',
    )
    @classmethod
    def _action_key(cls, action):
        try:
            return cls._action_order.index(action)
        except ValueError:
            #TODO log an error?
            return 100

    _slot_order = (
        'Elite',
        'System',
        'Cannon',
        'Turret',
        'Torpedo',
        'Missile',
        'Crew',
        'Astromech',
        'Salvaged Astromech',
        'Bomb',
        'Tech',
        'Illicit',
        'Hardpoint',
        'Team',
        'Cargo',
    )
    @classmethod
    def _slot_key(cls, slot):
        try:
            return cls._slot_order.index(slot)
        except ValueError:
            #TODO log an error?
            return 100

    def lookup(self, lookup):
        if self._lookup_data is None:
            self._lookup_data = {}
            self._name_to_xws = {}
            for group in self._processing_order:
                cards = self.data[group]
                for name, cards in cards.items():
                    for card in cards:
                        if 'slot' not in card:
                            if group == 'conditions':
                                card['slot'] = 'condition'
                            elif group == 'ships':
                                card['slot'] = card['xws']
                        if group == 'pilots':
                            card['ship_card'] = self._lookup_data[
                                self._name_to_xws[card['ship']]]

                            # Add pilot to it's ship so we can list ship pilots
                            card['ship_card'].setdefault('pilots', []).append(
                                card)

                            if 'ship_override' in card:
                                card['ship_card'] = copy.copy(card['ship_card'])
                                card['ship_card'].update(card['ship_override'])

                            card['slots'].sort(key=self._slot_key)

                            # Give ship slots if it doesn't have them
                            try:
                                skill = int(card['skill'])
                                if card['ship_card'].get('_slot_skill', 13) > skill:
                                    card['ship_card']['_slot_skill'] = skill
                                    card['ship_card']['slots'] = card['slots']
                            except ValueError:
                                pass

                            card['slot'] = card['ship_card']['xws']
                        elif group == 'ships':
                            card['actions'].sort(key=self._action_key)



                        self._lookup_data[name] = card
                        self._name_to_xws[card['name']] = card['xws']

        for name, card in self._lookup_data.items():
            if lookup in name:
                yield card

    _frontback = ('firespray31', 'arc170')
    _180 = ('yv666', 'auzituck')
    _turret = ('kwing', 'yt1300', 'jumpmaster5000', 'vt49decimator')

    def ship_stats(self, ship, pilot=None):
        line = []
        if pilot and 'faction' in pilot:
            line.append(self.iconify(pilot['faction']))

        stats = ''
        if pilot:
            stats += self.iconify(f"skill{pilot['skill']}")
        for stat in ('attack', 'energy', 'agility', 'hull', 'shields'):
            if stat in ship:
                # legacy naming
                icon_name = 'shield' if stat == 'shields' else stat
                stats += self.iconify(f"{icon_name}{ship[stat]}")
        line.append(stats)

        #TODO attack icon - missing from guidos data
        attack_type = None
        if ship['xws'] in self._frontback:
            attack_type = 'frontback'
        elif ship['xws'] in self._180:
            attack_type = '180'
        elif ship['xws'] in self._turret:
            attack_type = 'turret'
        if attack_type:
            line.append(self.iconify(f"attack-{attack_type}", hypens=True))

        if 'actions' in ship:
            line.append(' '.join(
                self.iconify(action) for action in ship['actions']))

        slots = None
        if pilot and 'slots' in pilot:
            slots = pilot['slots']
        elif 'slots' in ship:
            slots = ship['slots']
        if slots:
            line.append(''.join(self.iconify(slot) for slot in slots))


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
        # Find the longest row
        longest = max(len(row) for row in card['maneuvers'])
        # Check for blank columns so we can skip them
        # (eg. a ship with sloops but no k-turn)
        cols = []
        for bearing in range(longest):
            empty = True
            for distance in card['maneuvers']:
                try:
                    if distance[bearing] != 0:
                        empty = False
                except IndexError:
                    continue
            if not empty:
                cols.append(bearing)

        lines = []
        for distance in reversed(range(len(card['maneuvers']))):
            line = [f"{distance} "]
            no_bearings = True
            for bearing in cols:
                try:
                    difficulty = card['maneuvers'][distance][bearing]
                except IndexError:
                    difficulty = 0
                move = self.difficulties[difficulty]
                if difficulty != 0:
                    no_bearings = False
                    move += 'stop' if distance == 0 else self.bearings[bearing]
                line.append(self.iconify(move))
            if not no_bearings:
                lines.append(''.join(line))
        return lines

    def list_pilots(self, ship):
        factions = {}
        pilots = sorted(ship['pilots'], key=lambda pilot: pilot['skill'])
        for pilot in pilots:
            skill = self.iconify(f"skill{pilot['skill']}")
            unique = '• ' if pilot.get('unique', False) else ''
            elite = ' ' + self.iconify('elite') if 'Elite' in pilot['slots'] else ''
            name = self.format_name(pilot)
            text = f"{skill}{unique}{name}{elite} [{pilot['points']}]"
            factions.setdefault(pilot['faction'], []).append(text)
        return [f"{self.iconify(faction)} {', '.join(pilots)}"
                for faction, pilots in factions.items()]

    def format_name(self, card):
        if 'actions' in card or card['slot'] == 'crit':
            return card['name']
        else:
            #TODO links
            return card['name']


    def print_card(self, card):
        text = []
        unique = ' • ' if card.get('unique', False) else ' '
        slot = self.iconify(card['slot'])
        #TODO handle multi slot cards
        points = f" [{card['points']}]" if 'points' in card else ''
        #TODO handle deck
        #TODO name links
        name = self.bold(self.format_name(card))
        text.append(f"{slot}{unique}{name}{points}")

        if 'ship_card' in card:
            text.append(self.ship_stats(card['ship_card'], card))
        elif 'size' in card:  # A ship
            text.append(self.ship_stats(card))
        if 'maneuvers' in card:
            text += self.maneuvers(card)

        if 'pilots' in card:
            text += self.list_pilots(card)

        elif 'attack' in card or 'energy' in card:
            line = []
            if 'attack' in card:
                attack_size = self.iconify(f"attack{card['attack']}")
                line.append(f"{self.iconify('attack')}{attack_size}")
            if 'range' in card:
                line.append(f"Range: {card['range']}")
            if 'energy' in card:
                attack_size = self.iconify(f"energy{card['energy']}")
                line.append(f"{self.iconify('energy')}{attack_size}")
            text.append(' | '.join(line))

        if 'ship' in card and 'ship_card' not in card:
            ship = card['ship'] if isinstance(card['ship'], str) else card['ship'][0]
            text.append(self.italics(f"{ship} only."))

        if card.get('limited', False):
            text.append(self.italics('Limited.'))

        #TODO damage card type

        if 'text' in card:
            text.append(self.convert_html(card['text']))

        return text

    def handle_message(self, message):
        output = []
        for card in self.lookup(self.partial_canonicalize(message)):
            output += self.print_card(card)
        return output
