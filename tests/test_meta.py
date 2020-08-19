import pytest
from r2d7.meta import Metawing
import json

list_printer_tests = (
        ('{"position": 5, "id": 2085, "name": "DBS Swarm", "faction": "Separatist Alliance", "ships": [{"id": 55, "name": "Vulture-class Droid Fighter", "xws": "vultureclassdroidfighter", "link": "https://meta.listfortress.com/ships/55.json"}, {"id": 55, "name": "Vulture-class Droid Fighter", "xws": "vultureclassdroidfighter", "link": "https://meta.listfortress.com/ships/55.json"}, {"id": 55, "name": "Vulture-class Droid Fighter", "xws": "vultureclassdroidfighter", "link": "https://meta.listfortress.com/ships/55.json"}, {"id": 55, "name": "Vulture-class Droid Fighter", "xws": "vultureclassdroidfighter", "link": "https://meta.listfortress.com/ships/55.json"}, {"id": 55, "name": "Vulture-class Droid Fighter", "xws": "vultureclassdroidfighter", "link": "https://meta.listfortress.com/ships/55.json"}, {"id": 55, "name": "Vulture-class Droid Fighter", "xws": "vultureclassdroidfighter", "link": "https://meta.listfortress.com/ships/55.json"}, {"id": 55, "name": "Vulture-class Droid Fighter", "xws": "vultureclassdroidfighter", "link": "https://meta.listfortress.com/ships/55.json"}, {"id": 62, "name": "Hyena-class Droid Bomber", "xws": "hyenaclassdroidbomber", "link": "https://meta.listfortress.com/ships/62.json"}], "squadron_count": 1, "tournaments_count": 1, "average_percentile": 81.25, "weight": 0.803933897124467}',
        '''DBS Swarm :vultureclassdroidfighter::vultureclassdroidfighter::vultureclassdroidfighter::vultureclassdroidfighter::vultureclassdroidfighter::vultureclassdroidfighter::vultureclassdroidfighter::hyenaclassdroidbomber:
Average: 81%, Weighted: 80%'''),
        ('{"position": 1, "id": 2336, "name": null, "faction": "Resistance", "link": "https://meta.listfortress.com/ship_combos/2336.json", "ships": [{"id": 50, "name": "T-70 X-wing", "xws": "t70xwing", "link": "https://meta.listfortress.com/ships/50.json"}, {"id": 50, "name": "T-70 X-wing", "xws": "t70xwing", "link": "https://meta.listfortress.com/ships/50.json"}, {"id": 50, "name": "T-70 X-wing", "xws": "t70xwing", "link": "https://meta.listfortress.com/ships/50.json"}, {"id": 49, "name": "RZ-2 A-wing", "xws": "rz2awing", "link": "https://meta.listfortress.com/ships/49.json"}, {"id": 61, "name": "Resistance Transport Pod", "xws": "resistancetransportpod", "link": "https://meta.listfortress.com/ships/61.json"}], "squadron_count": 2, "tournaments_count": 2, "average_percentile": 98.68, "weight": 1.16857595629635}',
        '''<https://meta.listfortress.com/ship_combos/2336|(unnamed)> :t70xwing::t70xwing::t70xwing::rz2awing::resistancetransportpod:
Average: 99%, Weighted: 117%'''),
        ('{"position": 2, "id": 191, "name": "Double Firespray", "faction": "Scum and Villainy", "link": "https://meta.listfortress.com/ship_combos/191.json", "ships": [{"id": 22, "name": "Firespray-class Patrol Craft", "xws": "firesprayclasspatrolcraft", "link": "https://meta.listfortress.com/ships/22.json"}, {"id": 22, "name": "Firespray-class Patrol Craft", "xws": "firesprayclasspatrolcraft", "link": "https://meta.listfortress.com/ships/22.json"}], "squadron_count": 13, "tournaments_count": 8, "average_percentile": 38.81, "weight": 1.01919215760887}',
        '''<https://meta.listfortress.com/ship_combos/191|Double Firespray> :firesprayclasspatrolcraft::firesprayclasspatrolcraft:
Average: 39%, Weighted: 102%'''),
        ('{"position": 3, "id": 2801, "name": "The Baron and the Bros", "faction": "First Order", "link": "https://meta.listfortress.com/ship_combos/2801.json", "ships": [{"id": 51, "name": "TIE/fo Fighter", "xws": "tiefofighter", "link": "https://meta.listfortress.com/ships/51.json"}, {"id": 67, "name": "TIE/ba Interceptor", "xws": "tiebainterceptor", "link": "https://meta.listfortress.com/ships/67.json"}, {"id": 52, "name": "TIE/sf Fighter", "xws": "tiesffighter", "link": "https://meta.listfortress.com/ships/52.json"}, {"id": 52, "name": "TIE/sf Fighter", "xws": "tiesffighter", "link": "https://meta.listfortress.com/ships/52.json"}, {"id": 52, "name": "TIE/sf Fighter", "xws": "tiesffighter", "link": "https://meta.listfortress.com/ships/52.json"}], "squadron_count": 1, "tournaments_count": 1, "average_percentile": 95.45, "weight": 0.944481781237137}',
        '''<https://meta.listfortress.com/ship_combos/2801|The Baron and the Bros> :tiefofighter::tiebainterceptor::tiesffighter::tiesffighter::tiesffighter:
Average: 95%, Weighted: 94%'''),
        ('{"position": 4, "id": 2324, "name": null, "faction": "First Order", "link": "https://meta.listfortress.com/ship_combos/2324.json", "ships": [{"id": 51, "name": "TIE/fo Fighter", "xws": "tiefofighter", "link": "https://meta.listfortress.com/ships/51.json"}, {"id": 52, "name": "TIE/sf Fighter", "xws": "tiesffighter", "link": "https://meta.listfortress.com/ships/52.json"}, {"id": 52, "name": "TIE/sf Fighter", "xws": "tiesffighter", "link": "https://meta.listfortress.com/ships/52.json"}, {"id": 52, "name": "TIE/sf Fighter", "xws": "tiesffighter", "link": "https://meta.listfortress.com/ships/52.json"}, {"id": 53, "name": "TIE/vn Silencer", "xws": "tievnsilencer", "link": "https://meta.listfortress.com/ships/53.json"}], "squadron_count": 1, "tournaments_count": 1, "average_percentile": 91.47, "weight": 0.905128373685589}',
        '''<https://meta.listfortress.com/ship_combos/2324|(unnamed)> :tiefofighter::tiesffighter::tiesffighter::tiesffighter::tievnsilencer:
Average: 91%, Weighted: 91%'''),
)
@pytest.mark.parametrize('message, expected', list_printer_tests)
def test_list_printer(testbot, message, expected):
    j = json.loads(message)
    assert testbot.list_printer(j) == expected

