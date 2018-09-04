import pytest

from r2d7.listformatter import ListFormatter
from r2d7.slackdroid import SlackDroid


get_xws_tests = (
    (
        "https://raithos.github.io/?f=Scum%20and%20Villainy&d=v4!s!138:-1,168:-1:-1:U.-1&sn=Sunny%20B!&obs=",
        {"faction": "scum", "name": "Sunny B!", "pilots": [{"name": "sunnybounder", "ship": "m3ainterceptor", "upgrades": {"hardpoint": ["hardpointcannon"]}}], "vendor": {
            "yasb": {"builder": "(Yet Another) X-Wing Miniatures Squad Builder", "builder_url": "https://raithos.github.io/xwing", "link": "https://raithos.github.io/xwing/?f=Scum%20and%20Villainy&d=v4!s!138:-1,168:-1:-1:U.-1&sn=Sunny%20B!&obs="}}, "version": "0.3.0"},
    ),
)
@pytest.mark.parametrize('url, expected', get_xws_tests)
def test_get_xws(testbot, url, expected):
    assert testbot.get_xws(url) == expected

print_xws_tests = (
    (
        {"faction": "scum", "name": "Sunny B!", "pilots": [{"name": "sunnybounder", "ship": "m3ainterceptor", "upgrades": {"hardpoint": ["hardpointcannon"], "cannon":["heavylasercannon"]}}], "vendor": {"yasb": {
            "builder": "(Yet Another) X-Wing Miniatures Squad Builder", "builder_url": "https://raithos.github.io/xwing", "link": "https://raithos.github.io/?f=Scum%20and%20Villainy&d=v4!s!138:-1,168:-1:-1:U.10&sn=Sunny%20B!&obs="}}, "version": "0.3.0"},
        [
            ':scum: *<https://raithos.github.io/?f=Scum%20and%20Villainy&d=v4!s!138:-1,168:-1:-1:U.10&sn=Sunny%20B!&obs=|Sunny B!>* *[35]*',
            ':m3ainterceptor::initiative1: _<http://xwing-miniatures-second-edition.wikia.com/wiki/Sunny_Bounder|Sunny Bounder>_: <http://xwing-miniatures-second-edition.wikia.com/wiki/Heavy_Laser_Cannon|Heavy Laser Cannon> *[35]*',
        ],
    ),
    (
        {"faction":"scum","pilots":[{"name":"cartelmarauder","ship":"kihraxzfighter","upgrades":{"missile":["homingmissiles"],"illicit":["hotshotblaster"],"mod":["engineupgrade","stealthdevice","shieldupgrade"],"title":["vaksai"]}}],"version":"0.3.0","name":"Vaksai!"},
        [
            ':scum: *Vaksai!* *[34]*',
            ':kihraxzfighter::skill2: _<http://xwing-miniatures.wikia.com/wiki/Cartel_Marauder|Cartel Marauder>_: <http://xwing-miniatures.wikia.com/wiki/Homing_Missiles|Homing Missiles>, <http://xwing-miniatures.wikia.com/wiki/"Hot_Shot"_Blaster|"Hot Shot" Blaster>, <http://xwing-miniatures.wikia.com/wiki/Engine_Upgrade|Engine Upgrade>, <http://xwing-miniatures.wikia.com/wiki/Stealth_Device|Stealth Device>, <http://xwing-miniatures.wikia.com/wiki/Shield_Upgrade|Shield Upgrade>, <http://xwing-miniatures.wikia.com/wiki/Vaksai|Vaksai> *[34]*',
        ],
    ),
    (
        {"faction":"imperial","pilots":[{"name":"darthvader","ship":"tieadvanced","upgrades":{"system":["accuracycorrector"],"title":["tiex1"]}}],"version":"0.3.0","name":"TIE/X1"},
        [
            ':imperial: *TIE/X1* *[29]*',
            ':tieadvanced::skill9: _<http://xwing-miniatures.wikia.com/wiki/Darth_Vader|Darth Vader>_: <http://xwing-miniatures.wikia.com/wiki/Accuracy_Corrector|Accuracy Corrector>, <http://xwing-miniatures.wikia.com/wiki/TIE/x1|TIE/x1> *[29]*',
        ],
    ),
    (
        {'faction': 'rebel', 'pilots': [{'name': 'braylenstramm', 'ship': 'arc170'}], 'version': '0.3.0', 'name': 'No upgrades'},
        [
            ':rebel: *No upgrades* *[25]*',
            ':arc170::skill3: _<http://xwing-miniatures.wikia.com/wiki/Braylen_Stramm|Braylen Stramm>_ *[25]*',
        ]
    ),
    # Unrecognised upgrade
    (
        {'faction': 'rebel', 'pilots': [{'name': 'braylenstramm', 'ship': 'arc170', "upgrades":{"crew":["captainpicard"]}}], 'version': '0.3.0', 'name': 'No upgrades'},
        [
            ':rebel: *No upgrades* *[25]*',
            ':arc170::skill3: _<http://xwing-miniatures.wikia.com/wiki/Braylen_Stramm|Braylen Stramm>_: *Unrecognised Upgrade* *[25]*',
        ]
    ),
    (
        {"description":"","faction":"scum","name":"Adapatability","pilots":[{"name":"inaldra","points":15,"ship":"m3ainterceptor","upgrades":{"ept":["adaptability"]}}],"points":15,"version":"0.3.0"},
        [
            ':scum: *Adapatability* *[15]*',
            ':m3ainterceptor::skill3: _<http://xwing-miniatures.wikia.com/wiki/Inaldra|Inaldra>_: <http://xwing-miniatures.wikia.com/wiki/Adaptability|Adaptability>:skill_1: *[15]*',
        ]
    ),
    # Unrecognised pilot
    (
        {'faction': 'rebel', 'pilots': [{'name': 'sulu', 'ship': 'enterprise'}], 'version': '0.3.0', 'name': 'Bad ship'},
        [
            ':rebel: *Bad ship* *[0]*',
            ':question::question: _Unknown Pilot_',
        ]
    ),
    # Renegade refit
    (
        {"faction": "rebel", "name": "Renegade Refit", "pilots": [{"name": "cavernangelszealot", "ship": "xwing", "upgrades": {"ept": ["expertise"], "torpedo":["renegaderefit"]}}], "version": "0.3.0"},
        [
            ':rebel: *Renegade Refit* *[23]*',
            ':xwing::skill1: _<http://xwing-miniatures.wikia.com/wiki/Cavern_Angels_Zealot|Cavern Angels Zealot>_: <http://xwing-miniatures.wikia.com/wiki/Expertise|Expertise>, <http://xwing-miniatures.wikia.com/wiki/Renegade_Refit|Renegade Refit> *[23]*',
        ]
    ),
    (
        {"faction": "rebel", "name": "Renegade Refit 0", "pilots": [{"name": "cavernangelszealot", "ship": "xwing", "upgrades": {"ept": ["trickshot"], "torpedo":["renegaderefit"]}}], "version": "0.3.0"},
        [
            ':rebel: *Renegade Refit 0* *[20]*',
            ':xwing::skill1: _<http://xwing-miniatures.wikia.com/wiki/Cavern_Angels_Zealot|Cavern Angels Zealot>_: <http://xwing-miniatures.wikia.com/wiki/Trick_Shot|Trick Shot>, <http://xwing-miniatures.wikia.com/wiki/Renegade_Refit|Renegade Refit> *[20]*',
        ]
    ),
)

@pytest.mark.parametrize('xws, expected', print_xws_tests)
def test_print_xws(testbot, xws, expected):
    assert testbot.print_xws(xws) == expected


def test_handle_json(testbot):
    message = '{"faction": "rebel", "pilots": [{"name": "braylenstramm", "ship": "arc170"}], "version": "0.3.0", "name": "No upgrades"}'
    expected = [
        ':rebel: *No upgrades* *[25]*',
        ':arc170::skill3: _<http://xwing-miniatures.wikia.com/wiki/Braylen_Stramm|Braylen Stramm>_ *[25]*',
    ]
    assert testbot.handle_json(message) == expected
