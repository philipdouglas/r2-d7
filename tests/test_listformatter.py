import pytest

from r2d7.listformatter import ListFormatter
from r2d7.slackdroid import SlackDroid


#TODO Fix LBN, it isn't working correctly
get_xws_tests = (
    (
        "https://launchbaynext.app/?lbx=%27New%20Squadron%27.31.3.0.l44.188.l3.256rr&mode=full",
        {"name": "New Squadron", "description": "", "faction": "scumandvillainy", "pilots": [{"ship": "m3ainterceptor", "upgrades": {"cannon": ["heavylasercannon"]}, "id":"sunnybounder", "points": 31}], "version": "2.0.0", "points": 31, "vendor": {
            "lbn": {"builder": "Launch Bay Next", "builder_url": "https://launchbaynext.app", "link": "https://launchbaynext.app/print?lbx='New%20Squadron'.31.3.0.l44.188.l3.256rr"}}},
    ),
    (
        "https://yasb.app/?f=Scum%20and%20Villainy&d=v8ZsZ200Z138XW10&sn=Sunny%20B!&obs=",
        {"faction": "scumandvillainy", "name": "Sunny B!", "points": 4, "pilots": [{"id": "sunnybounder", "ship": "m3ainterceptor", "points": 4, "upgrades": {"cannon": ["heavylasercannon"]}}], "vendor": {}, "version": "2.5.0"},
    )
)

@pytest.mark.parametrize('url, expected', get_xws_tests)
def test_get_xws(testbot, url, expected):
    assert testbot.get_xws(url) == expected

print_xws_tests = (
    pytest.param(
        {"faction": "scum", "name": "Sunny B!", "pilots": [{"name": "sunnybounder", "ship": "m3ainterceptor", "upgrades": {"hardpoint": ["hardpointcannon"], "cannon":["heavylasercannon"]}}], "vendor": {"yasb": {
            "builder": "(Yet Another) X-Wing Miniatures Squad Builder", "builder_url": "https://yasb.app/xwing", "link": "https://yasb.app/xwing/?f=Scum%20and%20Villainy&d=v4!s!138:-1,168:-1:-1:U.10&sn=Sunny%20B!&obs="}}, "version": "0.3.0"},
        [
            ':scum: *<https://yasb.app/xwing/?f=Scum%20and%20Villainy&d=v4!s!138:-1,168:-1:-1:U.10&sn=Sunny%20B!&obs=|Sunny B!>* *[4]* *[Standard]*',
            ':m3ainterceptor::initiative1: _<https://xwingtmgwiki.com/Sunny_Bounder|Sunny Bounder>_: <https://xwingtmgwiki.com/Heavy_Laser_Cannon|Heavy Laser Cannon> *[4]*[4/10]',
        ],
    ),
    (
        {"description": "", "faction": "scumandvillainy", "name": "Variable point costs!", "pilots": [{"id": "captainjostero", "points": 4, "ship": "kihraxzfighter", "upgrades": {"mod": ["hullupgrade"]}}, {"id": "serissu", "points": 5, "ship": "m3ainterceptor", "upgrades": {"mod": ["hullupgrade"]}}], "points": 9, "version": "0.3.0"},
        [
            ':scum: *Variable point costs!* *[9]* *[Extended]*',
            ':kihraxzfighter::initiative3: _<https://xwingtmgwiki.com/Captain_Jostero|Captain Jostero>_: <https://xwingtmgwiki.com/Hull_Upgrade|Hull Upgrade> *[4]*[4/12]',
            ':m3ainterceptor::initiative5: _<https://xwingtmgwiki.com/Serissu|Serissu>_: <https://xwingtmgwiki.com/Hull_Upgrade|Hull Upgrade> *[5]*[4/18]',
        ]
    ),
    (
        {"description": "", "faction": "scumandvillainy", "name": "Lando", "pilots": [{"id": "landocalrissian", "points": 6, "ship": "customizedyt1300lightfreighter"}], "points": 6, "version": "0.3.0"},
        [
            ':scum: *Lando* *[6]* *[Standard]*',
            ':customizedyt1300lightfreighter::initiative4: _<https://xwingtmgwiki.com/Lando_Calrissian|Lando Calrissian>_ *[6]*[0/17]',
        ]
    ),
    (
        {"faction": "rebelalliance", "pilots": [{"id": "norrawexley-btla4ywing", "ship": "ywing"}, {"id": "lukeskywalker", "ship": "xwing", "upgrades": {"amd": ["r2d2"]}}], "vendor": {"yasb": {
            "builder": "(Yet Another) X-Wing Miniatures Squad Builder", "builder_url": "https://yasb.app", "link": "https://yasb.app/?f=Rebel%20Alliance&d=v4!s!25:-1,-1,-1,-1,-1,-1,-1:-1:-1:;4:-1,-1,3,-1,-1:-1:-1:&sn=Unnamed%20Squadron&obs="}}, "version": "0.3.0"},
        [
            ':rebel: *<https://yasb.app/?f=Rebel%20Alliance&d=v4!s!25:-1,-1,-1,-1,-1,-1,-1:-1:-1:;4:-1,-1,3,-1,-1:-1:-1:&sn=Unnamed%20Squadron&obs=|Nameless Squadron>* *[12]* *[Standard]*',
            ':btla4ywing::initiative5: _<https://xwingtmgwiki.com/Norra_Wexley|Norra Wexley>_ *[5]*[0/18]',
            ':t65xwing::initiative5: _<https://xwingtmgwiki.com/Luke_Skywalker|Luke Skywalker>_: <https://xwingtmgwiki.com/R2-D2|R2-D2> *[7]*[8/28]',
        ]
    )
)
@pytest.mark.parametrize('xws, expected', print_xws_tests)
def test_print_xws(testbot, xws, expected):
    assert testbot.print_xws(xws) == [expected]