ship_printer_tests = (
        ('{"position": 1, "id": 21, "xws": "fangfighter", "name": "Fang Fighter", "link": "https://meta.listfortress.com/ships/21.json", "pilots": [{"id": 99, "name": "Old Teroch", "link": "https://meta.listfortress.com/pilots/99.json", "image": "https://meta.listfortress.com/pilots/99/image.png"}, {"id": 96, "name": "Fenn Rau", "link": "https://meta.listfortress.com/pilots/96.json", "image": "https://meta.listfortress.com/pilots/96/image.png"}, {"id": 97, "name": "Joy Rekkoff", "link": "https://meta.listfortress.com/pilots/97.json", "image": "https://meta.listfortress.com/pilots/97/image.png"}, {"id": 98, "name": "Kad Solus", "link": "https://meta.listfortress.com/pilots/98.json", "image": "https://meta.listfortress.com/pilots/98/image.png"}, {"id": 100, "name": "Skull Squadron Pilot", "link": "https://meta.listfortress.com/pilots/100.json", "image": "https://meta.listfortress.com/pilots/100/image.png"}, {"id": 101, "name": "Zealous Recruit", "link": "https://meta.listfortress.com/pilots/101.json", "image": "https://meta.listfortress.com/pilots/101/image.png"}], "squadron_count": 18, "tournaments_count": 7, "average_percentile": 34.75, "weight": 1.24538930744309, "faction": "Scum and Villainy"}',
        '''<https://meta.listfortress.com/ships/21|Fang Fighter>:fangfighter:
Average: 35%, Weighted: 125%'''),
        ('{"position": 2, "id": 28, "xws": "m3ainterceptor", "name": "M3-A Interceptor", "link": "https://meta.listfortress.com/ships/28.json", "pilots": [{"id": 132, "name": "Cartel Spacer", "link": "https://meta.listfortress.com/pilots/132.json", "image": "https://meta.listfortress.com/pilots/132/image.png"}, {"id": 134, "name": "Inaldra", "link": "https://meta.listfortress.com/pilots/134.json", "image": "https://meta.listfortress.com/pilots/134/image.png"}, {"id": 135, "name": "Laetin A\'shera", "link": "https://meta.listfortress.com/pilots/135.json", "image": "https://meta.listfortress.com/pilots/135/image.png"}, {"id": 136, "name": "Quinn Jast", "link": "https://meta.listfortress.com/pilots/136.json", "image": "https://meta.listfortress.com/pilots/136/image.png"}, {"id": 137, "name": "Serissu", "link": "https://meta.listfortress.com/pilots/137.json", "image": "https://meta.listfortress.com/pilots/137/image.png"}, {"id": 138, "name": "Sunny Bounder", "link": "https://meta.listfortress.com/pilots/138.json", "image": "https://meta.listfortress.com/pilots/138/image.png"}, {"id": 139, "name": "Tansarii Point Veteran", "link": "https://meta.listfortress.com/pilots/139.json", "image": "https://meta.listfortress.com/pilots/139/image.png"}, {"id": 133, "name": "Genesis Red", "link": "https://meta.listfortress.com/pilots/133.json", "image": "https://meta.listfortress.com/pilots/133/image.png"}, {"id": 369, "name": "G4R-G0R V/M", "link": "https://meta.listfortress.com/pilots/369.json", "image": "https://meta.listfortress.com/pilots/369/image.png"}], "squadron_count": 17, "tournaments_count": 8, "average_percentile": 36.67, "weight": 1.23087941090141, "faction": "Scum and Villainy"}',
        '''<https://meta.listfortress.com/ships/28|M3-A Interceptor>:m3ainterceptor:
Average: 37%, Weighted: 123%'''),
        ('{"position": 4, "id": 61, "xws": "resistancetransportpod", "name": "Resistance Transport Pod", "link": "https://meta.listfortress.com/ships/61.json", "pilots": [{"id": 341, "name": "BB-8", "link": "https://meta.listfortress.com/pilots/341.json", "image": "https://meta.listfortress.com/pilots/341/image.png"}, {"id": 342, "name": "Rose Tico", "link": "https://meta.listfortress.com/pilots/342.json", "image": "https://meta.listfortress.com/pilots/342/image.png"}, {"id": 343, "name": "Vi Moradi", "link": "https://meta.listfortress.com/pilots/343.json", "image": "https://meta.listfortress.com/pilots/343/image.png"}, {"id": 344, "name": "Finn", "link": "https://meta.listfortress.com/pilots/344.json", "image": "https://meta.listfortress.com/pilots/344/image.png"}], "squadron_count": 8, "tournaments_count": 7, "average_percentile": 48.6, "weight": 0, "faction": "Resistance"}',
        '''<https://meta.listfortress.com/ships/61|Resistance Transport Pod>:resistancetransportpod:
Average: 49%, Weighted: 0%'''),
)
@pytest.mark.parametrize('message, expected', ship_printer_tests)
def test_ship_printer(testbot, message, expected):
    j = json.loads(message)
    assert testbot.ship_printer(j) == expected

