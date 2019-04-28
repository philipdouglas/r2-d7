import pytest
from r2d7.slackdroid import SlackDroid

iconify_tests = [
    ('firespray31', ':firespray31:'),
    ('bomb', ':xbomb:'),
    ('shield', ':xshield:'),
    ('Elite', ':elite:'),
    ('target lock', ':targetlock:'),
    ('Scum And Villainy', ':scum:'),
    ('Galactic Empire', ':imperial:'),
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
    ('you must receive 1', ['you *must* receive 1']),
    ('You may use your Adaptive Ailerons even while stressed.',
     ['You may use your _*Adaptive Ailerons*_ even while stressed.']),
    ('Mine During the System Phase', ['_*Mine:*_ During the System Phase']),
    ('Bomb During the System Phase', ['_*Bomb:*_ During the System Phase']),
    ('Ship damage card', ['_*Ship*_ damage card']),
    ('test, you may use another template of the same speed instead: either the turn',
     ['test, you may use another template of the same speed instead: either the turn']),
]
@pytest.mark.parametrize('before, after', convert_text_tests)
def test_convert_text(testbot, before, after):
    assert testbot.convert_text(before) == after
