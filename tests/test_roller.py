import pytest
import re
from r2d7.roller import Roller, VsRoll, ModdedRoll

roll_mistake_tests = (
    ('!roll a d20', ['I don\'t understand what you want me to roll. :barrelroll:?', 'Type `!roll syntax` for help']),
    ('!roll roger roger', ['I don\'t understand what you want me to roll. :barrelroll:?', 'Type `!roll syntax` for help']),
    ('!roll 200 red', ['Sorry, I can\'t carry more than 100 dice, and chopper won\'t help :chopper:', 'Type `!roll syntax` for help']),
    ('!roll 2 red 4 rerolls', ['Sorry, the calculator only allows up to 3 rerolls', 'Type `!roll syntax` for help']),
    ('!roll 2 blurgh', ['I don\'t understand what you want me to roll. :barrelroll:?', 'Type `!roll syntax` for help']),
    # no need to test -ve input as minus sign is ignored by parser
    ('!roll 0 red', ['Sorry, I can\'t roll fewer than 1 dice :jar_jar:', 'Type `!roll syntax` for help']),
    ('!roll 2 red vs 3 red', ['Opposing rolls cannot have same color', 'Type `!roll syntax` for help']),
    ('!roll syntax', ['To roll dice, type `!roll` followed by the number and color of dice. You may include comma-separated dice mods.','e.g.: `!roll 3 red with lock, 1 calculate`','You may also roll both red and green dice using `vs`.','e.g.: `!roll 2 red with focus vs 3 green with calc and evade`']),
    ('!roll help', ['To roll dice, type `!roll` followed by the number and color of dice. You may include comma-separated dice mods.','e.g.: `!roll 3 red with lock, 1 calculate`','You may also roll both red and green dice using `vs`.','e.g.: `!roll 2 red with focus vs 3 green with calc and evade`'])
)
@pytest.mark.parametrize('message, expected', roll_mistake_tests)
def test_roll_mistakes(testbot, message, expected):
    print(testbot.roll_dice(message))
    print(expected)
    assert testbot.roll_dice(message) == [expected]

roll_parse_tests = (
    ('!roll 3 red', {'dice': 3}),
    ('!roll 3 r focus 3', {'dice': 3, 'focus': True}),
    ('!roll 3 red', {'dice': 3, 'focus': False, 'lock': False, 'evade': 0, 'reinforce': 0, 'force': 0, 'calculate': 0, 'reroll': 0}),
    ('!roll 3 red lock', {'dice': 3, 'lock': True}),
    ('!roll 3 red 3 reroll', {'dice': 3, 'lock': False, 'reroll': 3}),
    ('!roll 2 red 3 reroll', {'dice': 2, 'lock': False, 'reroll': 3}),
    ('!roll 5 green with focus', {'dice': 5, 'focus': True, 'evade': 0}),
    ('!roll 22 green focus and lock and reinforce', {'dice': 22, 'focus': True, 'evade': 0, 'lock': True, 'reinforce': 1}),
    ('!roll 22 green focus and lock and reinforce and reinforce', {'dice': 22, 'focus': True, 'evade': 0, 'lock': True, 'reinforce': 1}),
    ('!roll 10 red with 10 reinforce and focus, also a lock and 3 calculate', {'dice': 10, 'focus': True, 'evade': 0, 'lock': True, 'reinforce': 10, 'calculate': 3}),
    ('!roll 1 green with focus, reinforce, evade, reroll, calculate, force', {'dice': 1, 'focus': True, 'reinforce': 1, 'evade': 1, 'reroll': 1, 'calculate': 1, 'force': 1}),
    ('!roll 2 green with 2 reinforce, 6 force', {'dice': 2, 'reinforce': 2, 'evade': 0, 'reroll': 0, 'calculate': 0, 'force': 6}),
    ('!roll 2 green with 3 reinforce, 66 force', {'dice': 2, 'reinforce': 3, 'force': 66}),
    ('!roll 2 green with 2 force, 6 reinforce', {'dice': 2, 'reinforce': 6, 'evade': 0, 'reroll': 0, 'calculate': 0, 'force': 2}),
    ('!roll 2 green with focus, 6 force, 2 reinforce, 4 evade, 3 reroll, 5 calculate', {'dice': 2, 'focus': True, 'reinforce': 2, 'evade': 4, 'reroll': 3, 'calculate': 5, 'force': 6}),
    ('!roll 66 red w 66 force', {'dice': 66, 'focus': False, 'force': 66}),
    ('!roll 50 green w/ 49 evade', {'dice': 50, 'focus': False, 'evade': 49}),
    ('!roll 3 red with a lock and a ham sandwich', {'dice': 3, 'lock': True}),
    ('!roll 3 red with a lock, cheese, and 2 calculates', {'dice': 3, 'lock': True, 'calculate': 2}),
)
@pytest.mark.parametrize('message, expected', roll_parse_tests)
def test_roll_parse(message, expected):
    parsed = ModdedRoll(message)
    for key, value in expected.items():
        if key == 'dice':
            assert len(getattr(parsed, key)) == value
        else:
            assert getattr(parsed, key) == value

