from enum import Enum
import struct
import ctypes
import base64
import urllib.request
import urllib.parse

# These classes are designd to interface with http://xwing.gateofstorms.net/2/multi/
# Structs etc are taken from https://github.com/punkUser/xwing_math/blob/master/source/

# see form.d for enums, encoding process, etc
class AttackPilot(Enum):
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

class DefencePilot(Enum):
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

class AttackShip(Enum):
    none = 0
    advancedTargetingComputer = 1
    calibratedLaserTargeting = 2

class DefenceShip(Enum):
    none = 0
    concordiaFaceoff = 1

class Form(object):
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

    def pack(self):
        return struct.pack('QB',self.data1.as_data, self.data2.as_data)

    def encode(self):
        return base64.b64encode(self.pack())

class Calculator(object):
    _url = 'http://xwing.gateofstorms.net/2/multi/'

    def __init__(self, attack_form, defence_form=Form(DefenceFormData1(), DefenceFormData2())):
        self.attack_form = attack_form
        self.defence_form = defence_form

    def calculate(self):
        attack_string = self.attack_form.encode()
        defence_string = self.defence_form.encode()



# see attack_form.d
class AttackFormBits1(ctypes.LittleEndianStructure):
    _fields_ = [
            ("enabled", c_uint8, 1),
            ("lock_count", c_uint8, 3),
            ("dice", c_uint8, 4), #8
            ("force_count", c_uint8, 3),
            ("focus_count", c_uint8, 3),
            ("calculate_count", c_uint8, 3),
            ("evade_count", c_uint8, 3),
            ("reinforce_count", c_uint8, 3),
            ("stress_count", c_uint8, 3),
            ("jam_count", c_uint8, 3),
            ("fire_control_system", c_uint8, 1),
            ("heavy_laser_cannon", c_uint8, 1),
            ("proton_torpedoes", c_uint8, 1), #32
            ("pilot", c_uint8, 6), # AttackPilot enum
            ("predator", c_uint8, 1),
            ("ion_weapon", c_uint8, 1), #40
            ("juke", c_uint8, 1),
            ("roll_all_hits", c_uint8, 1),
            ("howlrunner", c_uint8, 1),
            ("lone_wolf", c_uint8, 1),
            ("marksmanship", c_uint8, 1),
            ("defense_dice_diff", c_uint8, 4),
            ("fearless", c_uint8, 1),
            ("ship", c_uint8, 6), # AttackShip enum
            ("saw_gerrera_pilot", c_uint8, 1),
            ("scum_lando_crew", c_uint8, 1),
            ("agent_kallus", c_uint8, 1),
            ("finn_gunner", c_uint8, 1),
            ("fanatical", c_uint8, 1),
            ("heroic", c_uint8, 1),
            ("advanced_optics", c_uint8, 1),
            ("predictive_shot", c_uint8, 1), #64
        ]

class AttackFormData1(ctypes.Union):
    _fields_ = [("bits", AttackFormBits1),
                ("as_data", c_uint64)]

class AttackFormBits2(ctypes.LittleEndianStructure):
    _fields_ = [
            ("zuckuss_crew", c_uint8, 1),
            ("saturation_salvo", c_uint8, 1),
            ("previous_tokens_enabled", c_uint8, 1),
            ("plasma_torpedoes", c_uint8, 1),
            ("saw_gerrera_crew", c_uint8, 1),
            ("_unused", c_uint8, 3), #8
        ]

class AttackFormData2(ctypes.Union):
    _fields_ = [("bits", AttackFormBits2),
                ("as_data", c_uint8)]

# see defense_form.d
class DefenceFormBits1(ctypes.LittleEndianStructure):
    _fields_ = [
            ("dice", c_uint8, 4),
            ("force_count", c_uint8, 3),
            ("focus_count", c_uint8, 3),
            ("calculate_count", c_uint8, 3),
            ("evade_count", c_uint8, 3),
            ("reinforce_count", c_uint8, 3),
            ("stress_count", c_uint8, 3),
            ("jam_count", c_uint8, 3),
            ("c3p0", c_uint8, 1),
            ("lone_wolf", c_uint8, 1),
            ("stealth_device", c_uint8, 1),
            ("biggs", c_uint8, 1),
            ("_unused1", c_uint8, 1),
            ("iden", c_uint8, 1),
            ("selfless", c_uint8, 1), #32
            ("pilot", c_uint8, 6), # DefensePilot enum
            ("l337", c_uint8, 1),
            ("elusive", c_uint8, 1), #40
            ("lock_count", c_uint8, 3),
            ("scum_lando_crew", c_uint8, 1),
            ("ship", c_uint8, 6), # DefenseShip enum
            ("serissu", c_uint8, 1),
            ("rebel_millennium_falcon", c_uint8, 1),
            ("finn_gunner", c_uint8, 1),
            ("heroic", c_uint8, 1),
            ("ship_hull", c_uint8, 5), # 0..31
            ("ship_shields", c_uint8, 5), # 0..31 #64
        ]

class DefenceFormData1(ctypes.Union):
    _fields_ = [("bits", DefenceFormBits1),
                ("as_data", c_uint64)]

class DefenceFormBits2(ctypes.LittleEndianStructure):
    _fields_ = [
            ("brilliant_evasion", c_uint8, 1),
            ("max_force_count", c_uint8, 3),
            ("hate", c_uint8, 1),
            ("_unused", c_uint8, 3), #8
        ]

class DefenceFormData2(ctypes.Union):
    _fields_ = [("bits", DefenceFormBits2),
                ("as_data", c_uint8)]