pilot_printer_tests = (
        ('{"position": 1, "id": 271, "xws": "tn3465", "name": "TN-3465", "link": "https://meta.listfortress.com/pilots/271.json", "image": "https://meta.listfortress.com/pilots/271/image.png", "ship": {"id": 51, "name": "TIE/fo Fighter", "link": "https://meta.listfortress.com/ships/51.json"}, "squadron_count": 2, "tournaments_count": 1, "average_percentile": 93.46, "weight": 1.46578136825278, "faction": "First Order"}',
        '''<https://meta.listfortress.com/pilots/271|TN-3465> :tiefofighter:
Average: 93%, Weighted: 147%'''),
        ('{"position": 3, "id": 102, "xws": "bobafett", "name": "Boba Fett", "link": "https://meta.listfortress.com/pilots/102.json", "image": "https://meta.listfortress.com/pilots/102/image.png", "ship": {"id": 22, "name": "Firespray-class Patrol Craft", "link": "https://meta.listfortress.com/ships/22.json"}, "squadron_count": 21, "tournaments_count": 9, "average_percentile": 36.35, "weight": 1.16356864601878, "faction": "Scum and Villainy"}',
        '''<https://meta.listfortress.com/pilots/102|Boba Fett> :firesprayclasspatrolcraft:
Average: 36%, Weighted: 116%'''),
        ('{"position": 5, "id": 321, "xws": "plokoon", "name": "Plo Koon", "link": "https://meta.listfortress.com/pilots/321.json", "image": "https://meta.listfortress.com/pilots/321/image.png", "ship": {"id": 58, "name": "Delta-7 Aethersprite", "link": "https://meta.listfortress.com/ships/58.json"}, "squadron_count": 6, "tournaments_count": 4, "average_percentile": 48.14, "weight": 1.12182792544073, "faction": "Galactic Republic"}',
        '''<https://meta.listfortress.com/pilots/321|Plo Koon> :delta7aethersprite:
Average: 48%, Weighted: 112%'''),
)
@pytest.mark.parametrize('message, expected', pilot_printer_tests)
def test_pilot_printer(testbot, message, expected):
    j = json.loads(message)
    assert testbot.pilot_printer(j) == expected

