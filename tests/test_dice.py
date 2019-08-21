import pytest
from r2d7.dice import AttackDie, DefenseDie

def test_dice_implementation():
    for die in [AttackDie(), DefenseDie()]:
        for f in die._positive_faces:
            assert f in die._faces
        assert die._focussed in die._positive_faces
        assert set(die._faces).issubset(set(die._emoji.keys()))

def test_dice_focus():
    for die in [AttackDie(), DefenseDie()]:
        die.set_to_focus()
        assert die.result == 'focus'
        assert die.focus() == True
        assert die.result == die._focussed
        assert die.result in die._positive_faces
        die.set_to_blank()
        assert die.result == 'blank'
        assert die.focus() == False
        assert die.result == 'blank'

def test_dice_evade():
    die = DefenseDie()
    die.set_to_focus()
    assert die.result == 'focus'
    assert die.evade() == True
    assert die.result in die._positive_faces
    die.set_to_blank()
    assert die.result == 'blank'
    assert die.evade() == True
    assert die.result in die._positive_faces
    assert die.evade() == False
    assert die.result in die._positive_faces

