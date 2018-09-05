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
        ':missile: *<http://xwing-miniatures-second-edition.wikia.com/wiki/Homing_Missiles|Homing Missiles>* [3]',
        'Attack (:targetlock:): Spend 1 :Charge:. After you declare the defender, the defender may choose to suffer 1 :Hit: damage. If it does, skip the Attack and Defense Dice steps and the attack is treated as hitting.',
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
        'While another friendly ship defends or performs an attack, you may spend 1 :forcecharge: to modify 1 of its dice as though that ship had spent 1 :forcecharge:.',
        ':purpleforcecharge::forcechargeplus1recurring:',
    ]),
    ('os1arsenalloadout', [
        ':configuration: *<http://xwing-miniatures-second-edition.wikia.com/wiki/Os-1_Arsenal_Loadout|Os-1 Arsenal Loadout>* [0]',
        'Restrictions: :alphaclassstarwing:',
        'While you have exactly 1 disarm token, you can still perform :Torpedo: and :Missile: attacks against targets you have locked. If you do, you cannot spend your lock during the attack. Add :Torpedo: and :Missile: slots.',
    ]),
    ('shieldupgrade', [
        ':modification: *<http://xwing-miniatures-second-edition.wikia.com/wiki/Shield_Upgrade|Shield Upgrade>* [:greenagility::agility0:3:agility1:4:agility2:6:agility3:8]',
        '_Deflector shields are a substantial line of defense on most starships beyond the lightest fighters. While enhancing a ship\'s shield capacity can be costly, all but the most confident or reckless pilots see the value in this sort of investment._',
        ':blueshield::shieldplus1:'
    ]),
    ('starviperclassattackplatform', [
        ':starviperclassattackplatform: *<http://xwing-miniatures-second-edition.wikia.com/wiki/StarViper-class_Attack_Platform|StarViper-class Attack Platform>* :smallbase:',
        ':redfrontarc::attack3::greenagility::agility3::yellowhull::hull4::blueshield::shield1:  :focus:|:targetlock:|:barrelroll::linked::redfocus:|:boost::linked::redfocus:  :sensor::torpedo::modification::title:',
        '4 :blank::blank::straight::blank::blank::blank::blank:',
        '3 :blank::bankleft::bluestraight::bankright::blank::redsloopleft::redsloopright:',
        '2 :turnleft::bluebankleft::bluestraight::bluebankright::turnright::blank::blank:',
        '1 :turnleft::bluebankleft::bluestraight::bluebankright::turnright::blank::blank:',
        '_*Microthrusters:*_ While you perform a barrel roll, you must use the :bankleft: or :bankright: template instead of the :Straight: template.',
        ':scum: :initiative2:<http://xwing-miniatures-second-edition.wikia.com/wiki/Black_Sun_Enforcer|Black Sun Enforcer> [46], :initiative3:<http://xwing-miniatures-second-edition.wikia.com/wiki/Black_Sun_Assassin|Black Sun Assassin> :talent: [48], :initiative4:• <http://xwing-miniatures-second-edition.wikia.com/wiki/Dalan_Oberos|Dalan Oberos> :talent: [54], :initiative4:• <http://xwing-miniatures-second-edition.wikia.com/wiki/Prince_Xizor|Prince Xizor> :talent: [54], :initiative5:• <http://xwing-miniatures-second-edition.wikia.com/wiki/Guri|Guri> :talent: :calculate: [62]',
    ]),
    ('guri', [
        ':starviperclassattackplatform: • *<http://xwing-miniatures-second-edition.wikia.com/wiki/Guri|Guri>*: _Prince Xizor\'s Bodyguard_ [62]',
        ':scum:  :initiative5::redfrontarc::attack3::greenagility::agility3::yellowhull::hull4::blueshield::shield1:  :calculate:|:targetlock:|:barrelroll::linked::redcalculate:|:boost::linked::redcalculate:  :talent::sensor::torpedo::modification::title:',
        'At the start of the Engagement Phase, if there is at least 1 enemy ship at range 0-1, you may gain 1 focus token.',
        '_*Microthrusters:*_ While you perform a barrel roll, you must use the :bankleft: or :bankright: template instead of the :Straight: template.',
    ]),
    ('imdaartestpilot', [
        ':tiephphantom: *<http://xwing-miniatures-second-edition.wikia.com/wiki/Imdaar_Test_Pilot|Imdaar Test Pilot>* [44]',
        ':empire:  :initiative3::redfrontarc::attack3::greenagility::agility2::yellowhull::hull3::blueshield::shield2:  :focus:|:evade:|:barrelroll:|:cloak:  :sensor::crew::modification:',
        '_The primary result of a hidden research facility on Imdaar Alpha, the TIE phantom achieves what many thought was impossible: a small starfighter equipped with an advanced cloaking device._',
        '_*Stygium Array:*_ After you decloak, you may perform an :Evade: action. At the start of the End Phase, you may spend 1 evade token to gain 1 cloak token.',
    ]),
    ('pivotwing', [
        ':configuration: *<http://xwing-miniatures-second-edition.wikia.com/wiki/Pivot_Wing_(Closed)|Pivot Wing (Closed)>* [0]',
        'Restrictions: :ut60duwing:',
        'While you defend, roll 1 fewer defense die. After you execute a :stop: maneuver, you may rotate your ship 90˚ or 180˚. Before you activate, you may flip this card.',
        ':configuration: *<http://xwing-miniatures-second-edition.wikia.com/wiki/Pivot_Wing_(Open)|Pivot Wing (Open)>* [0]',
        'Restrictions: :ut60duwing:',
        'Before you activate, you may flip this card.',
    ]),
    ('directhit', [
        ':crit: *Direct Hit!* (core)',
        'Suffer 1 :Hit: damage. Then repair this card.',
    ]),
    ('hunted', [
        ':condition: *Hunted*',
        'After you are destroyed, you must choose another friendly ship and assign this condition to it, if able.',
    ]),
    ('agentkallus', [
        ':crew: • *<http://xwing-miniatures-second-edition.wikia.com/wiki/Agent_Kallus|Agent Kallus>* [6]',
        'Restrictions: Imperial',
        'Setup: Assign the Hunted condition to 1 enemy ship. While you perform an attack against th eship with the Hunted condition, you may change 1 of your :Focus: results to a :Hit: result.',
        ':condition: *Hunted*',
        'After you are destroyed, you must choose another friendly ship and assign this condition to it, if able.',
    ]),
)

