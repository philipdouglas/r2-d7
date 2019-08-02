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
    faces = []

    def roll(self):
        return random.choice(self.faces)

class AttackDie(Die):
    faces = ['hit', 'hit', 'hit', 'crit', 'blank', 'blank', 'focus', 'focus']
    die_type = DieType.attack

class DefenceDie(Die):
    faces = ['evade', 'evade', 'evade', 'blank', 'blank', 'blank', 'focus', 'focus']
    die_type = DieType.defence

class RollSyntaxError(Exception):
    pass

class ModdedRoll(object):
    _re_def = '((green)|(g))'
    _re_atk = '((red)|(r))'
    pattern_def = re.compile(_re_def, re.I)
    pattern_atk = re.compile(_re_atk, re.I)
    pattern_main = re.compile('(?P<num_dice>[0-9]+) ?(?P<color>%s|%s)' % (_re_def, _re_atk), re.I)
    pattern_count = re.compile('([0-9]+)', re.I)
    pattern_mod = {
            'focus':re.compile('focus', re.I),
            'evade':re.compile('evade', re.I),
            'reinforce':re.compile('reinforce', re.I),
            'lock':re.compile('(target )?lock(ed?)', re.I),
            'calculate':re.compile('(?P<calculate>([0-9]+ ?calc(ulate)?)|(calc(ulate)? ?[0-9]*))', re.I),
            'force':re.compile('(?P<force>([0-9]+ ?force)|(force ?[0-9]*))', re.I),
            'reroll':re.compile('(?P<reroll>([0-9]+ ?reroll)|(reroll ?[0-9]*))', re.I)
    }

    def __init__(self, message):
        match_main = ModdedRoll.pattern_main.search(message)
        if not match_main:
            logger.debug('incorrect roll syntax: %s' % message)
            raise RollSyntaxError('I don\'t understand what you want me to roll. :purplebarrelroll:?')
            return

        try:
            self.num_dice = int(match_main.group('num_dice'))
            if pattern_atk.search(message):
                self.die_type = DieType.attack
            elif pattern_def.search(message):
                self.die_type = DieType.defence
            else:
                raise RollSyntaxError('No dice color found')

            self.focus = ModdedRoll.pattern_mod['focus'].search(message) is not None
            self.evade = ModdedRoll.pattern_mod['evade'].search(message) is not None
            self.reinforce = ModdedRoll.pattern_mod['reinforce'].search(message) is not None
            self.lock = ModdedRoll.pattern_mod['lock'].search(message) is not None

            match_calculate = ModdedRoll.pattern_mod['calculate']
            if match_calculate:
                match_count = ModdedRoll.pattern_count.search(match_calculate.group(1))
                self.calculate = int(match_count.group(1)) if match_count is not None else 1
            match_force = ModdedRoll.pattern_mod['force']
            if match_force:
                match_count = ModdedRoll.pattern_count.search(match_force.group(1))
                self.force = int(match_count.group(1)) if match_count is not None else 1
            match_reroll = ModdedRoll.pattern_mod['reroll']
            if match_reroll:
                match_count = ModdedRoll.pattern_count.search(match_reroll.group(1))
                self.reroll = int(match_count.group(1)) if match_count is not None else 1

        except Exception as err:
            logger.debug('roll parsing error: %s \n message: %s' % (str(err), message))
            raise RollSyntaxError('Incorrect dice roll syntax. Someone call a judge.')

    def actual_roll(self):
        #TODO calculate roll with greedy modding
        return ':jar_jar:'

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
    def __init__(self, atk_roll, def_roll):
        if atk_roll.die_type != DieType.attack or def_roll.die_type != DieType.defence:
            raise RollSyntaxError('Invalid dice types for vs roll')
        self.atk_roll = atk_roll
        self.def_roll = def_roll

    def output(self):
        output = ['You rolled:']
        output.append(atk_roll.actual_roll())
        output.append('vs')
        output.append(def_roll.actual_roll())
        #TODO output.append('<INSERT CALC URL|Expected damage>: %s' % expected_damage)
        return output

class Roller(DroidCore):
    pattern_handler = re.compile('^!roll.*', re.I)
    pattern_vs = re.compile('(?P<vs>(vs)|(versus))', re.I)
    pattern_syntax = re.compile('syntax', re.I)

    def __init__(self):
        super().__init__()
        self.register_handler(Roller.pattern_handler, self.roll)

    def roll_dice(self, message):
        match_vs = Roller.pattern_vs.search(message)
        match_syntax = Roller.pattern_syntax.search(message)
        if match_syntax:
            return roll_syntax()
        else:
            try:
                if match_vs:
                    roll_strings = message.split(match_vs.group('vs'))
                    modded_rolls = [ModdedRoll(r) for r in roll_strings]
                    if modded_rolls[0].die_type == modded_rolls[1].die_type:
                        raise RollSyntaxError('Opposing rolls cannot have same color')
                    elif modded_rolls[0].die_type == attack:
                        roll = VsRoll(modded_rolls[0], modded_rolls[1])
                    else:
                        roll = VsRoll(modded_rolls[1], modded_rolls[0])

                else:
                    roll = ModdedRoll(message)
                return roll.output
            except RollSyntaxError as err:
                return [err, 'Type `!roll syntax` for help']

    def roll_syntax(self):
        output = []
        output.append('To roll dice, type `!roll` followed by the number and color of dice. You may include comma-separated dice mods.')
        output.append('e.g.: `!roll 3 red with lock, 1 calculate`')
        output.append('You may also roll both red and green dice using `vs`.')
        output.append('e.g.: `!roll 2 red with focus vs 3 green with calc and evade`')
        return output

