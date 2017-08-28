import pytest

from r2d7.factionlister import FactionLister
from r2d7.slackdroid import SlackDroid

print_faction_ships_tests = (
    ('nope', []),
    ('scum', [
        ':ywing::firespray31::hwk290::z95headhunter::starviper:'
        ':m3ainterceptor::aggressor::yv666::kihraxzfighter::jumpmaster5000:'
        ':g1astarfighter::protectoratestarfighter::lancerclasspursuitcraft:'
        ':quadjumper::scurrgh6bomber::m12lkimogilafighter:'
    ],),
    ('rebel', [
        ':xwing::ywing::awing::yt1300::tiefighter::hwk290::bwing:'
        ':z95headhunter::ewing::yt2400::kwing::t70xwing::vcx100:'
        ':attackshuttle::arc170::uwing::auzituckgunship::scurrgh6bomber:'
        ':sheathipedeclassshuttle:'
    ]),
)
@pytest.mark.parametrize('emoji, output', print_faction_ships_tests)
def test_print_faction_ships(testbot, emoji, output):
    assert testbot.print_faction_ships(emoji) == output
