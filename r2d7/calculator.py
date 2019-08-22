from enum import IntEnum
import requests

# These classes are designd to interface with http://xwing.gateofstorms.net/2/multi/
# For more info see https://github.com/punkUser/xwing_math/blob/master/source/
# Or run chrome inspector on the calculator site and look at simulate.json in network tab

# enums taken from https://github.com/punkUser/xwing_math/blob/master/source/form.d
class AttackPilot(IntEnum):
    none = 0
    leebo = 1
    sharaBey = 2
    reroll_1 = 3         # Boba/Horton w/ 1 reroll
    reroll_2 = 4         # Boba/Horton w/ 2 rerolls
    reroll_3 = 5         # Boba/Horton w/ 3 rerolls
    gavinDarklighter = 6
    majorVermeil = 7
    rearAdmiralChiraneau = 8
    ezraBridger = 9
    landoCalrissianScum = 10
    hanSoloRebel = 11
    rey = 12
    finnPod_Blank = 13    # Add blank
    finnPod_Focus = 14    # Add focus

class DefensePilot(IntEnum):
    none = 0
    leebo = 1
    norraWexley = 2
    lukeSkywalker = 3
    sharaBey = 4
    reroll_1 = 5         # Boba/Horton w/ 1 reroll
    reroll_2 = 6         # Boba/Horton w/ 2 rerolls
    reroll_3 = 7         # Boba/Horton w/ 3 rerolls
    zebOrrelios = 8
    captainFeroph = 9
    sabineWrenLancer = 10
    laetinAshera = 11
    ezraBridger = 12
    landoCalrissianScum = 13
    hanSoloRebel = 14
    rey = 15
    finnPod_Blank = 16    # Add blank
    finnPod_Focus = 17    # Add focus

class AttackShip(IntEnum):
    none = 0
    advancedTargetingComputer = 1
    calibratedLaserTargeting = 2

class DefenseShip(IntEnum):
    none = 0
    concordiaFaceoff = 1

class CalculatorForm(dict):
    # the calculator will silently limit inputs to these maximum values
    max_dice = 7
    max_tokens = 7 # all the basic tokens except reinforce and target lock
    max_reinforce = 1
    max_lock = 1

class AttackForm(CalculatorForm):
    """
    All fields required to define the "attack" part of a roll for the calculator
    This class is meant to be sent to the calculator as a json object
    Create the json by calling vars() on an instance of this class
    """
    def __init__(self, dice = 0, focus = 0, calculate = 0, evade = 0, reinforce = 0,
            lock = 0, force = 0, reroll = 0, all_hits = False):
        # mandatory fields
        self.enabled = 'on'
        self.dice = str(min(dice, self.max_dice))
        self.focus_count = str(min(focus, self.max_tokens))
        self.calculate_count = str(min(calculate, self.max_tokens))
        self.evade_count = str(min(evade, self.max_tokens))
        self.reinforce_count = str(min(reinforce, self.max_tokens))
        self.stress_count = '0'
        self.lock_count = str(min(lock, self.max_lock))
        self.force_count = str(min(force, self.max_tokens))
        self.max_force_count = self.force_count
        self.defense_dice_diff = '0'
        self.stress_count = '0'
        self.pilot = '0'
        self.ship = '0'
        if (reroll != 0):
            self.set_reroll(reroll)
        # optional fields (default to "off")
        self.roll_all_hits = 'on' if all_hits else 'off'
        self.howlrunner = 'off'
        self.saw_gerrera_pilot = 'off'
        self.fanatical = 'off'
        self.fearless = 'off'
        self.heroic = 'off'
        self.juke = 'off'
        self.lone_wolf = 'off'
        self.marksmanship = 'off'
        self.predator = 'off'
        self.predictive_shot = 'off'
        self.saturation_salvo = 'off'
        self.agent_kallus = 'off'
        self.finn_gunner = 'off'
        self.scum_lando_crew = 'off'
        self.saw_gerrera_crew = 'off'
        self.zuckuss_crew = 'off'
        self.advanced_optics = 'off'
        self.fire_control_system = 'off'
        # secondary weapons (max. 1 may be on)
        self.heavy_laser_cannon = 'off'
        self.ion_weapon = 'off'
        self.plasma_torpedoes = 'off'
        self.proton_torpedoes = 'off'

    def set_reroll(self, reroll):
        if reroll == 0:
            self.pilot = 0
        elif reroll == 1:
            self.pilot = AttackPilot.reroll_1
        elif reroll == 2:
            self.pilot = AttackPilot.reroll_2
        elif reroll == 3:
            self.pilot = AttackPilot.reroll_3

