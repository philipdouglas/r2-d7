import pytest

from r2d7.cardlookup import CardLookup
from r2d7.core import UserError
from r2d7.slackdroid import SlackDroid


print_card_tests = (
    ('tacticalofficer', [
        ':crew: *<https://xwingtmgwiki.com/Tactical_Officer|Tactical Officer>* [3] [Standard]',
        '_Restrictions: :redcoordinate:_',
        '_In the chaos of a starfighter battle, a single order can mean the difference between a victory and a massacre._',
        ':coordinate:',
    ]),
    ('predator', [
        ':talent: *<https://xwingtmgwiki.com/Predator|Predator>* [2] [Standard]',
        'While you perform a primary attack, if the defender is in your :bullseyearc:, you may reroll 1 attack die.',
    ]),
    ('homingmissiles', [
        ':missile: *<https://xwingtmgwiki.com/Homing_Missiles|Homing Missiles>* [5] [Standard]',
        'Attack (:targetlock:): Spend 1 :charge:. After you declare the defender, the defender may choose to suffer 1 :hit: damage. If it does, skip the Attack and Defense Dice steps and the attack is treated as hitting.',
        ':redfrontarc::attack4::redrangebonusindicator:2-3 | :orangecharge::charge2:',
    ]),
    ('r2astromech', [
        ':astromech: *<https://xwingtmgwiki.com/R2_Astromech|R2 Astromech>* [6] [Standard]',
        'After you reveal your dial, you may spend 1 :charge: and gain 1 disarm token to recover 1 shield.',
        ':orangecharge::charge2:',
    ]),
    ('emperorpalpatine', [
        ':crew::crew: • *<https://xwingtmgwiki.com/Emperor_Palpatine|Emperor Palpatine>* [12] [Standard]',
        '_Restrictions: Imperial_',
        'While another friendly ship defends or performs an attack, you may spend 1 :forcecharge: to modify 1 of its dice as though that ship had spent 1 :forcecharge:.',
        ':purpleforcecharge::forcechargeplus1recurring:',
    ]),
    ('os1arsenalloadout', [
        ':configuration: *<https://xwingtmgwiki.com/Os-1_Arsenal_Loadout|Os-1 Arsenal Loadout>* [0] [Extended]',
        '_Restrictions: Alpha-class Star Wing_',
        'While you have exactly 1 disarm token, you can still perform :torpedo: and :missile: attacks against targets you have locked. If you do, you cannot spend your lock during the attack. Add :torpedo: and :missile: slots.',
    ]),
    ('shieldupgrade', [
        ':modification: *<https://xwingtmgwiki.com/Shield_Upgrade|Shield Upgrade>* [6] [Standard]',
        '_Deflector shields are a substantial line of defense on most starships beyond the lightest fighters. While enhancing a ship\'s shield capacity can be costly, all but the most confident or reckless pilots see the value in this sort of investment._',
        ':blueshield::shieldplus1:'
    ]),
    ('starviperclassattackplatform', [
        ':starviperclassattackplatform: *<https://xwingtmgwiki.com/StarViper-class_Attack_Platform|StarViper-class Attack Platform>* :smallbase:',
        ':redfrontarc::attack3::greenagility::agility3::yellowhull::hull4::blueshield::shield1:  :focus:|:targetlock:|:barrelroll::linked::redfocus:|:boost::linked::redfocus:  :tech:',
        '`4` :blank::blank::straight::blank::blank::blank::blank:',
        '`3` :blank::bankleft::bluestraight::bankright::blank::redsloopleft::redsloopright:',
        '`2` :turnleft::bluebankleft::bluestraight::bluebankright::turnright::blank::blank:',
        '`1` :turnleft::bluebankleft::bluestraight::bluebankright::turnright::blank::blank:',
        '_*Microthrusters:*_ While you perform a barrel roll, you *must* use the :bankleft: or :bankright: template instead of the :straight: template.',
        ':scum: :initiative2:<https://xwingtmgwiki.com/Black_Sun_Enforcer|Black Sun Enforcer> *[5]* [6], :initiative3:<https://xwingtmgwiki.com/Black_Sun_Assassin|Black Sun Assassin> *[5]* [6], :initiative4:•<https://xwingtmgwiki.com/Dalan_Oberos|Dalan Oberos> :talent::torpedo::modification: *[5]* [10], :initiative4:•<https://xwingtmgwiki.com/Prince_Xizor|Prince Xizor> :talent::torpedo::modification::title: *[5]* [7], :initiative5:•<https://xwingtmgwiki.com/Guri|Guri> :talent::torpedo::modification::title: :calculate: *[7]* [20]',
    ]),
    ('guri', [
        ':starviperclassattackplatform: • *<https://xwingtmgwiki.com/Guri|Guri>*: _Prince Xizor’s Bodyguard_ *[7]* [20] [Droid] [Extended]',
        ':scum:  :initiative5::redfrontarc::attack3::greenagility::agility3::yellowhull::hull4::blueshield::shield1:  :calculate:|:targetlock:|:barrelroll::linked::redcalculate:|:boost::linked::redcalculate:  :talent::tech::torpedo::modification::title:',
        'At the start of the Engagement Phase, if there is at least 1 enemy ship at range 0-1, you may gain 1 focus token.',
        '_*Microthrusters:*_ While you perform a barrel roll, you *must* use the :bankleft: or :bankright: template instead of the :straight: template.',
    ]),
    ('imdaartestpilot', [
        ':tiephphantom: *<https://xwingtmgwiki.com/Imdaar_Test_Pilot|Imdaar Test Pilot>* *[5]* [6] [TIE] [Extended]',
        ':imperial:  :initiative3::redfrontarc::attack3::greenagility::agility2::yellowhull::hull3::blueshield::shield2:  :focus:|:evade:|:barrelroll:|:cloak:  :sensor::modification::gunner:',
        '_The primary result of a hidden research facility on Imdaar Alpha, the TIE phantom achieves what many thought was impossible: a small starfighter equipped with an advanced cloaking device._',
        '_*Stygium Array:*_ After you decloak, you may perform an :evade: action. At the start of the End Phase, you may spend 1 evade token to gain 1 cloak token.',
    ]),
    ('pivotwing', [
        ':configuration: *<https://xwingtmgwiki.com/Pivot_Wing_%28Closed%29|Pivot Wing (Closed)>* [0] [Standard]',
        '_Restrictions: UT-60D U-wing_',
        'While you defend, roll 1 fewer defense die. After you execute a [0 :stop:] maneuver, you may rotate your ship 90° or 180°. Before you activate, you may flip this card.',
        ':configuration: *<https://xwingtmgwiki.com/Pivot_Wing_%28Open%29|Pivot Wing (Open)>* [0] [Standard]',
        '_Restrictions: UT-60D U-wing_',
        'Before you activate, you may flip this card.',
    ]),
    ('directhit', [
        ':crit: *Direct Hit!* (core) •••••',
        'Suffer 1 :hit: damage. Then repair this card.',
    ]),
    ('hunted', [
        ':condition: *Hunted*',
        'After you are destroyed, you *must* choose another friendly ship and assign this condition to it, if able.',
    ]),
    ('agentkallus', [
        ':crew: • *<https://xwingtmgwiki.com/Agent_Kallus|Agent Kallus>* [5] [Standard]',
        '_Restrictions: Imperial_',
        '*Setup:* After placing forces, assign the _*Hunted*_ condition to 1 enemy ship. While you perform an attack against the ship with the _*Hunted*_ condition, you may change 1 of your :focus: results to a :hit: result.',
        ':condition: *Hunted*',
        'After you are destroyed, you *must* choose another friendly ship and assign this condition to it, if able.',
    ]),
    ('seismiccharges', [
        ':device: *<https://xwingtmgwiki.com/Seismic_Charges|Seismic Charges>* [3] [Standard]',
        '_*Bomb:*_ During the System Phase, you may spend 1 :charge: to drop a Seismic Charge with the [1 :straight:] template.',
        ':orangecharge::charge2:',
        '*Seismic Charge* (Bomb)',
        'At the end of the Activation Phase, this device detonates. When this device detonates, choose 1 obstacle at range 0-1. Each ship and remote at range 0-1 of the obstacle suffers 1 :hit: damage. Then remove that obstacle.',
    ]),
    ('snapshot', [
        ":talent: *<https://xwingtmgwiki.com/Snap_Shot|Snap Shot>* [9] [Standard]",
        "After an enemy ship executes a maneuver, you may perform this attack against it as a bonus attack.",
        "*Attack:* Your dice cannot be modified.",
        ':redfrontarc::attack2::redrangebonusindicator:2',
    ]),
)