print_xws_legality_tests = (
    pytest.param(
        {"description": "", "faction": "scumandvillainy", "name": "Lando", "pilots": [{"id": "landocalrissian", "points": 6, "ship": "customizedyt1300lightfreighter"}], "points": 6, "version": "0.3.0"},
        [
            ':scum: *Lando* *[6]* *[Standard]*',
            ':customizedyt1300lightfreighter::initiative4: _<https://xwingtmgwiki.com/Lando_Calrissian|Lando Calrissian>_ *[6]*[0/17]',
        ]
    ),
    (
        {"faction": "rebelalliance", "pilots": [{"id": "norrawexley-btla4ywing", "ship": "ywing"}, {"id": "lukeskywalker", "ship": "xwing", "upgrades": {"amd": ["r2d2"]}}], "vendor": {"yasb": {
            "builder": "(Yet Another) X-Wing Miniatures Squad Builder", "builder_url": "https://yasb.app", "link": "https://yasb.app/?f=Rebel%20Alliance&d=v4!s!25:-1,-1,-1,-1,-1,-1,-1:-1:-1:;4:-1,-1,3,-1,-1:-1:-1:&sn=Unnamed%20Squadron&obs="}}, "version": "0.3.0"},
        [
            ':rebel: *<https://yasb.app/?f=Rebel%20Alliance&d=v4!s!25:-1,-1,-1,-1,-1,-1,-1:-1:-1:;4:-1,-1,3,-1,-1:-1:-1:&sn=Unnamed%20Squadron&obs=|Nameless Squadron>* *[12]* *[Standard]*',
            ':btla4ywing::initiative5: _<https://xwingtmgwiki.com/Norra_Wexley|Norra Wexley>_ *[5]*[0/18]',
            ':t65xwing::initiative5: _<https://xwingtmgwiki.com/Luke_Skywalker|Luke Skywalker>_: <https://xwingtmgwiki.com/R2-D2|R2-D2> *[7]*[8/28]',
        ]
    )
)
@pytest.mark.parametrize('xws, expected', print_xws_legality_tests)
def test_print_xws_legality(testbot, xws, expected):
    assert testbot.print_xws(xws) == [expected]
