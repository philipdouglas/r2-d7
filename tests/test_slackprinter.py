import pytest
from r2d7.slackprinter import SlackPrinter

iconify_tests = [
    ('firespray31', ':firespray31:'),
    ('bomb', ':xbomb:'),
    ('shield', ':xshield:'),
    ('Elite', ':elite:'),
    ('target lock', ':targetlock:'),
    ('Scum And Villainy', ':scum:'),
    ('Galactic Empire', ':empire:'),
]

@pytest.mark.parametrize('name, icon', iconify_tests)
def test_iconify(name, icon):
    assert SlackPrinter.iconify(name) == icon

def test_bold():
    assert SlackPrinter.bold('test') == '*test*'

def test_italics():
    assert SlackPrinter.italics('test') == '_test_'

convert_html_tests = [
    ('<strong>Action:</strong> test', '*Action:* test'),
    ('<br /><br />', '\n'),
    ('<br />', '\n'),
    ('[evade] test', ':evade: test'),
    ('[evade] test [focus]', ':evade: test :focus:'),
    ('[Koiogran Turn]', ':kturn:'),
    ('[Bomb]', ':xbomb:'),
]
@pytest.mark.parametrize('before, after', convert_html_tests)
def test_convert_html(before, after):
    assert SlackPrinter.convert_html(before) == after
