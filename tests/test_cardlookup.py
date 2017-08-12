import pytest

from r2d7.cardlookup import CardLookup
from r2d7.slackprinter import SlackPrinter

class DummyBot(CardLookup, SlackPrinter):
    pass

print_card_tests = {
    'upgrades.veteraninstincts': [
        ':elite: *Veteran Instincts* [1]',
        'Increase your pilot skill value by 2.',
    ],
    'upgrades.tactician': [
        ':crew: *Tactician* [2]',
        '_Limited._',
        'After you perform an attack against a ship inside your firing arc at Range 2, that ship receives 1 stress token.',
    ],
    'upgrades.rage': [
        ':elite: *Rage* [1]',
        '*Action:* Assign 1 focus token to your ship and receive 2 stress tokens. Until the end of the round, when attacking, you may reroll up to 3 attack dice.',
    ],
    'upgrades.snapshot': [
        ':elite: *Snap Shot* [2]',
        ':attack::attack2: | Range: 1',
        'After an enemy ship executes a maneuver, you may perform this attack against that ship.\n*Attack:* Attack 1 ship. You cannot modify your attack dice and cannot attack again this phase.',
    ],
    'upgrades.heavylaserturret': [
        ':hardpoint: *Heavy Laser Turret* [5]',
        ':attack::attack4: | Range: 2-3 | :energy::energy2:',
        '_C-ROC Cruiser only._',
        '*Attack (energy):* Spend 2 energy from this card to perform this attack against 1 ship (even a ship outside of your firing arc).',
    ],
    'upgrades.brighthope': [
        ':title: • *Bright Hope* [5]',
        #TODO the card actually says +2 (:energyplus2:)
        ':energy::energy2:',
        #TODO the card actually says GR-75 only.
        '_GR-75 Medium Transport only._',
        'A reinforce token assigned to your fore section acts as 2 :Evade: results (instead of one).',
    ]
    # 'firespray31': [
    #     ':firespray31: *Firespray-31*',
    #     ':attack3::agility2::hull6::shield4: | :attack-frontback: | :focus: :targetlock: :evade: | :cannon::xbomb::crew::missile:',
    #     '4 :blank::blank::straight::blank::blank::redkturn:',
    #     '3 :turnleft::bankleft::straight::bankright::turnright::redkturn:',
    #     '2 :turnleft::bankleft::greenstraight::bankright::turnright::blank:',
    #     '1 :blank::greenbankleft::greenstraight::greenbankright::blank::blank:',
    #     ':empire: :skill3:Bounty Hunter [33], :skill5:• Krassis Trelix [36], :skill7:• Kath Scarlet :elite: [38], :skill8:• Boba Fett :elite: [39]',
    #     ':scum: :skill5:Mandalorian Mercenary :elite: [35], :skill6:• Emon Azzameen [36], :skill7:• Kath Scarlet :elite: [38], :skill8:• Boba Fett :elite: [39]',
    # ]
}

@pytest.mark.parametrize('name, expected', print_card_tests.items())
def test_print_card(name, expected):
    bot = DummyBot()
    kind, name = name.split('.')
    assert bot.print_card(bot.data[kind][name]) == expected


partial_canonicalize_tests = {
    'X-Wing': 'xwing',
    'T-70 X-Wing': 't70xwing',
    'Veteran instincts': 'veteraninstincts',
}
@pytest.mark.parametrize('before, after', partial_canonicalize_tests.items())
def test_partial_canonicalize(before, after):
    assert CardLookup.partial_canonicalize(before) == after
