import pytest

from r2d7.cardlookup import CardLookup
from r2d7.slackprinter import SlackPrinter

class DummyBot(CardLookup, SlackPrinter):
    pass

print_card_tests = {
    'veteraninstincts': [
        ':elite: *Veteran Instincts* [1]',
        'Increase your pilot skill value by 2.',
    ],
    'tactician': [
        ':crew: *Tactician* [2]',
        '_Limited._',
        'After you perform an attack against a ship inside your firing arc at Range 2, that ship receives 1 stress token.',
    ],
    'rage': [
        ':elite: *Rage* [1]',
        '*Action:* Assign 1 focus token to your ship and receive 2 stress tokens. Until the end of the round, when attacking, you may reroll up to 3 attack dice.',
    ],
    'snapshot': [
        ':elite: *Snap Shot* [2]',
        ':attack::attack2: | Range: 1',
        'After an enemy ship executes a maneuver, you may perform this attack against that ship.\n*Attack:* Attack 1 ship. You cannot modify your attack dice and cannot attack again this phase.',
    ],
    'heavylaserturret': [
        ':hardpoint: *Heavy Laser Turret* [5]',
        ':attack::attack4: | Range: 2-3 | :energy::energy2:',
        '_C-ROC Cruiser only._',
        '*Attack (energy):* Spend 2 energy from this card to perform this attack against 1 ship (even a ship outside of your firing arc).',
    ],
    'brighthope': [
        ':title: • *Bright Hope* [5]',
        #TODO the card actually says +2 (:energyplus2:)
        ':energy::energy2:',
        #TODO the card actually says GR-75 only.
        '_GR-75 Medium Transport only._',
        'A reinforce token assigned to your fore section acts as 2 :Evade: results (instead of one).',
    ],
    'xwing': [
        ':xwing: *X-Wing*',
        ':attack3::agility2::hull3::shield2: | :focus: :targetlock: | :torpedo::astromech:',
        '4 :blank::blank::straight::blank::blank::redkturn:',
        '3 :turnleft::bankleft::straight::bankright::turnright::blank:',
        '2 :turnleft::bankleft::greenstraight::bankright::turnright::blank:',
        '1 :blank::greenbankleft::greenstraight::greenbankright::blank::blank:',
        ':rebel: :skill2:Rookie Pilot [21], :skill3:• Tarn Mison [23], :skill4:Red Squadron Pilot [23], :skill5:• Biggs Darklighter [25], :skill5:• "Hobbie" Klivian [25], :skill6:• Garven Dreis [26], :skill7:• Jek Porkins :elite: [26], :skill8:• Luke Skywalker :elite: [28], :skill8:• Wes Janson :elite: [29], :skill9:• Wedge Antilles :elite: [29]',
    ],
    'firespray31': [
        ':firespray31: *Firespray-31*',
        ':attack3::agility2::hull6::shield4: | :attack-frontback: | :focus: :targetlock: :evade: | :cannon::xbomb::crew::missile:',
        '4 :blank::blank::straight::blank::blank::redkturn:',
        '3 :turnleft::bankleft::straight::bankright::turnright::redkturn:',
        '2 :turnleft::bankleft::greenstraight::bankright::turnright::blank:',
        '1 :blank::greenbankleft::greenstraight::greenbankright::blank::blank:',
        ':empire: :skill3:Bounty Hunter [33], :skill5:• Krassis Trelix [36], :skill7:• Kath Scarlet :elite: [38], :skill8:• Boba Fett :elite: [39]',
        ':scum: :skill5:Mandalorian Mercenary :elite: [35], :skill6:• Emon Azzameen [36], :skill7:• Kath Scarlet :elite: [38], :skill8:• Boba Fett :elite: [39]',
    ],
    'quadjumper': [
        ':quadjumper: *Quadjumper*',
        ':attack2::agility2::hull5::shield0: | :barrelroll: :focus: | :xbomb::crew::illicit::tech:',
        '3 :blank::bankleft::greenstraight::bankright::blank::blank::blank::blank::blank::blank:',
        '2 :turnleft::greenbankleft::greenstraight::greenbankright::turnright::redsloopleft::redsloopright::blank::blank::blank:',
        '1 :turnleft::blank::straight::blank::turnright::blank::blank::redreversebankleft::redreversestraight::redreversebankright:',
        ':scum: :skill1:Jakku Gunrunner [15], :skill3:• Unkar Plutt [17], :skill5:• Sarco Plank :elite: [18], :skill7:• Constable Zuvio :elite: [19]',
    ],
    'yv666': [
        ':yv666: *YV-666*',
        ':attack3::agility1::hull6::shield6: | :attack-180: | :focus: :targetlock: | :cannon::missile::crew::crew::crew::illicit:',
        '4 :blank::blank::straight::blank::blank:',
        '3 :turnleft::bankleft::greenstraight::bankright::turnright:',
        '2 :redturnleft::bankleft::greenstraight::bankright::redturnright:',
        '1 :blank::greenbankleft::greenstraight::greenbankright::blank:',
        '0 :blank::blank::redstop::blank::blank:',
        ':scum: :skill2:Trandoshan Slaver [29], :skill5:• Latts Razzi [33], :skill6:• Moralo Eval [34], :skill7:• Bossk :elite: [35]',
    ],
    'rey': [
        ':yt1300: • *Rey* [45]',
        ':resistance: | :skill8::attack3::agility1::hull8::shield5: | :attack-turret: | :focus: :targetlock: | :elite::missile::crew::crew:',
        'When attacking or defending, if the enemy ship is inside your firing arc, you may reroll up to 2 of your blank results.',
    ],
    'quinnjast': [
        ':m3ainterceptor: • *Quinn Jast* [18]',
        ':scum: | :skill6::attack2::agility3::hull2::shield1: | :focus: :targetlock: :barrelroll: :evade: | :elite:',
        'At the start of the Combat phase, you may receive a weapons disabled token to flip one of your discarded :Torpedo: or :Missile: Upgrade cards faceup.',
    ],
    'countessryad': [
        ':tiedefender: • *Countess Ryad* [34]',
        ':empire: | :skill5::attack3::agility3::hull3::shield3: | :focus: :targetlock: :barrelroll: | :elite::cannon::missile:',
        'When you reveal a :Straight: maneuver, you may treat it as a :kturn: maneuver.',
    ]
}

@pytest.mark.parametrize('name, expected', print_card_tests.items())
def test_print_card(name, expected):
    bot = DummyBot()
    result = list(bot.lookup(name))
    # TODO this is dangerous
    assert bot.print_card(result[0]) == expected


partial_canonicalize_tests = {
    'X-Wing': 'xwing',
    'T-70 X-Wing': 't70xwing',
    'Veteran instincts': 'veteraninstincts',
}
@pytest.mark.parametrize('before, after', partial_canonicalize_tests.items())
def test_partial_canonicalize(before, after):
    assert CardLookup.partial_canonicalize(before) == after
