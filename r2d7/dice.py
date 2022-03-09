from enum import Enum
import random

class DieType(Enum):
    attack = 'atk'
    defense = 'def'

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
        if self.result in self._positive_faces:
            return False
        self.roll()
        return True

    def focus(self):
        if self.result != 'focus':
            return False
        self.result = self._focussed
        return True

    def set_to_blank(self):
        if self.result == 'blank':
            return False
        self.result = 'blank'
        return True

    def set_to_focus(self):
        if self.result == 'focus':
            return False
        self.result = 'focus'
        return True

    def __str__(self):
        return f'/{self._emoji[self.result]}\\'

class AttackDie(Die):
    _faces = ['hit', 'hit', 'hit', 'crit', 'blank', 'blank', 'focus', 'focus']
    _focussed = 'hit'
    _emoji = {
            'hit': ':atkhit:',
            'crit': ':atkcrit:',
            'focus': ':atkfocus:',
            'blank': ':atkblank:',
            None: ' ? '
            }
    _positive_faces = ['hit', 'crit']
    die_type = DieType.attack

class DefenseDie(Die):
    _faces = ['evade', 'evade', 'evade', 'blank', 'blank', 'blank', 'focus', 'focus']
    _focussed = 'evade'
    _emoji = {
            'focus': ':deffocus:',
            'evade': ':defevade:',
            'blank': ':defblank:',
            None: ' ? '
            }
    _positive_faces = ['evade']
    die_type = DieType.defense

    def evade(self):
        if self.result in self._positive_faces:
            return False
        self.result = self._positive_faces[0]
        return True

dieFactory = {
        DieType.attack: AttackDie,
        DieType.defense: DefenseDie
        }

