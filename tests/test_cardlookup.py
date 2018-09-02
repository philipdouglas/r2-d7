import pytest

from r2d7.cardlookup import CardLookup
from r2d7.slackdroid import SlackDroid


print_card_tests = (
    ('tacticalofficer', [
        ':crew: *<http://xwing-miniatures-second-edition.wikia.com/wiki/Tactical_Officer|Tactical Officer>* [2]',
        'Restrictions: :redcoordinate:',
        '_In the chaos of a starfighter battle, a single order can mean the difference between a victory and a massacre._',
        ':coordinate:',
    ]),
    ('predator', [
        ':talent: *<http://xwing-miniatures-second-edition.wikia.com/wiki/Predator|Predator>* [2]',
        'While you perform a primary attack, if the defender is in your :bullseyearc:, you may reroll 1 attack die.',
    ]),
    ('homingmissiles', [
        ':missile: *<http://xwing-miniatures-second-edition.wikia.com/wiki/Homing_Missiles|Homing Missiles>* [2]',
        '*Attack (:targetlock:):* Spend 1 :Charge:. After you declare the defender, the defender may choose to suffer 1 :Hit: damage. If it does, skip the Attack and Defense Dice steps and the attack is treated as hitting.',
        ':redfrontarc::attack4::redrangebonusindicator:2-3 | :orangecharge::charge2:',
    ]),
    ('r2astromech', [
        ':astromech: *<http://xwing-miniatures-second-edition.wikia.com/wiki/R2_Astromech|R2 Astromech>* [6]',
        'After you reveal your dial, you may spend 1 :Charge: and gain 1 disarm token to recover 1 shield.',
        ':orangecharge::charge2:',
    ]),
    ('emperorpalpatine', [
        ':crew::crew: • *<http://xwing-miniatures-second-edition.wikia.com/wiki/Emperor_Palpatine|Emperor Palpatine>* [13]',
        'Restrictions: Imperial',
        'While another friendly ship defends or performs an attack, you may spend 1 :Force: to modify 1 of its dice as though that ship had spent 1 :Force:.',
        ':purpleforcepower::forceplus1::purplerecurring:',
    ]),
    ('os1arsenalloadout', [
        ':configuration: *<http://xwing-miniatures-second-edition.wikia.com/wiki/Os-1_Arsenal_Loadout|Os-1 Arsenal Loadout>* [0]',
        'Restrictions: :alphaclassstarwing:',
        'While you have exactly 1 disarm token, you can still perform :Torpedo: and :Missile: attacks against targets you have locked. If you do, you cannot spend your lock during the attack. Add :Torpedo: and :Missile: slots.',
    ]),
    ('starviperclassattackplatform', [
        ':starviperclassattackplatform: *<http://xwing-miniatures-second-edition.wikia.com/wiki/StarViper-class_Attack_Platform|StarViper-class Attack Platform>* :smallbase:',
        ':redfrontarc::attack3::greenagility::agility3::yellowhull::hull4::blueshield::shield1: | :focus: :targetlock: :barrelroll:⯈:redfocus: :boost:⯈:redfocus:',
        '4 :blank::blank::straight::blank::blank::blank::blank:',
        '3 :blank::bankleft::bluestraight::bankright::blank::redsloopleft::redsloopright:',
        '2 :turnleft::bluebankleft::bluestraight::bluebankright::turnright::blank::blank:',
        '1 :turnleft::bluebankleft::bluestraight::bluebankright::turnright::blank::blank:',
        ':scum: :initiative2:<http://xwing-miniatures-second-edition.wikia.com/wiki/Black_Sun_Enforcer|Black Sun Enforcer> [46], :initiative3:<http://xwing-miniatures-second-edition.wikia.com/wiki/Black_Sun_Assassin|Black Sun Assassin> [48], :initiative4:• <http://xwing-miniatures-second-edition.wikia.com/wiki/Dalan_Oberos|Dalan Oberos> [54], :initiative4:• <http://xwing-miniatures-second-edition.wikia.com/wiki/Prince_Xizor|Prince Xizor> [54], :initiative5:• <http://xwing-miniatures-second-edition.wikia.com/wiki/Guri|Guri> [62]',
    ])
)

