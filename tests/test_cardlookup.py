import pytest

from r2d7.cardlookup import CardLookup
from r2d7.slackdroid import SlackDroid


print_card_tests = (
    ('veteraninstincts', [
        ':elite: *<http://xwing-miniatures.wikia.com/wiki/Veteran_Instincts|Veteran Instincts>* [1]',
        'Increase your pilot skill value by 2.',
    ]),
    ('tactician', [
        ':crew: *<http://xwing-miniatures.wikia.com/wiki/Tactician|Tactician>* [2]',
        '_Limited._',
        'After you perform an attack against a ship inside your firing arc at Range 2, that ship receives 1 stress token.',
    ]),
    ('rage', [
        ':elite: *<http://xwing-miniatures.wikia.com/wiki/Rage|Rage>* [1]',
        '*Action:* Assign 1 focus token to your ship and receive 2 stress tokens. Until the end of the round, when attacking, you may reroll up to 3 attack dice.',
    ]),
    ('snapshot', [
        ':elite: *<http://xwing-miniatures.wikia.com/wiki/Snap_Shot|Snap Shot>* [2]',
        ':attack::attack2: | Range: 1',
        'After an enemy ship executes a maneuver, you may perform this attack against that ship.',
        '*Attack:* Attack 1 ship. You cannot modify your attack dice and cannot attack again this phase.',
    ]),
    ('heavylaserturret', [
        ':hardpoint: *<http://xwing-miniatures.wikia.com/wiki/Heavy_Laser_Turret|Heavy Laser Turret>* [5]',
        ':attack::attack4: | Range: 2-3 | :energy::energy2:',
        '_C-ROC Cruiser only._',
        '*Attack (energy):* Spend 2 energy from this card to perform this attack against 1 ship (even a ship outside of your firing arc).',
    ]),
    ('brighthope', [
        ':title: • *<http://xwing-miniatures.wikia.com/wiki/Bright_Hope|Bright Hope>* [5]',
        ':energy::energyplus2:',
        '_GR-75 Medium Transport only._',
        'A reinforce token assigned to your fore section acts as 2 :Evade: results (instead of one).',
    ]),
    ('xwing', [
        ':xwing: *X-wing*',
        ':attack3::agility2::hull3::shield2: | :focus: :targetlock: | :torpedo::astromech:',
        '4 :blank::blank::straight::blank::blank::redkturn:',
        '3 :turnleft::bankleft::straight::bankright::turnright::blank:',
        '2 :turnleft::bankleft::greenstraight::bankright::turnright::blank:',
        '1 :blank::greenbankleft::greenstraight::greenbankright::blank::blank:',
        ':rebel: :skill2:<http://xwing-miniatures.wikia.com/wiki/Rookie_Pilot|Rookie Pilot> [21], :skill3:• <http://xwing-miniatures.wikia.com/wiki/Tarn_Mison|Tarn Mison> [23], :skill4:<http://xwing-miniatures.wikia.com/wiki/Red_Squadron_Pilot|Red Squadron Pilot> [23], :skill5:• <http://xwing-miniatures.wikia.com/wiki/Biggs_Darklighter|Biggs Darklighter> [25], :skill5:• <http://xwing-miniatures.wikia.com/wiki/"Hobbie"_Klivian|"Hobbie" Klivian> [25], :skill6:• <http://xwing-miniatures.wikia.com/wiki/Garven_Dreis|Garven Dreis> [26], :skill7:• <http://xwing-miniatures.wikia.com/wiki/Jek_Porkins|Jek Porkins> :elite: [26], :skill8:• <http://xwing-miniatures.wikia.com/wiki/Luke_Skywalker|Luke Skywalker> :elite: [28], :skill8:• <http://xwing-miniatures.wikia.com/wiki/Wes_Janson|Wes Janson> :elite: [29], :skill9:• <http://xwing-miniatures.wikia.com/wiki/Wedge_Antilles|Wedge Antilles> :elite: [29]',
    ]),
    ('firespray31', [
        ':firespray31: *Firespray-31*',
        # The card actually has bomb before crew, but that contradicts other cards
        ':attack3::agility2::hull6::shield4: | :attack-frontback: | :focus: :targetlock: :evade: | :cannon::missile::crew::xbomb:',
        '4 :blank::blank::straight::blank::blank::redkturn:',
        '3 :turnleft::bankleft::straight::bankright::turnright::redkturn:',
        '2 :turnleft::bankleft::greenstraight::bankright::turnright::blank:',
        '1 :blank::greenbankleft::greenstraight::greenbankright::blank::blank:',
        ':empire: :skill3:<http://xwing-miniatures.wikia.com/wiki/Bounty_Hunter|Bounty Hunter> [33], :skill5:• <http://xwing-miniatures.wikia.com/wiki/Krassis_Trelix|Krassis Trelix> [36], :skill7:• <http://xwing-miniatures.wikia.com/wiki/Kath_Scarlet|Kath Scarlet> :elite: [38], :skill8:• <http://xwing-miniatures.wikia.com/wiki/Boba_Fett|Boba Fett> :elite: [39]',
        ':scum: :skill5:<http://xwing-miniatures.wikia.com/wiki/Mandalorian_Mercenary|Mandalorian Mercenary> :elite: [35], :skill6:• <http://xwing-miniatures.wikia.com/wiki/Emon_Azzameen|Emon Azzameen> [36], :skill7:• <http://xwing-miniatures.wikia.com/wiki/Kath_Scarlet|Kath Scarlet> :elite: [38], :skill8:• <http://xwing-miniatures.wikia.com/wiki/Boba_Fett|Boba Fett> :elite: [39]',    ]),
    ('quadjumper', [
        ':quadjumper: *Quadjumper*',
        ':attack2::agility2::hull5::shield0: | :focus: :barrelroll: | :crew::xbomb::tech::illicit:',
        '3 :blank::bankleft::greenstraight::bankright::blank::blank::blank::blank::blank::blank:',
        '2 :turnleft::greenbankleft::greenstraight::greenbankright::turnright::redsloopleft::redsloopright::blank::blank::blank:',
        '1 :turnleft::blank::straight::blank::turnright::blank::blank::redreversebankleft::redreversestraight::redreversebankright:',
        ':scum: :skill1:<http://xwing-miniatures.wikia.com/wiki/Jakku_Gunrunner|Jakku Gunrunner> [15], :skill3:• <http://xwing-miniatures.wikia.com/wiki/Unkar_Plutt|Unkar Plutt> [17], :skill5:• <http://xwing-miniatures.wikia.com/wiki/Sarco_Plank|Sarco Plank> :elite: [18], :skill7:• <http://xwing-miniatures.wikia.com/wiki/Constable_Zuvio|Constable Zuvio> :elite: [19]',
    ]),
    ('yv666', [
        ':yv666: *YV-666*',
        ':attack3::agility1::hull6::shield6: | :attack-180: | :focus: :targetlock: | :cannon::missile::crew::crew::crew::illicit:',
        '4 :blank::blank::straight::blank::blank:',
        '3 :turnleft::bankleft::greenstraight::bankright::turnright:',
        '2 :redturnleft::bankleft::greenstraight::bankright::redturnright:',
        '1 :blank::greenbankleft::greenstraight::greenbankright::blank:',
        '0 :blank::blank::redstop::blank::blank:',
        ':scum: :skill2:<http://xwing-miniatures.wikia.com/wiki/Trandoshan_Slaver|Trandoshan Slaver> [29], :skill5:• <http://xwing-miniatures.wikia.com/wiki/Latts_Razzi|Latts Razzi> [33], :skill6:• <http://xwing-miniatures.wikia.com/wiki/Moralo_Eval|Moralo Eval> [34], :skill7:• <http://xwing-miniatures.wikia.com/wiki/Bossk|Bossk> :elite: [35]',
    ]),
    ('rey.0', [
        ':crew: • *<http://xwing-miniatures.wikia.com/wiki/Rey_(Crew)|Rey>* [2]',
        '_Rebel only._',
        'At the start of the End phase, you may place 1 of your ship\'s focus tokens on this card. At the start of the Combat phase, you may assign 1 of those tokens to your ship.',
    ]),
    ('rey.1', [
        ':yt1300: • *<http://xwing-miniatures.wikia.com/wiki/Rey|Rey>* [45]',
        ':resistance: | :skill8::attack3::agility1::hull8::shield5: | :attack-turret: | :focus: :targetlock: | :elite::missile::crew::crew:',
        'When attacking or defending, if the enemy ship is inside your firing arc, you may reroll up to 2 of your blank results.',
    ]),
    ('quinnjast', [
        ':m3ainterceptor: • *<http://xwing-miniatures.wikia.com/wiki/Quinn_Jast|Quinn Jast>* [18]',
        ':scum: | :skill6::attack2::agility3::hull2::shield1: | :focus: :targetlock: :barrelroll: :evade: | :elite:',
        'At the start of the Combat phase, you may receive a weapons disabled token to flip one of your discarded :Torpedo: or :Missile: Upgrade cards faceup.',
    ]),
    ('countessryad', [
        ':tiedefender: • *<http://xwing-miniatures.wikia.com/wiki/Countess_Ryad|Countess Ryad>* [34]',
        ':empire: | :skill5::attack3::agility3::hull3::shield3: | :focus: :targetlock: :barrelroll: | :elite::cannon::missile:',
        'When you reveal a :Straight: maneuver, you may treat it as a :kturn: maneuver.',
    ]),
    ('outerrimsmuggler', [
        ':yt1300: *<http://xwing-miniatures.wikia.com/wiki/Outer_Rim_Smuggler|Outer Rim Smuggler>* [27]',
        ':rebel: | :skill1::attack2::agility1::hull6::shield4: | :attack-turret: | :focus: :targetlock: | :crew::crew:',
    ]),
    ('r3astromech', [
        ':astromech: *<http://xwing-miniatures.wikia.com/wiki/R3_Astromech|R3 Astromech>* [2]',
        'Once per round, when attacking with a primary weapon, you may cancel 1 of your :Focus: results during the "Modify Attack Dice" step to assign 1 evade token to your ship.',
    ]),
    ('adaptability.0', [
        ':elite: *<http://xwing-miniatures.wikia.com/wiki/Adaptability|Adaptability (-1)>* [0]',
        'Decrease your pilot skill value by 1.'
    ]),
    ('adaptability.1', [
        ':elite: *<http://xwing-miniatures.wikia.com/wiki/Adaptability|Adaptability (+1)>* [0]',
        'Increase your pilot skill value by 1.'
    ]),
    ('bombloadout', [
        ':torpedo: *<http://xwing-miniatures.wikia.com/wiki/Bomb_Loadout|Bomb Loadout>* [0]',
        '_Y-wing only. Limited._',
        'Your upgrade bar gains the :xbomb: icon.',
    ]),
    ('fleetofficer', [
        ':crew: *<http://xwing-miniatures.wikia.com/wiki/Fleet_Officer|Fleet Officer>* [3]',
        '_Imperial only._',
        '*Action:* Choose up to 2 friendly ships within Range 1-2 and assign 1 focus token to each of those ships. Then receive 1 stress token.',
    ]),
    ('r2d2-swx22', [
        ':crew: • *<http://xwing-miniatures.wikia.com/wiki/R2-D2_(Crew)|R2-D2>* [4]',
        '_Rebel only._',
        'At the end of the End phase, if you have no shields, you may recover 1 shield and roll 1 attack die.  On a :Hit: result, randomly flip 1 of your facedown Damage cards faceup and resolve it.',
    ]),
    ('mimicked', [
        ':condition: • *<http://xwing-miniatures.wikia.com/wiki/Mimicked|Mimicked>*',
        '"Thweek" is treated as having your pilot ability.',
        '"Thweek" cannot apply a Condition card by using your pilot ability.',
        '"Thweek" does not lose your pilot ability if you are destroyed.',
    ]),
    ('whisper', [
        ':tiephantom: • *<http://xwing-miniatures.wikia.com/wiki/"Whisper"|"Whisper">* [32]',
        ':empire: | :skill7::attack4::agility2::hull2::shield2: | :focus: :barrelroll: :evade: :cloak: | :elite::system::crew:',
        'After you perform an attack that hits, you may assign 1 focus token to your ship.',
    ]),
    ('tiex1', [
        ':title: *<http://xwing-miniatures.wikia.com/wiki/TIE/x1|TIE/x1>* [0]',
        '_TIE Advanced only._',
        'Your upgrade bar gains the :System: upgrade icon.',
        'If you equip a :System: upgrade, its squad point cost is reduced by 4 (to a minimum of 0).',
    ]),
    pytest.param('automatedprotocols', [
        ':modification: *<http://xwing-miniatures.wikia.com/wiki/Automated_Protocols|Automated Protocols>* [5]',
        '_Huge ship only._',
        'Once per round, after you perform an action that is not a recover or reinforce action, you may spend 1 energy to perform a free recover or reinforce action.',
    ], marks=pytest.mark.xfail),
    ('deadeye', [
        ':elite: *<http://xwing-miniatures.wikia.com/wiki/Deadeye|Deadeye>* [1]',
        '_Small ship only._',
        'You may treat the *Attack (target lock):* header as *Attack (focus):*.',
        'When an attack instructs you to spend a target lock, you may spend a focus token instead.',
    ]),
    ('tactician', [
        ':crew: *<http://xwing-miniatures.wikia.com/wiki/Tactician|Tactician>* [2]',
        '_Limited._',
        'After you perform an attack against a ship inside your firing arc at Range 2, that ship receives 1 stress token.',
    ]),
    ('twinionenginemkii', [
        ':modification: *<http://xwing-miniatures.wikia.com/wiki/Twin_Ion_Engine_Mk._II|Twin Ion Engine Mk. II>* [1]',
        '_TIE only._',
        'You may treat all bank maneuvers (:bankleft: or :bankright:) as green maneuvers.',
    ]),
    ('smugglingcompartment', [
        ':modification: *<http://xwing-miniatures.wikia.com/wiki/Smuggling_Compartment|Smuggling Compartment>* [0]',
        '_YT-1300 and YT-2400 only. Limited._',
        'Your upgrade bar gains the :Illicit: upgrade icon.',
        'You may equip 1 additional Modification upgrade that costs 3 or fewer squad points.',
    ]),
    ('gr75mediumtransport.0', [
        ':gr75mediumtransport: *GR-75 Medium Transport*',
        ':energy4::agility0::hull8::shield4: | :recover: :reinforce: :coordinate: :jam: | :crew::crew::cargo::cargo::cargo: | :epic:2',
        '4 :blank::straight::blank:',
        '3 :blank::straight::blank:',
        '2 :bankleft::straight::bankright:',
        '1 :bankleft::straight::bankright:',
        ':rebel: :skill3:<http://xwing-miniatures.wikia.com/wiki/GR-75_Medium_Transport|GR-75 Medium Transport> [30]',
    ]),
    ('gr75mediumtransport.1', [
        ':gr75mediumtransport: *<http://xwing-miniatures.wikia.com/wiki/GR-75_Medium_Transport|GR-75 Medium Transport>* [30]',
        ':rebel: | :skill3::energy4::agility0::hull8::shield4: | :recover: :reinforce: :coordinate: :jam: | :crew::crew::cargo::cargo::cargo: | :epic:2',
    ]),
    ('directhit.0', [
        ':crit: *Direct Hit!* (Original)',
        '_Ship_',
        'This card counts as *2 damage* against your hull.',
    ]),
    pytest.param('directhit.1', [
        ':crit: *Direct Hit!* (TFA)',
        '_Ship_',
        'This card counts as *2 damage* against your hull.',
    ], marks=pytest.mark.xfail),
    ('damagedsensorarray.0', [
        ':crit: *Damaged Sensor Array* (Original)',
        '_Ship_',
        'You cannot perform the actions listed in your action bar.',
        '*Action:* Roll 1 attack die. On a :Hit: results, flip this card facedown.',
    ]),
    ('damagedsensorarray.1', [
        ':crit: *Damaged Sensor Array* (TFA)',
        '_Ship_',
        'You cannot perform any actions except actions listed on Damage cards.',
        '*Action:* Roll 1 attack die. On a :Hit: or :crit: result, flip this card facedown.',
    ]),
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
        ('awingtestpilot', 'Title'), ('sienartestpilot', 'tieadvprototype')],
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
        ('kylorensshuttle', 'Title'),
    ],
}
@pytest.mark.parametrize('lookup, expected', lookup_tests.items())
def test_lookup(testbot, lookup, expected):
    actual = [(card['xws'], card['slot']) for card in testbot.lookup(lookup)]
    assert actual == expected


def test_card_limit(testbot):
    assert testbot.handle_lookup('squadron') == [
        'Your search matched more than 10 cards, please be more specific.']
