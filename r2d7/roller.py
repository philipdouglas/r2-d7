from enum import Enum
import logging
import re
from .calculator import *
from .dice import DieType, AttackDie, DefenseDie, dieFactory
from r2d7.core import DroidCore

logger = logging.getLogger(__name__)

class RollSyntaxError(Exception):
    pass

class ModdedRoll(object):
    """
    Class for managing all aspects of a roll. It parses, it rolls, it queries the online calculator.
    """
    _re_def = '\\b((green)|(g))\\b'
    _re_atk = '\\b((red)|(r))\\b'
    pattern_def = re.compile(_re_def, re.I)
    pattern_atk = re.compile(_re_atk, re.I)
    pattern_main = re.compile('(?P<num_dice>[0-9]+) ?(?P<color>%s|%s)' % (_re_def, _re_atk), re.I)
    pattern_count = re.compile('([0-9]+)', re.I)
    pattern_mod = {
            # \\b at the start forces a new word (stops force/reinforce confusion)
            # leaving it off the end allows plural matching
            'focus':re.compile('\\b(?P<focus>([0-9]+ ?focus)|(focus ?[0-9]*))', re.I),
            'evade':re.compile('\\b(?P<evade>([0-9]+ ?evade)|(evade ?[0-9]*))', re.I),
            'reinforce':re.compile('\\b(?P<reinforce>([0-9]+ ?reinforce)|(reinforce ?[0-9]*))', re.I),
            'lock':re.compile('\\b(target )?lock(ed)?\\b', re.I),
            'calculate':re.compile('\\b(?P<calculate>([0-9]+ ?calc(ulate)?)|(calc(ulate)? ?[0-9]*))', re.I),
            'force':re.compile('\\b(?P<force>([0-9]+ ?force)|(force ?[0-9]*))', re.I),
            'reroll':re.compile('\\b(?P<reroll>([0-9]+ ?reroll)|(reroll ?[0-9]*))', re.I)
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

        if self.num_dice > 100:
            logger.debug('Too many dice requested (max: 100, requested: %d)' % (self.num_dice))
            raise RollSyntaxError('Sorry, I can\'t carry more than 100 dice, and chopper won\'t help :chopper:')
        elif self.num_dice < 1:
            logger.debug('Too few dice requested (min: 1, requested: %d)' % (self.num_dice))
            raise RollSyntaxError('Sorry, I can\'t roll fewer than 1 dice :jar_jar:')

        color_string = match_main.group('color') or ''
        if ModdedRoll.pattern_atk.search(message):
            self.die_type = DieType.attack
        elif ModdedRoll.pattern_def.search(message):
            self.die_type = DieType.defense
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
            if not focussed and evades > 0 and d.die_type == DieType.defense:
                evades = evades - 1 if d.evade() else evades

    def roll_safe(self):
        return len(self.dice) <= CalculatorForm.max_dice and self.reinforce <= CalculatorForm.max_reinforce

    def calculator_form(self):
        if self.die_type == DieType.attack:
            form = AttackForm(dice = len(self.dice),
                    focus = 1 if self.focus else 0,
                    calculate = self.calculate,
                    evade = self.evade,
                    reinforce = self.reinforce,
                    lock = 1 if self.lock else 0,
                    force = self.force,
                    reroll = self.reroll)
        else:
            form = DefenseForm(dice = len(self.dice),
                    focus = 1 if self.focus else 0,
                    calculate = self.calculate,
                    evade = self.evade,
                    reinforce = self.reinforce,
                    lock = 1 if self.lock else 0,
                    force = self.force,
                    reroll = self.reroll)
        return form

    def actual_roll(self):
        output = ''.join([str(d) for d in self.dice])
        # reinforce is a special case
        # It can't be meaningfully added without knowing the attack roll
        # Instead of implementing it as an added result, just show that
        # there were reinforce tokens in play. This is just as useful to
        # users and is much simpler to implement.
        if self.reinforce > 0 and self.die_type == DieType.defense:
            output = output + ' + ' + ':reinforce:'*self.reinforce
        return output

    def output(self):
        output = []
        output.append('You rolled: %s' % self.actual_roll())
        if self.roll_safe():
            if self.die_type == DieType.attack:
                try:
                    calculator = Calculator(attack_form = self.calculator_form(), defense_form = DefenseForm())
                    calculator.calculate()
                    output.append('<%s|Expected total hits:> *%s*' % (calculator.url, calculator.expected_hits()))
                except Exception as err:
                    logger.debug('Dice calculator error: %s' % (str(err)))
            else:
                try:
                    num_dice = len(self.dice)
                    attack_form = AttackForm(dice = num_dice, all_hits = True)
                    calculator = Calculator(attack_form = attack_form, defense_form = self.calculator_form())
                    calculator.calculate()
                    output.append('<%s|Expected damage suffered from %d hits:> *%s*' % (calculator.url, num_dice, calculator.expected_hits()))
                except Exception as err:
                    logger.debug('Dice calculator error: %s' % (str(err)))
        return output

class VsRoll(object):
    """
    An attack roll and opposing defense roll
    """
    def __init__(self, atk_roll, def_roll):
        if atk_roll.die_type != DieType.attack or def_roll.die_type != DieType.defense:
            raise RollSyntaxError('Invalid dice types for vs roll')
        self.atk_roll = atk_roll
        self.def_roll = def_roll

    def output(self):
        output = ['You rolled:']
        output.append(self.atk_roll.actual_roll())
        output.append('vs')
        output.append(self.def_roll.actual_roll())
        if self.atk_roll.roll_safe() and self.def_roll.roll_safe():
            try:
                calculator = Calculator(attack_form = self.atk_roll.calculator_form(), defense_form = self.def_roll.calculator_form())
                calculator.calculate()
                output.append('<%s|Expected total hits:> *%s*' % (calculator.url, calculator.expected_hits()))
            except Exception as err:
                logger.debug('Dice calculator error: %s' % (str(err)))
        return output

class Roller(DroidCore):
    """
    Handler class, contains slack chat logic
    """
    pattern_handler = re.compile('(!roll.*)', re.I)
    pattern_vs = re.compile('\\b(?P<vs>(vs)|(versus)|(v))\\b', re.I)
    pattern_syntax = re.compile('\\bsyntax\\b', re.I)

    def __init__(self):
        super().__init__()
        self.register_handler(Roller.pattern_handler, self.roll_dice)

    def roll_dice(self, message):
        match_vs = Roller.pattern_vs.search(message)
        match_syntax = Roller.pattern_syntax.search(message)
        if match_syntax:
            return [self.roll_syntax()]
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