@pytest.mark.parametrize('name, expected', print_card_tests)
def test_print_card(testbot, name, expected):
    assert testbot.print_card(testbot.test_lookup(name)) == expected

print_card_image_tests = (
    ('directhit', []),
    ('hunted', []),
    ('sunnybounder', ['https://squadbuilder.fantasyflightgames.com/card_images/Card_Pilot_188.png']),
    ('l337.2', ['https://squadbuilder.fantasyflightgames.com/card_images/Card_Pilot_228.png']),
    ('chopper.0', ['https://squadbuilder.fantasyflightgames.com/card_images/Card_Upgrade_99.png']),
    ('servomotorsfoils', ['https://squadbuilder.fantasyflightgames.com/card_images/Card_Upgrade_108.png', 'https://squadbuilder.fantasyflightgames.com/card_images/Card_Upgrade_108b.png']),
)

@pytest.mark.parametrize('name, expected', print_card_image_tests)
def test_print_card_image(testbot, name, expected):
    assert sorted(testbot.print_image(testbot.test_lookup(name))) == sorted(expected)

lookup_tests = {
    'sunny bounder': [('sunnybounder', 'pilot')],
    'Rey': [('rey-gunner', 'gunner'), ('rey', 'pilot'), ('reysmillenniumfalcon', 'title')],
    'han solo': [
        ('hansolo-crew', 'crew'),
        ('hansolo', 'gunner'),
        ('hansolo-gunner', 'gunner'),
        ('hansolo-modifiedyt1300lightfreighter', 'pilot'),
        ('hansolo', 'pilot'),
        ('hansolo-scavengedyt1300', 'pilot')
    ],
    'xwing': [('t65xwing', 'ship'), ('t70xwing', 'ship')],
    ':gunner: Han solo': [('hansolo', 'gunner'), ('hansolo-gunner', 'gunner')],
    'Han solo :gunner:': [('hansolo', 'gunner'), ('hansolo-gunner', 'gunner')],
    ':astromech: r2d2': [('r2d2', 'astromech'), ('r2d2-republic', 'astromech'), ('r2d2-resistance', 'astromech')],
    'guri]]   [[finn': [('guri', 'pilot'), ('finn', 'gunner'), ('finn', 'pilot')],
    'guri]]   [[finn]] [[:astromech: r2d2]]': [
        ('guri', 'pilot'), ('finn', 'gunner'), ('finn', 'pilot'), ('r2d2', 'astromech'), ('r2d2-republic', 'astromech'), ('r2d2-resistance', 'astromech')],
    'han': [
        ('hansolo-crew', 'crew'),
        ('hansolo', 'gunner'),
        ('hansolo-gunner', 'gunner'),
        ('hansolo-modifiedyt1300lightfreighter', 'pilot'),
        ('hansolo', 'pilot'),
        ('hansolo-scavengedyt1300', 'pilot')
    ],
    ':modifiedyt1300lightfreighter: Han': [
        ('hansolo-modifiedyt1300lightfreighter', 'pilot'),
    ],
    'test': [('imdaartestpilot', 'pilot'), ('firstordertestpilot', 'pilot'), ('sienarjaemustestpilot', 'pilot')],
    'fcs': [('firecontrolsystem', 'sensor')],
    ':astromech: &gt; 6': [('r2d2', 'astromech'), ('r2d2-republic', 'astromech'), ('bb8', 'astromech'), ('c110p', 'astromech')],
    ':crew: = 13': [('grandinquisitor', 'crew'), ('supremeleadersnoke', 'crew')],
    ':focus:': [],
    'hot shot': [('hotshotgunner', 'gunner'), ('hotshottailblaster', 'illicit')],
    # Test for unescaped lookup in regex
    '{0}{0}{1}': [],
    'z95': [('z95af4headhunter', 'ship')],
    'tieddefender': [('tieddefender', 'ship')],
    'tiedefender': [('tiedefenderelite', 'configuration'), ('tieddefender', 'ship')],
    'TIE STRIKER': [('tieskstriker', 'ship')],
}
@pytest.mark.parametrize('lookup, expected', lookup_tests.items())
def test_lookup(testbot, lookup, expected):
    actual = [(card['xws'], card['category']) for card in testbot.lookup(lookup)]
    assert actual == expected

