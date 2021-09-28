import pytest

from r2d7.listformatter import ListFormatter
from r2d7.slackdroid import SlackDroid


get_xws_tests = (
    (
        "https://raithos.github.io/?f=Scum%20and%20Villainy&d=v8ZsZ200Z138XW10&sn=Sunny%20B!&obs=",
        {"faction": "scumandvillainy", "name": "Sunny B!", "points": 32, "pilots": [{"id": "sunnybounder", "ship": "m3ainterceptor", "points": 32, "upgrades": {"cannon": ["heavylasercannon"]}}], "vendor": {}, "version": "2.0.0"},
    ),
    (
        "https://squadbuilder.fantasyflightgames.com/squad-preview/d0966452-ec40-40d4-a3cd-ff384e1dcf70",
        {"faction": "scumandvillainy", "pilots": [{"id": "sunnybounder", "ship": "m3ainterceptor", "upgrades": {
            "cannon": ["heavylasercannon"]}, "points":32}], "name": "Sunny B!", "description": "", "points": 32, 'vendor': {}}
    ),
    (
        "https://launchbaynext.app/?lbx=%27New%20Squadron%27.32.3.0.l44.188.l3.256rr&mode=full",
        {"name": "New Squadron", "description": "", "faction": "scumandvillainy", "pilots": [{"ship": "m3ainterceptor", "upgrades": {"cannon": ["heavylasercannon"]}, "id":"sunnybounder", "points": 32}], "version": "2.0.0", "points": 32, "vendor": {
            "lbn": {"builder": "Launch Bay Next", "builder_url": "https://launchbaynext.app", "link": "https://launchbaynext.app/print?lbx='New%20Squadron'.32.3.0.l44.188.l3.256rr"}}},
    ),
    (
        "https://launch-bay-next.herokuapp.com/print?lbx=%27New%20Squadron%27.32.3.0.(44.188.(3.256))&mode=full",
        {"name": "New Squadron", "description": "", "faction": "scumandvillainy", "pilots": [{"ship": "m3ainterceptor", "upgrades": {"cannon": ["heavylasercannon"]}, "id":"sunnybounder", "points": 32}], "version": "2.0.0", "points": 32, "vendor": {
            "lbn": {"builder": "Launch Bay Next", "builder_url": "https://launch-bay-next.herokuapp.com", "link": "https://launch-bay-next.herokuapp.com/print?lbx='New%20Squadron'.32.3.0.(44.188.(3.256))"}}},
    ), # legacy LBN app. If this test fails, delete it and the legacy LBN parser from listformatter.py
)
@pytest.mark.parametrize('url, expected', get_xws_tests)
def test_get_xws(testbot, url, expected):
    assert testbot.get_xws(url) == expected

