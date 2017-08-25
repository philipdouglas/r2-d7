import pytest

from r2d7.listformatter import ListFormatter
from r2d7.slackdroid import SlackDroid


@pytest.fixture(scope="module")
def testbot():
    class TestBot(ListFormatter, SlackDroid):
        pass
    bot = TestBot()
    bot.load_data()
    return bot


get_xws_tests = (
    (
        "http://geordanr.github.io/xwing/?f=Scum%20and%20Villainy&d=v4!s!248::50:-1:&sn=Sunny%20B!&obs=",
        {"faction":"scum","pilots":[{"name":"sunnybounder","ship":"m3ainterceptor","upgrades":{"title":["lightscykinterceptor"]}}],"vendor":{"yasb":{"builder":"(Yet Another) X-Wing Miniatures Squad Builder","builder_url":"https://geordanr.github.io/xwing","link":"https://geordanr.github.io/xwing/?f=Scum%20and%20Villainy&d=v4!s!248::50:-1:&sn=Sunny%20B!&obs="}},"version":"0.3.0","name":"Sunny B!"},
    ),
    (
        "http://xwing-builder.co.uk/view/747933/sunny-b",
        {
            "version": "0.3.0",
            "name": "Sunny B!",
            "faction": "scum",
            "points": 12,
            "pilots": [
                {
                    "name": "sunnybounder",
                    "ship": "m3ainterceptor",
                    "points": 12,
                    "upgrades": {
                        "title": [
                            "lightscykinterceptor"
                        ]
                    }
                }
            ],
            "vendor": {
                "voidstate": {
                    "squadron_id": 747933,
                    "link": "http://xwing-builder.co.uk/view/747933/sunny-b",
                    "builder": "Voidstate's Unofficial X-Wing Squadron Builder",
                    "builder_link": "http://xwing-builder.co.uk/build"
                }
            }
        }
    ),
    (
        'http://x-wing.fabpsb.net/permalink.php?sq=z63f47',
        {"description":"","faction":"scum","pilots":[{"name":"sunnybounder","points":12,"ship":"m3ascykinterceptor","upgrades":{"title":["lightscykinterceptor"]}}],"points":12,"vendor":{"fab":{"builder":"Fabs Squadrons generator","builder_link":"http://x-wing.fabpsb.net/","link":"http://x-wing.fabpsb.net/permalink?sq=z63f47"}},"version":"1.0.0"}
    ),
)

@pytest.mark.parametrize('url, expected', get_xws_tests)
def test_get_xws(testbot, url, expected):
    assert testbot.get_xws(url) == expected

print_xws_tests = (
    (
        {"faction":"scum","pilots":[{"name":"sunnybounder","ship":"m3ainterceptor","upgrades":{"title":["lightscykinterceptor"]}}],"vendor":{"yasb":{"builder":"(Yet Another) X-Wing Miniatures Squad Builder","builder_url":"https://geordanr.github.io/xwing","link":"https://geordanr.github.io/xwing/?f=Scum%20and%20Villainy&d=v4!s!248::50:-1:&sn=Sunny%20B!&obs="}},"version":"0.3.0","name":"Sunny B!"},
        [
            #TODO links
            ':scum: *<https://geordanr.github.io/xwing/?f=Scum%20and%20Villainy&d=v4!s!248::50:-1:&sn=Sunny%20B!&obs=|Sunny B!>* *[12]*',
            ':m3ainterceptor::skill1: _<http://xwing-miniatures.wikia.com/wiki/Sunny_Bounder|Sunny Bounder>_: <http://xwing-miniatures.wikia.com/wiki/"Light_Scyk"_Interceptor|"Light Scyk" Interceptor> *[12]*',
        ],
    ),
    (
        {
            "version": "0.3.0",
            "name": "Sunny B!",
            "faction": "scum",
            "points": 12,
            "pilots": [
                {
                    "name": "sunnybounder",
                    "ship": "m3ainterceptor",
                    "points": 12,
                    "upgrades": {
                        "title": [
                            "lightscykinterceptor"
                        ]
                    }
                }
            ],
            "vendor": {
                "voidstate": {
                    "squadron_id": 747933,
                    "link": "http://xwing-builder.co.uk/view/747933/sunny-b",
                    "builder": "Voidstate's Unofficial X-Wing Squadron Builder",
                    "builder_link": "http://xwing-builder.co.uk/build"
                }
            }
        },
        [
            ':scum: *<http://xwing-builder.co.uk/view/747933/sunny-b|Sunny B!>* *[12]*',
            ':m3ainterceptor::skill1: _<http://xwing-miniatures.wikia.com/wiki/Sunny_Bounder|Sunny Bounder>_: <http://xwing-miniatures.wikia.com/wiki/"Light_Scyk"_Interceptor|"Light Scyk" Interceptor> *[12]*',
        ],
    ),
    (
        {"description":"","faction":"scum","pilots":[{"name":"sunnybounder","points":12,"ship":"m3ascykinterceptor","upgrades":{"title":["lightscykinterceptor"]}}],"points":12,"vendor":{"fab":{"builder":"Fabs Squadrons generator","builder_link":"http://x-wing.fabpsb.net/","link":"http://x-wing.fabpsb.net/permalink?sq=z63f47"}},"version":"1.0.0"},
        [
            ':scum: *<http://x-wing.fabpsb.net/permalink?sq=z63f47|Nameless Squadron>* *[12]*',
            ':m3ainterceptor::skill1: _<http://xwing-miniatures.wikia.com/wiki/Sunny_Bounder|Sunny Bounder>_: <http://xwing-miniatures.wikia.com/wiki/"Light_Scyk"_Interceptor|"Light Scyk" Interceptor> *[12]*',
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
    )
)

@pytest.mark.parametrize('xws, expected', print_xws_tests)
def test_print_xws(testbot, xws, expected):
    assert testbot.print_xws(xws) == expected