@pytest.mark.parametrize('name, expected', print_card_tests)
def test_print_card(testbot, name, expected):
    if '.' in name:
        name, num = name.split('.')
    else:
        num = 0
    assert name in testbot._lookup_data
    assert len(testbot._lookup_data[name]) > int(num)
    card = testbot._lookup_data[name][int(num)]
    assert testbot.print_card(card) == expected


lookup_tests = {
    'sunny bounder': [('sunnybounder', 'm3ainterceptor')],
    'Rey': [('rey', 'Crew'), ('rey', 'yt1300')],
    'han solo': [
        ('hansolo', 'Crew'), ('hansolo', 'yt1300'), ('hansolo-swx57', 'yt1300')
    ],
    'xwing': [('xwing', 'xwing'), ('t70xwing', 't70xwing')],
    ':crew: Rey': [('rey', 'Crew')],
    'Rey :crew:': [('rey', 'Crew')],
    ':astromech: r2d2': [('r2d2', 'Astromech')],
    ':elite: >3': [
        ('expose', 'Elite'), ('opportunist', 'Elite'), ('expertise', 'Elite')
    ],
    ':crew: rey]]   [[finn': [('rey', 'Crew'), ('finn', 'Crew')],
    ':crew: rey]]   [[finn]] [[:astromech: r2d2]]': [
        ('rey', 'Crew'), ('finn', 'Crew'), ('r2d2', 'Astromech')],
    'han': [
        ('hansolo', 'Crew'), ('hansolo', 'yt1300'), ('hansolo-swx57', 'yt1300')
    ],
    'test': [
        ('awingtestpilot', 'Title'),
        ('sienartestpilot', 'tieadvprototype'),
        ('testpilotblackout', 'tiesilencer'),
        ('firstordertestpilot', 'tiesilencer'),
    ],
    'fcs': [('firecontrolsystem', 'System')],
    'thweek': [
        ('thweek', 'starviper'),
        ('mimicked', 'condition'), ('shadowed', 'condition')
    ],
    ':astromech: &gt; 3': [('r2d2', 'Astromech')],
    ':focus:': [],
    ':imperial:': [('imperialtrainee', 'tiestriker')],
    'torpedo': [
        ('protontorpedoes', 'Torpedo'),
        ('advprotontorpedoes', 'Torpedo'),
        ('flechettetorpedoes', 'Torpedo'),
        ('iontorpedoes', 'Torpedo'),
        ('plasmatorpedoes', 'Torpedo'),
        ('seismictorpedo', 'Torpedo'),
    ],
    ':crew: = 8': [('emperorpalpatine', 'Crew')],
    'hot shot': [('hotshotblaster', 'Illicit'), ('hotshotcopilot', 'Crew')],
    'kylo': [
        ('kyloren', 'Crew'), ('illshowyouthedarkside', 'condition'),
        ('kyloren', 'upsilonclassshuttle'),
        ('kyloren', 'tiesilencer'),
        ('kylorensshuttle', 'Title'),
    ],
    # Test for unescaped lookup in regex
    '{0}{0}{1}': [],
    'z95': [
        ('z95headhunter', 'z95headhunter')
    ]
}
@pytest.mark.parametrize('lookup, expected', lookup_tests.items())
def test_lookup(testbot, lookup, expected):
    actual = [(card['xws'], card['slot']) for card in testbot.lookup(lookup)]
    assert actual == expected


def test_card_limit(testbot):
    assert testbot.handle_lookup('squadron') == [
        'Your search matched more than 10 cards, please be more specific.']