print_xws_tests = (
    pytest.param(
        {"faction": "scum", "name": "Sunny B!", "pilots": [{"name": "sunnybounder", "ship": "m3ainterceptor", "upgrades": {"hardpoint": ["hardpointcannon"], "cannon":["heavylasercannon"]}}], "vendor": {"yasb": {
            "builder": "(Yet Another) X-Wing Miniatures Squad Builder", "builder_url": "https://raithos.github.io/xwing", "link": "https://raithos.github.io/xwing/?f=Scum%20and%20Villainy&d=v4!s!138:-1,168:-1:-1:U.10&sn=Sunny%20B!&obs="}}, "version": "0.3.0"},
        [
            ':scum: *<https://raithos.github.io/xwing/?f=Scum%20and%20Villainy&d=v4!s!138:-1,168:-1:-1:U.10&sn=Sunny%20B!&obs=|Sunny B!>* *[32]*',
            ':m3ainterceptor::initiative1: _<https://xwingtmgwiki.com/Sunny_Bounder|Sunny Bounder>_: <https://xwingtmgwiki.com/Heavy_Laser_Cannon|Heavy Laser Cannon> *[32]*',
        ],
    ),
    (
        {"description": "", "faction": "scumandvillainy", "name": "Variable points", "pilots": [
            {"id": "cartelexecutioner", "points": 48, "ship": "m12lkimogilafighter", "upgrades": {"mod": ["shieldupgrade"]}}], "points": 45, "version": "0.3.0"},
        [
            ':scum: *Variable points* *[45]*',
            ':m12lkimogilafighter::initiative3: _<https://xwingtmgwiki.com/Cartel_Executioner|Cartel Executioner>_: <https://xwingtmgwiki.com/Shield_Upgrade|Shield Upgrade> *[45]*',
        ],
    ),
    (
        {"description": "", "faction": "scumandvillainy", "name": "Variable point costs!", "pilots": [{"id": "captainjostero", "points": 46, "ship": "kihraxzfighter", "upgrades": {"mod": ["hullupgrade"]}}, {"id": "serissu", "points": 47, "ship": "m3ainterceptor", "upgrades": {"mod": ["hullupgrade"]}}], "points": 98, "version": "0.3.0"},
        [
            ':scum: *Variable point costs!* *[93]*',
            ':kihraxzfighter::initiative3: _<https://xwingtmgwiki.com/Captain_Jostero|Captain Jostero>_: <https://xwingtmgwiki.com/Hull_Upgrade|Hull Upgrade> *[46]*',
            ':m3ainterceptor::initiative5: _<https://xwingtmgwiki.com/Serissu|Serissu>_: <https://xwingtmgwiki.com/Hull_Upgrade|Hull Upgrade> *[47]*',
        ]
    ),
    (
        {"description": "", "faction": "scumandvillainy", "name": "Lando", "pilots": [{"id": "landocalrissian", "points": 42, "ship": "customizedyt1300lightfreighter"}], "points": 42, "version": "0.3.0"},
        [
            ':scum: *Lando* *[42]*',
            ':customizedyt1300lightfreighter::initiative4: _<https://xwingtmgwiki.com/Lando_Calrissian|Lando Calrissian>_ *[42]*',
        ]
    ),
    (
        {"faction": "rebelalliance", "pilots": [{"id": "norrawexley-btla4ywing", "ship": "ywing"}, {"id": "lukeskywalker", "ship": "xwing", "upgrades": {"amd": ["r2d2"]}}], "vendor": {"yasb": {
            "builder": "(Yet Another) X-Wing Miniatures Squad Builder", "builder_url": "https://raithos.github.io", "link": "https://raithos.github.io/?f=Rebel%20Alliance&d=v4!s!25:-1,-1,-1,-1,-1,-1,-1:-1:-1:;4:-1,-1,3,-1,-1:-1:-1:&sn=Unnamed%20Squadron&obs="}}, "version": "0.3.0"},
        [
            ':rebel: *<https://raithos.github.io/?f=Rebel%20Alliance&d=v4!s!25:-1,-1,-1,-1,-1,-1,-1:-1:-1:;4:-1,-1,3,-1,-1:-1:-1:&sn=Unnamed%20Squadron&obs=|Nameless Squadron>* *[110]*',
            ':btla4ywing::initiative5: _<https://xwingtmgwiki.com/Norra_Wexley|Norra Wexley>_ *[41]*',
            ':t65xwing::initiative5: _<https://xwingtmgwiki.com/Luke_Skywalker|Luke Skywalker>_: <https://xwingtmgwiki.com/R2-D2|R2-D2> *[69]*',
        ]
    )
)
@pytest.mark.parametrize('xws, expected', print_xws_tests)
def test_print_xws(testbot, xws, expected):
    assert testbot.print_xws(xws) == [expected]


print_xws_hyperspace_tests = (
    pytest.param(
        {"description": "", "faction": "scumandvillainy", "name": "Lando", "pilots": [{"id": "landocalrissian", "points": 42, "ship": "customizedyt1300lightfreighter"}], "points": 42, "version": "0.3.0"},
        [
            ':scum: *Lando* *[42]* *[Hyperspace]*',
            ':customizedyt1300lightfreighter::initiative4: _<https://xwingtmgwiki.com/Lando_Calrissian|Lando Calrissian>_ *[42]*',
        ]
    ),
    (
        {"faction": "rebelalliance", "pilots": [{"id": "norrawexley-btla4ywing", "ship": "ywing"}, {"id": "lukeskywalker", "ship": "xwing", "upgrades": {"amd": ["r2d2"]}}], "vendor": {"yasb": {
            "builder": "(Yet Another) X-Wing Miniatures Squad Builder", "builder_url": "https://raithos.github.io", "link": "https://raithos.github.io/?f=Rebel%20Alliance&d=v4!s!25:-1,-1,-1,-1,-1,-1,-1:-1:-1:;4:-1,-1,3,-1,-1:-1:-1:&sn=Unnamed%20Squadron&obs="}}, "version": "0.3.0"},
        [
            ':rebel: *<https://raithos.github.io/?f=Rebel%20Alliance&d=v4!s!25:-1,-1,-1,-1,-1,-1,-1:-1:-1:;4:-1,-1,3,-1,-1:-1:-1:&sn=Unnamed%20Squadron&obs=|Nameless Squadron>* *[110]* *[Hyperspace]*',
            ':btla4ywing::initiative5: _<https://xwingtmgwiki.com/Norra_Wexley|Norra Wexley>_ *[41]*',
            ':t65xwing::initiative5: _<https://xwingtmgwiki.com/Luke_Skywalker|Luke Skywalker>_: <https://xwingtmgwiki.com/R2-D2|R2-D2> *[69]*',
        ]
    )
)
@pytest.mark.parametrize('xws, expected', print_xws_hyperspace_tests)
def test_print_xws_hyperspace(testbot, xws, expected):
    assert testbot.print_xws(xws, hyperspace=True) == [expected]
