import pytest
from r2d7.meta import Metawing
import json

list_printer_tests = (
        ('{"position": 5, "id": 2085, "name": "DBS Swarm", "faction": "Separatist Alliance", "ships": [{"id": 55, "name": "Vulture-class Droid Fighter", "xws": "vultureclassdroidfighter", "link": "https://meta.listfortress.com/ships/55.json"}, {"id": 55, "name": "Vulture-class Droid Fighter", "xws": "vultureclassdroidfighter", "link": "https://meta.listfortress.com/ships/55.json"}, {"id": 55, "name": "Vulture-class Droid Fighter", "xws": "vultureclassdroidfighter", "link": "https://meta.listfortress.com/ships/55.json"}, {"id": 55, "name": "Vulture-class Droid Fighter", "xws": "vultureclassdroidfighter", "link": "https://meta.listfortress.com/ships/55.json"}, {"id": 55, "name": "Vulture-class Droid Fighter", "xws": "vultureclassdroidfighter", "link": "https://meta.listfortress.com/ships/55.json"}, {"id": 55, "name": "Vulture-class Droid Fighter", "xws": "vultureclassdroidfighter", "link": "https://meta.listfortress.com/ships/55.json"}, {"id": 55, "name": "Vulture-class Droid Fighter", "xws": "vultureclassdroidfighter", "link": "https://meta.listfortress.com/ships/55.json"}, {"id": 62, "name": "Hyena-class Droid Bomber", "xws": "hyenaclassdroidbomber", "link": "https://meta.listfortress.com/ships/62.json"}], "squadron_count": 1, "tournaments_count": 1, "average_percentile": 81.25, "weight": 0.803933897124467}',
        '''DBS Swarm :vultureclassdroidfighter::vultureclassdroidfighter::vultureclassdroidfighter::vultureclassdroidfighter::vultureclassdroidfighter::vultureclassdroidfighter::vultureclassdroidfighter::hyenaclassdroidbomber:
Average: 81.25%, Weighted: 80.39%'''),
)
@pytest.mark.parametrize('message, expected', list_printer_tests)
def test_list_printer(testbot, message, expected):
    j = json.loads(message)
    assert testbot.list_printer(j) == expected

ship_printer_tests = ()
@pytest.mark.parametrize('message, expected', ship_printer_tests)
def test_ship_printer(testbot, message, expected):
    j = json.loads(message)
    assert testbot.ship_printer(j) == expected

pilot_printer_tests = ()
@pytest.mark.parametrize('message, expected', pilot_printer_tests)
def test_pilot_printer(testbot, message, expected):
    j = json.loads(message)
    assert testbot.pilot_printer(j) == expected

upgrade_printer_tests = ()
@pytest.mark.parametrize('message, expected', upgrade_printer_tests)
def test_upgrade_printer(testbot, message, expected):
    j = json.loads(message)
    assert testbot.upgrade_printer(j) == expected