class DefenseForm(CalculatorForm):
    """
    All fields required to define the "defense" part of the roll for the calculator
    This class is meant to be sent to the calculator as a json object
    Create the json by calling vars() on an instance of this class
    """
    def __init__(self, dice = 0, focus = 0, calculate = 0, evade = 0, reinforce = 0,
            lock = 0, force = 0, reroll = 0):
        # mandatory fields
        self.dice = str(min(dice, self.max_dice))
        self.focus_count = str(min(focus, self.max_tokens))
        self.calculate_count = str(min(calculate, self.max_tokens))
        self.evade_count = str(min(evade, self.max_tokens))
        self.reinforce_count = str(min(reinforce, self.max_tokens))
        self.stress_count = '0'
        self.lock_count = str(min(lock, self.max_lock))
        self.force_count = str(min(force, self.max_tokens))
        self.max_force_count = self.force_count
        self.pilot = '0'
        self.ship = '0'
        if (reroll != 0):
            self.set_reroll(reroll)
        # optional fields (default to "off")
        self.biggs = 'off'
        self.iden = 'off'
        self.selfless = 'off'
        self.serissu = 'off'
        self.brilliant_evasion = 'off'
        self.elusive = 'off'
        self.hate = 'off'
        self.heroic = 'off'
        self.lone_wolf = 'off'
        self.c3p0 = 'off'
        self.finn_gunner = 'off'
        self.l337 = 'off'
        self.scum_lando_crew = 'off'
        self.rebel_millennium_falcon = 'off'
        self.stealth_device = 'off'

    def set_reroll(self, reroll):
        if reroll == 0:
            self.pilot = 0
        elif reroll == 1:
            self.pilot = DefensePilot.reroll_1
        elif reroll == 2:
            self.pilot = DefensePilot.reroll_2
        elif reroll == 3:
            self.pilot = DefensePilot.reroll_3

class CalculatorError(Exception):
    pass

class Calculator(object):
    """
    This class handles json objects and sends them off to the calculator
    It also parses results from the calculator
    Note that calculate() can raise errors
    """
    _json_url = 'http://xwing.gateofstorms.net/2/multi/simulate.json'
    _human_url = 'http://xwing.gateofstorms.net/2/multi/'

    def __init__(self, attack_form = AttackForm(), defense_form = DefenseForm()):
        self.attack_form = attack_form
        self.defense_form = defense_form
        self.result = None
        self.url = self._human_url

    def calculate(self):
        payload = {}
        payload['simulate'] = {}
        payload['attack0'] = vars(self.attack_form)
        payload['defense'] = vars(self.defense_form)
        result = requests.post(self._json_url, json=payload)
        if result.ok:
            output = result.json()
            self.result = output['results'][0]
            query_string = output['form_state_string']
            self.url = self._human_url + '?' + query_string
        else:
            raise CalculatorError(f'Calculator failed with code {result.status_code}: {result.text}')

    def expected_hits(self):
        if self.result == None:
            self.calculate()
        return self.result['expected_total_hits']

    def crit_chance(self):
        if self.result == None:
            self.calculate()
        return self.result['at_least_one_crit']

