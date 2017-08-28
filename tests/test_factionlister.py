import pytest

from r2d7.factionlister import FactionLister
from r2d7.slackdroid import SlackDroid

@pytest.fixture(scope="module")
def testbot():
    class TestBot(SlackDroid, FactionLister):
        pass
    bot = TestBot()
    bot.load_data()
    return bot

print_faction_ships_tests = (
    ('nope', []),
    ('scum', [
        ':ywing::firespray31::hwk290::z95headhunter::starviper:'
        ':m3ainterceptor::aggressor::yv666::kihraxzfighter::jumpmaster5000:'
        ':g1astarfighter::protectoratestarfighter::lancerclasspursuitcraft:'
        ':quadjumper::scurrgh6bomber::m12lkimogilafighter:'
    ],),
)
@pytest.mark.parametrize('emoji, output', print_faction_ships_tests)
def test_print_faction_ships(testbot, emoji, output):
    assert testbot.print_faction_ships(emoji) == output
