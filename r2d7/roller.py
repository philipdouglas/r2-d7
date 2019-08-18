from collections import OrderedDict
from enum import Enum
import logging
import re
import random

from r2d7.core import DroidCore, DroidException

logger = logging.getLogger(__name__)
calc_url_base = 'http://xwing.gateofstorms.net/2/multi/'

class DieType(Enum):
    attack = 'atk'
    defence = 'def'

class Die(object):
    """
    Skeleton base class. Subclasses should populate the fields below
    """
    _faces = []
    _focussed = None
    _emoji = {
            None: ' ? '
            }
    _positive_faces = []
    die_type = None

    def __init__(self):
        self.roll() # to place a die on the table, you have to roll it

    def roll(self):
        self.result = random.choice(self._faces)
        return self.result

    def reroll(self):
        if self.result not in self._positive_faces:
            self.roll()
            return True
        else:
            return False

    def focus(self):
        if self.result == 'focus':
            self.result = self._focussed
            return True
        else:
            return False

    def __str__(self):
        return '/%s\\' % self._emoji[self.result]

class AttackDie(Die):
    _faces = ['hit', 'hit', 'hit', 'crit', 'blank', 'blank', 'focus', 'focus']
    _focussed = 'hit'
    _emoji = {
            'hit': ':hit:',
            'crit': ':crit:',
            'focus': ':focus:',
            'blank': ':blank:',
            None: ' ? '
            }
    _positive_faces = ['hit','crit']
    die_type = DieType.attack

class DefenceDie(Die):
    _faces = ['evade', 'evade', 'evade', 'blank', 'blank', 'blank', 'focus', 'focus']
    _focussed = 'evade'
    _emoji = {
            'focus': ':focus:',
            'evade': ':evade:',
            'blank': ':blank:',
            None: ' ? '
            }
    _positive_faces = ['evade']
    die_type = DieType.defence

    def evade(self):
        if self.result not in self._positive_faces:
            self.result = self._positive_faces[0]
            return True
        else:
            return False

dieFactory = {
        DieType.attack: AttackDie,
        DieType.defence: DefenceDie
        }

class RollSyntaxError(Exception):
    pass

class ModdedRoll(object):
    """
    Class for managing all aspects of a roll. It parses, it rolls, it queries the online calculator.
    """
    _re_def = '((green)|(g(?![a-z])))'
    _re_atk = '((red)|(r(?![a-z])))'
    pattern_def = re.compile(_re_def, re.I)
    pattern_atk = re.compile(_re_atk, re.I)
    pattern_main = re.compile('(?P<num_dice>[0-9]+) ?(?P<color>%s|%s)' % (_re_def, _re_atk), re.I)
    pattern_count = re.compile('([0-9]+)', re.I)
    pattern_mod = {
            'focus':re.compile('(?P<focus>([0-9]+ ?focus)|(focus ?[0-9]*))', re.I),
            'evade':re.compile('(?P<evade>([0-9]+ ?evade)|(evade ?[0-9]*))', re.I),
            'reinforce':re.compile('(?P<reinforce>([0-9]+ ?reinforce)|(reinforce ?[0-9]*))', re.I),
            'lock':re.compile('(target )?lock(ed)?', re.I),
            'calculate':re.compile('(?P<calculate>([0-9]+ ?calc(ulate)?)|(calc(ulate)? ?[0-9]*))', re.I),
            'force':re.compile('(?P<force>([0-9]+ ?force)|(force ?[0-9]*))', re.I),
            'reroll':re.compile('(?P<reroll>([0-9]+ ?reroll)|(reroll ?[0-9]*))', re.I)
    }

    def __init__(self, message):
        match_main = ModdedRoll.pattern_main.search(message)
        if not match_main:
            logger.debug('roll parsing error: bad roll syntax: %s' % message)
            raise RollSyntaxError('I don\'t understand what you want me to roll. :purplebarrelroll:?')
            return

        try:
            self.num_dice = int(match_main.group('num_dice'))
        except Exception as err:
            logger.debug('roll parsing error: unknown number of dice: %s \n message: %s' % (str(err), message))
            raise RollSyntaxError('I don\'t know how many dice you want me to roll')

        color_string = match_main.group('color') or ''
        if ModdedRoll.pattern_atk.search(message):
            self.die_type = DieType.attack
        elif ModdedRoll.pattern_def.search(message):
            self.die_type = DieType.defence
        else:
            logger.debug('roll parsing error: no dice color found')
            raise RollSyntaxError('I don\'t know what color dice you want me to roll')
        self.dice = [dieFactory[self.die_type]() for i in range(self.num_dice)]

        try:
            self.parse_mod_boolean('focus', message)
            self.parse_mod_boolean('lock', message)
            self.parse_mod_numeric('evade', message)
            self.parse_mod_numeric('reinforce', message)
            self.parse_mod_numeric('calculate', message)
            self.parse_mod_numeric('force', message)
            self.parse_mod_numeric('reroll', message)

        except Exception as err:
            logger.debug('roll parsing error: %s \n message: %s' % (str(err), message))
            raise RollSyntaxError('Incorrect dice roll syntax. Someone call a judge.')

        if self.reroll > 3:
            logger.debug('Too many rerolls requested (max: 3, requested: %d)' % (self.reroll))
            raise RollSyntaxError('Sorry, the calculator only allows up to 3 rerolls')

        self.modify_dice()

    def parse_mod_boolean(self, attr_name, message):
        value = ModdedRoll.pattern_mod[attr_name].search(message) is not None
        object.__setattr__(self, attr_name, value)

    def parse_mod_numeric(self, attr_name, message):
        match_mod = ModdedRoll.pattern_mod[attr_name].search(message)
        if match_mod:
            match_count = ModdedRoll.pattern_count.search(match_mod.group(1))
            value = int(match_count.group(1)) if match_count is not None else 1
        else:
            value = 0
        object.__setattr__(self, attr_name, value)

    def actual_roll(self):
        output = ''.join([str(d) for d in self.dice])
        # reinforce is a special case
        # It can't be meaningfully added without knowing the attack roll
        # Instead of implementing it as an added result, just show that
        # there were reinforce tokens in play. This is just as useful to
        # users and is much simpler to implement.
        if self.reinforce > 0 and self.die_type == DieType.defence:
            output = output + ' + ' + ':reinforce:'*self.reinforce
        return output

    def modify_dice(self):
        if len(self.dice) == 0:
            return

        #reroll first!
        if self.die_type == DieType.attack and self.lock:
            [d.reroll() for d in self.dice]
        elif self.reroll > 0:
            rerolls = self.reroll
            for d in self.dice:
                rerolls = rerolls - 1 if d.reroll() else rerolls
                if rerolls == 0:
                    break

        # after reroll, apply other mods
        # this is a 1-off calculation so we can spend force greedily
        calculates = self.calculate
        force = self.force
        evades = self.evade
        for d in self.dice:
            focussed = False
            if self.focus:
                focussed = d.focus()
            elif calculates > 0:
                focussed = d.focus()
                calculates = calculates - 1 if focussed else calculates
            elif force > 0:
                focussed = d.focus()
                force = force - 1 if focussed else force
            if not focussed and evades > 0 and d.die_type == DieType.defence:
                evades = evades - 1 if d.evade() else evades

    def expected_result(self):
        #TODO hit the calculator for an expected result
        # don't forget to set max_force = force
        return ':barrelroll:'

    def output(self):
        output = []
        output.append('Actual roll: %s' % self.actual_roll())
        #TODO use calc link etc output.append('Expected: %s' % self.expected_result())
        return output