@pytest.mark.parametrize('lookup, message', [
    ('tie', 'Your search matched more than 15 cards, please be more specific.'),
    ('> 4', 'You need to specify a slot to search by points value.')
])
def test_user_errors(testbot, lookup, message):
    with pytest.raises(UserError, match=message):
        testbot.handle_lookup(lookup)

@pytest.mark.parametrize('dialgen, slack', (
    ([
        "1TW", "1YW", "2TW", "2BB", "2FB", "2NB", "2YW", "3TW", "3BW", "3FB",
        "3NW", "3YW", "3KR", "4FW", "4KR", "5FW"
    ],
    [
        '`5` :blank::blank::straight::blank::blank::blank:',
        '`4` :blank::blank::straight::blank::blank::redkturn:',
        '`3` :turnleft::bankleft::bluestraight::bankright::turnright::redkturn:',
        '`2` :turnleft::bluebankleft::bluestraight::bluebankright::turnright::blank:',
        '`1` :turnleft::blank::blank::blank::turnright::blank:',
    ]
    ),
    ([
        "1AR", "1DR", "1TW", "1BW", "1FW", "1NW", "1YW", "2SR", "2LR", "2TW",
        "2BB", "2FB", "2NB", "2YW", "2PR", "3BW", "3FB", "3NW"
    ],
    [
        '`3` :blank::bankleft::bluestraight::bankright::blank::blank::blank::blank::blank::blank:',
        '`2` :turnleft::bluebankleft::bluestraight::bluebankright::turnright::redsloopleft::redsloopright::blank::redreversestraight::blank:',
        '`1` :turnleft::bankleft::straight::bankright::turnright::blank::blank::redreversebankleft::blank::redreversebankright:',
    ]
    ),
    ([
        "0OR", "1BB", "1FB", "1NB", "2TR", "2BW", "2FB", "2NW", "2YR", "3BR",
        "3FW", "3NR"
    ],
    [
        '`3` :blank::redbankleft::straight::redbankright::blank:',
        '`2` :redturnleft::bankleft::bluestraight::bankright::redturnright:',
        '`1` :blank::bluebankleft::bluestraight::bluebankright::blank:',
        '`0` :blank::blank::redstop::blank::blank:',
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
    ([{'action': {"difficulty": "Red", "type": "Focus"}}], "_Restrictions: :redfocus:_"),
    ([{'action': {"type": "Focus"}}], "_Restrictions: :focus:_"),
    ([{"ships": ["t65xwing"]}], "_Restrictions: T-65 X-wing_"),
    ([{'factions': ["Galactic Empire"]}], "_Restrictions: Imperial_"),
    ([{'factions': ["Rebel Alliance", "Scum and Villainy"]}], "_Restrictions: Rebel or Scum_"),
    ([{"ships": ["m3ainterceptor"], 'action': {"difficulty": "White", "type": "Focus"}}], "_Restrictions: :focus: or M3-A Interceptor_"),
    ([{"sizes": ["Small"]}], "_Restrictions: Small ship_"),
    ([{"sizes": ["Small", "Medium"]}], "_Restrictions: Small or Medium ship_"),
    ([{"factions": ["Scum and Villainy"], "names": ["Darth Vader"]}], "_Restrictions: Scum or squad including Darth Vader_"),
    ([{"arcs": ["Rear Arc"]}], "_Restrictions: :reararc:_"),
    ([{"factions": ["Scum and Villainy"]}, {"ships": ["aggressorassaultfighter"]}],
     "_Restrictions: Scum, Aggressor Assault Fighter_"),
    ([{"factions": ["Resistance"]}], "_Restrictions: Resistance_"),
    ([{"equipped": ["Astromech"]}], "_Restrictions: Equipped :astromech:_"),
    ([{"solitary": True}], "_Restrictions: Solitary_"),
    ([{"non-limited": True}], "_Restrictions: Non-Limited_"),
    ([{"solitary": False}], None),
    ([{"non-limtied": False}], None),
    ([{"force_side": ["dark"]}], "_Restrictions: Dark side_"),
])
def test_print_restrictions(testbot, res, expected):
    assert testbot.print_restrictions(res) == expected

@pytest.mark.parametrize('pilot, expected', [
    ('guri', ["_*Microthrusters:*_ While you perform a barrel roll, you *must* use the :bankleft: or :bankright: template instead of the :straight: template."]),
    ('autopilotdrone', ['_*Rigged Energy Cells:*_ During the System Phase, if you are not docked, lose 1 :charge:. At the end of the Activation Phase, if you have 0 :charge:, you are destroyed. Before you are removed, each ship at range 0-1 suffers 1 :crit: damage.'])
])
def test_print_ship_ability(testbot, pilot, expected):
    ability = testbot.test_lookup(pilot)['shipAbility']
    assert testbot.print_ship_ability(ability) == expected

@pytest.mark.parametrize('ship, expected', [
    ('starviperclassattackplatform', [
        '_*Microthrusters:*_ While you perform a barrel roll, you *must* use the :bankleft: or :bankright: template instead of the :straight: template.',
        ':scum: :initiative2:<https://xwingtmgwiki.com/Black_Sun_Enforcer|Black Sun Enforcer> *[5]* [6], :initiative3:<https://xwingtmgwiki.com/Black_Sun_Assassin|Black Sun Assassin> *[5]* [6], :initiative4:•<https://xwingtmgwiki.com/Dalan_Oberos|Dalan Oberos> :talent::torpedo::modification: *[5]* [10], :initiative4:•<https://xwingtmgwiki.com/Prince_Xizor|Prince Xizor> :talent::torpedo::modification::title: *[5]* [7], :initiative5:•<https://xwingtmgwiki.com/Guri|Guri> :talent::torpedo::modification::title: :calculate: *[7]* [20]',
    ]),
    ('hwk290lightfreighter', [
        ':rebel: :initiative2:<https://xwingtmgwiki.com/Rebel_Scout|Rebel Scout> :modification: *[4]* [6], :initiative3:•<https://xwingtmgwiki.com/Kyle_Katarn|Kyle Katarn> :talent::talent::crew::modification::title: *[6]* [12], :initiative4:•<https://xwingtmgwiki.com/Roark_Garnet|Roark Garnet> :talent::crew::modification::modification::title: *[6]* [15], :initiative5:•<https://xwingtmgwiki.com/Jan_Ors|Jan Ors> :talent::crew::modification::modification::title: *[6]* [10]',
        ':scum: :initiative1:<https://xwingtmgwiki.com/Spice_Runner|Spice Runner> :illicit: *[3]* [4], :initiative2:•<https://xwingtmgwiki.com/Torkil_Mux|Torkil Mux> :crew::illicit::modification::modification: *[4]* [10], :initiative3:•<https://xwingtmgwiki.com/Gamut_Key|Gamut Key> :talent::crew::illicit::modification::modification: *[3]* [8], :initiative3:•<https://xwingtmgwiki.com/Kanan_Jarrus|Kanan Jarrus> :forcepower::crew::illicit::modification::modification: *[4]* [10], :initiative3:•<https://xwingtmgwiki.com/Palob_Godalhi|Palob Godalhi> :talent::crew::illicit::modification::modification::title: *[6]* [12], :initiative4:•<https://xwingtmgwiki.com/Dace_Bonearm|Dace Bonearm> :talent::crew::illicit::illicit::modification: *[3]* [9], :initiative5:•<https://xwingtmgwiki.com/T%C3%A1pusk|Tápusk> :talent::crew::illicit::modification::modification: *[4]* [10]',
    ]),
    ('escapecraft', [
        '_*Rigged Energy Cells:*_ During the System Phase, if you are not docked, lose 1 :charge:. At the end of the Activation Phase, if you have 0 :charge:, you are destroyed. Before you are removed, each ship at range 0-1 suffers 1 :crit: damage.',
        ':scum: :initiative1:•<https://xwingtmgwiki.com/Autopilot_Drone|Autopilot Drone> :calculate: *[2]* [0]',
        '_*Co-Pilot:*_ While you are docked, your carrier ship has your pilot ability in addition to its own.',
        ':scum: :initiative2:•<https://xwingtmgwiki.com/L3-37|L3-37> :talent::crew::modification: :calculate: *[3]* [4], :initiative3:•<https://xwingtmgwiki.com/Outer_Rim_Pioneer|Outer Rim Pioneer> :talent::crew::modification: *[3]* [4], :initiative4:•<https://xwingtmgwiki.com/Lando_Calrissian|Lando Calrissian> :talent::crew::modification: *[3]* [4]',
    ])
])
def test_list_pilots(testbot, ship, expected):
    assert testbot.list_pilots(testbot.test_lookup(ship)) == expected

@pytest.mark.parametrize('ship, pilot, expected', [
    ('starviperclassattackplatform', None,
     ':redfrontarc::attack3::greenagility::agility3::yellowhull::hull4::blueshield::shield1:  :focus:|:targetlock:|:barrelroll::linked::redfocus:|:boost::linked::redfocus:  :tech:',
    ),
    ('starviperclassattackplatform', 'guri',
     ':scum:  :initiative5::redfrontarc::attack3::greenagility::agility3::yellowhull::hull4::blueshield::shield1:  :calculate:|:targetlock:|:barrelroll::linked::redcalculate:|:boost::linked::redcalculate:  :talent::tech::torpedo::modification::title:'
    ),
    ('m12lkimogilafighter', 'dalanoberos',
     ':scum:  :initiative3::redfrontarc::attack3::greenagility::agility1::yellowhull::hull7::blueshield::shield2::orangecharge::charge2:  :focus:|:targetlock:|:redbarrelroll:|:reload:  :talent::torpedo::missile::astromech::illicit::modification:'
    ),
    ('t65xwing', 'lukeskywalker.1',
        ':rebel:  :initiative5::redfrontarc::attack3::greenagility::agility2::yellowhull::hull4::blueshield::shield2::purpleforcecharge::forcecharge2recurring:  :focus:|:targetlock:|:barrelroll:  :talent::torpedo::astromech::modification::forcepower::configuration:'
    ),
    ('kihraxzfighter', None,
     ':redfrontarc::attack3::greenagility::agility2::yellowhull::hull5::blueshield::shield1:  :focus:|:targetlock:|:barrelroll:  '
    )
])
def test_ship_stats(testbot, ship, pilot, expected):
    ship = testbot.test_lookup(ship)
    if pilot:
        pilot = testbot.test_lookup(pilot)
    assert testbot.ship_stats(ship, pilot) == expected

@pytest.mark.parametrize('card, expected', [
    ('munitionsfailsafe', '[1]'),
    ('guri', '[7]'),
    ('shieldupgrade', '[6]'),
    ('engineupgrade', '[3]'),
    ('bb8', '[7]'),
])
def test_print_cost(testbot, card, expected):
    assert testbot.print_cost(testbot.test_lookup(card)['cost']) == expected


@pytest.mark.parametrize('data, expected', [
    ([
        {"type": "slot", "value": "Torpedo", "amount": 1},
        {"type": "slot", "value": "Missile", "amount": 1}
    ], None),
    ([{
        "type": "action",
        "value": {"type": "Calculate", "difficulty": "White"},
        "amount": 1
    }], [':calculate:']),
    ([{"type": "stat", "value": "hull", "amount": 1}], [':yellowhull::hullplus1:']),
    ([{"type": "stat", "value": "shields", "amount": 1}],
     [':blueshield::shieldplus1:']),
    ([
        {"type": "stat", "value": "agility", "amount": -1},
        {"type": "stat", "value": "shields", "amount": 2},
        {"type": "stat", "value": "attack", "arc": "Front Arc", "amount": 1}
    ], [
        ':greenagility::agilityminus1:',
        ':blueshield::shieldplus2:',
        ':redattack::attackplus1:'
    ]),
])
def test_print_grants(testbot, data, expected):
    assert testbot.print_grants(data) == expected


@pytest.mark.parametrize('card, expected', [
    ('homingmissiles', ':redfrontarc::attack4::redrangebonusindicator:2-3'),
    ('advprotontorpedoes', ':redfrontarc::attack5::redrangebonusindicator:1'),
    ('dorsalturret', ':redsingleturretarc::attack2:1-2')
])
def test_print_attack(testbot, card, expected):
    assert testbot.print_attack(testbot.test_lookup(
        card)['sides'][0]['attack']) == expected


@pytest.mark.parametrize('card, expected', [
    ('seismiccharges', [
        '*Seismic Charge* (Bomb)',
        'At the end of the Activation Phase, this device detonates. When this device detonates, choose 1 obstacle at range 0-1. Each ship and remote at range 0-1 of the obstacle suffers 1 :hit: damage. Then remove that obstacle.',
    ]),
])
def test_print_device(testbot, card, expected):
    assert testbot.print_device(testbot.test_lookup(
        card)['sides'][0]['device']) == expected