@pytest.mark.parametrize('name, expected', print_card_tests)
def test_print_card(testbot, name, expected):
    assert testbot.print_card(testbot.test_lookup(name)) == expected


lookup_tests = {
    'sunny bounder': [('sunnybounder', 'pilot')],
    'Rey': [('rey', 'pilot')],
    'han solo': [
        ('hansolo', 'gunner'),
        ('hansolo-gunner', 'gunner'),
        ('hansolo-modifiedyt1300lightfreighter', 'pilot'),
        ('hansolo', 'pilot'),
        ('hansolo-modifiedyt1300lightfreighter-resistance', 'pilot')
    ],
    'xwing': [('t65xwing', 'ship'), ('t70xwing', 'ship')],
    ':gunner: Han solo': [('hansolo', 'gunner'), ('hansolo-gunner', 'gunner')],
    'Han solo :gunner:': [('hansolo', 'gunner'), ('hansolo-gunner', 'gunner')],
    ':astromech: r2d2': [('r2d2', 'astromech')],
    'rey]]   [[finn': [('rey', 'pilot'), ('finn', 'gunner')],
    'rey]]   [[finn]] [[:astromech: r2d2]]': [
        ('rey', 'pilot'), ('finn', 'gunner'), ('r2d2', 'astromech')],
    'han': [
        ('hansolo', 'gunner'),
        ('hansolo-gunner', 'gunner'),
        ('hansolo-modifiedyt1300lightfreighter', 'pilot'),
        ('hansolo', 'pilot'),
        ('hansolo-modifiedyt1300lightfreighter-resistance', 'pilot')
    ],
    ':modifiedyt1300lightfreighter: Han': [
        ('hansolo-modifiedyt1300lightfreighter', 'pilot'),
        ('hansolo-modifiedyt1300lightfreighter-resistance', 'pilot')
    ],
    'test': [('imdaartestpilot', 'pilot')],
    'fcs': [('firecontrolsystem', 'sensor')],
    ':astromech: &gt; 7': [('r2d2', 'astromech')],
    ':crew: = 13': [('emperorpalpatine', 'crew'), ('maul', 'crew')],
    ':focus:': [],
    'hot shot': [('hotshotgunner', 'gunner')],
    # Test for unescaped lookup in regex
    '{0}{0}{1}': [],
    'z95': [('z95af4headhunter', 'ship')],
    'tieddefender': [('tieddefender', 'ship')],
    'tiedefender': [('tieddefender', 'ship')],
    'TIE STRIKER': [('tieskstriker', 'ship')],
}
@pytest.mark.parametrize('lookup, expected', lookup_tests.items())
def test_lookup(testbot, lookup, expected):
    actual = [(card['xws'], card['category']) for card in testbot.lookup(lookup)]
    assert actual == expected