calculator_safe_tests = (
    ('!roll 3 red', True),
    ('!roll 3 r focus 3', True),
    ('!roll 3 r focus 3, 1 reinforce', True),
    ('!roll 66 red w 66 force', False),
    ('!roll 50 green w/ 49 evade', False),
    ('!roll 3 red 2 reinforce', False),
)
@pytest.mark.parametrize('message, expected', calculator_safe_tests)
def test_calculator_safe(message, expected):
    parsed = ModdedRoll(message)
    assert parsed.calculator_safe() == expected

roll_output_tests = (
    ('!roll 3 red', r'/:[a-z]*:\\/:[a-z]*:\\/:[a-z]*:\\'),
    ('!roll 5 green with reinforce', r'/:[a-z]*:\\/:[a-z]*:\\/:[a-z]*:\\/:[a-z]*:\\/:[a-z]*:\\ [+] :reinforce:'),
    ('!roll 1 green with 4 reinforce', r'/:[a-z]*:\\ [+] :reinforce::reinforce::reinforce::reinforce:'),
    ('!roll 1 green with 1 reinforce', r'/:[a-z]*:\\ [+] :reinforce:'),
    ('!roll 2 green with 49 evade', r'/:evade:\\/:evade:\\')
    # watch out for backslashes when making new test cases
)
@pytest.mark.parametrize('message, expected_pattern', roll_output_tests)
def test_roll_output(message, expected_pattern):
    roll = ModdedRoll(message)
    print(roll.actual_roll())
    match = re.match(expected_pattern, roll.actual_roll())
    assert match is not None

# testing rerolls is kinda hard since the output is unknown
# but we can still test force, calculate, focus and evade
roll_focus_tests = (
    (10, True, 0, 0, 10),       # focus only
    (10, False, 10, 0, 10),     # calculate only
    (10, False, 0, 10, 10),     # force only
    (10, True, 10, 10, 10),     # all tokens
    (10, True, 100, 100, 10),   # excess tokens
    (10, False, 0, 5, 5),       # some tokens
    (10, False, 3, 3, 6),       # mix of tokens
    (10, False, 4, 1, 5),       # mix of tokens
    (10, False, 0, 0, 0),       # none
)
@pytest.mark.parametrize('num_dice, focus, num_calculate, num_force, expected_num_converted', roll_focus_tests)
def test_roll_focus(num_dice, focus, num_calculate, num_force, expected_num_converted):
    for color in ['red', 'green']:
        roll = ModdedRoll('!roll %d %s' % (num_dice, color))
        for d in roll.dice:
            d.set_to_focus()
        roll.focus = focus
        roll.calculate = num_calculate
        roll.force = num_force
        roll.modify_dice()
        num_converted = sum([1 for d in roll.dice if d.result == d._focussed])
        assert num_converted == expected_num_converted

roll_evade_tests = (
    (10, 10, 10),       # all
    (10, 60, 10),       # too many
    (10, 5, 5),         # some
    (10, 3, 3),         # some
    (10, 0, 0),         # none
)
@pytest.mark.parametrize('num_dice, num_evade, expected_num_converted', roll_evade_tests)
def test_roll_evade(num_dice, num_evade, expected_num_converted):
    roll = ModdedRoll('!roll %d green' % (num_dice))
    for d in roll.dice:
        d.set_to_blank()
    roll.evade = num_evade
    roll.modify_dice()
    num_converted = sum([1 for d in roll.dice if d.result == d._focussed])
    assert num_converted == expected_num_converted