upgrade_printer_tests = (
        ('{"position": 1, "id": 160, "xws": "heroic", "name": "Heroic", "link": "https://meta.listfortress.com/upgrades/160.json", "image": "https://meta.listfortress.com/upgrades/160/image.png", "squadron_count": 18, "tournaments_count": 11, "average_percentile": 43.71, "weight": 1.37863771336788}',
        '''<https://meta.listfortress.com/upgrades/160|Heroic>
Average: 44%, Weighted: 138%'''),
        ('{"position": 4, "id": 92, "xws": "protonbombs", "name": "Proton Bombs", "link": "https://meta.listfortress.com/upgrades/92.json", "image": "https://meta.listfortress.com/upgrades/92/image.png", "squadron_count": 28, "tournaments_count": 12, "average_percentile": 34.47, "weight": 1.22427215793812}',
        '''<https://meta.listfortress.com/upgrades/92|Proton Bombs>
Average: 34%, Weighted: 122%'''),
        ('{"position": 5, "id": 227, "xws": "autoblasters", "name": "Autoblasters", "link": "https://meta.listfortress.com/upgrades/227.json", "image": "https://meta.listfortress.com/upgrades/227/image.png", "squadron_count": 27, "tournaments_count": 12, "average_percentile": 6, "weight": 0.055}',
        '''<https://meta.listfortress.com/upgrades/227|Autoblasters>
Average: 6%, Weighted: 6%'''),
)
@pytest.mark.parametrize('message, expected', upgrade_printer_tests)
def test_upgrade_printer(testbot, message, expected):
    j = json.loads(message)
    assert testbot.upgrade_printer(j) == expected
