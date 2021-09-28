import pytest

from r2d7.factionlister import FactionLister
from r2d7.slackdroid import SlackDroid

print_faction_ships_tests = (
    ('nope', []),
    ('rebel', [
        ':arc170starfighter:'
        ':asf01bwing:'
        ':attackshuttle:'
        ':auzituckgunship:'
        ':btla4ywing:'
        ':btls8kwing:'
        ':cr90corelliancorvette:'
        ':ewing:'
        ':gr75mediumtransport:'
        ':hwk290lightfreighter:'
        ':modifiedyt1300lightfreighter:'
        ':rz1awing:'
        ':sheathipedeclassshuttle:'
        ':t65xwing:'
        ':tielnfighter:'
        ':ut60duwing:'
        ':vcx100lightfreighter:'
        ':yt2400lightfreighter:'
        ':z95af4headhunter:'
    ]),
    ('first_order', [
        ':gozanticlasscruiser:'
        ':raiderclasscorvette:'
        ':tiebainterceptor:'
        ':tiefofighter:'
        ':tiesebomber:'
        ':tiesffighter:'
        ':tievnsilencer:'
        ':tiewiwhispermodifiedinterceptor:'
        ':upsilonclassshuttle:'
        ':xiclasslightshuttle:'
    ])
)
@pytest.mark.parametrize('emoji, output', print_faction_ships_tests)
def test_print_faction_ships(testbot, emoji, output):
    assert testbot.print_faction_ships(emoji) == output
