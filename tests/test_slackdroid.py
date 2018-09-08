import pytest
from r2d7.slackdroid import SlackDroid

iconify_tests = [
    ('firespray31', ':firespray31:'),
    ('bomb', ':xbomb:'),
    ('shield', ':xshield:'),
    ('Elite', ':elite:'),
    ('target lock', ':targetlock:'),
    ('Scum And Villainy', ':scum:'),
    ('Galactic Empire', ':empire:'),
    ('First Order', ':first_order:'),
]

@pytest.mark.parametrize('name, icon', iconify_tests)
def test_iconify(name, icon):
    assert SlackDroid.iconify(name) == icon

def test_bold():
    assert SlackDroid.bold('test') == '*test*'

def test_italics():
    assert SlackDroid.italics('test') == '_test_'

convert_text_tests = [
    ('Action: test', ['*Action:* test']),
    ('Setup: test', ['*Setup:* test']),
    ('Test test. End of Game: test', ['Test test.', '*End of Game:* test']),
    ('Test test. Action: test', ['Test test.', '*Action:* test']),
    ('[evade] test', [':evade: test']),
    ('[evade] test [focus]', [':evade: test :focus:']),
    ('[Koiogran Turn]', [':kturn:']),
    ('[Turn Right]', [':turnright:']),
    ('[Turn Left]', [':turnleft:']),
    ('[Bank Right]', [':bankright:']),
    ('[Bank Left]', [':bankleft:']),
    ('[Segnor\'s Loop Left]', [':sloopleft:']),
    ('[Segnor\'s Loop Right]', [':sloopright:']),
    ('[Tallon Roll Left]', [':trollleft:']),
    ('[Tallon Roll Right]', [':trollright:']),
    ('[Critical Hit]', [':crit:']),
    ('[Bomb]', [':xbomb:']),
    ('[Barrel Roll]', [':barrelroll:']),
    ('[Lock]', [':targetlock:']),
    ('[0 [Stationary]]', ['[0 :stop:]']),
    ('[1 [Bank Right]]', ['[1 :bankright:]']),
]
@pytest.mark.parametrize('before, after', convert_text_tests)
def test_convert_text(before, after):
    assert SlackDroid.convert_text(before) == after