def test_card_limit(testbot):
    assert testbot.handle_lookup('tie') == [
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
    ({"type": "Focus"}, ":focus:"),
    ({"difficulty": "White", "type": "Barrel Roll", "linked": {
        "difficulty": "Red", "type": "Focus"}},
     ":barrelroll::linked::redfocus:")
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
    ([{'action': {"type": "Focus"}}], "Restrictions: :focus:"),
    ([{"ships": ["t65xwing"]}], "Restrictions: :t65xwing:"),
    ([{'factions': ["Galactic Empire"]}], "Restrictions: Imperial"),
    ([{'factions': ["Rebel Alliance", "Scum and Villainy"]}], "Restrictions: Rebel or Scum"),
    ([{"ships": ["m3ainterceptor"], 'action': {"difficulty": "White", "type": "Focus"}}], "Restrictions: :focus: or :m3ainterceptor:"),
    ([{"sizes": ["Small"]}], "Restrictions: Small ship"),
    ([{"sizes": ["Small", "Medium"]}], "Restrictions: Small or Medium ship"),
    ([{"factions": ["Scum and Villainy"], "names": ["Darth Vader"]}], "Restrictions: Scum or squad including Darth Vader"),
    ([{"arcs": ["Rear Arc"]}], "Restrictions: :reararc:"),
])
def test_print_restrictions(testbot, res, expected):
    assert testbot.print_restrictions(res) == expected

@pytest.mark.parametrize('pilot, expected', [
    ('guri', ["_*Microthrusters:*_ While you perform a barrel roll, you must use the :bankleft: or :bankright: template instead of the :Straight: template."]),
    ('autopilotdrone', ['_*Rigged Energy Cells:*_ During the System Phase, if you are not docked, lose 1 :Charge:. At the end of the Activation Phase, if you have 0 :Charge:, you are destroyed. Before you are removed, each ship at range 0-1 suffers 1 :crit: damage.'])
])
def test_print_ship_ability(testbot, pilot, expected):
    ability = testbot.test_lookup(pilot)['shipAbility']
    assert testbot.print_ship_ability(ability) == expected

@pytest.mark.parametrize('ship, expected', [
    ('starviperclassattackplatform', [
        '_*Microthrusters:*_ While you perform a barrel roll, you must use the :bankleft: or :bankright: template instead of the :Straight: template.',
        ':scum: :initiative2:<http://xwing-miniatures-second-edition.wikia.com/wiki/Black_Sun_Enforcer|Black Sun Enforcer> [46], :initiative3:<http://xwing-miniatures-second-edition.wikia.com/wiki/Black_Sun_Assassin|Black Sun Assassin> :talent: [48], :initiative4:• <http://xwing-miniatures-second-edition.wikia.com/wiki/Dalan_Oberos|Dalan Oberos> :talent: [54], :initiative4:• <http://xwing-miniatures-second-edition.wikia.com/wiki/Prince_Xizor|Prince Xizor> :talent: [54], :initiative5:• <http://xwing-miniatures-second-edition.wikia.com/wiki/Guri|Guri> :talent: :calculate: [62]',
    ]),
    ('hwk290lightfreighter', [
        ':rebel: :initiative2:<http://xwing-miniatures-second-edition.wikia.com/wiki/Rebel_Scout|Rebel Scout> [32], :initiative3:• <http://xwing-miniatures-second-edition.wikia.com/wiki/Kyle_Katarn|Kyle Katarn> :talent: [38], :initiative4:• <http://xwing-miniatures-second-edition.wikia.com/wiki/Roark_Garnet|Roark Garnet> :talent: [38], :initiative5:• <http://xwing-miniatures-second-edition.wikia.com/wiki/Jan_Ors|Jan Ors> :talent: [42]',
        ':scum: :initiative1:<http://xwing-miniatures-second-edition.wikia.com/wiki/Spice_Runner|Spice Runner> :illicit: [32], :initiative2:• <http://xwing-miniatures-second-edition.wikia.com/wiki/Torkil_Mux|Torkil Mux> :illicit: [36], :initiative3:• <http://xwing-miniatures-second-edition.wikia.com/wiki/Palob_Godalhi|Palob Godalhi> :talent::illicit: [38], :initiative4:• <http://xwing-miniatures-second-edition.wikia.com/wiki/Dace_Bonearm|Dace Bonearm> :talent::illicit: [36]'
    ]),
    ('escapecraft', [
        '_*Rigged Energy Cells:*_ During the System Phase, if you are not docked, lose 1 :Charge:. At the end of the Activation Phase, if you have 0 :Charge:, you are destroyed. Before you are removed, each ship at range 0-1 suffers 1 :crit: damage.',
        ':scum: :initiative1:• <http://xwing-miniatures-second-edition.wikia.com/wiki/Autopilot_Drone|Autopilot Drone> :calculate: [12]',
        '_*Co-Pilot:*_ While you are docked, your carrier ship has your pilot ability in addition to its own.',
        ':scum: :initiative2:• <http://xwing-miniatures-second-edition.wikia.com/wiki/L3-37|L3-37> :talent::crew::modification: :calculate: [22], :initiative3:• <http://xwing-miniatures-second-edition.wikia.com/wiki/Outer_Rim_Pioneer|Outer Rim Pioneer> :talent::crew::modification: [24], :initiative4:• <http://xwing-miniatures-second-edition.wikia.com/wiki/Lando_Calrissian|Lando Calrissian> :talent::crew::modification: [26]',
    ])
])
def test_list_pilots(testbot, ship, expected):
    assert testbot.list_pilots(testbot.test_lookup(ship)) == expected

