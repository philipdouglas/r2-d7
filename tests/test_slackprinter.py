import pytest
from r2d7.slackprinter import SlackPrinter

name_to_icon_tests = [
    ('firespray31', ':firespray31:'),
    ('bomb', ':xbomb:'),
    ('shield', ':xshield:'),
    ('Elite', ':elite:'),
    ('target lock', ':targetlock:'),
    ('Scum And Villainy', ':scum:'),
]

@pytest.mark.parametrize('name, icon', name_to_icon_tests)
def test_name_to_icon(name, icon):
    assert SlackPrinter.name_to_icon(name) == icon

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
]
@pytest.mark.parametrize('before, after', convert_html_tests)
def test_convert_html(before, after):
    assert SlackPrinter.convert_html(before) == after