@pytest.mark.parametrize('dialgen, slack', (
    ([
        "1TW", "1YW", "2TW", "2BB", "2FB", "2NB", "2YW", "3TW", "3BW", "3FB",
        "3NW", "3YW", "3KR", "4FW", "4KR", "5FW"
    ],
    [
        '5 :blank::blank::straight::blank::blank::blank:',
        '4 :blank::blank::straight::blank::blank::redkturn:',
        '3 :turnleft::bankleft::bluestraight::bankright::turnright::redkturn:',
        '2 :turnleft::bluebankleft::bluestraight::bluebankright::turnright::blank:',
        '1 :turnleft::blank::blank::blank::turnright::blank:',
    ]
    ),
    ([
        "1AR", "1DR", "1TW", "1BW", "1FW", "1NW", "1YW", "2SR", "2LR", "2TW",
        "2BB", "2FB", "2NB", "2YW", "2PR", "3BW", "3FB", "3NW"
    ],
    [
        '3 :blank::bankleft::bluestraight::bankright::blank::blank::blank::blank::blank::blank:',
        '2 :turnleft::bluebankleft::bluestraight::bluebankright::turnright::redsloopleft::redsloopright::blank::redreversestraight::blank:',
        '1 :turnleft::bankleft::straight::bankright::turnright::blank::blank::redreversebankleft::blank::redreversebankright:',
    ]
    ),
    ([
        "0OR", "1BB", "1FB", "1NB", "2TR", "2BW", "2FB", "2NW", "2YR", "3BR",
        "3FW", "3NR"
    ],
    [
        '3 :blank::redbankleft::straight::redbankright::blank:',
        '2 :redturnleft::bankleft::bluestraight::bankright::redturnright:',
        '1 :blank::bluebankleft::bluestraight::bluebankright::blank:',
        '0 :blank::blank::redstop::blank::blank:',
    ] )
))
def test_maneuvers(testbot, dialgen, slack):
    assert testbot.maneuvers(dialgen) == slack

@pytest.mark.parametrize('action, expected', [
    ({"difficulty": "White", "type": "Focus"}, ":focus:"),
    ({"difficulty": "White", "type": "Barrel Roll", "linked": {
        "difficulty": "Red", "type": "Focus"}},
     ":barrelroll:⯈:redfocus:")
])
def test_print_action(testbot, action, expected):
    assert testbot.print_action(action) == expected

@pytest.mark.parametrize('stat, expected', [
    ({'type': 'shields', "value": 3}, ":blueshield::shield3:"),
    ({'type': 'attack', 'arc': 'Front Arc', 'value': 4}, ":redfrontarc::attack4:"),
])
def test_print_stat(testbot, stat, expected):
    assert testbot.print_stat(stat) == expected

@pytest.mark.parametrize('res, expected', [
    ([{'action': {"difficulty": "Red", "type": "Focus"}}], "Restrictions: :redfocus:"),
    ([{"chassis": ["t65xwing"]}], "Restrictions: :t65xwing:"),
    ([{'factions': ["Galactic Empire"]}], "Restrictions: Imperial"),
    ([{'factions': ["Rebel Alliance", "Scum and Villainy"]}], "Restrictions: Rebel or Scum"),
    ([{"chassis": ["m3ainterceptor"], 'action': {"difficulty": "White", "type": "Focus"}}], "Restrictions: :focus: and :m3ainterceptor:"),
    ([{"sizes": ["Small"]}], "Restrictions: Small ship"),
    ([{"sizes": ["Small", "Medium"]}], "Restrictions: Small or Medium ship"),
])
def test_print_restrictions(testbot, res, expected):
    assert testbot.print_restrictions(res) == expected

@pytest.mark.parametrize('ability, expected', [
    ({
        "name": "Microthrusters",
        "text": "While you perform a barrel roll, you must use the [Bank Left] or [Bank Right] template instead of the [Straight] template."
    }, ["_*Microthrusters:*_ While you perform a barrel roll, you must use the :bankleft: or :bankright: template instead of the :Straight: template."]),
])
def test_print_ship_ability(testbot, ability, expected):
    assert testbot.print_ship_ability(ability) == expected
