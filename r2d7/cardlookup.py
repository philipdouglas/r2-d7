import copy
from html import unescape
from itertools import chain, groupby
import logging
import re

from r2d7.core import DroidCore, UserError

logger = logging.getLogger(__name__)


class CardLookup(DroidCore):
    def __init__(self):
        super().__init__()
        self.register_handler(r'\{\{(.*)\}\}', self.handle_image_lookup)
        self.register_handler(r'\[\[(.*)\]\]', self.handle_lookup)
        self.register_dm_handler(r'\{\{(.*)\}\}', self.handle_image_lookup)
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

    _slot_order = (
        'Talent',
        'Force Power',
        'Sensor',
        'Cannon',
        'Turret',
        'Torpedo',
        'Missile',
        'Tech',
        'Crew',
        'Gunner',
        'Astromech',
        'Device',
        'Illicit',
        'Modification',
        'Title',
        'Configuration',
        'Tactical Relay',
        # 'Hardpoint',
        # 'Team',
        # 'Cargo',
    )

    _aliases = {
        'fcs': 'firecontrolsystem',
        'ptl': 'pushthelimit',
        'hlc': 'heavylasercannon',
        'at': 'autothrusters',
        'as': 'advancedsensors',
        'eu': 'engineupgrade',
        'tap': 'tieadvancedprototype',
        'sd': 'stealthdevice',
        'countesskturn': 'countessryad',
        'countesskturns': 'countessryad',
        'ap': 'ap5',
        'scyk': 'm3ainterceptor',
        'terry': 'oldteroch',
        'kirax': 'kihraxzfighter',
        'kfighter': 'kihraxzfighter',
        'sassy': 'saeseetiin',
        'bulbasaur': 'belbullab22starfighter',
        'baobab': 'belbullab22starfighter',
        'bbb': 'belbullab22starfighter',
        'bellyrub': 'belbullab22starfighter',
        'bubblebub': 'belbullab22starfighter',
        'hcp': 'haorchallprototype',
        'hadrchallprototype': 'haorchallprototype'
    }

    def load_data(self):
        super().load_data()
        self._init_lookup_data()

    def _init_lookup_data(self):
        next_id = 0
        self._lookup_data = {}
        for cards in self.data.values():
            for card in cards.values():
                name = self.partial_canonicalize(card['name'])
                self._lookup_data.setdefault(name, []).append(card)
                card['_id'] = next_id
                next_id += 1

        for ship in self.data['ship'].values():
            all_bars = [
                pilot['slots']
                for pilots in ship.get('pilots', []).values()
                for pilot in pilots
                if 'slots' in pilot
            ]
            try:
                shortest = sorted(all_bars, key=len)[0]
            except IndexError:  # No ships have bars
                continue
            ship_bar = []
            for slot in shortest:
                for bar in all_bars:
                    if slot not in bar:
                        break
                else:
                    ship_bar.append(slot)
            ship['slots'] = ship_bar


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
            match = self.filter_pattern.match(lookup)
            if not match:
                match = (None, None, lookup, None, None, None)
            slot_filter = match[1] or match[5]

            if match[2]:
                lookup = self.partial_canonicalize(match[2])
                if len(lookup) > 2 or re.match(r'[a-z]\d', lookup):
                    ex_lookup = re.escape(match[2].lower().strip())
                    # We want "hot shot" to match "Hot Shot Blaster" and
                    # "Hotshot Co-pilot"
                    ex_lookup = re.sub(r' ', ' ?', ex_lookup)
                    # Fudge lookup for TIEs so you don't have to remember the /ln bit
                    ex_lookup = re.sub(r'tie', 'tie.*', ex_lookup)
                    exact = re.compile(
                        f'\\b{ex_lookup}(?:[\'e]?s)?\\b',
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
                    raise UserError(
                        'You need to specify a slot to search by points value.')
                matches = self._lookup_data.keys()
                operator = '==' if match[3] == '=' else match[3]
                operand = match[4]

                points_filter = lambda val: eval(f"{val}{operator}{operand}")

            for match in matches:
                for card in self._lookup_data[match]:
                    if card['_id'] in cards_yielded:
                        continue
                    if slot_filter and 'ship' not in card and self.iconify(card['category']) != slot_filter:
                        continue
                    if slot_filter and 'ship' in card and self.iconify(card['ship']['name']) != slot_filter:
                        continue
                    if points_filter and not points_filter(card.get('cost', {}).get('value', 0)):
                        continue

                    cards_yielded.add(card['_id'])
                    yield card

                    if 'conditions' in card:
                        for condition in self.data['condition'].values():
                            if condition['_id'] in cards_yielded:
                                continue
                            if condition['xws'] in card['conditions']:
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

        stats = []
        if pilot:
            stats.append(self.iconify(f"initiative{pilot['initiative']}"))
        for stat in ship['stats']:
            stats.append(self.print_stat(stat))
        if pilot and 'charges' in pilot:
            stats.append(self.print_charge(pilot['charges']))
        if pilot and 'force' in pilot:
            stats.append(self.print_charge(pilot['force'], force=True))
        line.append(''.join(stats))

        arcs = [self._arc_icons[arc] for arc in ship.get('firing_arcs', [])
                if arc in self._arc_icons]
        if arcs:
            line.append(''.join(
                self.iconify(f"attack-{arc}", special_chars=True)
                for arc in arcs))

        if pilot and 'shipActions' in pilot:
            line.append('|'.join(
                self.print_action(action) for action in pilot['shipActions']
            ))
        elif 'actions' in ship:
            line.append('|'.join(
                self.print_action(action) for action in ship['actions']
            ))

        if not pilot and 'slots' in ship:
            line.append(''.join(self.iconify(slot) for slot in ship['slots']))

        if pilot and 'slots' in pilot:
            line.append(''.join(self.iconify(slot) for slot in pilot['slots']))

        return '  '.join(line)

    # Dialgen format defined here: http://xwvassal.info/dialgen/dialgen
    maneuver_key = (
        ('T', 'turnleft'),
        ('B', 'bankleft'),
        ('F', 'straight'),
        ('N', 'bankright'),
        ('Y', 'turnright'),
        ('K', 'kturn'),
        ('L', 'sloopleft'),
        ('P', 'sloopright'),
        ('E', 'trollleft'),
        ('R', 'trollright'),
        ('A', 'reversebankleft'),
        ('S', 'reversestraight'),
        ('D', 'reversebankright'),
    )
    stop_maneuver = ('O', 'stop')

    difficulty_key = {
        'R': 'red',
        'W': '',
        'G': 'green',
        'B': 'blue',
    }

    def maneuvers(self, dial):
        used_moves = {move[1] for move in dial}
        dial = {speed: {move[1]: move[2] for move in moves}
                for speed, moves in groupby(dial, lambda move: move[0])}
        result = []
        blank = self.iconify('blank')
        for speed, moves in dial.items():
            line = [speed + ' ']
            for dialgen_move, droid_move in self.maneuver_key:
                if dialgen_move not in used_moves:
                    continue
                if speed == '0' and dialgen_move == 'F':
                    dialgen_move, droid_move = self.stop_maneuver
                if dialgen_move in moves:
                    line.append(self.iconify(
                        self.difficulty_key[moves[dialgen_move]] + droid_move
                    ))
                else:
                    line.append(blank)
            result.append(''.join(line))
        return list(reversed(result))

    def pilot_sort_key(self, pilot):
        try:
            return int(pilot['initiative']) + (pilot.get('cost', 0) / 200)
        except ValueError:
            # Put ?s at the end
            return 9

    @staticmethod
    def has_calculate(pilot):
        try:
            for action in pilot['shipActions']:
                if action['type'] == 'Calculate':
                    return True
        except KeyError:
            pass
        return False

    def list_pilots(self, ship):
        ability_faction_pilot_map = {}
        for faction, pilots in ship['pilots'].items():
            for pilot in pilots:
                ability = '\n'.join(self.print_ship_ability(pilot['shipAbility'])) if 'shipAbility' in pilot else None
                ability_faction_pilot_map.setdefault(ability, {}).setdefault(faction, []).append(pilot)
        out = []
        for ability, factions in ability_faction_pilot_map.items():
            if ability:
                out.append(ability)
            for faction, pilots in factions.items():
                pilots = sorted(pilots, key=self.pilot_sort_key)
                pilots_printed = []
                for pilot in pilots:
                    init = self.iconify(f"initiative{pilot['initiative']}")
                    unique = '•' * pilot.get('limited', 0)
                    slots = ''.join([
                        self.iconify(slot) for slot in pilot.get('slots', [])
                        if slot not in ship['slots']
                    ])
                    if slots:
                        slots = ' ' + slots
                    calculate = ' ' + self.iconify('calculate') if self.has_calculate(pilot) else ''
                    name = self.format_name(pilot)
                    pilots_printed.append(
                        f"{init}{unique}{name}{slots}{calculate} [{pilot.get('cost', '?')}]")
                out.append(f"{self.iconify(faction)} {', '.join(pilots_printed)}")
        return out

    def format_name(self, card, side=None):
        if side is None:
            side = card
        # There's no wiki pages for ships or crits
        if card['category'] in ('ships', 'damage', 'condition'):
            return card['name']
        else:
            return self.wiki_link(side.get('title', card['name']))
            #TODO handle special cases

    def print_action(self, action):
        difficulty = '' if action.get('difficulty', 'White') == 'White' else action['difficulty']
        out = self.iconify(difficulty + action['type'])
        if 'linked' in action:
            out += self.iconify('linked') + self.print_action(action['linked'])
        return out

    stat_colours = {
        "attack": "red",
        "agility": "green",
        "hull": "yellow",
        "shield": "blue",
        "charge": "orange",
        "forcecharge": "purple",
        "initiative": "initiative"
    }

    def print_stat(self, stat):
        stat_type = stat['type']
        if stat['type'] == 'shields':
            stat_type = 'shield'
        colour = self.stat_colours[stat_type]
        if stat_type == 'attack':
            out = self.iconify(f"red{stat['arc']}")
        else:
            out = self.iconify(f"{colour}{stat_type}")
        plus = 'plus' if stat.get('plus', False) else ''
        recurring = 'recurring' if stat.get('recovers', False) else ''
        out += self.iconify(f"{stat_type}{plus}{stat['value']}{recurring}")
        return out

    def print_charge(self, charge, force=False, plus=False):
        charge['type'] = 'forcecharge' if force else 'charge'
        charge['plus'] = plus
        return self.print_stat(charge)

    restriction_faction_map = {
        'Galactic Empire': 'Imperial',
        'Rebel Alliance': 'Rebel',
        'Scum and Villainy': 'Scum',
        'Separatist Alliance': 'Separatist',
        'Galactic Republic': 'Republic',
    }

    def print_restrictions(self, restrictions):
        ands = []
        for restrict in restrictions:
            ors = []
            if 'action' in restrict:
                ors.append(self.print_action(restrict['action']))
            if 'factions' in restrict:
                ors += [self.restriction_faction_map.get(faction, faction)
                        for faction in restrict['factions']]
            if 'ships' in restrict:
                ors += [self.data['ship'][ship]['name']
                        for ship in restrict['ships']]
            if 'sizes' in restrict:
                ors.append(' or '.join(restrict['sizes']) + ' ship')
            if 'names' in restrict:
                ors.append(
                    f"squad including {' or '.join(restrict['names'])}")
            if 'arcs' in restrict:
                ors += [self.iconify(arc) for arc in restrict['arcs']]
            if restrict.get('solitary', False):
                ors.append('Solitary')
            if restrict.get('non-limited', False):
                ors.append('Non-Limited')
            if 'equipped' in restrict:
                ors.append(
                    f"Equipped {''.join(self.iconify(slot) for slot in restrict['equipped'])}")
            if 'force_side' in restrict:
                ors += [f"{side.capitalize()} side" for side in restrict['force_side']]
            if ors:
                ands.append(' or '.join(ors))
        if ands:
            return self.italics('Restrictions: ' + ', '.join(ands))
        return None


    def print_ship_ability(self, ability):
        lines = ability['text']
        return [self.italics(self.bold(ability['name'] + ':')) + ' ' + lines[0]] + lines[1:]

    def print_cost(self, cost):
        try:
            if 'variable' in cost:
                out = ''
                if cost['variable'] == 'shields':
                    cost['variable'] = 'shield'
                if cost['variable'] in self.stat_colours.keys():
                    if cost['variable'] != self.stat_colours[cost['variable']]:
                        out += self.iconify(
                            f"{self.stat_colours[cost['variable']]}{cost['variable']}")
                    icons = [self.iconify(f"{cost['variable']}{stat}")
                            for stat in cost['values'].keys()]
                elif cost['variable'] == 'size':
                    icons = [self.iconify(f"{size}base")
                            for size in cost['values'].keys()]
                else:
                    logger.warning(f"Unrecognised cost variable: {cost['variable']}")
                    icons = ['?' for stat in cost['values']]
                out += ''.join(
                    f"{icon}{cost}" for icon, cost in zip(icons, cost['values'].values()))
            else:
                out = cost['value']
        except TypeError:
            out = cost
        return f"[{out}]"

    def print_grants(self, grants):
        out = []
        for grant in grants:
            if grant['type'] == 'slot':
                continue
            elif grant['type'] == 'action':
                out += [self.print_action(grant['value'])] * grant.get('amount', 1)
            elif grant['type'] == 'stat':
                stat = 'shield' if grant['value'] == 'shields' else grant['value']
                symbol = 'minus' if grant['amount'] < 0 else 'plus'
                out.append(
                    self.iconify(f"{self.stat_colours[stat]}{stat}") +
                    self.iconify(f"{stat}{symbol}{grant['amount']}")
                )
        return out if out else None

    def print_attack(self, atk):
        if atk['minrange'] != atk['maxrange']:
            ranges = f"{atk['minrange']}-{atk['maxrange']}"
        else:
            ranges = str(atk['minrange'])
        return (
            self.iconify('red' + atk['arc']) +
            self.iconify(f"attack{atk['value']}") +
            (self.iconify('redrangebonusindicator')
                if atk.get('ordnance', False) else '') +
            ranges
        )

    def print_card(self, card):
        is_ship = card['category'] == 'ship'
        is_pilot = card['category'] == 'pilot'
        is_crit = card['category'] == 'damage'
        is_remote = card['category'] == 'Remote'

        if 'sides' not in card:
            if is_pilot:
                slot = card['ship']['xws']
            elif is_crit:
                slot = 'crit'
            elif card['category'] == 'condition':
                slot = 'condition'
            elif is_remote:
                slot = 'device'
            else:
                slot = card['xws']
            fake_side = {'slots': [slot]}
            if 'ability' in card:
                fake_side['ability'] = card['ability']
            if is_pilot and 'text' in card:
                fake_side['text'] = card['text']
            elif is_crit and 'text' in card:
                fake_side['ability'] = card['text']
            card['sides'] = [fake_side]

        text = []
        for side in card['sides']:
            text.append(' '.join(filter(len, (
                ''.join(self.iconify(slot) for slot in side['slots']),
                '•' * card.get('limited', 0),
                self.bold(self.format_name(card, side)) +
                (f": {self.italics(card['caption'])}" if 'caption' in card else ''),
                self.print_cost(card['cost']) if 'cost' in card else '',
                f"({card['deck']})" if 'deck' in card else '',
                self.iconify(f"{card['size']}base") if 'size' in card else '',
                "[Hyperspace]" if card.get('hyperspace', False) else '',
            ))))

            if 'restrictions' in card:
                restrictions = self.print_restrictions(card['restrictions'])
                if restrictions:
                    text.append(restrictions)

            if is_pilot:
                text.append(self.ship_stats(card['ship'], card))
            elif is_ship:
                text.append(self.ship_stats(card))
            elif is_remote:
                text.append(self.ship_stats(card, card))

            if 'ability' in side:
                text += side['ability']

            if 'text' in side:
                text.append(self.italics(side['text']))

            if 'shipAbility' in card:
                text += self.print_ship_ability(card['shipAbility'])

            last_line = []
            if 'attack' in side:
                last_line.append(self.print_attack(side['attack']))
            if 'charges' in side:
                last_line.append(self.print_charge(side['charges']))
            if 'force' in side:
                last_line.append(
                    self.print_charge(side['force'], force=True, plus=True))
            if 'grants' in side:
                grants = self.print_grants(side['grants'])
                if grants:
                    last_line += grants
            if last_line:
                text.append(' | '.join(last_line))

            if 'device' in side:
                if side['device']['type'] == 'Remote':
                    side['device']['category'] = 'Remote'
                    side['device']['ability'] = side['device']['effect']
                    text += self.print_card(side['device'])
                else:
                    text += self.print_device(side['device'])

            if 'conditions' in side:
                for condition in side['conditions']:
                    text += self.print_card(self.data['condition'][condition])

        if 'dial' in card:
            text += self.maneuvers(card['dial'])

        if 'pilots' in card:
            text += self.list_pilots(card)

        return text

    def print_image(self, card):
        text = []
        if 'sides' not in card:
            if 'image' in card:
                text.append(card['image'])
        else:
            for side in card['sides']:
                if 'image' in side:
                    text.append(side['image'])
        return text

    def handle_lookup(self, lookup):
        output = []
        count = 0
        for card in self.lookup(lookup):
            count += 1
            if count > 10:
                raise UserError(
                    'Your search matched more than 10 cards, please be more specific.'
                )
            output.append(self.print_card(card))
        return output

    def handle_image_lookup(self, lookup):
        output = []
        count = 0
        for card in self.lookup(lookup):
            count += 1
            if count > 10:
                raise UserError(
                    'Your search matched more than 10 cards, please be more specific.'
                )
            output += self.print_image(card)
        return [output]

    def print_device(self, device):
        return [f"{self.bold(device['name'])} ({device['type']})"] + device['effect']
