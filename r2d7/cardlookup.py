import copy
from html import unescape
from itertools import chain
import logging
import re

from r2d7.core import DroidCore, DroidException, long_substr

logger = logging.getLogger(__name__)


class CardLookup(DroidCore):
    def __init__(self):
        super().__init__()
        self.register_handler(r'\[\[(.*)\]\]', self.handle_lookup)
        self.register_dm_handler(r'(.*)', self.handle_lookup)

    _lookup_data = None

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
        'Talent',
        'Force',
        'System',
        'Cannon',
        'Turret',
        'Torpedo',
        'Missile',
        'Crew',
        'Gunner',
        'Astromech Droid',
        'Device',
        'Illicit',
        'Modification',
        'Title',
        'Configuration',
        # 'Tech',
        # 'Hardpoint',
        # 'Team',
        # 'Cargo',
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
        'countessbluekturn': 'countessryad',
        'bmst': 'blackmarketslicertools',
        'snuggling': 'smugglingcompartment',
        'snugglingcompartment': 'smugglingcompartment',
    }

    def load_data(self):
        super().load_data()
        self._init_lookup_data()


    def _init_lookup_data(self):
        next_id = 0
        self._lookup_data = {}
        self._name_to_xws = {}
        for names in self.data.values():
            for name, cards in names.items():
                for card in cards:
                    self._lookup_data.setdefault(name, []).append(card)
                    self._name_to_xws[card['name']] = card['xws']
                    card['_id'] = next_id
                    next_id += 1
        # for group in self._processing_order:
        #     cards = self.data[group]
        #     for name, cards in cards.items():
        #         for card in cards:
        #             if group == 'conditions':
        #                 card['slot'] = 'condition'
        #             elif group == 'ships':
        #                 card['slot'] = card['xws']
        #                 card['actions'].sort(key=self._action_key)
        #             elif 'damage-deck' in group:
        #                 card['slot'] = 'crit'
        #                 card['deck'] = 'TFA' if 'tfa' in group else 'Original'
        #             elif group == 'pilots':
        #                 ships = self._lookup_data[
        #                     self._name_to_xws[card['ship']]]
        #                 if len(ships) > 1:
        #                     raise DroidException(
        #                         f"Duplicate ship found: {ships}")
        #                 card['ship_card'] = ships[0]

        #                 # Add pilot to it's ship so we can list ship pilots
        #                 card['ship_card'].setdefault('pilots', []).append(
        #                     card)

        #                 if 'ship_override' in card:
        #                     card['ship_card'] = copy.copy(card['ship_card'])
        #                     card['ship_card'].update(card['ship_override'])

        #                 card['slots'].sort(key=self._slot_key)

        #                 # Give ship slots if it doesn't have them
        #                 try:
        #                     skill = int(card['skill'])
        #                     if card['ship_card'].get('_slot_skill', 13) > skill:
        #                         card['ship_card']['_slot_skill'] = skill
        #                         card['ship_card']['slots'] = card['slots']
        #                 except ValueError:
        #                     pass

        #                 card['slot'] = card['ship_card']['xws']

        #             card['_id'] = next_id
        #             card['_group'] = group
        #             next_id += 1
        #             self._lookup_data.setdefault(name, []).append(card)
        #             self._name_to_xws[card['name']] = card['xws']

    _multi_lookup_pattern = re.compile(r'\]\][^\[]*\[\[')
    @property
    def filter_pattern(self):
        raise NotImplementedError()

    def lookup(self, lookup):
        if self._lookup_data is None:
            self.load_data()

        lookup = unescape(lookup)
        logger.debug(f"Looking up: {repr(lookup)}")

        cards_yielded = set()
        for lookup in self._multi_lookup_pattern.split(lookup):
            matches = []
            slot_filter = None
            points_filter = None
            search = lookup
            match = self.filter_pattern.match(lookup)
            if not match:
                match = (None, None, lookup, None, None, None)
            slot_filter = match[1] or match[5]

            if match[2]:
                lookup = self.partial_canonicalize(match[2])
                if len(lookup) > 2 or re.match(r'[a-z]\d', lookup):
                    ex_lookup = match[2].lower().strip()
                    # We want "hot shot" to match "Hot Shot Blaster" and
                    # "Hotshot Co-pilot"
                    ex_lookup = re.sub(r' ', ' ?', ex_lookup)
                    exact = re.compile(
                        f'\\b{re.escape(ex_lookup)}(?:[\'e]?s)?\\b',
                        re.IGNORECASE
                    )
                    matches = [
                        key for key, cards in self._lookup_data.items() if any(
                            exact.search(card['name']) for card in cards
                        )
                    ]
                    if not matches:
                        matches = [key for key in self._lookup_data.keys()
                                   if lookup in key]
                if lookup in self._aliases:
                    matches.append(self._aliases[lookup])
            else:
                if not slot_filter:
                    raise DroidException(
                        'You need to specify a slot to search by points value.')
                matches = self._lookup_data.keys()
                operator = '==' if match[3] == '=' else match[3]
                operand = match[4]

                points_filter = lambda val: eval(f"{val}{operator}{operand}")

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
                            if condition['_id'] in cards_yielded:
                                continue
                            if condition['name'] in card['conditions']:
                                yield condition
                                cards_yielded.add(condition['_id'])

    _arc_icons = {
        'Turret': 'turret',
        'Auxiliary Rear': 'frontback',
        'Auxiliary 180': '180',
        'Bullseye': 'bullseye',
    }

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

        arcs = [self._arc_icons[arc] for arc in ship.get('firing_arcs', [])
                if arc in self._arc_icons]
        if arcs:
            line.append(''.join(
                self.iconify(f"attack-{arc}", special_chars=True)
                for arc in arcs))

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

        if 'epic_points' in ship:
            line.append(self.iconify('epic') + str(ship['epic_points']))

        return ' | '.join(line)

    difficulties = {
        0: 'blank',
        1: '',  # Default black icons are white for our purposes
        2: 'blue',
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

    def pilot_skill_key(self, pilot):
        try:
            return int(pilot['skill'])
        except ValueError:
            # Put ?s at the end
            return 15

    def list_pilots(self, ship):
        factions = {}
        pilots = sorted(ship['pilots'], key=self.pilot_skill_key)
        for pilot in pilots:
            if pilot['skill'] == '?':
                continue
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
        if card['category'] == 'ships' or card['category'] == 'damage':
            return card['name']
        else:
            return self.wiki_link(card['name'])
            #TODO handle special cases

    def ship_restriction(self, card):
        """
        Deal with the special cases in ship restrictions.
        """
        if isinstance(card['ship'], str):
            restriction = card['ship']
        elif len(card['ship']) == 1:
            restriction = card['ship'][0]
        else:
            restriction = long_substr(card['ship'])
            # If the longest common substring isn't a whole word, list the ship
            # names instead
            if not re.search(f"(^|\\W){restriction}(\\W|$)", card['ship'][0]):
                restriction = ' and '.join(card['ship'])
        return f"{restriction} only."

    def action_icon(self, action):
        difficulty = '' if action['difficulty'] == 'White' else action['difficulty']
        return self.iconify(difficulty + action['type'])

    def print_card(self, card):
        is_ship = card['category'] == 'ship'
        is_pilot = card['category'] == 'pilot'

        front_side = card['sides'][0]

        text = []
        text.append(''.join((
            ''.join(self.iconify(slot) for slot in front_side['slots']),
            ' • ' if card.get('limited', False) else ' ',
            self.bold(self.format_name(card)),
            f" [{card['points']}]" if 'points' in card else '',
            f" ({card['deck']})" if 'deck' in card else '',
        )))

        second_line = []
        if 'restrictions' in card:
            restrictions = []
            for restrict in card['restrictions']:
                if restrict['action']:
                    restrictions.append(self.action_icon(restrict['action']))
            second_line.append('Restrictions: ' + ' '.join(restrictions))
        if 'actions' in front_side:
            second_line.append('Actions: ' + ''.join(
                self.action_icon(action) for action in front_side['actions']
            ))
        text.append(' | '.join(second_line))

        if is_pilot:
            text.append(self.ship_stats(card['ship_card'], card))
        elif is_ship:
            text.append(self.ship_stats(card))
        # New ships have empty manuevers lists so don't try and print them
        if card.get('maneuvers', None):
            text += self.maneuvers(card)

        if 'pilots' in card:
            text += self.list_pilots(card)

        elif 'attack' in card:
            line = []
            if 'attack' in card:
                attack_size = self.iconify(f"attack{card['attack']}")
                line.append(f"{self.iconify('attack')}{attack_size}")
            if 'range' in card:
                line.append(f"Range: {card['range']}")
            text.append(' | '.join(line))

        if 'ability' in front_side:
            text += self.convert_html(front_side['ability'])

        if 'text' in front_side:
            # text += self.convert_html(front_side['text'])
            text.append(self.italics(front_side['text']))

        return text


    def handle_lookup(self, lookup):
        output = []
        count = 0
        for card in self.lookup(lookup):
            count += 1
            if count > 10:
                return ['Your search matched more than 10 cards, please be '
                        'more specific.']
            output += self.print_card(card)
        return output
