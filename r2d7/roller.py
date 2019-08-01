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
    pattern_def = re.compile('((green)|(g))', re.I)
    pattern_atk = re.compile('((red)|(r))', re.I)
    target_num_dice = 'num_dice'
    target_color = 'color'
    pattern_main = re.compile('(?P<num_dice>[0-9]+) ?(?P<color>%s|%s)' % (re_def, re_atk), re.I)
    pattern_mod_count = re.compile('[0-9]+', re.I)
    pattern_mod = {
            'focus':re.compile('focus', re.I),
            'evade':re.compile('evade', re.I),
            'reinforce':re.compile('reinforce', re.I),
            'lock':re.compile('(target )?lock(ed?)', re.I),
            'calculate':re.compile('(?P<calculate>([0-9]+ calculate)|(calculate [0-9]+))', re.I),
            'force':re.compile('(?P<force>([0-9]+ force)|(force [0-9]+))', re.I), #TODO don't forget to set max_force
            'reroll':re.compile('(?P<reroll>([0-9]+ reroll)|(reroll [0-9]+))', re.I
    }
    def __init__(self, message):
        match_main = re.search
        try:
            
            self.focus = re.match

        except Exception as e:
            raise RollError('You confused me. Type `!roll syntax` for help')

        #TODO parse input string
        #TODO raise RollSyntaxError('error text') if input string is bad

    def actual_roll(self):
        #TODO
        return ':jar_jar:'

    def expected_result(self):
        #TODO hit the calculator for an expected result
        return ':agreedo:'

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
    target_vs = 'vs'
    pattern_vs = re.compile('(?P<%s>(vs)|(versus))' % target_vs, re.I)
    pattern_syntax = re.compile('syntax', re.I)

    def __init__(self):
        super().__init__()
        self.register_handler(Roller.pattern_handler, self.roll)

    def roll_dice(self, message):
        match_vs = re.search(Roller.pattern_vs, message)
        match_syntax = re.search(Roller.pattern_syntax, message)
        if match_syntax:
            return roll_syntax()
        else:
            try:
                if match_vs:
                    roll_strings = message.split(match_vs.group(target_vs))
                    modded_rolls = [ModdedRoll(r) for r in roll_strings]
                    if modded_rolls[0].die_type == modded_rolls[1].die_type:
                        raise RollSyntaxError('Opposing rolls cannot have same color')
                    else if modded_rolls[0].die_type == attack:
                        roll = VsRoll(modded_rolls[0], modded_rolls[1])
                    else:
                        roll = VsRoll(modded_rolls[1], modded_rolls[0])

                else:
                    roll = ModdedRoll(message)
                return roll.output
            except RollSyntaxError as err:
                logger.debug('incorrect roll syntax: %s' % str(err))
                return [err]

    def roll_syntax(self):
        output = []
        output.append('To roll dice, type `!roll` followed by the number and color of dice. You may include comma-separated dice mods.')
        output.append('e.g.: `!roll 3 red with lock, 1 calculate`')
        output.append('You may also roll both red and green dice using `vs`.')
        output.append('e.g.: `!roll 2 red with focus vs 3 green with calculate and evade`')
        return output