@pytest.mark.parametrize('ship, pilot, expected', [
    ('starviperclassattackplatform', None,
     ':redfrontarc::attack3::greenagility::agility3::yellowhull::hull4::blueshield::shield1:  :focus:|:targetlock:|:barrelroll::linked::redfocus:|:boost::linked::redfocus:  :sensor::torpedo::modification::title:',
    ),
    ('starviperclassattackplatform', 'guri',
     ':scum:  :initiative5::redfrontarc::attack3::greenagility::agility3::yellowhull::hull4::blueshield::shield1:  :calculate:|:targetlock:|:barrelroll::linked::redcalculate:|:boost::linked::redcalculate:  :talent::sensor::torpedo::modification::title:'
    ),
    ('m12lkimogilafighter', 'dalanoberos',
     ':scum:  :initiative3::redfrontarc::attack3::greenagility::agility1::yellowhull::hull7::blueshield::shield2::orangecharge::charge2:  :focus:|:targetlock:|:redbarrelroll:|:reload:  :talent::torpedo::missile::astromech::illicit::modification:'
    ),
    ('t65xwing', 'lukeskywalker.1',
     ':rebel:  :initiative5::redfrontarc::attack3::greenagility::agility2::yellowhull::hull4::blueshield::shield2::purpleforcecharge::forcecharge2recurring:  :focus:|:targetlock:|:barrelroll:  :forcepower::torpedo::astromech::modification::configuration:'
    ),
    ('kihraxzfighter', None,
     ':redfrontarc::attack3::greenagility::agility2::yellowhull::hull5::blueshield::shield1:  :focus:|:targetlock:|:barrelroll:  :missile::illicit::modification::modification::modification:'
    )
])
def test_ship_stats(testbot, ship, pilot, expected):
    ship = testbot.test_lookup(ship)
    if pilot:
        pilot = testbot.test_lookup(pilot)
    assert testbot.ship_stats(ship, pilot) == expected

@pytest.mark.parametrize('card, expected', [
    ('munitionsfailsafe', '[2]'),
    ('guri', '[62]'),
    ('shieldupgrade', '[:greenagility::agility0:3:agility1:4:agility2:6:agility3:8]'),
    ('engineupgrade', '[:smallbase:3:mediumbase:6:largebase:9]'),
])
def test_print_cost(testbot, card, expected):
    assert testbot.print_cost(testbot.test_lookup(card)['cost']) == expected


@pytest.mark.parametrize('card, expected', [
    ('os1arsenalloadout', None),
    ('c3po', [':calculate:']),
    ('hullupgrade', [':yellowhull::hullplus1:']),
    ('shieldupgrade', [':blueshield::shieldplus1:']),
])
def test_print_grants(testbot, card, expected):
    assert testbot.print_grants(testbot.test_lookup(card)['sides'][0]['grants']) == expected


@pytest.mark.parametrize('card, expected', [
    ('homingmissiles', ':redfrontarc::attack4::redrangebonusindicator:2-3'),
    ('advprotontorpedoes', ':redfrontarc::attack5::redrangebonusindicator:1'),
    ('dorsalturret', ':redsingleturretarc::attack2:1-2')
])
def test_print_attack(testbot, card, expected):
    assert testbot.print_attack(testbot.test_lookup(
        card)['sides'][0]['attack']) == expected
