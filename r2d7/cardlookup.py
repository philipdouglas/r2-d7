import copy
from itertools import chain
import re

from r2d7.core import DroidCore, DroidException


class CardLookup(DroidCore):
    def __init__(self):
        super().__init__()
        self.register_handler(r'\[\[(.*)\]\]', self.handle_lookup)
        self.register_dm_handler(r'(.*)', self.handle_lookup)

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

    _aliases = {
        'fcs': 'firecontrolsystem',
        'apl': 'antipursuitlasers',
        'atc': 'advancedtargetingcomputer',
        'ptl': 'pushthelimit',
        'hlc': 'heavylasercannon',
        'tlt': 'twinlaserturret',
        'vi': 'veteraninstincts',
        'at': 'autothrusters',
        'as': 'advancedsensors',
        'acd': 'advancedcloakingdevice',
        'eu': 'engineupgrade',
        'tap': 'tieadvancedprototype',
        'ac': 'accuracycorrector',
        'abt': 'autoblasterturret',
        'sd': 'stealthdevice',
        'ei': 'experimentalinterface',
        'k4': 'k4securitydroid',
        'stressbot': 'r3a2',
        'countesskturn': 'countessryad',
        'countesskturns': 'countessryad',
        'countessgreenkturn': 'countessryad',
        'bmst': 'blackmarketslicertools',
        'snuggling': 'smugglingcompartment',
        'snugglingcompartment': 'smugglingcompartment',
    }


    def _init_lookup_data(self):
        next_id = 0
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
                        ships = self._lookup_data[
                            self._name_to_xws[card['ship']]]
                        if len(ships) > 1:
                            raise DroidException(f"Duplicate ship found: {ships}")
                        card['ship_card'] = ships[0]

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

                    card['_id'] = next_id
                    next_id += 1
                    self._lookup_data.setdefault(name, []).append(card)
                    self._name_to_xws[card['name']] = card['xws']

    _multi_lookup_pattern = re.compile(r'\]\][^\[]*\[\[')
    #TODO this is slack specific
    _filter_pattern = re.compile(
        r' *(?:(:[^:]+:))? *(?:([^=><:]*[^=><: ][^=><:]*)|([=><][=><]?)'
        r' *(\d+)) *(?:(:[^:]+:))? *'
    )

    def lookup(self, lookup):
        if self._lookup_data is None:
            self._init_lookup_data()

        cards_yielded = set()
        for lookup in self._multi_lookup_pattern.split(lookup):
            matches = []
            match = self._filter_pattern.match(lookup)
            slot_filter = match[1] or match[5]
            points_filter = None

            if match[2]:
                lookup = self.partial_canonicalize(match[2])
                if len(lookup) > 2 or re.match(r'[a-z]\d', lookup):
                    exact = re.compile(f'\\b{lookup}(?:\'s)?\\b', re.IGNORECASE)
                    matches = [
                        key for key, cards in self._lookup_data.items() if any(
                            exact.search(card['name']) for card in cards
                        )
                    ]
                    if not matches:
                        print("No exactsies")
                        matches = [key for key in self._lookup_data.keys()
                                   if lookup in key]
                if lookup in self._aliases:
                    matches.append(self._aliases[lookup])
            else:
                if not slot_filter:
                    raise DroidException(
                        'You need to specify a slot to search by points value.')
                matches = self._lookup_data.keys()
                operator = match[3]
                operand = match[4]

                points_filter = lambda value: eval(f"{value}{operator}{operand}")

            for match in matches:
                for card in self._lookup_data[match]:
                    if card['_id'] in cards_yielded:
                        continue
                    if slot_filter and self.iconify(card['slot']) != slot_filter:
                        continue
                    if points_filter and not points_filter(card['points']):
                        continue

                    cards_yielded.add(card['_id'])
                    yield card

                    if 'conditions' in card:
                        for condition in chain.from_iterable(
                                self.data['conditions'].values()):
                            if condition['name'] in card['conditions']:
                                yield condition

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
            line.append(self.iconify(f"attack-{attack_type}", hyphens=True))

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
        1: '',  # Default black icons are white for our purposes
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
        # There's no wiki pages for ships or crits
        if 'size' in card or card['slot'] == 'crit':
            return card['name']
        else:
            return self.wiki_link(
                card['name'],
                (
                    card['slot'] == 'Crew' and (
                        card['xws'] in self.data['pilots'] or
                        card['xws'] == 'r2d2-swx22'
                    )
                )
            )

    def print_card(self, card):
        is_ship = 'size' in card
        is_pilot = 'ship_card' in card

        text = []
        unique = ' • ' if card.get('unique', False) else ' '
        slot = self.iconify(card['slot'])
        #TODO handle multi slot cards
        points = f" [{card['points']}]" if 'points' in card else ''
        #TODO handle deck
        #TODO name links
        name = self.bold(self.format_name(card))
        text.append(f"{slot}{unique}{name}{points}")

        if is_pilot:
            text.append(self.ship_stats(card['ship_card'], card))
        elif is_ship:
            text.append(self.ship_stats(card))
        # New ships have empty manuevers lists so don't try and print them
        if card.get('maneuvers', None):
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

        restrictions = []
        if 'ship' in card and not is_pilot:
            ship = card['ship'] if isinstance(card['ship'], str) else card['ship'][0]
            restrictions.append(f"{ship} only.")

        if card.get('limited', False):
            restrictions.append('Limited.')

        if 'faction' in card and not (is_ship or is_pilot):
            #TODO data doesn't understand multi faction cards (PRS)
            faction = card['faction'].split(' ')[0]
            if faction == 'Galactic':
                faction = 'Imperial'
            restrictions.append(f"{faction} only.")

        if restrictions:
            text.append(self.italics(' '.join(restrictions)))
        #TODO damage card type

        if 'text' in card:
            text += self.convert_html(card['text'])

        return text

    def handle_lookup(self, lookup):
        output = []
        for card in self.lookup(lookup):
            output += self.print_card(card)
        return output
