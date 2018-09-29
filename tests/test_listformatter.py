import pytest

from r2d7.listformatter import ListFormatter
from r2d7.slackdroid import SlackDroid


get_xws_tests = (
    (
        "https://raithos.github.io/?f=Scum%20and%20Villainy&d=v4!s!138:-1,168:-1:-1:U.-1&sn=Sunny%20B!&obs=",
        {"faction": "scumandvillainy", "name": "Sunny B!", "pilots": [{"id": "sunnybounder", "ship": "m3ainterceptor", "upgrades": {"hardpoint": ["hardpointcannon"]}}], "vendor": {
            "yasb": {"builder": "(Yet Another) X-Wing Miniatures Squad Builder", "builder_url": "https://raithos.github.io", "link": "https://raithos.github.io/?f=Scum%20and%20Villainy&d=v4!s!138:-1,168:-1:-1:U.-1&sn=Sunny%20B!&obs="}}, "version": "0.3.0"},
    ),
    (
        "https://squadbuilder.fantasyflightgames.com/squad-preview/d0966452-ec40-40d4-a3cd-ff384e1dcf70",
        {"faction": "scumandvillainy", "pilots": [{"id": "sunnybounder", "ship": "m3ainterceptor", "upgrades": {
            "cannon": ["heavylasercannon"]}, "points":35}], "name": "Sunny B!", "description": "", "points": 35}
    ),
    (
        "https://devjonny.github.io/xwing2estopgap/scum?id=cc7d945d-66e6-470d-9e58-8c93c7ccd402",
        {"name": "Sunny B!", "faction": "scumandvillainy", "pilots": [{"id": "sunnybounder", "upgrades": {"cannon": [
            "heavylasercannon"]}}], "vendor": {"stopgapp": {"builder": "Stop Gapp builder by DevJonny and dbouckley"}}}
    )
)
@pytest.mark.parametrize('url, expected', get_xws_tests)
def test_get_xws(testbot, url, expected):
    assert testbot.get_xws(url) == expected

print_xws_tests = (
    pytest.param(
        {"faction": "scum", "name": "Sunny B!", "pilots": [{"name": "sunnybounder", "ship": "m3ainterceptor", "upgrades": {"hardpoint": ["hardpointcannon"], "cannon":["heavylasercannon"]}}], "vendor": {"yasb": {
            "builder": "(Yet Another) X-Wing Miniatures Squad Builder", "builder_url": "https://raithos.github.io/xwing", "link": "https://raithos.github.io/xwing/?f=Scum%20and%20Villainy&d=v4!s!138:-1,168:-1:-1:U.10&sn=Sunny%20B!&obs="}}, "version": "0.3.0"},
        [
            ':scum: *<https://raithos.github.io/?f=Scum%20and%20Villainy&d=v4!s!138:-1,168:-1:-1:U.10&sn=Sunny%20B!&obs=|Sunny B!>* *[35]*',
            ':m3ainterceptor::initiative1: _<http://xwing-miniatures-second-edition.wikia.com/wiki/Sunny_Bounder|Sunny Bounder>_: <http://xwing-miniatures-second-edition.wikia.com/wiki/Heavy_Laser_Cannon|Heavy Laser Cannon> *[35]*',
        ],
        marks=pytest.mark.xfail(),  # title links causing problems
    ),
    (
        {"description": "", "faction": "scumandvillainy", "name": "Variable points", "pilots": [
            {"id": "cartelexecutioner", "points": 48, "ship": "m12lkimogilafighter", "upgrades": {"mod": ["shieldupgrade"]}}], "points": 48, "version": "0.3.0"},
        [
            ':scum: *Variable points* *[48]*',
            ':m12lkimogilafighter::initiative3: _<http://xwing-miniatures-second-edition.wikia.com/wiki/Cartel_Executioner|Cartel Executioner>_: <http://xwing-miniatures-second-edition.wikia.com/wiki/Shield_Upgrade|Shield Upgrade> *[48]*',
        ],
    ),
    (
        {"description": "", "faction": "scumandvillainy", "name": "Variable point costs!", "pilots": [{"id": "captainjostero", "points": 48, "ship": "kihraxzfighter", "upgrades": {"mod": ["hullupgrade"]}}, {"id": "serissu", "points": 50, "ship": "m3ainterceptor", "upgrades": {"mod": ["hullupgrade"]}}], "points": 98, "version": "0.3.0"},
        [
            ':scum: *Variable point costs!* *[98]*',
            ':kihraxzfighter::initiative3: _<http://xwing-miniatures-second-edition.wikia.com/wiki/Captain_Jostero|Captain Jostero>_: <http://xwing-miniatures-second-edition.wikia.com/wiki/Hull_Upgrade|Hull Upgrade> *[48]*',
            ':m3ainterceptor::initiative5: _<http://xwing-miniatures-second-edition.wikia.com/wiki/Serissu|Serissu>_: <http://xwing-miniatures-second-edition.wikia.com/wiki/Hull_Upgrade|Hull Upgrade> *[50]*',
        ]
    ),
    (
        {"description": "", "faction": "scumandvillainy", "name": "Lando", "pilots": [{"id": "landocalrissian", "points": 49, "ship": "customizedyt1300lightfreighter"}], "points": 49, "version": "0.3.0"},
        [
            ':scum: *Lando* *[49]*',
            ':customizedyt1300lightfreighter::initiative4: _<http://xwing-miniatures-second-edition.wikia.com/wiki/Lando_Calrissian|Lando Calrissian>_ *[49]*',
        ]
    ),
    (
        {"faction": "rebelalliance", "pilots": [{"id": "norrawexley-btla4ywing", "ship": "ywing"}, {"id": "lukeskywalker", "ship": "xwing", "upgrades": {"amd": ["r2d2"]}}], "vendor": {"yasb": {
            "builder": "(Yet Another) X-Wing Miniatures Squad Builder", "builder_url": "https://raithos.github.io", "link": "https://raithos.github.io/?f=Rebel%20Alliance&d=v4!s!25:-1,-1,-1,-1,-1,-1,-1:-1:-1:;4:-1,-1,3,-1,-1:-1:-1:&sn=Unnamed%20Squadron&obs="}}, "version": "0.3.0"},
        [
            ':rebel: *Nameless Squadron* *[113]*',
            ':btla4ywing::initiative5: _<http://xwing-miniatures-second-edition.wikia.com/wiki/Norra_Wexley|Norra Wexley>_ *[43]*',
            ':t65xwing::initiative5: _<http://xwing-miniatures-second-edition.wikia.com/wiki/Luke_Skywalker|Luke Skywalker>_: <http://xwing-miniatures-second-edition.wikia.com/wiki/R2-D2|R2-D2> *[70]*',
        ]
    )
)
@pytest.mark.parametrize('xws, expected', print_xws_tests)
def test_print_xws(testbot, xws, expected):
    assert testbot.print_xws(xws) == expected


@pytest.mark.xfail()
def test_handle_json(testbot):
    message = '{"faction": "rebel", "pilots": [{"name": "braylenstramm", "ship": "arc170"}], "version": "0.3.0", "name": "No upgrades"}'
    expected = [
        ':rebel: *No upgrades* *[25]*',
        ':arc170::skill3: _<http://xwing-miniatures.wikia.com/wiki/Braylen_Stramm|Braylen Stramm>_ *[25]*',
    ]
    assert testbot.handle_json(message) == expected