class VsRoll(object):
    """
    An attack roll and opposing defence roll
    """
    def __init__(self, atk_roll, def_roll):
        if atk_roll.die_type != DieType.attack or def_roll.die_type != DieType.defence:
            raise RollSyntaxError('Invalid dice types for vs roll')
        self.atk_roll = atk_roll
        self.def_roll = def_roll

    def output(self):
        output = ['You rolled:']
        output.append(self.atk_roll.actual_roll())
        output.append('vs')
        output.append(self.def_roll.actual_roll())
        #TODO output.append('<INSERT CALC URL|Expected damage>: %s' % expected_damage)
        return output

class Roller(DroidCore):
    """
    Handler class, contains slack chat logic
    """
    pattern_handler = re.compile('(!roll.*)', re.I)
    pattern_vs = re.compile('(?P<vs>(vs)|(versus))', re.I)
    pattern_syntax = re.compile('syntax', re.I)

    def __init__(self):
        super().__init__()
        self.register_handler(Roller.pattern_handler, self.roll_dice)

    def roll_dice(self, message):
        match_vs = Roller.pattern_vs.search(message)
        match_syntax = Roller.pattern_syntax.search(message)
        if match_syntax:
            return [roll_syntax()]
        else:
            try:
                if match_vs:
                    roll_strings = message.split(match_vs.group('vs'))
                    modded_rolls = [ModdedRoll(r) for r in roll_strings]
                    if modded_rolls[0].die_type == modded_rolls[1].die_type:
                        raise RollSyntaxError('Opposing rolls cannot have same color')
                    elif modded_rolls[0].die_type == DieType.attack:
                        roll = VsRoll(modded_rolls[0], modded_rolls[1])
                    else:
                        roll = VsRoll(modded_rolls[1], modded_rolls[0])

                else:
                    roll = ModdedRoll(message)
                return [roll.output()]
            except RollSyntaxError as err:
                return [[err.__str__(), 'Type `!roll syntax` for help']]

    def roll_syntax(self):
        output = []
        output.append('To roll dice, type `!roll` followed by the number and color of dice. You may include comma-separated dice mods.')
        output.append('e.g.: `!roll 3 red with lock, 1 calculate`')
        output.append('You may also roll both red and green dice using `vs`.')
        output.append('e.g.: `!roll 2 red with focus vs 3 green with calc and evade`')
        return output

