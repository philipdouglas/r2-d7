import pytest
from r2d7.calculator import *

def test_form_reroll():
    for num_rerolls in [1,2,3]:
        attack = AttackForm(reroll = num_rerolls)
        defense = DefenseForm(reroll = num_rerolls)
        assert attack.pilot == getattr(AttackPilot, 'reroll_%d' % num_rerolls)
        assert defense.pilot == getattr(DefensePilot, 'reroll_%d' % num_rerolls)

# no other calculator tests as they require an internet connection, and the calculator class itself is pretty simple

