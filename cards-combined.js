exportObj = typeof exports !== "undefined" && exports !== null ? exports : this;

exportObj.unreleasedExpansions = ["Imperial Veterans Expansion Pack", "Heroes of the Resistance Expansion Pack", "ARC-170 Expansion Pack", "Special Forces TIE Expansion Pack", "Protectorate Starfighter Expansion Pack", "Shadow Caster Expansion Pack"];

exportObj.isReleased = function(data) {
  var source, _i, _len, _ref;
  _ref = data.sources;
  for (_i = 0, _len = _ref.length; _i < _len; _i++) {
    source = _ref[_i];
    if (__indexOf.call(exportObj.unreleasedExpansions, source) < 0) {
      return true;
    }
  }
  return false;
};

String.prototype.canonicalize = function() {
  return this.toLowerCase().replace(/[^a-z0-9]/g, '').replace(/\s+/g, '-');
};

exportObj.hugeOnly = function(ship) {
  var _ref;
  return (_ref = ship.data.huge) != null ? _ref : false;
};

exportObj.basicCardData = function() {
  return {
    ships: {
      "X-Wing": {
        name: "X-Wing",
        factions: ["Rebel Alliance"],
        attack: 3,
        agility: 2,
        hull: 3,
        shields: 2,
        actions: ["Focus", "Target Lock"],
        maneuvers: [[0, 0, 0, 0, 0, 0], [0, 2, 2, 2, 0, 0], [1, 1, 2, 1, 1, 0], [1, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 3]]
      },
      "Y-Wing": {
        name: "Y-Wing",
        factions: ["Rebel Alliance", "Scum and Villainy"],
        attack: 2,
        agility: 1,
        hull: 5,
        shields: 3,
        actions: ["Focus", "Target Lock"],
        maneuvers: [[0, 0, 0, 0, 0, 0], [0, 1, 2, 1, 0, 0], [1, 1, 2, 1, 1, 0], [3, 1, 1, 1, 3, 0], [0, 0, 3, 0, 0, 3]]
      },
      "A-Wing": {
        name: "A-Wing",
        factions: ["Rebel Alliance"],
        attack: 2,
        agility: 3,
        hull: 2,
        shields: 2,
        actions: ["Focus", "Target Lock", "Boost", "Evade"],
        maneuvers: [[0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0], [2, 2, 2, 2, 2, 0], [1, 1, 2, 1, 1, 3], [0, 0, 2, 0, 0, 0], [0, 0, 2, 0, 0, 3]]
      },
      "YT-1300": {
        name: "YT-1300",
        factions: ["Rebel Alliance"],
        attack: 2,
        agility: 1,
        hull: 6,
        shields: 4,
        actions: ["Focus", "Target Lock"],
        attack_icon: 'xwing-miniatures-font-attack-turret',
        maneuvers: [[0, 0, 0, 0, 0, 0], [1, 2, 2, 2, 1, 0], [1, 1, 2, 1, 1, 0], [0, 1, 1, 1, 0, 3], [0, 0, 1, 0, 0, 3]],
        large: true
      },
      "TIE Fighter": {
        name: "TIE Fighter",
        factions: ["Galactic Empire"],
        attack: 2,
        agility: 3,
        hull: 3,
        shields: 0,
        actions: ["Focus", "Barrel Roll", "Evade"],
        maneuvers: [[0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0], [1, 2, 2, 2, 1, 0], [1, 1, 2, 1, 1, 3], [0, 0, 1, 0, 0, 3], [0, 0, 1, 0, 0, 0]]
      },
      "TIE Advanced": {
        name: "TIE Advanced",
        factions: ["Galactic Empire"],
        attack: 2,
        agility: 3,
        hull: 3,
        shields: 2,
        actions: ["Focus", "Target Lock", "Barrel Roll", "Evade"],
        maneuvers: [[0, 0, 0, 0, 0, 0], [0, 2, 0, 2, 0, 0], [1, 1, 2, 1, 1, 0], [1, 1, 2, 1, 1, 0], [0, 0, 1, 0, 0, 3], [0, 0, 1, 0, 0, 0]]
      },
      "TIE Interceptor": {
        name: "TIE Interceptor",
        factions: ["Galactic Empire"],
        attack: 3,
        agility: 3,
        hull: 3,
        shields: 0,
        actions: ["Focus", "Barrel Roll", "Boost", "Evade"],
        maneuvers: [[0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0], [2, 2, 2, 2, 2, 0], [1, 1, 2, 1, 1, 3], [0, 0, 2, 0, 0, 0], [0, 0, 1, 0, 0, 3]]
      },
      "Firespray-31": {
        name: "Firespray-31",
        factions: ["Galactic Empire", "Scum and Villainy"],
        attack: 3,
        agility: 2,
        hull: 6,
        shields: 4,
        actions: ["Focus", "Target Lock", "Evade"],
        attack_icon: 'xwing-miniatures-font-attack-frontback',
        maneuvers: [[0, 0, 0, 0, 0, 0], [0, 2, 2, 2, 0, 0], [1, 1, 2, 1, 1, 0], [1, 1, 1, 1, 1, 3], [0, 0, 1, 0, 0, 3]],
        large: true
      },
      "HWK-290": {
        name: "HWK-290",
        factions: ["Rebel Alliance", "Scum and Villainy"],
        attack: 1,
        agility: 2,
        hull: 4,
        shields: 1,
        actions: ["Focus", "Target Lock"],
        maneuvers: [[0, 0, 0, 0, 0], [0, 2, 2, 2, 0], [1, 1, 2, 1, 1], [0, 3, 1, 3, 0], [0, 0, 3, 0, 0]]
      },
      "Lambda-Class Shuttle": {
        name: "Lambda-Class Shuttle",
        factions: ["Galactic Empire"],
        attack: 3,
        agility: 1,
        hull: 5,
        shields: 5,
        actions: ["Focus", "Target Lock"],
        maneuvers: [[0, 0, 3, 0, 0], [0, 2, 2, 2, 0], [3, 1, 2, 1, 3], [0, 3, 1, 3, 0]],
        large: true
      },
      "B-Wing": {
        name: "B-Wing",
        factions: ["Rebel Alliance"],
        attack: 3,
        agility: 1,
        hull: 3,
        shields: 5,
        actions: ["Focus", "Target Lock", "Barrel Roll"],
        maneuvers: [[0, 0, 0, 0, 0, 0], [3, 2, 2, 2, 3, 0], [1, 1, 2, 1, 1, 3], [0, 3, 1, 3, 0, 0], [0, 0, 3, 0, 0, 0]]
      },
      "TIE Bomber": {
        name: "TIE Bomber",
        factions: ["Galactic Empire"],
        attack: 2,
        agility: 2,
        hull: 6,
        shields: 0,
        actions: ["Focus", "Target Lock", "Barrel Roll"],
        maneuvers: [[0, 0, 0, 0, 0, 0], [0, 1, 2, 1, 0, 0], [3, 2, 2, 2, 3, 0], [1, 1, 2, 1, 1, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 3]]
      },
      "GR-75 Medium Transport": {
        name: "GR-75 Medium Transport",
        factions: ["Rebel Alliance"],
        energy: 4,
        agility: 0,
        hull: 8,
        shields: 4,
        actions: ["Recover", "Reinforce", "Coordinate", "Jam"],
        huge: true,
        epic_points: 2,
        maneuvers: [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0]]
      },
      "Z-95 Headhunter": {
        name: "Z-95 Headhunter",
        factions: ["Rebel Alliance", "Scum and Villainy"],
        attack: 2,
        agility: 2,
        hull: 2,
        shields: 2,
        actions: ["Focus", "Target Lock"],
        maneuvers: [[0, 0, 0, 0, 0, 0], [0, 1, 2, 1, 0, 0], [1, 2, 2, 2, 1, 0], [1, 1, 1, 1, 1, 3], [0, 0, 1, 0, 0, 0]]
      },
      "TIE Defender": {
        name: "TIE Defender",
        factions: ["Galactic Empire"],
        attack: 3,
        agility: 3,
        hull: 3,
        shields: 3,
        actions: ["Focus", "Target Lock", "Barrel Roll"],
        maneuvers: [[0, 0, 0, 0, 0, 0], [3, 1, 0, 1, 3, 0], [3, 1, 2, 1, 3, 0], [1, 1, 2, 1, 1, 0], [0, 0, 2, 0, 0, 1], [0, 0, 2, 0, 0, 0]]
      },
      "E-Wing": {
        name: "E-Wing",
        factions: ["Rebel Alliance"],
        attack: 3,
        agility: 3,
        hull: 2,
        shields: 3,
        actions: ["Focus", "Target Lock", "Barrel Roll", "Evade"],
        maneuvers: [[0, 0, 0, 0, 0, 0], [0, 1, 2, 1, 0, 0], [1, 2, 2, 2, 1, 0], [1, 1, 2, 1, 1, 3], [0, 0, 1, 0, 0, 3], [0, 0, 1, 0, 0, 0]]
      },
      "TIE Phantom": {
        name: "TIE Phantom",
        factions: ["Galactic Empire"],
        attack: 4,
        agility: 2,
        hull: 2,
        shields: 2,
        actions: ["Focus", "Barrel Roll", "Evade", "Cloak"],
        maneuvers: [[0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0], [1, 2, 2, 2, 1, 0], [1, 1, 2, 1, 1, 3], [0, 0, 1, 0, 0, 3]]
      },
      "CR90 Corvette (Fore)": {
        name: "CR90 Corvette (Fore)",
        factions: ["Rebel Alliance"],
        attack: 4,
        agility: 0,
        hull: 8,
        shields: 5,
        actions: ["Coordinate", "Target Lock"],
        huge: true,
        epic_points: 1.5,
        attack_icon: 'xwing-miniatures-font-attack-turret',
        maneuvers: [[0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0], [0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0]],
        multisection: ["CR90 Corvette (Aft)".canonicalize()],
        canonical_name: "CR90 Corvette".canonicalize()
      },
      "CR90 Corvette (Aft)": {
        name: "CR90 Corvette (Aft)",
        factions: ["Rebel Alliance"],
        energy: 5,
        agility: 0,
        hull: 8,
        shields: 3,
        actions: ["Reinforce", "Recover"],
        huge: true,
        epic_points: 1.5,
        maneuvers: [[0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0], [0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0]],
        multisection: ["CR90 Corvette (Fore)".canonicalize()],
        canonical_name: "CR90 Corvette".canonicalize()
      },
      "YT-2400": {
        name: "YT-2400",
        canonical_name: "YT-2400 Freighter".canonicalize(),
        factions: ["Rebel Alliance"],
        attack: 2,
        agility: 2,
        hull: 5,
        shields: 5,
        actions: ["Focus", "Target Lock", "Barrel Roll"],
        large: true,
        attack_icon: 'xwing-miniatures-font-attack-turret',
        maneuvers: [[0, 0, 0, 0, 0, 0], [1, 2, 2, 2, 1, 0], [1, 1, 2, 1, 1, 0], [1, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 3]]
      },
      "VT-49 Decimator": {
        name: "VT-49 Decimator",
        factions: ["Galactic Empire"],
        attack: 3,
        agility: 0,
        hull: 12,
        shields: 4,
        actions: ["Focus", "Target Lock"],
        large: true,
        attack_icon: 'xwing-miniatures-font-attack-turret',
        maneuvers: [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0], [1, 2, 2, 2, 1, 0], [1, 1, 2, 1, 1, 0], [0, 0, 1, 0, 0, 0]]
      },
      "StarViper": {
        name: "StarViper",
        factions: ["Scum and Villainy"],
        attack: 3,
        agility: 3,
        hull: 4,
        shields: 1,
        actions: ["Focus", "Target Lock", "Barrel Roll", "Boost"],
        maneuvers: [[0, 0, 0, 0, 0, 0, 0, 0], [1, 2, 2, 2, 1, 0, 0, 0], [1, 1, 2, 1, 1, 0, 0, 0], [0, 1, 2, 1, 0, 0, 3, 3], [0, 0, 1, 0, 0, 0, 0, 0]]
      },
      "M3-A Interceptor": {
        name: "M3-A Interceptor",
        factions: ["Scum and Villainy"],
        attack: 2,
        agility: 3,
        hull: 2,
        shields: 1,
        actions: ["Focus", "Target Lock", "Barrel Roll", "Evade"],
        maneuvers: [[0, 0, 0, 0, 0, 0], [1, 2, 0, 2, 1, 0], [1, 2, 2, 2, 1, 0], [0, 1, 2, 1, 0, 3], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 3]]
      },
      "Aggressor": {
        name: "Aggressor",
        factions: ["Scum and Villainy"],
        attack: 3,
        agility: 3,
        hull: 4,
        shields: 4,
        actions: ["Focus", "Target Lock", "Boost", "Evade"],
        large: true,
        maneuvers: [[0, 0, 0, 0, 0, 0, 0, 0], [1, 2, 2, 2, 1, 0, 0, 0], [1, 2, 2, 2, 1, 0, 0, 0], [0, 2, 2, 2, 0, 0, 3, 3], [0, 0, 0, 0, 0, 3, 0, 0]]
      },
      "Raider-class Corvette (Fore)": {
        name: "Raider-class Corvette (Fore)",
        factions: ["Galactic Empire"],
        attack: 4,
        agility: 0,
        hull: 8,
        shields: 6,
        actions: ["Recover", "Reinforce"],
        huge: true,
        epic_points: 1.5,
        maneuvers: [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0]]
      },
      "Raider-class Corvette (Aft)": {
        name: "Raider-class Corvette (Aft)",
        factions: ["Galactic Empire"],
        energy: 6,
        agility: 0,
        hull: 8,
        shields: 4,
        actions: ["Coordinate", "Target Lock"],
        huge: true,
        epic_points: 1.5,
        maneuvers: [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0]]
      },
      "YV-666": {
        name: "YV-666",
        factions: ["Scum and Villainy"],
        attack: 3,
        agility: 1,
        hull: 6,
        shields: 6,
        large: true,
        actions: ["Focus", "Target Lock"],
        attack_icon: 'xwing-miniatures-font-attack-180',
        maneuvers: [[0, 0, 3, 0, 0, 0], [0, 2, 2, 2, 0, 0], [3, 1, 2, 1, 3, 0], [1, 1, 2, 1, 1, 0], [0, 0, 1, 0, 0, 0]]
      },
      "Kihraxz Fighter": {
        name: "Kihraxz Fighter",
        factions: ["Scum and Villainy"],
        attack: 3,
        agility: 2,
        hull: 4,
        shields: 1,
        actions: ["Focus", "Target Lock"],
        maneuvers: [[0, 0, 0, 0, 0, 0], [1, 2, 0, 2, 1, 0], [1, 2, 2, 2, 1, 0], [0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 3], [0, 0, 0, 0, 0, 3]]
      },
      "K-Wing": {
        name: "K-Wing",
        factions: ["Rebel Alliance"],
        attack: 2,
        agility: 1,
        hull: 5,
        shields: 4,
        actions: ["Focus", "Target Lock", "SLAM"],
        attack_icon: 'xwing-miniatures-font-attack-turret',
        maneuvers: [[0, 0, 0, 0, 0, 0], [0, 2, 2, 2, 0, 0], [1, 1, 2, 1, 1, 0], [0, 1, 1, 1, 0, 0]]
      },
      "TIE Punisher": {
        name: "TIE Punisher",
        factions: ["Galactic Empire"],
        attack: 2,
        agility: 1,
        hull: 6,
        shields: 3,
        actions: ["Focus", "Target Lock", "Boost"],
        maneuvers: [[0, 0, 0, 0, 0, 0], [0, 2, 2, 2, 0, 0], [3, 1, 2, 1, 3, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 3]]
      },
      "Gozanti-class Cruiser": {
        name: "Gozanti-class Cruiser",
        factions: ["Galactic Empire"],
        energy: 4,
        agility: 0,
        hull: 9,
        shields: 5,
        huge: true,
        epic_points: 2,
        actions: ["Recover", "Reinforce", "Coordinate", "Target Lock"],
        maneuvers: [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0]]
      },
      "VCX-100": {
        name: "VCX-100",
        factions: ["Rebel Alliance"],
        attack: 4,
        agility: 0,
        hull: 10,
        shields: 6,
        large: true,
        actions: ["Focus", "Target Lock", "Evade"],
        maneuvers: [[0, 0, 0, 0, 0, 0], [3, 1, 2, 1, 3, 0], [1, 2, 2, 2, 1, 0], [3, 1, 1, 1, 3, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 3]]
      },
      "Attack Shuttle": {
        name: "Attack Shuttle",
        factions: ["Rebel Alliance"],
        attack: 3,
        agility: 2,
        hull: 2,
        shields: 2,
        actions: ["Focus", "Barrel Roll", "Evade"],
        maneuvers: [[0, 0, 0, 0, 0, 0], [3, 2, 2, 2, 3, 0], [1, 1, 2, 1, 1, 0], [3, 1, 1, 1, 3, 0], [0, 0, 1, 0, 0, 3]]
      },
      "TIE Advanced Prototype": {
        name: "TIE Advanced Prototype",
        canonical_name: 'TIE Adv. Prototype'.canonicalize(),
        factions: ["Galactic Empire"],
        attack: 2,
        agility: 3,
        hull: 2,
        shields: 2,
        actions: ["Focus", "Target Lock", "Barrel Roll", "Boost"],
        maneuvers: [[0, 0, 0, 0, 0, 0], [2, 2, 0, 2, 2, 0], [1, 1, 2, 1, 1, 0], [1, 1, 2, 1, 1, 0], [0, 0, 2, 0, 0, 3], [0, 0, 1, 0, 0, 0]]
      },
      "G-1A Starfighter": {
        name: "G-1A Starfighter",
        factions: ["Scum and Villainy"],
        attack: 3,
        agility: 1,
        hull: 4,
        shields: 4,
        actions: ["Focus", "Target Lock", "Evade"],
        maneuvers: [[0, 0, 0, 0, 0, 0], [3, 2, 2, 2, 3, 0], [1, 1, 2, 1, 1, 0], [0, 3, 2, 3, 0, 3], [0, 0, 1, 0, 0, 3]]
      },
      "JumpMaster 5000": {
        name: "JumpMaster 5000",
        factions: ["Scum and Villainy"],
        large: true,
        attack: 2,
        agility: 2,
        hull: 5,
        shields: 4,
        actions: ["Focus", "Target Lock", "Barrel Roll"],
        attack_icon: 'xwing-miniatures-font-attack-turret',
        maneuvers: [[0, 0, 0, 0, 0, 0, 0, 0], [2, 2, 2, 1, 1, 0, 0, 0], [2, 2, 2, 1, 1, 0, 1, 3], [0, 1, 1, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 3, 0, 0]]
      },
      "T-70 X-Wing": {
        name: "T-70 X-Wing",
        factions: ["Resistance"],
        attack: 3,
        agility: 2,
        hull: 3,
        shields: 3,
        actions: ["Focus", "Target Lock", "Boost"],
        maneuvers: [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 2, 2, 0, 0, 0, 0, 0, 0], [1, 1, 2, 1, 1, 0, 0, 0, 0, 0], [1, 1, 2, 1, 1, 0, 0, 0, 3, 3], [0, 0, 1, 0, 0, 3, 0, 0, 0, 0]]
      },
      "TIE/fo Fighter": {
        name: "TIE/fo Fighter",
        factions: ["First Order"],
        attack: 2,
        agility: 3,
        hull: 3,
        shields: 1,
        actions: ["Focus", "Target Lock", "Barrel Roll", "Evade"],
        maneuvers: [[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0], [2, 2, 2, 2, 2, 0, 3, 3], [1, 1, 2, 1, 1, 0, 0, 0], [0, 0, 1, 0, 0, 3, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0]]
      },
      'ARC-170': {
        name: 'ARC-170',
        factions: ["Rebel Alliance"],
        attack: 2,
        agility: 1,
        hull: 6,
        shields: 3,
        actions: ["Focus", "Target Lock"],
        maneuvers: []
      },
      'TIE/sf Fighter': {
        name: 'TIE/sf Fighter',
        factions: ["Galactic Empire"],
        attack: 2,
        agility: 2,
        hull: 3,
        shields: 3,
        actions: ['Focus', 'Target Lock', 'Barrel Roll'],
        maneuvers: []
      },
      'Protectorate Starfighter': {
        name: 'Protectorate Starfighter',
        factions: ["Scum and Villainy"],
        attack: 3,
        agility: 3,
        hull: 4,
        shields: 0,
        actions: ['Focus', 'Target Lock', 'Barrel Roll', 'Boost'],
        maneuvers: []
      },
      'Lancer-class Pursuit Craft': {
        name: 'Lancer-class Pursuit Craft',
        factions: ["Scum and Villainy"],
        large: true,
        attack: 3,
        agility: 2,
        hull: 7,
        shields: 3,
        actions: ['Focus', 'Target Lock', 'Evade', 'Rotate Arc'],
        maneuvers: []
      }
    },
    pilotsById: [
      {
        name: "Wedge Antilles",
        faction: "Rebel Alliance",
        id: 0,
        unique: true,
        ship: "X-Wing",
        skill: 9,
        points: 29,
        slots: ["Elite", "Torpedo", "Astromech"]
      }, {
        name: "Garven Dreis",
        faction: "Rebel Alliance",
        id: 1,
        unique: true,
        ship: "X-Wing",
        skill: 6,
        points: 26,
        slots: ["Torpedo", "Astromech"]
      }, {
        name: "Red Squadron Pilot",
        faction: "Rebel Alliance",
        id: 2,
        ship: "X-Wing",
        skill: 4,
        points: 23,
        slots: ["Torpedo", "Astromech"]
      }, {
        name: "Rookie Pilot",
        faction: "Rebel Alliance",
        id: 3,
        ship: "X-Wing",
        skill: 2,
        points: 21,
        slots: ["Torpedo", "Astromech"]
      }, {
        name: "Biggs Darklighter",
        faction: "Rebel Alliance",
        id: 4,
        unique: true,
        ship: "X-Wing",
        skill: 5,
        points: 25,
        slots: ["Torpedo", "Astromech"]
      }, {
        name: "Luke Skywalker",
        faction: "Rebel Alliance",
        id: 5,
        unique: true,
        ship: "X-Wing",
        skill: 8,
        points: 28,
        slots: ["Elite", "Torpedo", "Astromech"]
      }, {
        name: "Gray Squadron Pilot",
        faction: "Rebel Alliance",
        id: 6,
        ship: "Y-Wing",
        skill: 4,
        points: 20,
        slots: ["Turret", "Torpedo", "Torpedo", "Astromech"]
      }, {
        name: '"Dutch" Vander',
        faction: "Rebel Alliance",
        id: 7,
        unique: true,
        ship: "Y-Wing",
        skill: 6,
        points: 23,
        slots: ["Turret", "Torpedo", "Torpedo", "Astromech"]
      }, {
        name: "Horton Salm",
        faction: "Rebel Alliance",
        id: 8,
        unique: true,
        ship: "Y-Wing",
        skill: 8,
        points: 25,
        slots: ["Turret", "Torpedo", "Torpedo", "Astromech"]
      }, {
        name: "Gold Squadron Pilot",
        faction: "Rebel Alliance",
        id: 9,
        ship: "Y-Wing",
        skill: 2,
        points: 18,
        slots: ["Turret", "Torpedo", "Torpedo", "Astromech"]
      }, {
        name: "Academy Pilot",
        faction: "Galactic Empire",
        id: 10,
        ship: "TIE Fighter",
        skill: 1,
        points: 12,
        slots: []
      }, {
        name: "Obsidian Squadron Pilot",
        faction: "Galactic Empire",
        id: 11,
        ship: "TIE Fighter",
        skill: 3,
        points: 13,
        slots: []
      }, {
        name: "Black Squadron Pilot",
        faction: "Galactic Empire",
        id: 12,
        ship: "TIE Fighter",
        skill: 4,
        points: 14,
        slots: ["Elite"]
      }, {
        name: '"Winged Gundark"',
        faction: "Galactic Empire",
        id: 13,
        unique: true,
        ship: "TIE Fighter",
        skill: 5,
        points: 15,
        slots: []
      }, {
        name: '"Night Beast"',
        faction: "Galactic Empire",
        id: 14,
        unique: true,
        ship: "TIE Fighter",
        skill: 5,
        points: 15,
        slots: []
      }, {
        name: '"Backstabber"',
        faction: "Galactic Empire",
        id: 15,
        unique: true,
        ship: "TIE Fighter",
        skill: 6,
        points: 16,
        slots: []
      }, {
        name: '"Dark Curse"',
        faction: "Galactic Empire",
        id: 16,
        unique: true,
        ship: "TIE Fighter",
        skill: 6,
        points: 16,
        slots: []
      }, {
        name: '"Mauler Mithel"',
        faction: "Galactic Empire",
        id: 17,
        unique: true,
        ship: "TIE Fighter",
        skill: 7,
        points: 17,
        slots: ["Elite"]
      }, {
        name: '"Howlrunner"',
        faction: "Galactic Empire",
        id: 18,
        unique: true,
        ship: "TIE Fighter",
        skill: 8,
        points: 18,
        slots: ["Elite"]
      }, {
        name: "Maarek Stele",
        faction: "Galactic Empire",
        id: 19,
        unique: true,
        ship: "TIE Advanced",
        skill: 7,
        points: 27,
        slots: ["Elite", "Missile"]
      }, {
        name: "Tempest Squadron Pilot",
        faction: "Galactic Empire",
        id: 20,
        ship: "TIE Advanced",
        skill: 2,
        points: 21,
        slots: ["Missile"]
      }, {
        name: "Storm Squadron Pilot",
        faction: "Galactic Empire",
        id: 21,
        ship: "TIE Advanced",
        skill: 4,
        points: 23,
        slots: ["Missile"]
      }, {
        name: "Darth Vader",
        faction: "Galactic Empire",
        id: 22,
        unique: true,
        ship: "TIE Advanced",
        skill: 9,
        points: 29,
        slots: ["Elite", "Missile"]
      }, {
        name: "Alpha Squadron Pilot",
        faction: "Galactic Empire",
        id: 23,
        ship: "TIE Interceptor",
        skill: 1,
        points: 18,
        slots: []
      }, {
        name: "Avenger Squadron Pilot",
        faction: "Galactic Empire",
        id: 24,
        ship: "TIE Interceptor",
        skill: 3,
        points: 20,
        slots: []
      }, {
        name: "Saber Squadron Pilot",
        faction: "Galactic Empire",
        id: 25,
        ship: "TIE Interceptor",
        skill: 4,
        points: 21,
        slots: ["Elite"]
      }, {
        name: "\"Fel's Wrath\"",
        faction: "Galactic Empire",
        id: 26,
        unique: true,
        ship: "TIE Interceptor",
        skill: 5,
        points: 23,
        slots: []
      }, {
        name: "Turr Phennir",
        faction: "Galactic Empire",
        id: 27,
        unique: true,
        ship: "TIE Interceptor",
        skill: 7,
        points: 25,
        slots: ["Elite"]
      }, {
        name: "Soontir Fel",
        faction: "Galactic Empire",
        id: 28,
        unique: true,
        ship: "TIE Interceptor",
        skill: 9,
        points: 27,
        slots: ["Elite"]
      }, {
        name: "Tycho Celchu",
        faction: "Rebel Alliance",
        id: 29,
        unique: true,
        ship: "A-Wing",
        skill: 8,
        points: 26,
        slots: ["Elite", "Missile"]
      }, {
        name: "Arvel Crynyd",
        faction: "Rebel Alliance",
        id: 30,
        unique: true,
        ship: "A-Wing",
        skill: 6,
        points: 23,
        slots: ["Missile"]
      }, {
        name: "Green Squadron Pilot",
        faction: "Rebel Alliance",
        id: 31,
        ship: "A-Wing",
        skill: 3,
        points: 19,
        slots: ["Elite", "Missile"]
      }, {
        name: "Prototype Pilot",
        faction: "Rebel Alliance",
        id: 32,
        ship: "A-Wing",
        skill: 1,
        points: 17,
        slots: ["Missile"]
      }, {
        name: "Outer Rim Smuggler",
        faction: "Rebel Alliance",
        id: 33,
        ship: "YT-1300",
        skill: 1,
        points: 27,
        slots: ["Crew", "Crew"]
      }, {
        name: "Chewbacca",
        faction: "Rebel Alliance",
        id: 34,
        unique: true,
        ship: "YT-1300",
        skill: 5,
        points: 42,
        slots: ["Elite", "Missile", "Crew", "Crew"],
        ship_override: {
          attack: 3,
          agility: 1,
          hull: 8,
          shields: 5
        }
      }, {
        name: "Lando Calrissian",
        faction: "Rebel Alliance",
        id: 35,
        unique: true,
        ship: "YT-1300",
        skill: 7,
        points: 44,
        slots: ["Elite", "Missile", "Crew", "Crew"],
        ship_override: {
          attack: 3,
          agility: 1,
          hull: 8,
          shields: 5
        }
      }, {
        name: "Han Solo",
        faction: "Rebel Alliance",
        id: 36,
        unique: true,
        ship: "YT-1300",
        skill: 9,
        points: 46,
        slots: ["Elite", "Missile", "Crew", "Crew"],
        ship_override: {
          attack: 3,
          agility: 1,
          hull: 8,
          shields: 5
        }
      }, {
        name: "Kath Scarlet",
        faction: "Galactic Empire",
        id: 37,
        unique: true,
        ship: "Firespray-31",
        skill: 7,
        points: 38,
        slots: ["Elite", "Cannon", "Bomb", "Crew", "Missile"]
      }, {
        name: "Boba Fett",
        faction: "Galactic Empire",
        id: 38,
        unique: true,
        ship: "Firespray-31",
        skill: 8,
        points: 39,
        slots: ["Elite", "Cannon", "Bomb", "Crew", "Missile"]
      }, {
        name: "Krassis Trelix",
        faction: "Galactic Empire",
        id: 39,
        unique: true,
        ship: "Firespray-31",
        skill: 5,
        points: 36,
        slots: ["Cannon", "Bomb", "Crew", "Missile"]
      }, {
        name: "Bounty Hunter",
        faction: "Galactic Empire",
        id: 40,
        ship: "Firespray-31",
        skill: 3,
        points: 33,
        slots: ["Cannon", "Bomb", "Crew", "Missile"]
      }, {
        name: "Ten Numb",
        faction: "Rebel Alliance",
        id: 41,
        unique: true,
        ship: "B-Wing",
        skill: 8,
        points: 31,
        slots: ["Elite", "System", "Cannon", "Torpedo", "Torpedo"]
      }, {
        name: "Ibtisam",
        faction: "Rebel Alliance",
        id: 42,
        unique: true,
        ship: "B-Wing",
        skill: 6,
        points: 28,
        slots: ["Elite", "System", "Cannon", "Torpedo", "Torpedo"]
      }, {
        name: "Dagger Squadron Pilot",
        faction: "Rebel Alliance",
        id: 43,
        ship: "B-Wing",
        skill: 4,
        points: 24,
        slots: ["System", "Cannon", "Torpedo", "Torpedo"]
      }, {
        name: "Blue Squadron Pilot",
        faction: "Rebel Alliance",
        id: 44,
        ship: "B-Wing",
        skill: 2,
        points: 22,
        slots: ["System", "Cannon", "Torpedo", "Torpedo"]
      }, {
        name: "Rebel Operative",
        faction: "Rebel Alliance",
        id: 45,
        ship: "HWK-290",
        skill: 2,
        points: 16,
        slots: ["Turret", "Crew"]
      }, {
        name: "Roark Garnet",
        faction: "Rebel Alliance",
        id: 46,
        unique: true,
        ship: "HWK-290",
        skill: 4,
        points: 19,
        slots: ["Turret", "Crew"]
      }, {
        name: "Kyle Katarn",
        faction: "Rebel Alliance",
        id: 47,
        unique: true,
        ship: "HWK-290",
        skill: 6,
        points: 21,
        slots: ["Elite", "Turret", "Crew"]
      }, {
        name: "Jan Ors",
        faction: "Rebel Alliance",
        id: 48,
        unique: true,
        ship: "HWK-290",
        skill: 8,
        points: 25,
        slots: ["Elite", "Turret", "Crew"]
      }, {
        name: "Scimitar Squadron Pilot",
        faction: "Galactic Empire",
        id: 49,
        ship: "TIE Bomber",
        skill: 2,
        points: 16,
        slots: ["Torpedo", "Torpedo", "Missile", "Missile", "Bomb"]
      }, {
        name: "Gamma Squadron Pilot",
        faction: "Galactic Empire",
        id: 50,
        ship: "TIE Bomber",
        skill: 4,
        points: 18,
        slots: ["Torpedo", "Torpedo", "Missile", "Missile", "Bomb"]
      }, {
        name: "Captain Jonus",
        faction: "Galactic Empire",
        id: 51,
        unique: true,
        ship: "TIE Bomber",
        skill: 6,
        points: 22,
        slots: ["Elite", "Torpedo", "Torpedo", "Missile", "Missile", "Bomb"]
      }, {
        name: "Major Rhymer",
        faction: "Galactic Empire",
        id: 52,
        unique: true,
        ship: "TIE Bomber",
        skill: 7,
        points: 26,
        slots: ["Elite", "Torpedo", "Torpedo", "Missile", "Missile", "Bomb"]
      }, {
        name: "Captain Kagi",
        faction: "Galactic Empire",
        id: 53,
        unique: true,
        ship: "Lambda-Class Shuttle",
        skill: 8,
        points: 27,
        slots: ["System", "Cannon", "Crew", "Crew"]
      }, {
        name: "Colonel Jendon",
        faction: "Galactic Empire",
        id: 54,
        unique: true,
        ship: "Lambda-Class Shuttle",
        skill: 6,
        points: 26,
        slots: ["System", "Cannon", "Crew", "Crew"]
      }, {
        name: "Captain Yorr",
        faction: "Galactic Empire",
        id: 55,
        unique: true,
        ship: "Lambda-Class Shuttle",
        skill: 4,
        points: 24,
        slots: ["System", "Cannon", "Crew", "Crew"]
      }, {
        name: "Omicron Group Pilot",
        faction: "Galactic Empire",
        id: 56,
        ship: "Lambda-Class Shuttle",
        skill: 2,
        points: 21,
        slots: ["System", "Cannon", "Crew", "Crew"]
      }, {
        name: "Lieutenant Lorrir",
        faction: "Galactic Empire",
        id: 57,
        unique: true,
        ship: "TIE Interceptor",
        skill: 5,
        points: 23,
        slots: []
      }, {
        name: "Royal Guard Pilot",
        faction: "Galactic Empire",
        id: 58,
        ship: "TIE Interceptor",
        skill: 6,
        points: 22,
        slots: ["Elite"]
      }, {
        name: "Tetran Cowall",
        faction: "Galactic Empire",
        id: 59,
        unique: true,
        ship: "TIE Interceptor",
        skill: 7,
        points: 24,
        slots: ["Elite"],
        modifier_func: function(stats) {
          return stats.maneuvers[1][5] = 3;
        }
      }, {
        name: "I messed up this pilot, sorry",
        id: 60,
        skip: true
      }, {
        name: "Kir Kanos",
        faction: "Galactic Empire",
        id: 61,
        unique: true,
        ship: "TIE Interceptor",
        skill: 6,
        points: 24,
        slots: []
      }, {
        name: "Carnor Jax",
        faction: "Galactic Empire",
        id: 62,
        unique: true,
        ship: "TIE Interceptor",
        skill: 8,
        points: 26,
        slots: ["Elite"]
      }, {
        name: "GR-75 Medium Transport",
        faction: "Rebel Alliance",
        id: 63,
        epic: true,
        ship: "GR-75 Medium Transport",
        skill: 3,
        points: 30,
        slots: ["Crew", "Crew", "Cargo", "Cargo", "Cargo"]
      }, {
        name: "Bandit Squadron Pilot",
        faction: "Rebel Alliance",
        id: 64,
        ship: "Z-95 Headhunter",
        skill: 2,
        points: 12,
        slots: ["Missile"]
      }, {
        name: "Tala Squadron Pilot",
        faction: "Rebel Alliance",
        id: 65,
        ship: "Z-95 Headhunter",
        skill: 4,
        points: 13,
        slots: ["Missile"]
      }, {
        name: "Lieutenant Blount",
        faction: "Rebel Alliance",
        id: 66,
        unique: true,
        ship: "Z-95 Headhunter",
        skill: 6,
        points: 17,
        slots: ["Elite", "Missile"]
      }, {
        name: "Airen Cracken",
        faction: "Rebel Alliance",
        id: 67,
        unique: true,
        ship: "Z-95 Headhunter",
        skill: 8,
        points: 19,
        slots: ["Elite", "Missile"]
      }, {
        name: "Delta Squadron Pilot",
        faction: "Galactic Empire",
        id: 68,
        ship: "TIE Defender",
        skill: 1,
        points: 30,
        slots: ["Cannon", "Missile"]
      }, {
        name: "Onyx Squadron Pilot",
        faction: "Galactic Empire",
        id: 69,
        ship: "TIE Defender",
        skill: 3,
        points: 32,
        slots: ["Cannon", "Missile"]
      }, {
        name: "Colonel Vessery",
        faction: "Galactic Empire",
        id: 70,
        unique: true,
        ship: "TIE Defender",
        skill: 6,
        points: 35,
        slots: ["Elite", "Cannon", "Missile"]
      }, {
        name: "Rexler Brath",
        faction: "Galactic Empire",
        id: 71,
        unique: true,
        ship: "TIE Defender",
        skill: 8,
        points: 37,
        slots: ["Elite", "Cannon", "Missile"]
      }, {
        name: "Knave Squadron Pilot",
        faction: "Rebel Alliance",
        id: 72,
        ship: "E-Wing",
        skill: 1,
        points: 27,
        slots: ["System", "Torpedo", "Astromech"]
      }, {
        name: "Blackmoon Squadron Pilot",
        faction: "Rebel Alliance",
        id: 73,
        ship: "E-Wing",
        skill: 3,
        points: 29,
        slots: ["System", "Torpedo", "Astromech"]
      }, {
        name: "Etahn A'baht",
        faction: "Rebel Alliance",
        id: 74,
        unique: true,
        ship: "E-Wing",
        skill: 5,
        points: 32,
        slots: ["Elite", "System", "Torpedo", "Astromech"]
      }, {
        name: "Corran Horn",
        faction: "Rebel Alliance",
        id: 75,
        unique: true,
        ship: "E-Wing",
        skill: 8,
        points: 35,
        slots: ["Elite", "System", "Torpedo", "Astromech"]
      }, {
        name: "Sigma Squadron Pilot",
        faction: "Galactic Empire",
        id: 76,
        ship: "TIE Phantom",
        skill: 3,
        points: 25,
        slots: ["System", "Crew"]
      }, {
        name: "Shadow Squadron Pilot",
        faction: "Galactic Empire",
        id: 77,
        ship: "TIE Phantom",
        skill: 5,
        points: 27,
        slots: ["System", "Crew"]
      }, {
        name: '"Echo"',
        faction: "Galactic Empire",
        id: 78,
        unique: true,
        ship: "TIE Phantom",
        skill: 6,
        points: 30,
        slots: ["Elite", "System", "Crew"]
      }, {
        name: '"Whisper"',
        faction: "Galactic Empire",
        id: 79,
        unique: true,
        ship: "TIE Phantom",
        skill: 7,
        points: 32,
        slots: ["Elite", "System", "Crew"]
      }, {
        name: "CR90 Corvette (Fore)",
        faction: "Rebel Alliance",
        id: 80,
        epic: true,
        ship: "CR90 Corvette (Fore)",
        skill: 4,
        points: 50,
        slots: ["Crew", "Hardpoint", "Hardpoint", "Team", "Team", "Cargo"]
      }, {
        name: "CR90 Corvette (Aft)",
        faction: "Rebel Alliance",
        id: 81,
        epic: true,
        ship: "CR90 Corvette (Aft)",
        skill: 4,
        points: 40,
        slots: ["Crew", "Hardpoint", "Team", "Cargo"]
      }, {
        name: "Wes Janson",
        faction: "Rebel Alliance",
        id: 82,
        unique: true,
        ship: "X-Wing",
        skill: 8,
        points: 29,
        slots: ["Elite", "Torpedo", "Astromech"]
      }, {
        name: "Jek Porkins",
        faction: "Rebel Alliance",
        id: 83,
        unique: true,
        ship: "X-Wing",
        skill: 7,
        points: 26,
        slots: ["Elite", "Torpedo", "Astromech"]
      }, {
        name: '"Hobbie" Klivian',
        faction: "Rebel Alliance",
        id: 84,
        unique: true,
        ship: "X-Wing",
        skill: 5,
        points: 25,
        slots: ["Torpedo", "Astromech"]
      }, {
        name: "Tarn Mison",
        faction: "Rebel Alliance",
        id: 85,
        unique: true,
        ship: "X-Wing",
        skill: 3,
        points: 23,
        slots: ["Torpedo", "Astromech"]
      }, {
        name: "Jake Farrell",
        faction: "Rebel Alliance",
        id: 86,
        unique: true,
        ship: "A-Wing",
        skill: 7,
        points: 24,
        slots: ["Elite", "Missile"]
      }, {
        name: "Gemmer Sojan",
        faction: "Rebel Alliance",
        id: 87,
        unique: true,
        ship: "A-Wing",
        skill: 5,
        points: 22,
        slots: ["Missile"]
      }, {
        name: "Keyan Farlander",
        faction: "Rebel Alliance",
        id: 88,
        unique: true,
        ship: "B-Wing",
        skill: 7,
        points: 29,
        slots: ["Elite", "System", "Cannon", "Torpedo", "Torpedo"]
      }, {
        name: "Nera Dantels",
        faction: "Rebel Alliance",
        id: 89,
        unique: true,
        ship: "B-Wing",
        skill: 5,
        points: 26,
        slots: ["Elite", "System", "Cannon", "Torpedo", "Torpedo"]
      }, {
        name: "CR90 Corvette (Crippled Fore)",
        skip: true,
        faction: "Rebel Alliance",
        id: 90,
        ship: "CR90 Corvette (Fore)",
        skill: 4,
        points: 0,
        epic: true,
        slots: ["Crew"],
        ship_override: {
          attack: 2,
          agility: 0,
          hull: 0,
          shields: 0,
          actions: []
        }
      }, {
        name: "CR90 Corvette (Crippled Aft)",
        skip: true,
        faction: "Rebel Alliance",
        id: 91,
        ship: "CR90 Corvette (Aft)",
        skill: 4,
        points: 0,
        epic: true,
        slots: ["Cargo"],
        ship_override: {
          energy: 1,
          agility: 0,
          hull: 0,
          shields: 0,
          actions: []
        },
        modifier_func: function(stats) {
          stats.maneuvers[2][1] = 0;
          stats.maneuvers[2][3] = 0;
          return stats.maneuvers[4][2] = 0;
        }
      }, {
        name: "Wild Space Fringer",
        faction: "Rebel Alliance",
        id: 92,
        ship: "YT-2400",
        skill: 2,
        points: 30,
        slots: ["Cannon", "Missile", "Crew"]
      }, {
        name: "Eaden Vrill",
        faction: "Rebel Alliance",
        id: 93,
        ship: "YT-2400",
        unique: true,
        skill: 3,
        points: 32,
        slots: ["Cannon", "Missile", "Crew"]
      }, {
        name: '"Leebo"',
        faction: "Rebel Alliance",
        id: 94,
        ship: "YT-2400",
        unique: true,
        skill: 5,
        points: 34,
        slots: ["Elite", "Cannon", "Missile", "Crew"]
      }, {
        name: "Dash Rendar",
        faction: "Rebel Alliance",
        id: 95,
        ship: "YT-2400",
        unique: true,
        skill: 7,
        points: 36,
        slots: ["Elite", "Cannon", "Missile", "Crew"]
      }, {
        name: "Patrol Leader",
        faction: "Galactic Empire",
        id: 96,
        ship: "VT-49 Decimator",
        skill: 3,
        points: 40,
        slots: ["Torpedo", "Crew", "Crew", "Crew", "Bomb"]
      }, {
        name: "Captain Oicunn",
        faction: "Galactic Empire",
        id: 97,
        ship: "VT-49 Decimator",
        skill: 4,
        points: 42,
        unique: true,
        slots: ["Elite", "Torpedo", "Crew", "Crew", "Crew", "Bomb"]
      }, {
        name: "Commander Kenkirk",
        faction: "Galactic Empire",
        id: 98,
        ship: "VT-49 Decimator",
        skill: 6,
        points: 44,
        unique: true,
        slots: ["Elite", "Torpedo", "Crew", "Crew", "Crew", "Bomb"]
      }, {
        name: "Rear Admiral Chiraneau",
        faction: "Galactic Empire",
        id: 99,
        ship: "VT-49 Decimator",
        skill: 8,
        points: 46,
        unique: true,
        slots: ["Elite", "Torpedo", "Crew", "Crew", "Crew", "Bomb"]
      }, {
        name: "Prince Xizor",
        faction: "Scum and Villainy",
        id: 100,
        unique: true,
        ship: "StarViper",
        skill: 7,
        points: 31,
        slots: ["Elite", "Torpedo"]
      }, {
        name: "Guri",
        faction: "Scum and Villainy",
        id: 101,
        unique: true,
        ship: "StarViper",
        skill: 5,
        points: 30,
        slots: ["Elite", "Torpedo"]
      }, {
        name: "Black Sun Vigo",
        faction: "Scum and Villainy",
        id: 102,
        ship: "StarViper",
        skill: 3,
        points: 27,
        slots: ["Torpedo"]
      }, {
        name: "Black Sun Enforcer",
        faction: "Scum and Villainy",
        id: 103,
        ship: "StarViper",
        skill: 1,
        points: 25,
        slots: ["Torpedo"]
      }, {
        name: "Serissu",
        faction: "Scum and Villainy",
        id: 104,
        ship: "M3-A Interceptor",
        skill: 8,
        points: 20,
        unique: true,
        slots: ["Elite"]
      }, {
        name: "Laetin A'shera",
        faction: "Scum and Villainy",
        id: 105,
        ship: "M3-A Interceptor",
        skill: 6,
        points: 18,
        unique: true,
        slots: []
      }, {
        name: "Tansarii Point Veteran",
        faction: "Scum and Villainy",
        id: 106,
        ship: "M3-A Interceptor",
        skill: 5,
        points: 17,
        slots: ["Elite"]
      }, {
        name: "Cartel Spacer",
        faction: "Scum and Villainy",
        id: 107,
        ship: "M3-A Interceptor",
        skill: 2,
        points: 14,
        slots: []
      }, {
        name: "IG-88A",
        faction: "Scum and Villainy",
        id: 108,
        unique: true,
        ship: "Aggressor",
        skill: 6,
        points: 36,
        slots: ["Elite", "System", "Cannon", "Cannon", "Bomb", "Illicit"]
      }, {
        name: "IG-88B",
        faction: "Scum and Villainy",
        id: 109,
        unique: true,
        ship: "Aggressor",
        skill: 6,
        points: 36,
        slots: ["Elite", "System", "Cannon", "Cannon", "Bomb", "Illicit"]
      }, {
        name: "IG-88C",
        faction: "Scum and Villainy",
        id: 110,
        unique: true,
        ship: "Aggressor",
        skill: 6,
        points: 36,
        slots: ["Elite", "System", "Cannon", "Cannon", "Bomb", "Illicit"]
      }, {
        name: "IG-88D",
        faction: "Scum and Villainy",
        id: 111,
        unique: true,
        ship: "Aggressor",
        skill: 6,
        points: 36,
        slots: ["Elite", "System", "Cannon", "Cannon", "Bomb", "Illicit"]
      }, {
        name: "N'Dru Suhlak",
        unique: true,
        faction: "Scum and Villainy",
        id: 112,
        ship: "Z-95 Headhunter",
        skill: 7,
        points: 17,
        slots: ["Elite", "Missile", "Illicit"]
      }, {
        name: "Kaa'To Leeachos",
        unique: true,
        faction: "Scum and Villainy",
        id: 113,
        ship: "Z-95 Headhunter",
        skill: 5,
        points: 15,
        slots: ["Elite", "Missile", "Illicit"]
      }, {
        name: "Black Sun Soldier",
        faction: "Scum and Villainy",
        id: 114,
        ship: "Z-95 Headhunter",
        skill: 3,
        points: 13,
        slots: ["Missile", "Illicit"]
      }, {
        name: "Binayre Pirate",
        faction: "Scum and Villainy",
        id: 115,
        ship: "Z-95 Headhunter",
        skill: 1,
        points: 12,
        slots: ["Missile", "Illicit"]
      }, {
        name: "Boba Fett (Scum)",
        canonical_name: 'Boba Fett'.canonicalize(),
        faction: "Scum and Villainy",
        id: 116,
        ship: "Firespray-31",
        skill: 8,
        points: 39,
        unique: true,
        slots: ["Elite", "Cannon", "Bomb", "Crew", "Missile", "Illicit"]
      }, {
        name: "Kath Scarlet (Scum)",
        canonical_name: 'Kath Scarlet'.canonicalize(),
        unique: true,
        faction: "Scum and Villainy",
        id: 117,
        ship: "Firespray-31",
        skill: 7,
        points: 38,
        slots: ["Elite", "Cannon", "Bomb", "Crew", "Missile", "Illicit"]
      }, {
        name: "Emon Azzameen",
        unique: true,
        faction: "Scum and Villainy",
        id: 118,
        ship: "Firespray-31",
        skill: 6,
        points: 36,
        slots: ["Cannon", "Bomb", "Crew", "Missile", "Illicit"]
      }, {
        name: "Mandalorian Mercenary",
        faction: "Scum and Villainy",
        id: 119,
        ship: "Firespray-31",
        skill: 5,
        points: 35,
        slots: ["Elite", "Cannon", "Bomb", "Crew", "Missile", "Illicit"]
      }, {
        name: "Kavil",
        unique: true,
        faction: "Scum and Villainy",
        id: 120,
        ship: "Y-Wing",
        skill: 7,
        points: 24,
        slots: ["Elite", "Turret", "Torpedo", "Torpedo", "Salvaged Astromech"]
      }, {
        name: "Drea Renthal",
        unique: true,
        faction: "Scum and Villainy",
        id: 121,
        ship: "Y-Wing",
        skill: 5,
        points: 22,
        slots: ["Turret", "Torpedo", "Torpedo", "Salvaged Astromech"]
      }, {
        name: "Hired Gun",
        faction: "Scum and Villainy",
        id: 122,
        ship: "Y-Wing",
        skill: 4,
        points: 20,
        slots: ["Turret", "Torpedo", "Torpedo", "Salvaged Astromech"]
      }, {
        name: "Syndicate Thug",
        faction: "Scum and Villainy",
        id: 123,
        ship: "Y-Wing",
        skill: 2,
        points: 18,
        slots: ["Turret", "Torpedo", "Torpedo", "Salvaged Astromech"]
      }, {
        name: "Dace Bonearm",
        unique: true,
        faction: "Scum and Villainy",
        id: 124,
        ship: "HWK-290",
        skill: 7,
        points: 23,
        slots: ["Elite", "Turret", "Crew", "Illicit"]
      }, {
        name: "Palob Godalhi",
        unique: true,
        faction: "Scum and Villainy",
        id: 125,
        ship: "HWK-290",
        skill: 5,
        points: 20,
        slots: ["Elite", "Turret", "Crew", "Illicit"]
      }, {
        name: "Torkil Mux",
        unique: true,
        faction: "Scum and Villainy",
        id: 126,
        ship: "HWK-290",
        skill: 3,
        points: 19,
        slots: ["Turret", "Crew", "Illicit"]
      }, {
        name: "Spice Runner",
        faction: "Scum and Villainy",
        id: 127,
        ship: "HWK-290",
        skill: 1,
        points: 16,
        slots: ["Turret", "Crew", "Illicit"]
      }, {
        name: "Commander Alozen",
        faction: "Galactic Empire",
        id: 128,
        ship: "TIE Advanced",
        unique: true,
        skill: 5,
        points: 25,
        slots: ["Elite", "Missile"]
      }, {
        name: "Raider-class Corvette (Fore)",
        faction: "Galactic Empire",
        id: 129,
        ship: "Raider-class Corvette (Fore)",
        skill: 4,
        points: 50,
        epic: true,
        slots: ["Hardpoint", "Team", "Cargo"]
      }, {
        name: "Raider-class Corvette (Aft)",
        faction: "Galactic Empire",
        id: 130,
        ship: "Raider-class Corvette (Aft)",
        skill: 4,
        points: 50,
        epic: true,
        slots: ["Crew", "Crew", "Hardpoint", "Hardpoint", "Team", "Team", "Cargo"]
      }, {
        name: "Bossk",
        faction: "Scum and Villainy",
        id: 131,
        ship: "YV-666",
        unique: true,
        skill: 7,
        points: 35,
        slots: ["Elite", "Cannon", "Missile", "Crew", "Crew", "Crew", "Illicit"]
      }, {
        name: "Moralo Eval",
        faction: "Scum and Villainy",
        id: 132,
        ship: "YV-666",
        unique: true,
        skill: 6,
        points: 34,
        slots: ["Cannon", "Missile", "Crew", "Crew", "Crew", "Illicit"]
      }, {
        name: "Latts Razzi",
        faction: "Scum and Villainy",
        id: 133,
        ship: "YV-666",
        unique: true,
        skill: 5,
        points: 33,
        slots: ["Cannon", "Missile", "Crew", "Crew", "Crew", "Illicit"]
      }, {
        name: "Trandoshan Slaver",
        faction: "Scum and Villainy",
        id: 134,
        ship: "YV-666",
        skill: 2,
        points: 29,
        slots: ["Cannon", "Missile", "Crew", "Crew", "Crew", "Illicit"]
      }, {
        name: "Talonbane Cobra",
        unique: true,
        id: 135,
        faction: "Scum and Villainy",
        ship: "Kihraxz Fighter",
        skill: 9,
        slots: ["Elite", "Missile", "Illicit"],
        points: 28
      }, {
        name: "Graz the Hunter",
        unique: true,
        id: 136,
        faction: "Scum and Villainy",
        ship: "Kihraxz Fighter",
        skill: 6,
        slots: ["Missile", "Illicit"],
        points: 25
      }, {
        name: "Black Sun Ace",
        faction: "Scum and Villainy",
        id: 137,
        ship: "Kihraxz Fighter",
        skill: 5,
        slots: ["Elite", "Missile", "Illicit"],
        points: 23
      }, {
        name: "Cartel Marauder",
        faction: "Scum and Villainy",
        id: 138,
        ship: "Kihraxz Fighter",
        skill: 2,
        slots: ["Missile", "Illicit"],
        points: 20
      }, {
        name: "Miranda Doni",
        unique: true,
        id: 139,
        faction: "Rebel Alliance",
        ship: "K-Wing",
        skill: 8,
        slots: ["Turret", "Torpedo", "Torpedo", "Missile", "Crew", "Bomb", "Bomb"],
        points: 29
      }, {
        name: "Esege Tuketu",
        unique: true,
        id: 140,
        faction: "Rebel Alliance",
        ship: "K-Wing",
        skill: 6,
        slots: ["Turret", "Torpedo", "Torpedo", "Missile", "Crew", "Bomb", "Bomb"],
        points: 28
      }, {
        name: "Guardian Squadron Pilot",
        faction: "Rebel Alliance",
        id: 141,
        ship: "K-Wing",
        skill: 4,
        slots: ["Turret", "Torpedo", "Torpedo", "Missile", "Crew", "Bomb", "Bomb"],
        points: 25
      }, {
        name: "Warden Squadron Pilot",
        faction: "Rebel Alliance",
        id: 142,
        ship: "K-Wing",
        skill: 2,
        slots: ["Turret", "Torpedo", "Torpedo", "Missile", "Crew", "Bomb", "Bomb"],
        points: 23
      }, {
        name: '"Redline"',
        unique: true,
        id: 143,
        faction: "Galactic Empire",
        ship: "TIE Punisher",
        skill: 7,
        slots: ["System", "Torpedo", "Torpedo", "Missile", "Missile", "Bomb", "Bomb"],
        points: 27
      }, {
        name: '"Deathrain"',
        unique: true,
        id: 144,
        faction: "Galactic Empire",
        ship: "TIE Punisher",
        skill: 6,
        slots: ["System", "Torpedo", "Torpedo", "Missile", "Missile", "Bomb", "Bomb"],
        points: 26
      }, {
        name: 'Black Eight Squadron Pilot',
        canonical_name: 'Black Eight Sq. Pilot'.canonicalize(),
        faction: "Galactic Empire",
        id: 145,
        ship: "TIE Punisher",
        skill: 4,
        slots: ["System", "Torpedo", "Torpedo", "Missile", "Missile", "Bomb", "Bomb"],
        points: 23
      }, {
        name: 'Cutlass Squadron Pilot',
        faction: "Galactic Empire",
        id: 146,
        ship: "TIE Punisher",
        skill: 2,
        slots: ["System", "Torpedo", "Torpedo", "Missile", "Missile", "Bomb", "Bomb"],
        points: 21
      }, {
        name: "Juno Eclipse",
        id: 147,
        faction: "Galactic Empire",
        ship: "TIE Advanced",
        unique: true,
        skill: 8,
        points: 28,
        slots: ["Elite", "Missile"]
      }, {
        name: "Zertik Strom",
        id: 148,
        faction: "Galactic Empire",
        ship: "TIE Advanced",
        unique: true,
        skill: 6,
        points: 26,
        slots: ["Elite", "Missile"]
      }, {
        name: "Lieutenant Colzet",
        id: 149,
        faction: "Galactic Empire",
        ship: "TIE Advanced",
        unique: true,
        skill: 3,
        points: 23,
        slots: ["Missile"]
      }, {
        name: "Gozanti-class Cruiser",
        id: 150,
        faction: "Galactic Empire",
        ship: "Gozanti-class Cruiser",
        skill: 2,
        slots: ['Crew', 'Crew', 'Hardpoint', 'Team', 'Cargo', 'Cargo'],
        points: 40
      }, {
        name: '"Scourge"',
        id: 151,
        unique: true,
        faction: "Galactic Empire",
        ship: "TIE Fighter",
        skill: 7,
        slots: ['Elite'],
        points: 17
      }, {
        name: '"Youngster"',
        id: 152,
        unique: true,
        faction: "Galactic Empire",
        ship: "TIE Fighter",
        skill: 6,
        slots: ['Elite'],
        points: 15
      }, {
        name: '"Wampa"',
        id: 153,
        unique: true,
        faction: "Galactic Empire",
        ship: "TIE Fighter",
        skill: 4,
        slots: [],
        points: 14
      }, {
        name: '"Chaser"',
        id: 154,
        unique: true,
        faction: "Galactic Empire",
        ship: "TIE Fighter",
        skill: 3,
        slots: [],
        points: 14
      }, {
        name: "Hera Syndulla",
        id: 155,
        unique: true,
        faction: "Rebel Alliance",
        ship: "VCX-100",
        skill: 7,
        slots: ['System', 'Turret', 'Torpedo', 'Torpedo', 'Crew', 'Crew'],
        points: 40
      }, {
        name: "Kanan Jarrus",
        id: 156,
        unique: true,
        faction: "Rebel Alliance",
        ship: "VCX-100",
        skill: 5,
        slots: ['System', 'Turret', 'Torpedo', 'Torpedo', 'Crew', 'Crew'],
        points: 38
      }, {
        name: '"Chopper"',
        id: 157,
        unique: true,
        faction: "Rebel Alliance",
        ship: "VCX-100",
        skill: 4,
        slots: ['System', 'Turret', 'Torpedo', 'Torpedo', 'Crew', 'Crew'],
        points: 37
      }, {
        name: 'Lothal Rebel',
        id: 158,
        faction: "Rebel Alliance",
        ship: "VCX-100",
        skill: 3,
        slots: ['System', 'Turret', 'Torpedo', 'Torpedo', 'Crew', 'Crew'],
        points: 35
      }, {
        name: 'Hera Syndulla (Attack Shuttle)',
        id: 159,
        canonical_name: 'Hera Syndulla'.canonicalize(),
        unique: true,
        faction: "Rebel Alliance",
        ship: "Attack Shuttle",
        skill: 7,
        slots: ['Elite', 'Turret', 'Crew'],
        points: 22
      }, {
        name: 'Sabine Wren',
        id: 160,
        unique: true,
        faction: "Rebel Alliance",
        ship: "Attack Shuttle",
        skill: 5,
        slots: ['Elite', 'Turret', 'Crew'],
        points: 21
      }, {
        name: 'Ezra Bridger',
        id: 161,
        unique: true,
        faction: "Rebel Alliance",
        ship: "Attack Shuttle",
        skill: 4,
        slots: ['Elite', 'Turret', 'Crew'],
        points: 20
      }, {
        name: '"Zeb" Orrelios',
        id: 162,
        unique: true,
        faction: "Rebel Alliance",
        ship: "Attack Shuttle",
        skill: 3,
        slots: ['Turret', 'Crew'],
        points: 18
      }, {
        name: "The Inquisitor",
        id: 163,
        unique: true,
        faction: "Galactic Empire",
        ship: "TIE Advanced Prototype",
        skill: 8,
        slots: ['Elite', 'Missile'],
        points: 25
      }, {
        name: "Valen Rudor",
        id: 164,
        unique: true,
        faction: "Galactic Empire",
        ship: "TIE Advanced Prototype",
        skill: 6,
        slots: ['Elite', 'Missile'],
        points: 22
      }, {
        name: "Baron of the Empire",
        id: 165,
        faction: "Galactic Empire",
        ship: "TIE Advanced Prototype",
        skill: 4,
        slots: ['Elite', 'Missile'],
        points: 19
      }, {
        name: "Sienar Test Pilot",
        id: 166,
        faction: "Galactic Empire",
        ship: "TIE Advanced Prototype",
        skill: 2,
        slots: ['Missile'],
        points: 16
      }, {
        name: "Zuckuss",
        id: 167,
        unique: true,
        faction: "Scum and Villainy",
        ship: "G-1A Starfighter",
        skill: 7,
        slots: ['Elite', 'Crew', 'System', 'Illicit'],
        points: 28
      }, {
        name: "4-LOM",
        id: 168,
        unique: true,
        faction: "Scum and Villainy",
        ship: "G-1A Starfighter",
        skill: 6,
        slots: ['Elite', 'Crew', 'System', 'Illicit'],
        points: 27
      }, {
        name: "Gand Findsman",
        id: 169,
        faction: "Scum and Villainy",
        ship: "G-1A Starfighter",
        skill: 5,
        slots: ['Elite', 'Crew', 'System', 'Illicit'],
        points: 25
      }, {
        name: "Ruthless Freelancer",
        id: 170,
        faction: "Scum and Villainy",
        ship: "G-1A Starfighter",
        skill: 3,
        slots: ['Crew', 'System', 'Illicit'],
        points: 23
      }, {
        name: "Dengar",
        id: 171,
        unique: true,
        faction: "Scum and Villainy",
        ship: "JumpMaster 5000",
        skill: 9,
        slots: ['Elite', 'Torpedo', 'Torpedo', 'Crew', 'Salvaged Astromech', 'Illicit'],
        points: 33
      }, {
        name: "Tel Trevura",
        id: 172,
        unique: true,
        faction: "Scum and Villainy",
        ship: "JumpMaster 5000",
        skill: 7,
        slots: ['Elite', 'Torpedo', 'Torpedo', 'Crew', 'Salvaged Astromech', 'Illicit'],
        points: 30
      }, {
        name: "Manaroo",
        id: 173,
        unique: true,
        faction: "Scum and Villainy",
        ship: "JumpMaster 5000",
        skill: 4,
        slots: ['Elite', 'Torpedo', 'Torpedo', 'Crew', 'Salvaged Astromech', 'Illicit'],
        points: 27
      }, {
        name: "Contracted Scout",
        id: 174,
        faction: "Scum and Villainy",
        ship: "JumpMaster 5000",
        skill: 3,
        slots: ['Elite', 'Torpedo', 'Torpedo', 'Crew', 'Salvaged Astromech', 'Illicit'],
        points: 25
      }, {
        name: "Poe Dameron",
        id: 175,
        unique: true,
        faction: "Resistance",
        ship: "T-70 X-Wing",
        skill: 8,
        slots: ['Elite', 'Torpedo', 'Astromech', 'Tech'],
        points: 31
      }, {
        name: '"Blue Ace"',
        id: 176,
        unique: true,
        faction: "Resistance",
        ship: "T-70 X-Wing",
        skill: 5,
        slots: ['Torpedo', 'Astromech', 'Tech'],
        points: 27
      }, {
        name: "Red Squadron Veteran",
        id: 177,
        faction: "Resistance",
        ship: "T-70 X-Wing",
        skill: 4,
        slots: ['Elite', 'Torpedo', 'Astromech', 'Tech'],
        points: 26
      }, {
        name: "Blue Squadron Novice",
        id: 178,
        faction: "Resistance",
        ship: "T-70 X-Wing",
        skill: 2,
        slots: ['Torpedo', 'Astromech', 'Tech'],
        points: 24
      }, {
        name: '"Omega Ace"',
        id: 179,
        unique: true,
        faction: "First Order",
        ship: "TIE/fo Fighter",
        skill: 7,
        slots: ['Elite', 'Tech'],
        points: 20
      }, {
        name: '"Epsilon Leader"',
        id: 180,
        unique: true,
        faction: "First Order",
        ship: "TIE/fo Fighter",
        skill: 6,
        slots: ['Tech'],
        points: 19
      }, {
        name: '"Zeta Ace"',
        id: 181,
        unique: true,
        faction: "First Order",
        ship: "TIE/fo Fighter",
        skill: 5,
        slots: ['Elite', 'Tech'],
        points: 18
      }, {
        name: "Omega Squadron Pilot",
        id: 182,
        faction: "First Order",
        ship: "TIE/fo Fighter",
        skill: 4,
        slots: ['Elite', 'Tech'],
        points: 17
      }, {
        name: "Zeta Squadron Pilot",
        id: 183,
        faction: "First Order",
        ship: "TIE/fo Fighter",
        skill: 3,
        slots: ['Tech'],
        points: 16
      }, {
        name: "Epsilon Squadron Pilot",
        id: 184,
        faction: "First Order",
        ship: "TIE/fo Fighter",
        skill: 1,
        slots: ['Tech'],
        points: 15
      }, {
        name: "Ello Asty",
        id: 185,
        unique: true,
        faction: "Resistance",
        ship: "T-70 X-Wing",
        skill: 7,
        slots: ['Elite', 'Torpedo', 'Astromech', 'Tech'],
        points: 30
      }, {
        name: '"Red Ace"',
        id: 186,
        unique: true,
        faction: "Resistance",
        ship: "T-70 X-Wing",
        skill: 6,
        slots: ['Torpedo', 'Astromech', 'Tech'],
        points: 29
      }, {
        name: '"Omega Leader"',
        id: 187,
        unique: true,
        faction: "First Order",
        ship: "TIE/fo Fighter",
        skill: 8,
        slots: ['Elite', 'Tech'],
        points: 21
      }, {
        name: '"Zeta Leader"',
        id: 188,
        unique: true,
        faction: "First Order",
        ship: "TIE/fo Fighter",
        skill: 7,
        slots: ['Elite', 'Tech'],
        points: 20
      }, {
        name: '"Epsilon Ace"',
        id: 189,
        unique: true,
        faction: "First Order",
        ship: "TIE/fo Fighter",
        skill: 4,
        slots: ['Tech'],
        points: 17
      }, {
        name: "Tomax Bren",
        id: 190,
        unique: true,
        faction: "Galactic Empire",
        ship: "TIE Bomber",
        skill: 8,
        slots: ['Elite', 'Torpedo', 'Torpedo', 'Missile', 'Missile', 'Bomb'],
        points: 24
      }, {
        name: "Gamma Squadron Veteran",
        id: 191,
        faction: "Galactic Empire",
        ship: "TIE Bomber",
        skill: 5,
        slots: ['Elite', 'Torpedo', 'Torpedo', 'Missile', 'Missile', 'Bomb'],
        points: 19
      }, {
        name: '"Deathfire"',
        id: 192,
        unique: true,
        faction: "Galactic Empire",
        ship: "TIE Bomber",
        skill: 3,
        slots: ['Torpedo', 'Torpedo', 'Missile', 'Missile', 'Bomb'],
        points: 17
      }, {
        name: "Maarek Stele (TIE Defender)",
        canonical_name: 'Maarek Stele'.canonicalize(),
        id: 193,
        unique: true,
        faction: "Galactic Empire",
        ship: "TIE Defender",
        skill: 7,
        slots: ['Elite', 'Cannon', 'Missile'],
        points: 35
      }, {
        name: "Glaive Squadron Pilot",
        id: 194,
        faction: "Galactic Empire",
        ship: "TIE Defender",
        skill: 6,
        slots: ['Elite', 'Cannon', 'Missile'],
        points: 34
      }, {
        name: "Countess Ryad",
        id: 195,
        unique: true,
        faction: "Galactic Empire",
        ship: "TIE Defender",
        skill: 5,
        slots: ['Elite', 'Cannon', 'Missile'],
        points: 34
      }, {
        name: "Poe Dameron (PS9)",
        canonical_name: "poedameron-swx57",
        id: 196,
        unique: true,
        faction: "Resistance",
        ship: "T-70 X-Wing",
        skill: 9,
        slots: ['Elite', 'Torpedo', 'Astromech', 'Tech'],
        points: 33
      }, {
        name: 'Nien Nunb',
        id: 197,
        unique: true,
        faction: "Resistance",
        ship: "T-70 X-Wing",
        skill: 7,
        slots: ['Torpedo', 'Astromech', 'Tech'],
        points: 100
      }, {
        name: '"Snap" Wexley',
        id: 198,
        unique: true,
        faction: "Resistance",
        ship: "T-70 X-Wing",
        skill: 6,
        slots: ['Torpedo', 'Astromech', 'Tech'],
        points: 100
      }, {
        name: 'Jess Pava',
        id: 199,
        unique: true,
        faction: "Resistance",
        ship: "T-70 X-Wing",
        skill: 3,
        slots: ['Torpedo', 'Astromech', 'Tech'],
        points: 100
      }, {
        name: "Han Solo (TFA)",
        canonical_name: "hansolo-swx57",
        id: 200,
        unique: true,
        faction: "Resistance",
        ship: "YT-1300",
        skill: 9,
        points: 100,
        slots: ["Elite", "Missile", "Crew", "Crew"],
        ship_override: {
          attack: 3,
          agility: 1,
          hull: 8,
          shields: 5
        }
      }, {
        name: "Rey",
        id: 201,
        unique: true,
        faction: "Resistance",
        ship: "YT-1300",
        skill: 8,
        points: 45,
        slots: ["Elite", "Missile", "Crew", "Crew"],
        ship_override: {
          attack: 3,
          agility: 1,
          hull: 8,
          shields: 5
        }
      }, {
        name: "Chewbacca (TFA)",
        canonical_name: "chewbacca-swx57",
        id: 202,
        unique: true,
        faction: "Resistance",
        ship: "YT-1300",
        skill: 5,
        points: 100,
        slots: ["Elite", "Missile", "Crew", "Crew"],
        ship_override: {
          attack: 3,
          agility: 1,
          hull: 8,
          shields: 5
        }
      }, {
        name: "Resistance???",
        id: 203,
        faction: "Resistance",
        ship: "YT-1300",
        skill: 5,
        points: 100,
        slots: ["Missile", "Crew", "Crew"]
      }, {
        name: 'Norra Wexley',
        id: 204,
        unique: true,
        faction: 'Rebel Alliance',
        ship: 'ARC-170',
        skill: 7,
        slots: ['Elite', 'Torpedo', 'Crew', 'Astromech'],
        points: 29
      }, {
        name: 'Shara Bey',
        id: 205,
        unique: true,
        faction: 'Rebel Alliance',
        ship: 'ARC-170',
        skill: 6,
        slots: ['Elite', 'Torpedo', 'Crew', 'Astromech'],
        points: 28
      }, {
        name: 'Unspoiled PS4 ARC-170 Pilot',
        id: 206,
        unique: true,
        faction: 'Rebel Alliance',
        ship: 'ARC-170',
        skill: 4,
        slots: ['Torpedo', 'Crew', 'Astromech'],
        points: 100
      }, {
        name: 'Unspoiled PS3 ARC-170 Pilot',
        id: 207,
        unique: true,
        faction: 'Rebel Alliance',
        ship: 'ARC-170',
        skill: 3,
        slots: ['Torpedo', 'Crew', 'Astromech'],
        points: 100
      }, {
        name: '"Quickdraw"',
        id: 208,
        unique: true,
        faction: 'Galactic Empire',
        ship: 'TIE/sf Fighter',
        skill: 9,
        slots: ['Elite', 'System', 'Missile', 'Tech'],
        points: 29
      }, {
        name: 'Unspoiled PS7 TIE/sf Pilot',
        id: 209,
        unique: true,
        faction: 'Galactic Empire',
        ship: 'TIE/sf Fighter',
        skill: 7,
        slots: ['System', 'Missile', 'Tech'],
        points: 100
      }, {
        name: 'Unspoiled PS5 TIE/sf Pilot',
        id: 210,
        faction: 'Galactic Empire',
        ship: 'TIE/sf Fighter',
        skill: 5,
        slots: ['System', 'Missile', 'Tech'],
        points: 100
      }, {
        name: 'Unspoiled PS3 TIE/sf Pilot',
        id: 211,
        faction: 'Galactic Empire',
        ship: 'TIE/sf Fighter',
        skill: 3,
        slots: ['System', 'Missile', 'Tech'],
        points: 100
      }, {
        name: 'Fenn Rau',
        id: 212,
        unique: true,
        faction: 'Scum and Villainy',
        ship: 'Protectorate Starfighter',
        skill: 9,
        slots: ['Elite', 'Torpedo'],
        points: 28
      }, {
        name: 'Old ???',
        id: 213,
        unique: true,
        faction: 'Scum and Villainy',
        ship: 'Protectorate Starfighter',
        skill: 7,
        slots: ['Torpedo'],
        points: 100
      }, {
        name: 'Kad Solus',
        id: 214,
        unique: true,
        faction: 'Scum and Villainy',
        ship: 'Protectorate Starfighter',
        skill: 6,
        slots: ['Torpedo'],
        points: 25
      }, {
        name: 'Unspoiled PS5 Protectorate Starfighter Pilot',
        id: 215,
        faction: 'Scum and Villainy',
        ship: 'Protectorate Starfighter',
        skill: 5,
        slots: ['Torpedo'],
        points: 100
      }, {
        name: 'Unspoiled PS3 Protectorate Starfighter Pilot',
        id: 216,
        faction: 'Scum and Villainy',
        ship: 'Protectorate Starfighter',
        skill: 3,
        slots: ['Torpedo'],
        points: 100
      }, {
        name: 'Zealous ???',
        id: 217,
        faction: 'Scum and Villainy',
        ship: 'Protectorate Starfighter',
        skill: 1,
        slots: ['Torpedo'],
        points: 100
      }, {
        name: 'Ketsu Onyo',
        id: 218,
        unique: true,
        faction: 'Scum and Villainy',
        ship: 'Lancer-class Pursuit Craft',
        skill: 7,
        slots: ['Elite', 'Crew', 'Illicit', 'Illicit'],
        points: 38
      }, {
        name: 'Asajj ???',
        id: 219,
        unique: true,
        faction: 'Scum and Villainy',
        ship: 'Lancer-class Pursuit Craft',
        skill: 6,
        slots: ['Crew', 'Illicit', 'Illicit'],
        points: 100
      }, {
        name: 'Sabine Wren',
        canonical_name: "sabinewren-swx56",
        id: 220,
        unique: true,
        faction: 'Scum and Villainy',
        ship: 'Lancer-class Pursuit Craft',
        skill: 5,
        slots: ['Crew', 'Illicit', 'Illicit'],
        points: 35
      }, {
        name: 'Shadowfo???',
        id: 221,
        faction: 'Scum and Villainy',
        ship: 'Lancer-class Pursuit Craft',
        skill: 2,
        slots: ['Crew', 'Illicit', 'Illicit'],
        points: 100
      }
    ],
    upgradesById: [
      {
        name: "Ion Cannon Turret",
        id: 0,
        slot: "Turret",
        points: 5,
        attack: 3,
        range: "1-2"
      }, {
        name: "Proton Torpedoes",
        id: 1,
        slot: "Torpedo",
        points: 4,
        attack: 4,
        range: "2-3"
      }, {
        name: "R2 Astromech",
        id: 2,
        slot: "Astromech",
        points: 1,
        modifier_func: function(stats) {
          var turn, _i, _ref, _results;
          if ((stats.maneuvers != null) && stats.maneuvers.length > 0) {
            _results = [];
            for (turn = _i = 0, _ref = stats.maneuvers[1].length; 0 <= _ref ? _i < _ref : _i > _ref; turn = 0 <= _ref ? ++_i : --_i) {
              if (stats.maneuvers[1][turn] > 0) {
                stats.maneuvers[1][turn] = 2;
              }
              if (stats.maneuvers[2][turn] > 0) {
                _results.push(stats.maneuvers[2][turn] = 2);
              } else {
                _results.push(void 0);
              }
            }
            return _results;
          }
        }
      }, {
        name: "R2-D2",
        aka: ["R2-D2 (Crew)"],
        canonical_name: 'r2d2-swx22',
        id: 3,
        unique: true,
        slot: "Astromech",
        points: 4
      }, {
        name: "R2-F2",
        id: 4,
        unique: true,
        slot: "Astromech",
        points: 3
      }, {
        name: "R5-D8",
        id: 5,
        unique: true,
        slot: "Astromech",
        points: 3
      }, {
        name: "R5-K6",
        id: 6,
        unique: true,
        slot: "Astromech",
        points: 2
      }, {
        name: "R5 Astromech",
        id: 7,
        slot: "Astromech",
        points: 1
      }, {
        name: "Determination",
        id: 8,
        slot: "Elite",
        points: 1
      }, {
        name: "Swarm Tactics",
        id: 9,
        slot: "Elite",
        points: 2
      }, {
        name: "Squad Leader",
        id: 10,
        unique: true,
        slot: "Elite",
        points: 2
      }, {
        name: "Expert Handling",
        id: 11,
        slot: "Elite",
        points: 2
      }, {
        name: "Marksmanship",
        id: 12,
        slot: "Elite",
        points: 3
      }, {
        name: "Concussion Missiles",
        id: 13,
        slot: "Missile",
        points: 4,
        attack: 4,
        range: "2-3"
      }, {
        name: "Cluster Missiles",
        id: 14,
        slot: "Missile",
        points: 4,
        attack: 3,
        range: "1-2"
      }, {
        name: "Daredevil",
        id: 15,
        slot: "Elite",
        points: 3
      }, {
        name: "Elusiveness",
        id: 16,
        slot: "Elite",
        points: 2
      }, {
        name: "Homing Missiles",
        id: 17,
        slot: "Missile",
        attack: 4,
        range: "2-3",
        points: 5
      }, {
        name: "Push the Limit",
        id: 18,
        slot: "Elite",
        points: 3
      }, {
        name: "Deadeye",
        id: 19,
        slot: "Elite",
        points: 1
      }, {
        name: "Expose",
        id: 20,
        slot: "Elite",
        points: 4
      }, {
        name: "Gunner",
        id: 21,
        slot: "Crew",
        points: 5
      }, {
        name: "Ion Cannon",
        id: 22,
        slot: "Cannon",
        points: 3,
        attack: 3,
        range: "1-3"
      }, {
        name: "Heavy Laser Cannon",
        id: 23,
        slot: "Cannon",
        points: 7,
        attack: 4,
        range: "2-3"
      }, {
        name: "Seismic Charges",
        id: 24,
        slot: "Bomb",
        points: 2
      }, {
        name: "Mercenary Copilot",
        id: 25,
        slot: "Crew",
        points: 2
      }, {
        name: "Assault Missiles",
        id: 26,
        slot: "Missile",
        points: 5,
        attack: 4,
        range: "2-3"
      }, {
        name: "Veteran Instincts",
        id: 27,
        slot: "Elite",
        points: 1,
        modifier_func: function(stats) {
          return stats.skill += 2;
        }
      }, {
        name: "Proximity Mines",
        id: 28,
        slot: "Bomb",
        points: 3
      }, {
        name: "Weapons Engineer",
        id: 29,
        slot: "Crew",
        points: 3
      }, {
        name: "Draw Their Fire",
        id: 30,
        slot: "Elite",
        points: 1
      }, {
        name: "Luke Skywalker",
        id: 31,
        unique: true,
        faction: "Rebel Alliance",
        slot: "Crew",
        points: 7
      }, {
        name: "Nien Nunb",
        id: 32,
        unique: true,
        faction: "Rebel Alliance",
        slot: "Crew",
        points: 1,
        modifier_func: function(stats) {
          var s, _i, _len, _ref, _ref1, _results;
          _ref1 = (_ref = stats.maneuvers) != null ? _ref : [];
          _results = [];
          for (_i = 0, _len = _ref1.length; _i < _len; _i++) {
            s = _ref1[_i];
            if (s[2] > 0) {
              _results.push(s[2] = 2);
            } else {
              _results.push(void 0);
            }
          }
          return _results;
        }
      }, {
        name: "Chewbacca",
        id: 33,
        unique: true,
        faction: "Rebel Alliance",
        slot: "Crew",
        points: 4
      }, {
        name: "Advanced Proton Torpedoes",
        canonical_name: 'Adv. Proton Torpedoes'.canonicalize(),
        id: 34,
        slot: "Torpedo",
        attack: 5,
        range: "1",
        points: 6
      }, {
        name: "Autoblaster",
        id: 35,
        slot: "Cannon",
        attack: 3,
        range: "1",
        points: 5
      }, {
        name: "Fire-Control System",
        id: 36,
        slot: "System",
        points: 2
      }, {
        name: "Blaster Turret",
        id: 37,
        slot: "Turret",
        points: 4,
        attack: 3,
        range: "1-2"
      }, {
        name: "Recon Specialist",
        id: 38,
        slot: "Crew",
        points: 3
      }, {
        name: "Saboteur",
        id: 39,
        slot: "Crew",
        points: 2
      }, {
        name: "Intelligence Agent",
        id: 40,
        slot: "Crew",
        points: 1
      }, {
        name: "Proton Bombs",
        id: 41,
        slot: "Bomb",
        points: 5
      }, {
        name: "Adrenaline Rush",
        id: 42,
        slot: "Elite",
        points: 1
      }, {
        name: "Advanced Sensors",
        id: 43,
        slot: "System",
        points: 3
      }, {
        name: "Sensor Jammer",
        id: 44,
        slot: "System",
        points: 4
      }, {
        name: "Darth Vader",
        id: 45,
        unique: true,
        faction: "Galactic Empire",
        slot: "Crew",
        points: 3
      }, {
        name: "Rebel Captive",
        id: 46,
        unique: true,
        faction: "Galactic Empire",
        slot: "Crew",
        points: 3
      }, {
        name: "Flight Instructor",
        id: 47,
        slot: "Crew",
        points: 4
      }, {
        name: "Navigator",
        id: 48,
        slot: "Crew",
        points: 3,
        epic_restriction_func: function(ship) {
          var _ref;
          return !((_ref = ship.huge) != null ? _ref : false);
        }
      }, {
        name: "Opportunist",
        id: 49,
        slot: "Elite",
        points: 4
      }, {
        name: "Comms Booster",
        id: 50,
        slot: "Cargo",
        points: 4
      }, {
        name: "Slicer Tools",
        id: 51,
        slot: "Cargo",
        points: 7
      }, {
        name: "Shield Projector",
        id: 52,
        slot: "Cargo",
        points: 4
      }, {
        name: "Ion Pulse Missiles",
        id: 53,
        slot: "Missile",
        points: 3,
        attack: 3,
        range: "2-3"
      }, {
        name: "Wingman",
        id: 54,
        slot: "Elite",
        points: 2
      }, {
        name: "Decoy",
        id: 55,
        slot: "Elite",
        points: 2
      }, {
        name: "Outmaneuver",
        id: 56,
        slot: "Elite",
        points: 3
      }, {
        name: "Predator",
        id: 57,
        slot: "Elite",
        points: 3
      }, {
        name: "Flechette Torpedoes",
        id: 58,
        slot: "Torpedo",
        points: 2,
        attack: 3,
        range: "2-3"
      }, {
        name: "R7 Astromech",
        id: 59,
        slot: "Astromech",
        points: 2
      }, {
        name: "R7-T1",
        id: 60,
        unique: true,
        slot: "Astromech",
        points: 3
      }, {
        name: "Tactician",
        id: 61,
        slot: "Crew",
        points: 2,
        limited: true
      }, {
        name: "R2-D2 (Crew)",
        aka: ["R2-D2"],
        canonical_name: 'r2d2',
        id: 62,
        unique: true,
        slot: "Crew",
        points: 4,
        faction: "Rebel Alliance"
      }, {
        name: "C-3PO",
        unique: true,
        id: 63,
        slot: "Crew",
        points: 3,
        faction: "Rebel Alliance"
      }, {
        name: "Single Turbolasers",
        id: 64,
        slot: "Hardpoint",
        points: 8,
        energy: 2,
        attack: 4,
        range: "3-5"
      }, {
        name: "Quad Laser Cannons",
        id: 65,
        slot: "Hardpoint",
        points: 6,
        energy: 2,
        attack: 3,
        range: "1-2"
      }, {
        name: "Tibanna Gas Supplies",
        id: 66,
        slot: "Cargo",
        points: 4,
        limited: true
      }, {
        name: "Ionization Reactor",
        id: 67,
        slot: "Cargo",
        points: 4,
        energy: 5,
        limited: true
      }, {
        name: "Engine Booster",
        id: 68,
        slot: "Cargo",
        points: 3,
        limited: true
      }, {
        name: "R3-A2",
        id: 69,
        unique: true,
        slot: "Astromech",
        points: 2
      }, {
        name: "R2-D6",
        id: 70,
        unique: true,
        slot: "Astromech",
        points: 1,
        restriction_func: function(ship) {
          var conferred_addon, upgrade, _i, _j, _len, _len1, _ref, _ref1, _ref2;
          if (ship.effectiveStats().skill <= 2 || __indexOf.call(ship.pilot.slots, 'Elite') >= 0) {
            return false;
          }
          _ref = ship.upgrades;
          for (_i = 0, _len = _ref.length; _i < _len; _i++) {
            upgrade = _ref[_i];
            if ((upgrade != null) && ((_ref1 = upgrade.data) != null ? _ref1.name : void 0) !== 'R2-D6') {
              _ref2 = upgrade.conferredAddons;
              for (_j = 0, _len1 = _ref2.length; _j < _len1; _j++) {
                conferred_addon = _ref2[_j];
                if (conferred_addon.slot === 'Elite') {
                  return false;
                }
              }
            }
          }
          return true;
        },
        confersAddons: [
          {
            type: exportObj.Upgrade,
            slot: "Elite"
          }
        ]
      }, {
        name: "Enhanced Scopes",
        id: 71,
        slot: "System",
        points: 1
      }, {
        name: "Chardaan Refit",
        id: 72,
        slot: "Missile",
        points: -2,
        ship: "A-Wing"
      }, {
        name: "Proton Rockets",
        id: 73,
        slot: "Missile",
        points: 3,
        attack: 2,
        range: "1"
      }, {
        name: "Kyle Katarn",
        id: 74,
        unique: true,
        slot: "Crew",
        points: 3,
        faction: "Rebel Alliance"
      }, {
        name: "Jan Ors",
        id: 75,
        unique: true,
        slot: "Crew",
        points: 2,
        faction: "Rebel Alliance"
      }, {
        name: "Toryn Farr",
        id: 76,
        unique: true,
        slot: "Crew",
        points: 6,
        faction: "Rebel Alliance",
        restriction_func: exportObj.hugeOnly
      }, {
        name: "R4-D6",
        id: 77,
        unique: true,
        slot: "Astromech",
        points: 1
      }, {
        name: "R5-P9",
        id: 78,
        unique: true,
        slot: "Astromech",
        points: 3
      }, {
        name: "WED-15 Repair Droid",
        id: 79,
        slot: "Crew",
        points: 2,
        restriction_func: exportObj.hugeOnly
      }, {
        name: "Carlist Rieekan",
        id: 80,
        unique: true,
        slot: "Crew",
        points: 3,
        faction: "Rebel Alliance",
        restriction_func: exportObj.hugeOnly
      }, {
        name: "Jan Dodonna",
        id: 81,
        unique: true,
        slot: "Crew",
        points: 6,
        faction: "Rebel Alliance",
        restriction_func: exportObj.hugeOnly
      }, {
        name: "Expanded Cargo Hold",
        id: 82,
        slot: "Cargo",
        points: 1,
        ship: "GR-75 Medium Transport"
      }, {
        name: "Backup Shield Generator",
        id: 83,
        slot: "Cargo",
        limited: true,
        points: 3
      }, {
        name: "EM Emitter",
        id: 84,
        slot: "Cargo",
        limited: true,
        points: 3
      }, {
        name: "Frequency Jammer",
        id: 85,
        slot: "Cargo",
        limited: true,
        points: 4
      }, {
        name: "Han Solo",
        id: 86,
        slot: "Crew",
        unique: true,
        faction: "Rebel Alliance",
        points: 2
      }, {
        name: "Leia Organa",
        id: 87,
        slot: "Crew",
        unique: true,
        faction: "Rebel Alliance",
        points: 4
      }, {
        name: "Targeting Coordinator",
        id: 88,
        slot: "Crew",
        limited: true,
        points: 4
      }, {
        name: "Raymus Antilles",
        id: 89,
        slot: "Crew",
        unique: true,
        faction: "Rebel Alliance",
        points: 6,
        restriction_func: exportObj.hugeOnly
      }, {
        name: "Gunnery Team",
        id: 90,
        slot: "Team",
        limited: true,
        points: 4
      }, {
        name: "Sensor Team",
        id: 91,
        slot: "Team",
        points: 4
      }, {
        name: "Engineering Team",
        id: 92,
        slot: "Team",
        limited: true,
        points: 4
      }, {
        name: "Lando Calrissian",
        id: 93,
        slot: "Crew",
        unique: true,
        faction: "Rebel Alliance",
        points: 3
      }, {
        name: "Mara Jade",
        id: 94,
        slot: "Crew",
        unique: true,
        faction: "Galactic Empire",
        points: 3
      }, {
        name: "Fleet Officer",
        id: 95,
        slot: "Crew",
        faction: "Galactic Empire",
        points: 3
      }, {
        name: "Stay On Target",
        id: 96,
        slot: "Elite",
        points: 2
      }, {
        name: "Dash Rendar",
        id: 97,
        unique: true,
        slot: "Crew",
        points: 2,
        faction: "Rebel Alliance"
      }, {
        name: "Lone Wolf",
        id: 98,
        unique: true,
        slot: "Elite",
        points: 2
      }, {
        name: '"Leebo"',
        id: 99,
        unique: true,
        slot: "Crew",
        points: 2,
        faction: "Rebel Alliance"
      }, {
        name: "Ruthlessness",
        id: 100,
        slot: "Elite",
        points: 3,
        faction: "Galactic Empire"
      }, {
        name: "Intimidation",
        id: 101,
        slot: "Elite",
        points: 2
      }, {
        name: "Ysanne Isard",
        id: 102,
        unique: true,
        slot: "Crew",
        points: 4,
        faction: "Galactic Empire"
      }, {
        name: "Moff Jerjerrod",
        id: 103,
        unique: true,
        slot: "Crew",
        points: 2,
        faction: "Galactic Empire"
      }, {
        name: "Ion Torpedoes",
        id: 104,
        slot: "Torpedo",
        points: 5,
        attack: 4,
        range: "2-3"
      }, {
        name: "Bodyguard",
        id: 105,
        unique: true,
        slot: "Elite",
        points: 2,
        faction: "Scum and Villainy"
      }, {
        name: "Calculation",
        id: 106,
        slot: "Elite",
        points: 1
      }, {
        name: "Accuracy Corrector",
        id: 107,
        slot: "System",
        points: 3
      }, {
        name: "Inertial Dampeners",
        id: 108,
        slot: "Illicit",
        points: 1
      }, {
        name: "Flechette Cannon",
        id: 109,
        slot: "Cannon",
        points: 2,
        attack: 3,
        range: "1-3"
      }, {
        name: '"Mangler" Cannon',
        id: 110,
        slot: "Cannon",
        points: 4,
        attack: 3,
        range: "1-3"
      }, {
        name: "Dead Man's Switch",
        id: 111,
        slot: "Illicit",
        points: 2
      }, {
        name: "Feedback Array",
        id: 112,
        slot: "Illicit",
        points: 2
      }, {
        name: '"Hot Shot" Blaster',
        id: 113,
        slot: "Illicit",
        points: 3,
        attack: 3,
        range: "1-2"
      }, {
        name: "Greedo",
        id: 114,
        unique: true,
        slot: "Crew",
        faction: "Scum and Villainy",
        points: 1
      }, {
        name: "Salvaged Astromech",
        id: 115,
        slot: "Salvaged Astromech",
        points: 2
      }, {
        name: "Bomb Loadout",
        id: 116,
        limited: true,
        slot: "Torpedo",
        points: 0,
        ship: "Y-Wing",
        confersAddons: [
          {
            type: exportObj.Upgrade,
            slot: "Bomb"
          }
        ]
      }, {
        name: '"Genius"',
        id: 117,
        unique: true,
        slot: "Salvaged Astromech",
        points: 0
      }, {
        name: "Unhinged Astromech",
        id: 118,
        slot: "Salvaged Astromech",
        points: 1,
        modifier_func: function(stats) {
          var turn, _i, _ref, _results;
          if ((stats.maneuvers != null) && stats.maneuvers.length > 3) {
            _results = [];
            for (turn = _i = 0, _ref = stats.maneuvers[3].length; 0 <= _ref ? _i < _ref : _i > _ref; turn = 0 <= _ref ? ++_i : --_i) {
              if (stats.maneuvers[3][turn] > 0) {
                _results.push(stats.maneuvers[3][turn] = 2);
              } else {
                _results.push(void 0);
              }
            }
            return _results;
          }
        }
      }, {
        name: "R4-B11",
        id: 119,
        unique: true,
        slot: "Salvaged Astromech",
        points: 3
      }, {
        name: "Autoblaster Turret",
        id: 120,
        slot: "Turret",
        points: 2,
        attack: 2,
        range: "1"
      }, {
        name: "R4 Agromech",
        id: 121,
        slot: "Salvaged Astromech",
        points: 2
      }, {
        name: "K4 Security Droid",
        id: 122,
        slot: "Crew",
        faction: "Scum and Villainy",
        points: 3
      }, {
        name: "Outlaw Tech",
        id: 123,
        limited: true,
        slot: "Crew",
        faction: "Scum and Villainy",
        points: 2
      }, {
        name: 'Advanced Targeting Computer',
        canonical_name: 'Adv. Targeting Computer'.canonicalize(),
        id: 124,
        slot: "System",
        points: 5,
        ship: "TIE Advanced"
      }, {
        name: 'Ion Cannon Battery',
        id: 125,
        slot: "Hardpoint",
        points: 6,
        energy: 2,
        attack: 4,
        range: "2-4"
      }, {
        name: "Extra Munitions",
        id: 126,
        slot: "Torpedo",
        limited: true,
        points: 2
      }, {
        name: "Cluster Mines",
        id: 127,
        slot: "Bomb",
        points: 4
      }, {
        name: 'Glitterstim',
        id: 128,
        slot: "Illicit",
        points: 2
      }, {
        name: 'Grand Moff Tarkin',
        unique: true,
        id: 129,
        slot: "Crew",
        points: 6,
        faction: "Galactic Empire",
        restriction_func: function(ship) {
          var _ref;
          return (_ref = ship.data.huge) != null ? _ref : false;
        }
      }, {
        name: 'Captain Needa',
        unique: true,
        id: 130,
        slot: "Crew",
        points: 2,
        faction: "Galactic Empire",
        restriction_func: function(ship) {
          var _ref;
          return (_ref = ship.data.huge) != null ? _ref : false;
        }
      }, {
        name: 'Admiral Ozzel',
        unique: true,
        id: 131,
        slot: "Crew",
        points: 2,
        faction: "Galactic Empire",
        restriction_func: function(ship) {
          var _ref;
          return (_ref = ship.data.huge) != null ? _ref : false;
        }
      }, {
        name: 'Emperor Palpatine',
        unique: true,
        id: 132,
        slot: "Crew",
        points: 8,
        faction: "Galactic Empire",
        restriction_func: function(ship, upgrade_obj) {
          return ship.hasAnotherUnoccupiedSlotLike(upgrade_obj);
        },
        validation_func: function(ship, upgrade_obj) {
          return upgrade_obj.occupiesAnotherUpgradeSlot();
        },
        also_occupies_upgrades: ["Crew"]
      }, {
        name: 'Bossk',
        unique: true,
        id: 133,
        faction: "Scum and Villainy",
        slot: "Crew",
        points: 2
      }, {
        name: "Lightning Reflexes",
        id: 134,
        slot: "Elite",
        points: 1,
        restriction_func: function(ship) {
          var _ref, _ref1;
          return !(((_ref = ship.data.large) != null ? _ref : false) || ((_ref1 = ship.data.huge) != null ? _ref1 : false));
        }
      }, {
        name: "Twin Laser Turret",
        id: 135,
        slot: "Turret",
        points: 6,
        attack: 3,
        range: "2-3"
      }, {
        name: "Plasma Torpedoes",
        id: 136,
        slot: "Torpedo",
        points: 3,
        attack: 4,
        range: "2-3"
      }, {
        name: "Ion Bombs",
        id: 137,
        slot: "Bomb",
        points: 2
      }, {
        name: "Conner Net",
        id: 138,
        slot: "Bomb",
        points: 4
      }, {
        name: "Bombardier",
        id: 139,
        slot: "Crew",
        points: 1
      }, {
        name: 'Crack Shot',
        id: 140,
        slot: 'Elite',
        points: 1
      }, {
        name: "Advanced Homing Missiles",
        canonical_name: 'Adv. Homing Missiles'.canonicalize(),
        id: 141,
        slot: "Missile",
        points: 3,
        attack: 3,
        range: "2"
      }, {
        name: 'Agent Kallus',
        id: 142,
        unique: true,
        points: 2,
        slot: 'Crew',
        faction: 'Galactic Empire'
      }, {
        name: 'XX-23 S-Thread Tracers',
        id: 143,
        points: 1,
        slot: 'Missile',
        attack: 3,
        range: '1-3'
      }, {
        name: "Tractor Beam",
        id: 144,
        slot: "Cannon",
        attack: 3,
        range: "1-3",
        points: 1
      }, {
        name: "Cloaking Device",
        id: 145,
        unique: true,
        slot: "Illicit",
        points: 2,
        restriction_func: function(ship) {
          var _ref, _ref1;
          return !(((_ref = ship.data.large) != null ? _ref : false) || ((_ref1 = ship.data.huge) != null ? _ref1 : false));
        }
      }, {
        name: 'Shield Technician',
        id: 146,
        slot: "Crew",
        points: 1,
        restriction_func: function(ship) {
          var _ref;
          return (_ref = ship.data.huge) != null ? _ref : false;
        }
      }, {
        name: 'Weapons Guidance',
        id: 147,
        slot: "Tech",
        points: 2
      }, {
        name: 'BB-8',
        id: 148,
        unique: true,
        slot: "Astromech",
        points: 2
      }, {
        name: 'R5-X3',
        id: 149,
        unique: true,
        slot: "Astromech",
        points: 1
      }, {
        name: 'Wired',
        id: 150,
        slot: "Elite",
        points: 1
      }, {
        name: 'Cool Hand',
        id: 151,
        slot: 'Elite',
        points: 1
      }, {
        name: 'Juke',
        id: 152,
        slot: 'Elite',
        points: 2,
        restriction_func: function(ship) {
          var _ref, _ref1;
          return !(((_ref = ship.data.large) != null ? _ref : false) || ((_ref1 = ship.data.huge) != null ? _ref1 : false));
        }
      }, {
        name: 'Comm Relay',
        id: 153,
        slot: 'Tech',
        points: 3
      }, {
        name: 'Dual Laser Turret',
        id: 154,
        points: 5,
        slot: 'Hardpoint',
        attack: 3,
        range: '1-3',
        energy: 1,
        ship: 'Gozanti-class Cruiser'
      }, {
        name: 'Broadcast Array',
        id: 155,
        ship: 'Gozanti-class Cruiser',
        points: 2,
        slot: 'Cargo',
        modifier_func: function(stats) {
          if (__indexOf.call(stats.actions, 'Jam') < 0) {
            return stats.actions.push('Jam');
          }
        }
      }, {
        name: 'Rear Admiral Chiraneau',
        id: 156,
        unique: true,
        points: 3,
        slot: 'Crew',
        faction: 'Galactic Empire',
        restriction_func: function(ship) {
          var _ref;
          return (_ref = ship.data.huge) != null ? _ref : false;
        }
      }, {
        name: 'Ordnance Experts',
        id: 157,
        limited: true,
        points: 5,
        slot: 'Team'
      }, {
        name: 'Docking Clamps',
        id: 158,
        points: 0,
        limited: true,
        slot: 'Cargo',
        ship: 'Gozanti-class Cruiser'
      }, {
        name: 'Kanan Jarrus',
        id: 159,
        unique: true,
        faction: 'Rebel Alliance',
        points: 3,
        slot: 'Crew'
      }, {
        name: '"Zeb" Orrelios',
        id: 160,
        unique: true,
        faction: 'Rebel Alliance',
        points: 1,
        slot: 'Crew'
      }, {
        name: 'Reinforced Deflectors',
        id: 161,
        points: 3,
        slot: 'System',
        restriction_func: function(ship) {
          var _ref;
          return (_ref = ship.data.large) != null ? _ref : false;
        }
      }, {
        name: 'Dorsal Turret',
        id: 162,
        points: 3,
        slot: 'Turret',
        attack: 2,
        range: '1-2'
      }, {
        name: 'Targeting Astromech',
        id: 163,
        slot: 'Astromech',
        points: 2
      }, {
        name: 'Hera Syndulla',
        id: 164,
        unique: true,
        faction: 'Rebel Alliance',
        points: 1,
        slot: 'Crew'
      }, {
        name: 'Ezra Bridger',
        id: 165,
        unique: true,
        faction: 'Rebel Alliance',
        points: 3,
        slot: 'Crew'
      }, {
        name: 'Sabine Wren',
        id: 166,
        unique: true,
        faction: 'Rebel Alliance',
        points: 2,
        slot: 'Crew',
        confersAddons: [
          {
            type: exportObj.Upgrade,
            slot: "Bomb"
          }
        ]
      }, {
        name: '"Chopper"',
        id: 167,
        unique: true,
        faction: 'Rebel Alliance',
        points: 0,
        slot: 'Crew'
      }, {
        name: 'Construction Droid',
        id: 168,
        points: 3,
        slot: 'Crew',
        limited: true,
        restriction_func: function(ship) {
          var _ref;
          return (_ref = ship.data.huge) != null ? _ref : false;
        }
      }, {
        name: 'Cluster Bombs',
        id: 169,
        points: 4,
        slot: 'Cargo'
      }, {
        name: "Adaptability",
        id: 170,
        slot: "Elite",
        points: 0
      }, {
        name: "Adaptability (old)",
        skip: true,
        id: 171,
        superseded_by_id: 170,
        slot: "Elite",
        points: 0
      }, {
        name: "Electronic Baffle",
        id: 172,
        slot: "System",
        points: 1
      }, {
        name: "4-LOM",
        id: 173,
        unique: true,
        slot: "Crew",
        points: 1,
        faction: "Scum and Villainy"
      }, {
        name: "Zuckuss",
        id: 174,
        unique: true,
        slot: "Crew",
        points: 1,
        faction: "Scum and Villainy"
      }, {
        name: 'Rage',
        id: 175,
        points: 1,
        slot: 'Elite'
      }, {
        name: "Attanni Mindlink",
        id: 176,
        faction: "Scum and Villainy",
        slot: "Elite",
        points: 1
      }, {
        name: "Boba Fett",
        id: 177,
        unique: true,
        slot: "Crew",
        points: 1,
        faction: "Scum and Villainy"
      }, {
        name: "Dengar",
        id: 178,
        unique: true,
        slot: "Crew",
        points: 3,
        faction: "Scum and Villainy"
      }, {
        name: '"Gonk"',
        id: 179,
        unique: true,
        slot: "Crew",
        faction: "Scum and Villainy",
        points: 2
      }, {
        name: "R5-P8",
        id: 180,
        unique: true,
        slot: "Salvaged Astromech",
        points: 3
      }, {
        name: 'Thermal Detonators',
        id: 181,
        points: 3,
        slot: 'Bomb'
      }, {
        name: "Overclocked R4",
        id: 182,
        slot: "Salvaged Astromech",
        points: 1
      }, {
        name: 'Systems Officer',
        id: 183,
        faction: 'Galactic Empire',
        limited: true,
        points: 2,
        slot: 'Crew'
      }
    ],
    modificationsById: [
      {
        name: "Zero modification",
        id: 0,
        skip: true
      }, {
        name: "Stealth Device",
        id: 1,
        points: 3,
        modifier_func: function(stats) {
          return stats.agility += 1;
        }
      }, {
        name: "Shield Upgrade",
        id: 2,
        points: 4,
        modifier_func: function(stats) {
          return stats.shields += 1;
        }
      }, {
        name: "Engine Upgrade",
        id: 3,
        points: 4,
        modifier_func: function(stats) {
          if (__indexOf.call(stats.actions, 'Boost') < 0) {
            return stats.actions.push('Boost');
          }
        }
      }, {
        name: "Anti-Pursuit Lasers",
        id: 4,
        points: 2,
        restriction_func: function(ship) {
          var _ref;
          return (_ref = ship.data.large) != null ? _ref : false;
        }
      }, {
        name: "Targeting Computer",
        id: 5,
        points: 2,
        modifier_func: function(stats) {
          if (__indexOf.call(stats.actions, 'Target Lock') < 0) {
            return stats.actions.push('Target Lock');
          }
        }
      }, {
        name: "Hull Upgrade",
        id: 6,
        points: 3,
        modifier_func: function(stats) {
          return stats.hull += 1;
        }
      }, {
        name: "Munitions Failsafe",
        id: 7,
        points: 1
      }, {
        name: "Stygium Particle Accelerator",
        id: 8,
        points: 2
      }, {
        name: "Advanced Cloaking Device",
        id: 9,
        points: 4,
        ship: "TIE Phantom"
      }, {
        name: "Combat Retrofit",
        id: 10,
        points: 10,
        ship: "GR-75 Medium Transport",
        huge: true,
        modifier_func: function(stats) {
          stats.hull += 2;
          return stats.shields += 1;
        }
      }, {
        name: "B-Wing/E2",
        id: 11,
        points: 1,
        ship: "B-Wing",
        confersAddons: [
          {
            type: exportObj.Upgrade,
            slot: "Crew"
          }
        ]
      }, {
        name: "Countermeasures",
        id: 12,
        points: 3,
        restriction_func: function(ship) {
          var _ref;
          return (_ref = ship.data.large) != null ? _ref : false;
        }
      }, {
        name: "Experimental Interface",
        id: 13,
        unique: true,
        points: 3
      }, {
        name: "Tactical Jammer",
        id: 14,
        points: 1,
        restriction_func: function(ship) {
          var _ref;
          return (_ref = ship.data.large) != null ? _ref : false;
        }
      }, {
        name: "Autothrusters",
        id: 15,
        points: 2,
        restriction_func: function(ship) {
          return __indexOf.call(ship.effectiveStats().actions, "Boost") >= 0;
        }
      }, {
        name: "Advanced SLAM",
        id: 16,
        points: 2
      }, {
        name: "Twin Ion Engine Mk. II",
        id: 17,
        points: 1,
        restriction_func: function(ship) {
          return ship.data.name.indexOf('TIE') !== -1;
        },
        modifier_func: function(stats) {
          var s, _i, _len, _ref, _ref1, _results;
          _ref1 = (_ref = stats.maneuvers) != null ? _ref : [];
          _results = [];
          for (_i = 0, _len = _ref1.length; _i < _len; _i++) {
            s = _ref1[_i];
            if (s[1] !== 0) {
              s[1] = 2;
            }
            if (s[3] !== 0) {
              _results.push(s[3] = 2);
            } else {
              _results.push(void 0);
            }
          }
          return _results;
        }
      }, {
        name: "Maneuvering Fins",
        id: 18,
        points: 1,
        ship: "YV-666"
      }, {
        name: "Ion Projector",
        id: 19,
        points: 2,
        restriction_func: function(ship) {
          var _ref;
          return (_ref = ship.data.large) != null ? _ref : false;
        }
      }, {
        name: 'Integrated Astromech',
        id: 20,
        restriction_func: function(ship) {
          return ship.data.canonical_name.indexOf('xwing') !== -1;
        },
        points: 0
      }, {
        name: 'Optimized Generators',
        id: 21,
        points: 5,
        restriction_func: function(ship) {
          var _ref;
          return (_ref = ship.data.huge) != null ? _ref : false;
        }
      }, {
        name: 'Automated Protocols',
        id: 22,
        points: 5,
        restriction_func: function(ship) {
          var _ref;
          return (_ref = ship.data.huge) != null ? _ref : false;
        }
      }, {
        name: 'Ordnance Tubes',
        id: 23,
        points: 5,
        slot: 'Hardpoint',
        restriction_func: function(ship) {
          var _ref;
          return (_ref = ship.data.huge) != null ? _ref : false;
        }
      }, {
        name: 'Long-Range Scanners',
        id: 24,
        points: 0,
        restriction_func: function(ship) {
          var upgrade;
          return (((function() {
            var _i, _len, _ref, _results;
            _ref = ship.upgrades;
            _results = [];
            for (_i = 0, _len = _ref.length; _i < _len; _i++) {
              upgrade = _ref[_i];
              if (upgrade.slot === 'Torpedo' && (upgrade.occupied_by == null)) {
                _results.push(upgrade);
              }
            }
            return _results;
          })()).length >= 1) && (((function() {
            var _i, _len, _ref, _results;
            _ref = ship.upgrades;
            _results = [];
            for (_i = 0, _len = _ref.length; _i < _len; _i++) {
              upgrade = _ref[_i];
              if (upgrade.slot === 'Missile' && (upgrade.occupied_by == null)) {
                _results.push(upgrade);
              }
            }
            return _results;
          })()).length >= 1);
        }
      }, {
        name: "Guidance Chips",
        id: 25,
        points: 0
      }
    ],
    titlesById: [
      {
        name: "Zero Title",
        id: 0,
        skip: true
      }, {
        name: "Slave I",
        id: 1,
        unique: true,
        points: 0,
        ship: "Firespray-31",
        confersAddons: [
          {
            type: exportObj.Upgrade,
            slot: "Torpedo"
          }
        ]
      }, {
        name: "Millennium Falcon",
        id: 2,
        unique: true,
        points: 1,
        ship: "YT-1300",
        actions: "Evade",
        modifier_func: function(stats) {
          if (__indexOf.call(stats.actions, 'Evade') < 0) {
            return stats.actions.push('Evade');
          }
        }
      }, {
        name: "Moldy Crow",
        id: 3,
        unique: true,
        points: 3,
        ship: "HWK-290"
      }, {
        name: "ST-321",
        id: 4,
        unique: true,
        points: 3,
        ship: "Lambda-Class Shuttle"
      }, {
        name: "Royal Guard TIE",
        id: 5,
        points: 0,
        ship: "TIE Interceptor",
        confersAddons: [
          {
            type: exportObj.Modification
          }
        ],
        restriction_func: function(ship) {
          return ship.effectiveStats().skill > 4;
        },
        special_case: 'Royal Guard TIE'
      }, {
        name: "Dodonna's Pride",
        id: 6,
        unique: true,
        points: 4,
        ship: "CR90 Corvette (Fore)"
      }, {
        name: "A-Wing Test Pilot",
        id: 7,
        points: 0,
        ship: "A-Wing",
        restriction_func: function(ship) {
          return ship.effectiveStats().skill > 1;
        },
        validation_func: function(ship, upgrade_obj) {
          var elite, elites, upgrade;
          if (!(ship.effectiveStats().skill > 1)) {
            return false;
          }
          elites = (function() {
            var _i, _len, _ref, _results;
            _ref = ship.upgrades;
            _results = [];
            for (_i = 0, _len = _ref.length; _i < _len; _i++) {
              upgrade = _ref[_i];
              if (upgrade.slot === 'Elite' && (upgrade.data != null)) {
                _results.push(upgrade.data.canonical_name);
              }
            }
            return _results;
          })();
          while (elites.length > 0) {
            elite = elites.pop();
            if (__indexOf.call(elites, elite) >= 0) {
              return false;
            }
          }
          return true;
        },
        confersAddons: [
          {
            type: exportObj.Upgrade,
            slot: "Elite"
          }
        ],
        special_case: "A-Wing Test Pilot"
      }, {
        name: "B-Wing/E",
        id: 8,
        skip: true,
        points: 99,
        ship: "B-Wing",
        confersAddons: [
          {
            type: exportObj.Upgrade,
            slot: "Crew"
          }
        ]
      }, {
        name: "Tantive IV",
        id: 9,
        unique: true,
        points: 4,
        ship: "CR90 Corvette (Fore)",
        confersAddons: [
          {
            type: exportObj.Upgrade,
            slot: "Crew"
          }, {
            type: exportObj.Upgrade,
            slot: "Team"
          }
        ]
      }, {
        name: "Bright Hope",
        id: 10,
        energy: "+2",
        unique: true,
        points: 5,
        ship: "GR-75 Medium Transport",
        modifier_func: function(stats) {
          return stats.energy += 2;
        }
      }, {
        name: "Quantum Storm",
        id: 11,
        energy: "+1",
        unique: true,
        points: 4,
        ship: "GR-75 Medium Transport",
        modifier_func: function(stats) {
          return stats.energy += 1;
        }
      }, {
        name: "Dutyfree",
        id: 12,
        energy: "+0",
        unique: true,
        points: 2,
        ship: "GR-75 Medium Transport"
      }, {
        name: "Jaina's Light",
        id: 13,
        unique: true,
        points: 2,
        ship: "CR90 Corvette (Fore)"
      }, {
        name: "Outrider",
        id: 14,
        unique: true,
        points: 5,
        ship: "YT-2400"
      }, {
        name: "Dauntless",
        id: 15,
        unique: true,
        points: 2,
        ship: "VT-49 Decimator"
      }, {
        name: "Virago",
        id: 16,
        unique: true,
        points: 1,
        ship: "StarViper",
        restriction_func: function(ship) {
          return ship.pilot.skill > 3;
        },
        confersAddons: [
          {
            type: exportObj.Upgrade,
            slot: "System"
          }, {
            type: exportObj.Upgrade,
            slot: "Illicit"
          }
        ]
      }, {
        name: '"Heavy Scyk" Interceptor (Cannon)',
        canonical_name: '"Heavy Scyk" Interceptor'.canonicalize(),
        id: 17,
        points: 2,
        ship: "M3-A Interceptor",
        confersAddons: [
          {
            type: exportObj.Upgrade,
            slot: "Cannon"
          }
        ]
      }, {
        name: '"Heavy Scyk" Interceptor (Torpedo)',
        canonical_name: '"Heavy Scyk" Interceptor'.canonicalize(),
        id: 18,
        points: 2,
        ship: "M3-A Interceptor",
        confersAddons: [
          {
            type: exportObj.Upgrade,
            slot: "Torpedo"
          }
        ]
      }, {
        name: '"Heavy Scyk" Interceptor (Missile)',
        canonical_name: '"Heavy Scyk" Interceptor'.canonicalize(),
        id: 19,
        points: 2,
        ship: "M3-A Interceptor",
        confersAddons: [
          {
            type: exportObj.Upgrade,
            slot: "Missile"
          }
        ]
      }, {
        name: 'IG-2000',
        id: 20,
        points: 0,
        ship: "Aggressor"
      }, {
        name: "BTL-A4 Y-Wing",
        id: 21,
        points: 0,
        ship: "Y-Wing"
      }, {
        name: "Andrasta",
        id: 22,
        unique: true,
        points: 0,
        ship: "Firespray-31",
        confersAddons: [
          {
            type: exportObj.Upgrade,
            slot: "Bomb"
          }, {
            type: exportObj.Upgrade,
            slot: "Bomb"
          }
        ]
      }, {
        name: 'TIE/x1',
        id: 23,
        points: 0,
        ship: "TIE Advanced",
        confersAddons: [
          {
            type: exportObj.Upgrade,
            slot: "System",
            adjustment_func: function(upgrade) {
              var copy;
              copy = $.extend(true, {}, upgrade);
              copy.points = Math.max(0, copy.points - 4);
              return copy;
            }
          }
        ]
      }, {
        name: "Hound's Tooth",
        id: 24,
        points: 6,
        unique: true,
        ship: "YV-666"
      }, {
        name: "Ghost",
        id: 25,
        unique: true,
        points: 0,
        ship: "VCX-100"
      }, {
        name: "Phantom",
        id: 26,
        unique: true,
        points: 0,
        ship: "Attack Shuttle"
      }, {
        name: "TIE/v1",
        id: 27,
        points: 1,
        ship: "TIE Advanced Prototype"
      }, {
        name: "Mist Hunter",
        id: 28,
        unique: true,
        points: 0,
        ship: "G-1A Starfighter",
        confersAddons: [
          {
            type: exportObj.RestrictedUpgrade,
            slot: "Cannon",
            filter_func: function(upgrade) {
              return upgrade.english_name === 'Tractor Beam';
            },
            auto_equip: 144
          }
        ],
        modifier_func: function(stats) {
          if (__indexOf.call(stats.actions, 'Barrel Roll') < 0) {
            return stats.actions.push('Barrel Roll');
          }
        }
      }, {
        name: "Punishing One",
        id: 29,
        unique: true,
        points: 12,
        ship: "JumpMaster 5000",
        modifier_func: function(stats) {
          return stats.attack += 1;
        }
      }, {
        name: 'Assailer',
        id: 30,
        points: 2,
        unique: true,
        ship: "Raider-class Corvette (Aft)"
      }, {
        name: 'Instigator',
        id: 31,
        points: 4,
        unique: true,
        ship: "Raider-class Corvette (Aft)"
      }, {
        name: 'Impetuous',
        id: 32,
        points: 3,
        unique: true,
        ship: "Raider-class Corvette (Aft)"
      }, {
        name: 'TIE/x7',
        id: 33,
        ship: 'TIE Defender',
        points: -2,
        unequips_upgrades: ['Cannon', 'Missile'],
        also_occupies_upgrades: ['Cannon', 'Missile']
      }, {
        name: 'TIE/D',
        id: 34,
        ship: 'TIE Defender',
        points: 0
      }, {
        name: 'TIE Shuttle',
        id: 35,
        ship: 'TIE Bomber',
        points: 0,
        unequips_upgrades: ['Torpedo', 'Torpedo', 'Missile', 'Missile', 'Bomb'],
        also_occupies_upgrades: ['Torpedo', 'Torpedo', 'Missile', 'Missile', 'Bomb'],
        confersAddons: [
          {
            type: exportObj.RestrictedUpgrade,
            slot: 'Crew',
            filter_func: function(upgrade) {
              return upgrade.points <= 4;
            }
          }, {
            type: exportObj.RestrictedUpgrade,
            slot: 'Crew',
            filter_func: function(upgrade) {
              return upgrade.points <= 4;
            }
          }
        ]
      }, {
        name: 'Requiem',
        id: 36,
        unique: true,
        ship: 'Gozanti-class Cruiser',
        energy: '+0',
        points: 4
      }, {
        name: 'Vector',
        id: 37,
        unique: true,
        ship: 'Gozanti-class Cruiser',
        energy: '+1',
        points: 2,
        modifier_func: function(stats) {
          return stats.energy += 1;
        }
      }, {
        name: 'Suppressor',
        id: 38,
        unique: true,
        ship: 'Gozanti-class Cruiser',
        energy: '+2',
        points: 6,
        modifier_func: function(stats) {
          return stats.energy += 2;
        }
      }, {
        name: 'Black One',
        id: 39,
        unique: true,
        ship: 'T-70 X-Wing',
        points: 1,
        restriction_func: function(ship) {
          return ship.effectiveStats().skill > 6;
        }
      }, {
        name: "Millennium Falcon (TFA)",
        canonical_name: "millenniumfalcon-swx57",
        id: 40,
        unique: true,
        points: 1,
        ship: "YT-1300"
      }, {
        name: 'Alliance Overhaul',
        id: 41,
        ship: 'ARC-170',
        points: 0
      }, {
        name: 'Special Ops Training',
        id: 42,
        ship: 'TIE/sf Fighter',
        points: 0
      }, {
        name: 'Concord Dawn Protector',
        id: 43,
        ship: 'Protectorate Starfighter',
        points: 1
      }, {
        name: 'Shadow Caster',
        id: 44,
        ship: 'Lancer-class Pursuit Craft',
        points: 3
      }
    ]
  };
};

exportObj.setupCardData = function(basic_cards, pilot_translations, upgrade_translations, modification_translations, title_translations) {
  var card, cards, e, expansion, field, i, modification, modification_data, modification_name, name, pilot, pilot_data, pilot_name, source, title, title_data, title_name, translation, translations, upgrade, upgrade_data, upgrade_name, _base, _base1, _base10, _base2, _base3, _base4, _base5, _base6, _base7, _base8, _base9, _i, _j, _k, _l, _len, _len1, _len10, _len11, _len12, _len2, _len3, _len4, _len5, _len6, _len7, _len8, _len9, _m, _n, _name, _name1, _name2, _name3, _name4, _name5, _name6, _name7, _name8, _o, _p, _q, _r, _ref, _ref1, _ref10, _ref11, _ref12, _ref13, _ref14, _ref15, _ref16, _ref17, _ref18, _ref19, _ref2, _ref20, _ref21, _ref22, _ref23, _ref24, _ref25, _ref3, _ref4, _ref5, _ref6, _ref7, _ref8, _ref9, _s, _t, _u;
  _ref = basic_cards.pilotsById;
  for (i = _i = 0, _len = _ref.length; _i < _len; i = ++_i) {
    pilot_data = _ref[i];
    if (pilot_data.id !== i) {
      throw new Error("ID mismatch: pilot at index " + i + " has ID " + pilot_data.id);
    }
  }
  _ref1 = basic_cards.upgradesById;
  for (i = _j = 0, _len1 = _ref1.length; _j < _len1; i = ++_j) {
    upgrade_data = _ref1[i];
    if (upgrade_data.id !== i) {
      throw new Error("ID mismatch: upgrade at index " + i + " has ID " + upgrade_data.id);
    }
  }
  _ref2 = basic_cards.titlesById;
  for (i = _k = 0, _len2 = _ref2.length; _k < _len2; i = ++_k) {
    title_data = _ref2[i];
    if (title_data.id !== i) {
      throw new Error("ID mismatch: title at index " + i + " has ID " + title_data.id);
    }
  }
  _ref3 = basic_cards.modificationsById;
  for (i = _l = 0, _len3 = _ref3.length; _l < _len3; i = ++_l) {
    modification_data = _ref3[i];
    if (modification_data.id !== i) {
      throw new Error("ID mismatch: modification at index " + i + " has ID " + modification_data.id);
    }
  }
  exportObj.pilots = {};
  _ref4 = basic_cards.pilotsById;
  for (_m = 0, _len4 = _ref4.length; _m < _len4; _m++) {
    pilot_data = _ref4[_m];
    if (pilot_data.skip == null) {
      pilot_data.sources = [];
      pilot_data.english_name = pilot_data.name;
      pilot_data.english_ship = pilot_data.ship;
      if (pilot_data.canonical_name == null) {
        pilot_data.canonical_name = pilot_data.english_name.canonicalize();
      }
      exportObj.pilots[pilot_data.name] = pilot_data;
    }
  }
  for (pilot_name in pilot_translations) {
    translations = pilot_translations[pilot_name];
    for (field in translations) {
      translation = translations[field];
      try {
        exportObj.pilots[pilot_name][field] = translation;
      } catch (_error) {
        e = _error;
        console.error("Cannot find translation for attribute " + field + " for pilot " + pilot_name);
        throw e;
      }
    }
  }
  exportObj.upgrades = {};
  _ref5 = basic_cards.upgradesById;
  for (_n = 0, _len5 = _ref5.length; _n < _len5; _n++) {
    upgrade_data = _ref5[_n];
    if (upgrade_data.skip == null) {
      upgrade_data.sources = [];
      upgrade_data.english_name = upgrade_data.name;
      if (upgrade_data.canonical_name == null) {
        upgrade_data.canonical_name = upgrade_data.english_name.canonicalize();
      }
      exportObj.upgrades[upgrade_data.name] = upgrade_data;
    }
  }
  for (upgrade_name in upgrade_translations) {
    translations = upgrade_translations[upgrade_name];
    for (field in translations) {
      translation = translations[field];
      try {
        exportObj.upgrades[upgrade_name][field] = translation;
      } catch (_error) {
        e = _error;
        console.error("Cannot find translation for attribute " + field + " for upgrade " + upgrade_name);
        throw e;
      }
    }
  }
  exportObj.modifications = {};
  _ref6 = basic_cards.modificationsById;
  for (_o = 0, _len6 = _ref6.length; _o < _len6; _o++) {
    modification_data = _ref6[_o];
    if (modification_data.skip == null) {
      modification_data.sources = [];
      modification_data.english_name = modification_data.name;
      if (modification_data.canonical_name == null) {
        modification_data.canonical_name = modification_data.english_name.canonicalize();
      }
      exportObj.modifications[modification_data.name] = modification_data;
    }
  }
  for (modification_name in modification_translations) {
    translations = modification_translations[modification_name];
    for (field in translations) {
      translation = translations[field];
      try {
        exportObj.modifications[modification_name][field] = translation;
      } catch (_error) {
        e = _error;
        console.error("Cannot find translation for attribute " + field + " for modification " + modification_name);
        throw e;
      }
    }
  }
  exportObj.titles = {};
  _ref7 = basic_cards.titlesById;
  for (_p = 0, _len7 = _ref7.length; _p < _len7; _p++) {
    title_data = _ref7[_p];
    if (title_data.skip == null) {
      title_data.sources = [];
      title_data.english_name = title_data.name;
      if (title_data.canonical_name == null) {
        title_data.canonical_name = title_data.english_name.canonicalize();
      }
      exportObj.titles[title_data.name] = title_data;
    }
  }
  for (title_name in title_translations) {
    translations = title_translations[title_name];
    for (field in translations) {
      translation = translations[field];
      try {
        exportObj.titles[title_name][field] = translation;
      } catch (_error) {
        e = _error;
        console.error("Cannot find translation for attribute " + field + " for title " + title_name);
        throw e;
      }
    }
  }
  _ref8 = exportObj.manifestByExpansion;
  for (expansion in _ref8) {
    cards = _ref8[expansion];
    for (_q = 0, _len8 = cards.length; _q < _len8; _q++) {
      card = cards[_q];
      if (card.skipForSource) {
        continue;
      }
      try {
        switch (card.type) {
          case 'pilot':
            exportObj.pilots[card.name].sources.push(expansion);
            break;
          case 'upgrade':
            exportObj.upgrades[card.name].sources.push(expansion);
            break;
          case 'modification':
            exportObj.modifications[card.name].sources.push(expansion);
            break;
          case 'title':
            exportObj.titles[card.name].sources.push(expansion);
            break;
          case 'ship':
            '';
            break;
          default:
            throw new Error("Unexpected card type " + card.type + " for card " + card.name + " of " + expansion);
        }
      } catch (_error) {
        e = _error;
        console.error("Error adding card " + card.name + " (" + card.type + ") from " + expansion);
      }
    }
  }
  _ref9 = exportObj.pilots;
  for (name in _ref9) {
    card = _ref9[name];
    card.sources = card.sources.sort();
  }
  _ref10 = exportObj.upgrades;
  for (name in _ref10) {
    card = _ref10[name];
    card.sources = card.sources.sort();
  }
  _ref11 = exportObj.modifications;
  for (name in _ref11) {
    card = _ref11[name];
    card.sources = card.sources.sort();
  }
  _ref12 = exportObj.titles;
  for (name in _ref12) {
    card = _ref12[name];
    card.sources = card.sources.sort();
  }
  exportObj.expansions = {};
  exportObj.pilotsById = {};
  exportObj.pilotsByLocalizedName = {};
  _ref13 = exportObj.pilots;
  for (pilot_name in _ref13) {
    pilot = _ref13[pilot_name];
    exportObj.fixIcons(pilot);
    exportObj.pilotsById[pilot.id] = pilot;
    exportObj.pilotsByLocalizedName[pilot.name] = pilot;
    _ref14 = pilot.sources;
    for (_r = 0, _len9 = _ref14.length; _r < _len9; _r++) {
      source = _ref14[_r];
      if (!(source in exportObj.expansions)) {
        exportObj.expansions[source] = 1;
      }
    }
  }
  if (Object.keys(exportObj.pilotsById).length !== Object.keys(exportObj.pilots).length) {
    throw new Error("At least one pilot shares an ID with another");
  }
  exportObj.pilotsByFactionCanonicalName = {};
  exportObj.pilotsByUniqueName = {};
  _ref15 = exportObj.pilots;
  for (pilot_name in _ref15) {
    pilot = _ref15[pilot_name];
    ((_base = ((_base1 = exportObj.pilotsByFactionCanonicalName)[_name1 = pilot.faction] != null ? _base1[_name1] : _base1[_name1] = {}))[_name = pilot.canonical_name] != null ? _base[_name] : _base[_name] = []).push(pilot);
    ((_base2 = exportObj.pilotsByUniqueName)[_name2 = pilot.canonical_name] != null ? _base2[_name2] : _base2[_name2] = []).push(pilot);
    switch (pilot.faction) {
      case 'Resistance':
        ((_base3 = ((_base4 = exportObj.pilotsByFactionCanonicalName)['Rebel Alliance'] != null ? _base4['Rebel Alliance'] : _base4['Rebel Alliance'] = {}))[_name3 = pilot.canonical_name] != null ? _base3[_name3] : _base3[_name3] = []).push(pilot);
        break;
      case 'First Order':
        ((_base5 = ((_base6 = exportObj.pilotsByFactionCanonicalName)['Galactic Empire'] != null ? _base6['Galactic Empire'] : _base6['Galactic Empire'] = {}))[_name4 = pilot.canonical_name] != null ? _base5[_name4] : _base5[_name4] = []).push(pilot);
    }
  }
  exportObj.upgradesById = {};
  exportObj.upgradesByLocalizedName = {};
  _ref16 = exportObj.upgrades;
  for (upgrade_name in _ref16) {
    upgrade = _ref16[upgrade_name];
    exportObj.fixIcons(upgrade);
    exportObj.upgradesById[upgrade.id] = upgrade;
    exportObj.upgradesByLocalizedName[upgrade.name] = upgrade;
    _ref17 = upgrade.sources;
    for (_s = 0, _len10 = _ref17.length; _s < _len10; _s++) {
      source = _ref17[_s];
      if (!(source in exportObj.expansions)) {
        exportObj.expansions[source] = 1;
      }
    }
  }
  if (Object.keys(exportObj.upgradesById).length !== Object.keys(exportObj.upgrades).length) {
    throw new Error("At least one upgrade shares an ID with another");
  }
  exportObj.upgradesBySlotCanonicalName = {};
  exportObj.upgradesBySlotUniqueName = {};
  _ref18 = exportObj.upgrades;
  for (upgrade_name in _ref18) {
    upgrade = _ref18[upgrade_name];
    ((_base7 = exportObj.upgradesBySlotCanonicalName)[_name5 = upgrade.slot] != null ? _base7[_name5] : _base7[_name5] = {})[upgrade.canonical_name] = upgrade;
    ((_base8 = exportObj.upgradesBySlotUniqueName)[_name6 = upgrade.slot] != null ? _base8[_name6] : _base8[_name6] = {})[upgrade.canonical_name] = upgrade;
  }
  exportObj.modificationsById = {};
  exportObj.modificationsByLocalizedName = {};
  _ref19 = exportObj.modifications;
  for (modification_name in _ref19) {
    modification = _ref19[modification_name];
    exportObj.fixIcons(modification);
    if (modification.huge != null) {
      if (modification.restriction_func == null) {
        modification.restriction_func = exportObj.hugeOnly;
      }
    } else if (modification.restriction_func == null) {
      modification.restriction_func = function(ship) {
        var _ref20;
        return !((_ref20 = ship.data.huge) != null ? _ref20 : false);
      };
    }
    exportObj.modificationsById[modification.id] = modification;
    exportObj.modificationsByLocalizedName[modification.name] = modification;
    _ref20 = modification.sources;
    for (_t = 0, _len11 = _ref20.length; _t < _len11; _t++) {
      source = _ref20[_t];
      if (!(source in exportObj.expansions)) {
        exportObj.expansions[source] = 1;
      }
    }
  }
  if (Object.keys(exportObj.modificationsById).length !== Object.keys(exportObj.modifications).length) {
    throw new Error("At least one modification shares an ID with another");
  }
  exportObj.modificationsByCanonicalName = {};
  exportObj.modificationsByUniqueName = {};
  _ref21 = exportObj.modifications;
  for (modification_name in _ref21) {
    modification = _ref21[modification_name];
    (exportObj.modificationsByCanonicalName != null ? exportObj.modificationsByCanonicalName : exportObj.modificationsByCanonicalName = {})[modification.canonical_name] = modification;
    (exportObj.modificationsByUniqueName != null ? exportObj.modificationsByUniqueName : exportObj.modificationsByUniqueName = {})[modification.canonical_name] = modification;
  }
  exportObj.titlesById = {};
  exportObj.titlesByLocalizedName = {};
  _ref22 = exportObj.titles;
  for (title_name in _ref22) {
    title = _ref22[title_name];
    exportObj.fixIcons(title);
    exportObj.titlesById[title.id] = title;
    exportObj.titlesByLocalizedName[title.name] = title;
    _ref23 = title.sources;
    for (_u = 0, _len12 = _ref23.length; _u < _len12; _u++) {
      source = _ref23[_u];
      if (!(source in exportObj.expansions)) {
        exportObj.expansions[source] = 1;
      }
    }
  }
  if (Object.keys(exportObj.titlesById).length !== Object.keys(exportObj.titles).length) {
    throw new Error("At least one title shares an ID with another");
  }
  exportObj.titlesByShip = {};
  _ref24 = exportObj.titles;
  for (title_name in _ref24) {
    title = _ref24[title_name];
    if (!(title.ship in exportObj.titlesByShip)) {
      exportObj.titlesByShip[title.ship] = [];
    }
    exportObj.titlesByShip[title.ship].push(title);
  }
  exportObj.titlesByCanonicalName = {};
  exportObj.titlesByUniqueName = {};
  _ref25 = exportObj.titles;
  for (title_name in _ref25) {
    title = _ref25[title_name];
    if (title.canonical_name === '"Heavy Scyk" Interceptor'.canonicalize()) {
      ((_base9 = (exportObj.titlesByCanonicalName != null ? exportObj.titlesByCanonicalName : exportObj.titlesByCanonicalName = {}))[_name7 = title.canonical_name] != null ? _base9[_name7] : _base9[_name7] = []).push(title);
      ((_base10 = (exportObj.titlesByUniqueName != null ? exportObj.titlesByUniqueName : exportObj.titlesByUniqueName = {}))[_name8 = title.canonical_name] != null ? _base10[_name8] : _base10[_name8] = []).push(title);
    } else {
      (exportObj.titlesByCanonicalName != null ? exportObj.titlesByCanonicalName : exportObj.titlesByCanonicalName = {})[title.canonical_name] = title;
      (exportObj.titlesByUniqueName != null ? exportObj.titlesByUniqueName : exportObj.titlesByUniqueName = {})[title.canonical_name] = title;
    }
  }
  return exportObj.expansions = Object.keys(exportObj.expansions).sort();
};

exportObj.fixIcons = function(data) {
  if (data.text != null) {
    return data.text = data.text.replace(/%ASTROMECH%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-astromech"></i>').replace(/%BANKLEFT%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-bankleft"></i>').replace(/%BANKRIGHT%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-bankright"></i>').replace(/%BARRELROLL%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-barrelroll"></i>').replace(/%BOMB%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-bomb"></i>').replace(/%BOOST%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-boost"></i>').replace(/%CANNON%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-cannon"></i>').replace(/%CARGO%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-cargo"></i>').replace(/%CLOAK%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-cloak"></i>').replace(/%COORDINATE%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-coordinate"></i>').replace(/%CRIT%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-crit"></i>').replace(/%CREW%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-crew"></i>').replace(/%ELITE%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-elite"></i>').replace(/%EVADE%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-evade"></i>').replace(/%FOCUS%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-focus"></i>').replace(/%HARDPOINT%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-hardpoint"></i>').replace(/%HIT%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-hit"></i>').replace(/%ILLICIT%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-illicit"></i>').replace(/%JAM%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-jam"></i>').replace(/%KTURN%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-kturn"></i>').replace(/%MISSILE%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-missile"></i>').replace(/%RECOVER%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-recover"></i>').replace(/%REINFORCE%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-reinforce"></i>').replace(/%SALVAGEDASTROMECH%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-salvagedastromech"></i>').replace(/%SLOOPLEFT%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-sloopleft"></i>').replace(/%SLOOPRIGHT%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-sloopright"></i>').replace(/%STRAIGHT%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-straight"></i>').replace(/%STOP%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-stop"></i>').replace(/%SYSTEM%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-system"></i>').replace(/%TARGETLOCK%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-targetlock"></i>').replace(/%TEAM%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-team"></i>').replace(/%TECH%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-tech"></i>').replace(/%TORPEDO%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-torpedo"></i>').replace(/%TROLLLEFT%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-trollleft"></i>').replace(/%TROLLRIGHT%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-trollright"></i>').replace(/%TURNLEFT%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-turnleft"></i>').replace(/%TURNRIGHT%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-turnright"></i>').replace(/%TURRET%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-turret"></i>').replace(/%UTURN%/g, '<i class="xwing-miniatures-font xwing-miniatures-font-kturn"></i>').replace(/%HUGESHIPONLY%/g, '<span class="card-restriction">Huge ship only.</span>').replace(/%LARGESHIPONLY%/g, '<span class="card-restriction">Large ship only.</span>').replace(/%SMALLSHIPONLY%/g, '<span class="card-restriction">Small ship only.</span>').replace(/%REBELONLY%/g, '<span class="card-restriction">Rebel only.</span>').replace(/%IMPERIALONLY%/g, '<span class="card-restriction">Imperial only.</span>').replace(/%SCUMONLY%/g, '<span class="card-restriction">Scum only.</span>').replace(/%LIMITED%/g, '<span class="card-restriction">Limited.</span>').replace(/%LINEBREAK%/g, '<br /><br />').replace(/%DE_HUGESHIPONLY%/g, '<span class="card-restriction">Nur für riesige Schiffe.</span>').replace(/%DE_LARGESHIPONLY%/g, '<span class="card-restriction">Nur für grosse Schiffe.</span>').replace(/%DE_REBELONLY%/g, '<span class="card-restriction">Nur für Rebellen.</span>').replace(/%DE_IMPERIALONLY%/g, '<span class="card-restriction">Nur für das Imperium.</span>').replace(/%DE_SCUMONLY%/g, '<span class="card-restriction">Nur für Abschaum & Kriminelle.</span>').replace(/%DE_GOZANTIONLY%/g, '<span class="card-restriction">Nur für Kreuzer der <em>Gozanti</em>-Klasse.</span>').replace(/%DE_LIMITED%/g, '<span class="card-restriction">Limitiert.</span>').replace(/%DE_SMALLSHIPONLY%/g, '<span class="card-restriction">Nur für kleine Schiffe.</span>').replace(/%FR_HUGESHIPONLY%/g, '<span class="card-restriction">Vaisseau immense uniquement.</span>').replace(/%FR_LARGESHIPONLY%/g, '<span class="card-restriction">Grand vaisseau uniquement.</span>').replace(/%FR_REBELONLY%/g, '<span class="card-restriction">Rebelle uniquement.</span>').replace(/%FR_IMPERIALONLY%/g, '<span class="card-restriction">Impérial uniquement.</span>').replace(/%FR_SCUMONLY%/g, '<span class="card-restriction">Racailles uniquement.</span>').replace(/%GOZANTIONLY%/g, '<span class="card-restriction"><em>Gozanti</em>-class cruiser only.</span>');
  }
};

exportObj.canonicalizeShipNames = function(card_data) {
  var ship_data, ship_name, _ref, _results;
  _ref = card_data.ships;
  _results = [];
  for (ship_name in _ref) {
    ship_data = _ref[ship_name];
    ship_data.english_name = ship_name;
    _results.push(ship_data.canonical_name != null ? ship_data.canonical_name : ship_data.canonical_name = ship_data.english_name.canonicalize());
  }
  return _results;
};

exportObj.renameShip = function(english_name, new_name) {
  exportObj.ships[new_name] = exportObj.ships[english_name];
  exportObj.ships[new_name].name = new_name;
  return delete exportObj.ships[english_name];
};

exportObj = typeof exports !== "undefined" && exports !== null ? exports : this;

if (exportObj.codeToLanguage == null) {
  exportObj.codeToLanguage = {};
}

exportObj.codeToLanguage.de = 'Deutsch';

if (exportObj.translations == null) {
  exportObj.translations = {};
}

exportObj.translations.Deutsch = {
  action: {
    "Barrel Roll": "Fassrolle",
    "Boost": "Schub",
    "Evade": "Ausweichen",
    "Focus": "Fokussierung",
    "Target Lock": "Zielerfassung",
    "Recover": "Aufladen",
    "Reinforce": "Verstärken",
    "Jam": "Störsignal",
    "Coordinate": "Koordination",
    "SLAM": "SLAM",
    "Cloak": "Tarnen"
  },
  slot: {
    "Astromech": "Astromech",
    "Bomb": "Bombe",
    "Cannon": "Kanonen",
    "Crew": "Crew",
    "Elite": "Elite",
    "Missile": "Raketen",
    "System": "System",
    "Torpedo": "Torpedo",
    "Turret": "Geschützturm",
    "Cargo": "Fracht",
    "Hardpoint": "Hardpoint",
    "Team": "Team",
    "Illicit": "Illegales",
    "Salvaged Astromech": "geborgener Astromech"
  },
  sources: {
    "Core": "Grundspiel",
    "A-Wing Expansion Pack": "A-Wing Erweiterung",
    "B-Wing Expansion Pack": "B-Wing Erweiterung",
    "X-Wing Expansion Pack": "X-Wing Erweiterung",
    "Y-Wing Expansion Pack": "Y-Wing Erweiterung",
    "Millennium Falcon Expansion Pack": "Millenium Falke Erweiterung",
    "HWK-290 Expansion Pack": "HWK-290 Erweiterung",
    "TIE Fighter Expansion Pack": "TIE-Jäger Erweiterung",
    "TIE Interceptor Expansion Pack": "TIE-Abfangjäger Erweiterung",
    "TIE Bomber Expansion Pack": "TIE-Bomber Erweiterung",
    "TIE Advanced Expansion Pack": "TIE-Advanced Erweiterung",
    "Lambda-Class Shuttle Expansion Pack": "Raumfähre der Lambda-Klasse Erweiterung",
    "Slave I Expansion Pack": "Sklave I Erweiterung",
    "Imperial Aces Expansion Pack": "Fliegerasse des Imperiums Erweiterung",
    "Rebel Transport Expansion Pack": "Rebellentransporter Erweiterung",
    "Z-95 Headhunter Expansion Pack": "Z-95-Kopfjäger Erweiterung",
    "TIE Defender Expansion Pack": "TIE-Jagdbomber Erweiterung",
    "E-Wing Expansion Pack": "E-Wing Erweiterung",
    "TIE Phantom Expansion Pack": "TIE-Phantom Erweiterung",
    "Tantive IV Expansion Pack": "Tantive IV Erweiterung",
    "Rebel Aces Expansion Pack": "Fliegerasse der Rebellenallianz Erweiterung",
    "YT-2400 Freighter Expansion Pack": "YT-2400-Frachter Erweiterung",
    "VT-49 Decimator Expansion Pack": "VT-49 Decimator Erweiterung",
    "StarViper Expansion Pack": "SternenViper Erweiterung",
    "M3-A Interceptor Expansion Pack": "M3-A Abfangjäger Erweiterung",
    "IG-2000 Expansion Pack": "IG-2000 Erweiterung",
    "Most Wanted Expansion Pack": "Abschaum und Kriminelle Erweiterung",
    "Imperial Raider Expansion Pack": "Imperiale Sturm-Korvette Erweiterung",
    "Hound's Tooth Expansion Pack": "Reisszahn Erweiterung",
    "Kihraxz Fighter Expansion Pack": "Kihraxz-Jäger Erweiterung",
    "K-Wing Expansion Pack": "K-Wing Erweiterung",
    "TIE Punisher Expansion Pack": "TIE-Vergelter Erweiterung",
    "The Force Awakens Core Set": "Das Erwachen der Macht Grundspiel",
    "Imperial Assault Carrier Expansion Pack": "Imperialer Angriffsträger Erweiterung",
    "T-70 X-Wing Expansion Pack": "T-70-X-Flügler Erweiterung",
    "TIE/fo Fighter Expansion Pack": "TIE/EO-Jäger Erweiterung",
    "Inquisitor's TIE Expansion Pack": "TIE des Inquisitors Erweiterung",
    "Mist Hunter Expansion Pack": "Nebeljäger Erweiterung",
    "Punishing One Expansion Pack": "Vollstrecker Eins Erweiterung",
    "Ghost Expansion Pack": "Ghost Erweiterung"
  },
  ui: {
    shipSelectorPlaceholder: "Wähle ein Schiff",
    pilotSelectorPlaceholder: "Wähle einen Piloten",
    upgradePlaceholder: function(translator, language, slot) {
      return "kein " + (translator(language, 'slot', slot)) + " Upgrade";
    },
    modificationPlaceholder: "keine Modifikation",
    titlePlaceholder: "kein Titel",
    upgradeHeader: function(translator, language, slot) {
      return "" + (translator(language, 'slot', slot)) + " Upgrade";
    },
    unreleased: "unveröffentlicht",
    epic: "Episch",
    limited: "limitiert"
  },
  byCSSSelector: {
    '.translate.sort-cards-by': 'Sortiere Karten nach',
    '.xwing-card-browser option[value="name"]': 'Name',
    '.xwing-card-browser option[value="source"]': 'Quelle',
    '.xwing-card-browser option[value="type-by-points"]': 'Typ (Punkte)',
    '.xwing-card-browser option[value="type-by-name"]': 'Typ (Name)',
    '.xwing-card-browser .translate.select-a-card': 'Wähle eine Karte aus der Liste.',
    '.xwing-card-browser .info-range td': 'Reichweite',
    '.info-well .info-ship td.info-header': 'Schiff',
    '.info-well .info-skill td.info-header': 'Pilotenwert',
    '.info-well .info-actions td.info-header': 'Aktionen',
    '.info-well .info-upgrades td.info-header': 'Aufwertungen',
    '.info-well .info-range td.info-header': 'Reichweite',
    '.clear-squad': 'Neue Staffel',
    '.save-list': 'Speichern',
    '.save-list-as': 'Speichern als…',
    '.delete-list': 'Löschen',
    '.backend-list-my-squads': 'Staffel laden',
    '.view-as-text': '<span class="hidden-phone"><i class="icon-print"></i>&nbsp;Drucken/Anzeigen als </span>Text',
    '.collection': '<span class="hidden-phone"><i class="icon-folder-open hidden-phone hidden-tabler"></i>&nbsp;Deine Sammlung</span>',
    '.randomize': 'Zufallsliste!',
    '.randomize-options': 'Zufallslisten-Optionen…',
    '.notes-container > span': 'Staffelnotizen',
    '.bbcode-list': 'Kopiere den BBCode von unten und füge ihn in deine Forenposts ein.<textarea></textarea>',
    '.vertical-space-checkbox': "Platz für Schadenskarten und Aufwertungen im Druck berücksichtigen. <input type=\"checkbox\" class=\"toggle-vertical-space\" />",
    '.color-print-checkbox': "Ausdrucken in Farbe. <input type=\"checkbox\" class=\"toggle-color-print\" />",
    '.print-list': '<i class="icon-print"></i>&nbsp;Druck',
    '.do-randomize': 'Zufall!',
    '#empireTab': 'Galaktisches Imperium',
    '#rebelTab': 'Rebellen Allianz',
    '#scumTab': 'Abschaum und Kriminelle',
    '#browserTab': 'Karten Browser',
    '#aboutTab': 'Über',
    '.from-xws': 'Import von XWS (beta)',
    '.to-xws': 'Export nach XWS (beta)'
  },
  singular: {
    'pilots': 'Pilot',
    'modifications': 'Modifikation',
    'titles': 'Titel'
  },
  types: {
    'Pilot': 'Pilot',
    'Modification': 'Modifikation',
    'Title': 'Titel'
  }
};

if (exportObj.cardLoaders == null) {
  exportObj.cardLoaders = {};
}

exportObj.cardLoaders.Deutsch = function() {
  var basic_cards, modification_translations, pilot_translations, title_translations, upgrade_translations;
  exportObj.cardLanguage = 'Deutsch';
  basic_cards = exportObj.basicCardData();
  exportObj.canonicalizeShipNames(basic_cards);
  exportObj.ships = basic_cards.ships;
  exportObj.renameShip('TIE Fighter', 'TIE-Jäger');
  exportObj.renameShip('TIE Interceptor', 'TIE-Abfangjäger');
  exportObj.renameShip('TIE Bomber', 'TIE-Bomber');
  exportObj.renameShip('Z-95 Headhunter', 'Z-95-Kopfjäger');
  exportObj.renameShip('TIE Defender', 'TIE-Jagdbomber');
  exportObj.renameShip('Lambda-Class Shuttle', 'Raumfähre der Lambda-Klasse');
  exportObj.renameShip('GR-75 Medium Transport', 'Medium-Transporter GR-75');
  exportObj.renameShip('CR90 Corvette (Fore)', 'CR90-Korvette (Bug)');
  exportObj.renameShip('CR90 Corvette (Aft)', 'CR90-Korvette (Heck)');
  exportObj.renameShip('M3-A Interceptor', 'M3-A Abfangjäger');
  exportObj.renameShip('Raider-class Corvette (Fore)', 'Korv. der Sturm-Klasse (Bug)');
  exportObj.renameShip('Raider-class Corvette (Aft)', 'Korv. der Sturm-Klasse (Heck)');
  exportObj.renameShip('TIE Phantom', 'TIE-Phantom');
  exportObj.renameShip('Kihraxz Fighter', 'Kihraxz-Jäger');
  exportObj.renameShip('TIE Punisher', 'TIE-Vergelter');
  exportObj.renameShip('StarViper', 'SternenViper');
  exportObj.renameShip('T-70 X-Wing', 'T-70-X-Flügler');
  exportObj.renameShip('TIE/fo Fighter', 'TIE/EO-Jäger');
  exportObj.renameShip('Gozanti-class Cruiser', 'Kreuzer der Gozanti-Klasse');
  exportObj.renameShip('TIE Advanced Prototype', 'TIE-Turbojäger-Prototyp');
  exportObj.renameShip('G-1A Starfighter', 'G-1A-Sternenjäger');
  exportObj.renameShip('Attack Shuttle', 'Jagdshuttle');
  pilot_translations = {
    "Wedge Antilles": {
      text: "Wenn du angreifst, sinkt der Wendigkeitswert des Verteidigers um 1 (Minimum 0)."
    },
    "Garven Dreis": {
      text: "Wenn du einen Fokusmarker ausgibst, darfst du ihn auf ein anderes freundliches Schiff in Reichweite 1-2 legen (anstatt ihn abzulegen)."
    },
    "Red Squadron Pilot": {
      name: "Pilot der Rot-Staffel"
    },
    "Rookie Pilot": {
      name: "Anfängerpilot"
    },
    "Biggs Darklighter": {
      text: "Andere freundliche Schiffe in Reichweite 1 dürfen nur dann angegriffen werden, wenn der Angreifer dich nicht zum Ziel bestimmen kann."
    },
    "Luke Skywalker": {
      text: "Wenn du verteidigst, kannst du 1 deiner %FOCUS% in ein %EVADE% ändern."
    },
    "Gray Squadron Pilot": {
      name: "Pilot der Grau-Staffel"
    },
    '"Dutch" Vander': {
      text: "Wähle ein anderes freundliches Schiff in Reichweite 1-2, nachdem du eine Zielerfassung durchgeführt hast. Das gewählte Schiff darf sofort ebenfalls eine Zielerfassung durchführen."
    },
    "Horton Salm": {
      text: "Wenn du ein Ziel in Reichweite 2-3 angreifst, darfst du beliebig viele Leerseiten neu würfeln."
    },
    "Gold Squadron Pilot": {
      name: "Pilot der Gold-Staffel"
    },
    "Academy Pilot": {
      ship: "TIE-Jäger",
      name: "Pilot der Akademie"
    },
    "Obsidian Squadron Pilot": {
      ship: "TIE-Jäger",
      name: "Pilot der Obsidian-Staffel"
    },
    "Black Squadron Pilot": {
      ship: "TIE-Jäger",
      name: "Pilot der Schwarz-Staffel"
    },
    '"Winged Gundark"': {
      ship: "TIE-Jäger",
      name: '"Geflügelter Gundark"',
      text: "Wenn du ein Ziel in Reichweite 1 angreifst, darfst du eines deiner %HIT% in ein %CRIT% ändern."
    },
    '"Night Beast"': {
      name: '"Nachtbestie"',
      ship: "TIE-Jäger",
      text: "Nachdem du ein grünes Manöver ausgeführt hast, darfst du als freie Aktion eine Fokussierung durchführen."
    },
    '"Backstabber"': {
      ship: "TIE-Jäger",
      text: "Wenn du bei deinem Angriff nicht im Feuerwinkel des Verteidigers bist, erhältst du 1 zusätzlichen Angriffswürfel."
    },
    '"Dark Curse"': {
      ship: "TIE-Jäger",
      text: "Wenn du verteidigst, können angreifende Schiffe keine Fokusmarker ausgeben oder Angriffswürfel neu würfeln."
    },
    '"Mauler Mithel"': {
      ship: "TIE-Jäger",
      text: "Wirf 1 zusätzlichen Angriffswürfel, wenn du ein Ziel in Reichweite 1 angreifst."
    },
    '"Howlrunner"': {
      ship: "TIE-Jäger",
      name: '"Kreischläufer"',
      text: "Wenn ein anderes freundliches Schiff in Reichweite 1 mit seinen Primärwaffen angreift, darf es 1 Angriffswürfel neu würfeln."
    },
    "Maarek Stele": {
      text: "Wenn ein Verteidiger durch deinen Angriff eine offene Schadenskarte erhalten würde, ziehst du stattdessen 3 Schadenskarten, wählst eine davon zum Austeilen und legst die restlichen ab."
    },
    "Tempest Squadron Pilot": {
      name: "Pilot der Tornado-Staffel"
    },
    "Storm Squadron Pilot": {
      name: "Pilot der Storm-Staffel"
    },
    "Darth Vader": {
      text: "Im Schritt \"Aktionen durchführen\" darfst du 2 Aktionen durchführen."
    },
    "Alpha Squadron Pilot": {
      name: "Pilot der Alpha-Staffel",
      ship: "TIE-Abfangjäger"
    },
    "Avenger Squadron Pilot": {
      name: "Pilot der Avenger-Staffel",
      ship: "TIE-Abfangjäger"
    },
    "Saber Squadron Pilot": {
      name: "Pilot der Saber-Staffel",
      ship: "TIE-Abfangjäger"
    },
    "\"Fel's Wrath\"": {
      ship: "TIE-Abfangjäger",
      text: "Wenn die Summe deiner Schadenskarten deinen Hüllenwert erreicht oder übersteigt, wirst du nicht sofort zerstört, sondern erst am Ende der Kampfphase."
    },
    "Turr Phennir": {
      ship: "TIE-Abfangjäger",
      text: "Nachdem du angegriffen hast, darfst du eine freie Aktion Schub oder Fassrolle durchführen."
    },
    "Soontir Fel": {
      ship: "TIE-Abfangjäger",
      text: "Immer wenn du einen Stressmarker erhältst, darfst du deinem Schiff auch einen Fokusmarker geben."
    },
    "Tycho Celchu": {
      text: "Du darfst auch dann Aktionen durchführen, wenn du Stressmarker hast."
    },
    "Arvel Crynyd": {
      text: "Wenn du angreifst, darfst du auch auf feindliche Schiffe zielen, deren Basen du berührst (vorausgesetzt sie sind innerhalb deines Feuerwinkels)."
    },
    "Green Squadron Pilot": {
      name: "Pilot der Grün-Staffel"
    },
    "Prototype Pilot": {
      name: "Testpilot"
    },
    "Outer Rim Smuggler": {
      name: "Schmuggler aus dem Outer Rim"
    },
    "Chewbacca": {
      text: "Wenn du eine offene Schadenskarte erhältst, wird sie sofort umgedreht (ohne dass ihr Kartentext in Kraft tritt)."
    },
    "Lando Calrissian": {
      text: "Wähle nach dem Ausführen eines grünen Manövers ein anderes freundliches Schiff in Reichweite 1. Dieses Schiff darf eine freie Aktion aus seiner Aktionsleiste durchführen."
    },
    "Han Solo": {
      text: "Wenn du angreifst, darfst du all deine Würfel neu würfeln. Tust du dies, musst du so viele Würfel wie möglich neu würfeln."
    },
    "Kath Scarlet": {
      text: "Wenn du angreifst und der Verteidiger mindestens 1 %CRIT% negiert, erhält er 1 Stressmarker."
    },
    "Boba Fett": {
      text: "Sobald du ein Drehmanöver (%BANKLEFT% oder %BANKRIGHT%) aufdeckst, darfst du das Drehmanöver mit gleicher eschwindigkeit, aber anderer Richtung, auf deinem Rad nachträglich einstellen."
    },
    "Krassis Trelix": {
      text: "Wenn du mit einer Sekundärwaffe angreifst, darfst du 1 Angriffswürfel neu würfeln."
    },
    "Bounty Hunter": {
      name: "Kopfgeldjäger"
    },
    "Ten Numb": {
      text: "Wenn du angreifst, kann 1 deiner %CRIT% von Verteidigungswürfeln nicht negiert werden."
    },
    "Ibtisam": {
      text: "Beim Angreifen oder Verteidigen darfst du 1 deiner Würfel neu würfeln, sofern du mindestens 1 Stressmarker hast."
    },
    "Dagger Squadron Pilot": {
      name: "Pilot der Dagger-Staffel"
    },
    "Blue Squadron Pilot": {
      name: "Pilot der Blauen Staffel"
    },
    "Rebel Operative": {
      name: "Rebellenagent"
    },
    "Roark Garnet": {
      text: 'Wähle zu Beginn der Kampfphase 1 anderes freundliches Schiff in Reichweite 1-3. Bis zum Ende der Phase wird dieses Schiff behandelt, als hätte es einen Pilotenwert von 12.'
    },
    "Kyle Katarn": {
      text: "Zu Beginn der Kampfphase darfst du einem anderen freundlichen Schiff in Reichweite 1-3 einen deiner Fokusmarker geben."
    },
    "Jan Ors": {
      text: "Wenn ein anderes freundliches Schiff in Reichweite 1-3 angreift und du keine Stressmarker hast, darfst du 1 Stressmarker nehmen, damit dieses Schiff 1 zusätzlichen Angriffswürfel erhält."
    },
    "Scimitar Squadron Pilot": {
      ship: "TIE-Bomber",
      name: "Pilot der Scimitar-Staffel"
    },
    "Gamma Squadron Pilot": {
      ship: "TIE-Bomber",
      name: "Pilot der Gamma-Staffel"
    },
    "Captain Jonus": {
      ship: "TIE-Bomber",
      text: "Wenn ein anderes freundliches Schiff in Reichweite 1 mit einer Sekundärwaffe angreift, darf es bis zu 2 Angriffswürfel neu würfeln."
    },
    "Major Rhymer": {
      ship: "TIE-Bomber",
      text: "Beim Angreifen mit einer Sekundärwaffe darfst du die Reichweite der Waffe um 1 erhöhen oder verringern, bis zu einer Reichweite von 1-3."
    },
    "Captain Kagi": {
      ship: "Raumfähre der Lambda-Klasse",
      text: "Wenn ein feindliches Schiff eine Zielerfassung durchführt, muss es wenn möglich dich als Ziel erfassen."
    },
    "Colonel Jendon": {
      ship: "Raumfähre der Lambda-Klasse",
      text: "Zu Beginn der Kampfphase darfst du 1 deiner blauen Zielerfassungsmarker auf ein freundliches Schiff in Reichweite 1 legen, das noch keinen blauen Zielerfassungsmarker hat."
    },
    "Captain Yorr": {
      ship: "Raumfähre der Lambda-Klasse",
      text: "Wenn ein anderes freundliches Schiff in Reichweite 1-2 einen Stressmarker erhalten würde und du 2 oder weniger Stressmarker hast, darfst du statt ihm diesen Marker nehmen."
    },
    "Omicron Group Pilot": {
      ship: "Raumfähre der Lambda-Klasse",
      name: "Pilot der Omikron-Gruppe"
    },
    "Lieutenant Lorrir": {
      ship: "TIE-Abfangjäger",
      text: "Wenn du die Aktion Fassrolle ausführst, kannst du 1 Stressmarker erhalten, um die (%BANKLEFT% 1) oder (%BANKRIGHT% 1) Manöverschablone anstatt der (%STRAIGHT% 1) Manöverschablone zu benutzen."
    },
    "Royal Guard Pilot": {
      ship: "TIE-Abfangjäger",
      name: "Pilot der Roten Garde"
    },
    "Tetran Cowall": {
      ship: "TIE-Abfangjäger",
      text: "Immer wenn du ein %UTURN% Manöver aufdeckst, kannst du das Manöver mit einer Geschwindigkeit von \"1,\" \"3,\" oder \"5\" ausführen."
    },
    "Kir Kanos": {
      ship: "TIE-Abfangjäger",
      text: "Wenn du ein Ziel in Reichweite 2-3 angreifst, darfst du einen Ausweichmarker ausgeben, um 1 %HIT% zu deinem Wurf hinzuzufügen."
    },
    "Carnor Jax": {
      ship: "TIE-Abfangjäger",
      text: "Feindliche Schiffe in Reichweite 1 können weder Fokussierung und Ausweichen Aktionen durchführen noch Ausweichmarker und Fokusmarker ausgeben."
    },
    "GR-75 Medium Transport": {
      ship: "Medium-Transporter GR-75",
      name: "Medium-Transporter GR-75"
    },
    "Bandit Squadron Pilot": {
      ship: "Z-95-Kopfjäger",
      name: "Pilot der Bandit-Staffel"
    },
    "Tala Squadron Pilot": {
      ship: "Z-95-Kopfjäger",
      name: "Pilot der Tala-Staffel"
    },
    "Lieutenant Blount": {
      ship: "Z-95-Kopfjäger",
      name: "Lieutenant Blount",
      text: "Wenn du angreifst, triffst du immer, selbst wenn das verteidigende Schiff keinen Schaden nimmt."
    },
    "Airen Cracken": {
      ship: "Z-95-Kopfjäger",
      name: "Airen Cracken",
      text: "Nachdem du angegriffen hast, darfst du ein anderes freundliches Schiff in Reichweite 1 wählen. Dieses Schiff darf 1 freie Aktion durchführen."
    },
    "Delta Squadron Pilot": {
      ship: "TIE-Jagdbomber",
      name: "Pilot der Delta-Staffel"
    },
    "Onyx Squadron Pilot": {
      ship: "TIE-Jagdbomber",
      name: "Pilot der Onyx-Staffel"
    },
    "Colonel Vessery": {
      ship: "TIE-Jagdbomber",
      text: "Wenn du angreifst und der Verteidiger bereits einen roten Zielerfassungsmarker hat, darfst du ihn unmittelbar nach dem Angriffswurf in die Zielerfassung nehmen."
    },
    "Rexler Brath": {
      ship: "TIE-Jagdbomber",
      text: "Nachdem du angegriffen und damit dem Verteidiger mindestens 1 Schadenskarte zugeteilt hast, kannst du einen Fokusmarker ausgeben, um die soeben zugeteilten Schadenskarten aufzudecken."
    },
    "Knave Squadron Pilot": {
      name: "Pilot der Schurken-Staffel"
    },
    "Blackmoon Squadron Pilot": {
      name: "Pilot der Schwarzmond-Staffel"
    },
    "Etahn A'baht": {
      text: "Sobald ein feindliches Schiff in Reichweite 1–3 und innerhalb deines Feuerwinkels verteidigt, darf der Angreifer 1 %HIT% seiner in ein %CRIT% ändern."
    },
    "Corran Horn": {
      text: "Zu Beginn der Endphase kannst du einen Angriff durchführen. Tust du das, darfst du in der nächsten Runde nicht angreifen."
    },
    "Sigma Squadron Pilot": {
      ship: "TIE-Phantom",
      name: "Pilot der Sigma-Staffel"
    },
    "Shadow Squadron Pilot": {
      ship: "TIE-Phantom",
      name: "Pilot der Schatten-Staffel"
    },
    '"Echo"': {
      ship: "TIE-Phantom",
      name: '"Echo"',
      text: "Wenn du dich enttarnst, musst du statt der (%STRAIGHT% 2)-Manöverschablone die (%BANKRIGHT% 2)- oder (%BANKLEFT% 2)-Schablone verwenden."
    },
    '"Whisper"': {
      ship: "TIE-Phantom",
      name: '"Geflüster"',
      text: "Nachdem du mit einem Angriff getroffen hast, darfst du deinem Schiff 1 Fokusmarker geben."
    },
    "CR90 Corvette (Fore)": {
      name: "CR90-Korvette (Bug)",
      ship: "CR90-Korvette (Bug)",
      text: "Wenn du mit deinen Primärwaffen angreifst, kannst du 1 Energie ausgeben, um 1 zusätzlichen Angriffswürfel zu bekommen"
    },
    "CR90 Corvette (Aft)": {
      name: "CR90-Korvette (Heck)",
      ship: "CR90-Korvette (Heck)"
    },
    "Wes Janson": {
      text: "Nachdem du einen Angriff durchgeführt hast, darfst du 1 Fokus-, Ausweich- oder blauen Zielerfassungsmarker vom Verteidiger entfernen."
    },
    "Jek Porkins": {
      text: "Wenn du einen Stressmarker erhältst, darfst du ihn entfernen und 1 Angriffswürfel werfen. Bei %HIT% bekommt dein Schiff 1 verdeckte Schadenskarte."
    },
    '"Hobbie" Klivian': {
      text: "Wenn du ein Schiff in die Zielerfassung nimmst oder einen Zielerfassungsmarker ausgibst, kannst du 1 Stressmarker von deinem Schiff entfernen."
    },
    "Tarn Mison": {
      text: "Wenn ein feindliches Schiff einen Angriff gegen dich ansagt, kannst du dieses Schiff in die Zielerfassung nehmen."
    },
    "Jake Farrell": {
      text: "Nachdem du die Aktion Fokussierung durchgeführt oder einen Fokusmarker erhalten hast, darfst du als freie Aktion einen Schub oder eine Fassrolle durchführen."
    },
    "Gemmer Sojan": {
      name: "Gemmer Sojan",
      text: "Solange du in Reichweite 1 zu mindestens einem feindlichen Schiff bist, steigt dein Wendigkeitswert um 1."
    },
    "Keyan Farlander": {
      text: "Beim Angreifen darfst du 1 Stressmarker entfernen, um alle deine %FOCUS% in %HIT% zu ändern."
    },
    "Nera Dantels": {
      text: "Mit %TORPEDO%-Sekundärwaffen kannst du auch feindliche Schiffe außerhalb deines Feuerwinkels angreifen."
    },
    "Wild Space Fringer": {
      name: "Grenzgänger aus dem Wilden Raum"
    },
    "Dash Rendar": {
      text: "Du darfst in der Aktivierungsphase und beim Durchführen von Aktionen Hindernisse ignorieren."
    },
    '"Leebo"': {
      text: "Immer wenn du eine offene Schadenskarte erhältst, ziehst du 1 weitere Schadenskarte. Wähle 1, die abgehandelt wird, und lege die andere ab."
    },
    "Eaden Vrill": {
      text: "Wirf 1 zusätzlichen Angriffswürfel, wenn du mit den Primärwaffen auf ein Schiff mit Stressmarker schießt."
    },
    "Patrol Leader": {
      name: "Patrouillenführer"
    },
    "Rear Admiral Chiraneau": {
      name: "Konteradmiral Chiraneau",
      text: "Wenn du ein Ziel in Reichweite 1-2 angreifst, kannst du ein %FOCUS% in ein %CRIT% ändern."
    },
    "Commander Kenkirk": {
      text: "Wenn du keine Schilde und mindestens 1 Schadenskarte hast, steigt deine Wendigkeit um 1."
    },
    "Captain Oicunn": {
      text: "Nach dem Ausführen eines Manövers nimmt jedes feindliche Schiff, das du berührst, 1 Schaden."
    },
    "Prince Xizor": {
      ship: "SternenViper",
      name: "Prinz Xizor",
      text: "Sobald du verteidigst, darf ein freundliches Schiff in Reichweite 1 ein nicht-negiertes %HIT% oder %CRIT% an deiner Stelle nehmen."
    },
    "Guri": {
      ship: "SternenViper",
      text: "Wenn du zu Beginn der Kampfphase in Reichweite 1 zu einem feindlichen Schiff bist, darfst du 1 Fokusmarker auf dein Schiff legen."
    },
    "Black Sun Vigo": {
      ship: "SternenViper",
      name: "Vigo der Schwarzen Sonne"
    },
    "Black Sun Enforcer": {
      ship: "SternenViper",
      name: "Vollstrecker der Schwarzen Sonne"
    },
    "Serissu": {
      ship: "M3-A Abfangjäger",
      text: "Sobald ein anderes freundliches Schiff in Reichweite 1 verteidigt, darf es 1 Verteidigungswürfel neu würfeln."
    },
    "Laetin A'shera": {
      ship: "M3-A Abfangjäger",
      text: "Nachdem du gegen einen Angriff verteidigt hast und falls der Angriff nicht getroffen hat, darfst du deinem Schiff 1 Ausweichmarker zuordnen."
    },
    "Tansarii Point Veteran": {
      ship: "M3-A Abfangjäger",
      name: "Veteran von Tansarii Point"
    },
    "Cartel Spacer": {
      ship: "M3-A Abfangjäger",
      name: "Raumfahrer des Kartells"
    },
    "IG-88A": {
      text: "Nachdem du einen Angriff durchgeführt hast, der den Verteidiger zerstört, darfst du 1 Schild wiederaufladen."
    },
    "IG-88B": {
      text: "Ein Mal pro Runde darfst du, nachdem du mit einem Angriff verfehlt hast, einen weiteren Angriff mit einer ausgerüsteten %CANNON%-Sekundärwaffe durchführen."
    },
    "IG-88C": {
      text: "Nachdem du die Aktion Schub durchgeführt hast, darfst du eine freie Aktion Ausweichen durchführen."
    },
    "IG-88D": {
      text: "Du darfst die Manöver (%SLOOPLEFT% 3) oder (%SLOOPRIGHT% 3) auch mit den entsprechenden Schablonen für Wendemanöver (%TURNLEFT% 3) bzw. (%TURNRIGHT% 3) ausführen."
    },
    "Boba Fett (Scum)": {
      name: "Boba Fett (Abschaum)",
      text: "Sobald du angreifst oder verteidigst, darfst du für jedes feindliche Schiff in Reichweite 1 einen deiner Würfel neu würfeln."
    },
    "Kath Scarlet (Scum)": {
      name: "Kath Scarlet (Abschaum)",
      text: "Sobald du ein Schiff innerhalb deines Zusatz-Feuerwinkels angreifst, erhältst du 1 zusätzlichen Angriffswürfel."
    },
    "Emon Azzameen": {
      text: "Sobald du eine Bombe legst, darfst du auch die Schablone [%TURNLEFT% 3], [%STRAIGHT% 3] oder [%TURNRIGHT% 3] anstatt der [%STRAIGHT% 1]-Schablone verwenden."
    },
    "Mandalorian Mercenary": {
      name: "Mandalorianischer Söldner"
    },
    "Kavil": {
      text: "Sobald du ein Schiff außerhalb deines Feuerwinkels angreifst, erhältst du 1 zusätzlichen Angriffswürfel."
    },
    "Drea Renthal": {
      text: "Nachdem du einen Zielerfassungsmarker ausgegeben hast, darfst du 1 Stressmarker nehmen, um ein Schiff in die Zielerfassung zu nehmen."
    },
    "Syndicate Thug": {
      name: "Verbrecher des Syndikats"
    },
    "Hired Gun": {
      name: "Söldner"
    },
    "Dace Bonearm": {
      text: "Sobald ein feindliches Schiff in Reichweite 1-3 mindestens 1 Ionenmarker erhält und falls du keinen Stressmarker hast, darfst du 1 Stressmarker nehmen, damit das Schiff 1 Schaden nimmt."
    },
    "Palob Godalhi": {
      text: "Zu Beginn der Kampfphase darfst du 1 Fokus- oder Ausweichmarker von einem feindlichen Schiff in Reichweite 1-2 entfernen und dir selbst zuordnen."
    },
    "Torkil Mux": {
      text: "Wähle am Ende der Aktivierungsphase 1 feindliches Schiff in Reichweite 1-2. Bis zum Ende der Kampfphase wird der Pilotenwert des Schiffs als \"0\" behandelt."
    },
    "Spice Runner": {
      name: "Spiceschmuggler"
    },
    "N'Dru Suhlak": {
      ship: "Z-95-Kopfjäger",
      text: "Sobald du angreifst, erhältst du 1 zusätzlichen Angriffswürfel, falls keine anderen freundlichen Schiffe in Reichweite 1-2 zu dir sind."
    },
    "Kaa'To Leeachos": {
      ship: "Z-95-Kopfjäger",
      text: "Zu Beginn der Kampfphase darfst du 1 Fokus- oder Ausweichmarker von einem anderem freundlichen Schiff in Reichweite 1-2 entfernen und dir selbst zuordnen."
    },
    "Binayre Pirate": {
      ship: "Z-95-Kopfjäger",
      name: "Binayre-Pirat"
    },
    "Black Sun Soldier": {
      ship: "Z-95-Kopfjäger",
      name: "Kampfpilot der Schwarzen Sonne"
    },
    "Commander Alozen": {
      text: "Zu Beginn der Kampfphase darfst du ein feindliches Schiff in Reichweite 1 in die Zielerfassung nehmen."
    },
    "Raider-class Corvette (Fore)": {
      ship: "Korv. der Sturm-Klasse (Bug)",
      name: "Korv. der Sturm-Klasse (Bug)",
      text: "Ein Mal pro Runde darfst du, nachdem du einen Primärwaffen-Angriff durchgeführt hast, 2 Energie ausgeben, um einen weiteren Primärwaffen-Angriff durchzuführen."
    },
    "Raider-class Corvette (Aft)": {
      ship: "Korv. der Sturm-Klasse (Heck)",
      name: "Korv. der Sturm-Klasse (Heck)"
    },
    "Bossk": {
      text: "Sobald du einen Angriff durchführst und triffst, kannst du , bevor du Schaden verursachst, 1 deiner %CRIT% negieren, um 2 %HIT% hinzuzufügen."
    },
    "Talonbane Cobra": {
      ship: "Kihraxz-Jäger",
      text: "Sobald du angreifst oder verteidigst, wird der Effekt deiner Kampfvorteile durch Reichweite verdoppelt."
    },
    "Miranda Doni": {
      text: "Ein Mal pro Runde darfst du, sobald du angreifst, entweder 1 Schild ausgeben, um 1 zusätzlichen Angriffswürfel zu werfen, <strong>oder</strong> 1 Angriffswürfel weniger werfen, um 1 Schild wiederaufzuladen."
    },
    '"Redline"': {
      name: '"Rote Linie"',
      ship: "TIE-Vergelter",
      text: "Du darfst 2 Zielerfassungen auf demselben Schiff haben. Sobald du ein Schiff in die Zielerfassung nimmst, darfst du es ein zweites Mal in die Zielerfassung nehmen."
    },
    '"Deathrain"': {
      name: '"Todesregen"',
      ship: "TIE-Vergelter",
      text: "Sobald du eine Bombe legst, darfst du die Stopper am Bug deines Schiffs benutzen. Nachdem du eine Bombe gelegt hast, darfst du als freie Aktion eine Fassrolle durchführen."
    },
    "Juno Eclipse": {
      text: "Sobald du dein Manöver aufdeckst, darfst du die Geschwindigkeit um 1 erhöhen oder reduzieren (bis zu einem Minimum von 1)."
    },
    "Zertik Strom": {
      text: "Sobald feindliche Schiffe in Reichweite 1 angreifen, können sie ihren Kampfvorteil durch Reichweite nicht hinzufügen."
    },
    "Lieutenant Colzet": {
      text: "Zu Beginn der Endphase darfst du einen Zielerfassungsmarker , den du auf einem feindlichen Schiff liegen hast, ausgeben, um 1 seiner verdeckten Schadenskarten (zufällig bestimmt) aufzudecken."
    },
    "Latts Razzi": {
      text: "Sobald ein freundliches Schiff einen Angriff deklariert und du den Verteidiger in der Zielerfassung hast, kannst du einen Zielerfassungsmarker ausgeben, um die Wendigkeit des Verteidigers für diesen Angriff um 1 zu senken."
    },
    "Graz the Hunter": {
      ship: "Kihraxz-Jäger",
      name: "Graz der Jäger",
      text: "Wirf 1 zusätzlichen Verteidigungswürfel, wenn der Angreifer in deinem Feuerwinkel ist, sobald du verteidigst."
    },
    "Esege Tuketu": {
      text: "Sobald ein anderes freundliches Schiff in Reichweite 1-2 angreift, darf es deine Fokusmarker wie seine eigenen behandeln."
    },
    "Moralo Eval": {
      text: "Du darfst Angriffe mit %CANNON%-Sekundärwaffen gegen Schiffe in deinem Zusatz-Feuerwinkel durchführen."
    },
    "Warden Squadron Pilot": {
      ship: "K-Wing",
      name: "Pilot der Beschützer-Staffel"
    },
    "Guardian Squadron Pilot": {
      ship: "K-Wing",
      name: "Pilot der Wächter-Staffel"
    },
    "Cutlass Squadron Pilot": {
      ship: "TIE-Vergelter",
      name: "Pilot der Entermesser-Staffel"
    },
    "Black Eight Squadron Pilot": {
      ship: "TIE-Vergelter",
      name: "Pilot der Schwarzen-Acht-Staffel"
    },
    "Cartel Marauder": {
      ship: "Kihraxz-Jäger",
      name: "Kartell-Marodeur"
    },
    "Black Sun Ace": {
      ship: "Kihraxz-Jäger",
      name: "Fliegerass der schwarzen Sonne"
    },
    "Trandoshan Slaver": {
      ship: "YV-666",
      name: "Trandoshanischer Sklavenjäger"
    },
    "Poe Dameron": {
      ship: "T-70-X-Flügler",
      text: "Solange du angreifst oder verteidigst, und wenn du einen Fokusmarker hast, darfst du 1 deiner %FOCUS% in %HIT% oder %EVADE% ändern."
    },
    '"Blue Ace"': {
      ship: "T-70-X-Flügler",
      name: '"Ass Blau"',
      text: "Soabld du eine Schub-Aktion ausführst, darfst du das Manöver (%TURNLEFT% 1) oder (%TURNRIGHT% 1) verwenden."
    },
    '"Red Ace"': {
      ship: "T-70-X-Flügler",
      name: '"Ass Rot"',
      text: 'Das erste Mal wenn du in jeder Runde ein Schild von deinem Schiff entfernst, weise deinem Schiff 1 Ausweichmarker zu.'
    },
    "Blue Squadron Novice": {
      ship: "T-70-X-Flügler",
      name: "Anfängerpilot der Blauen Staffel"
    },
    "Red Squadron Veteran": {
      ship: "T-70-X-Flügler",
      name: "Veteran der Roten Staffel"
    },
    'Ello Asty': {
      ship: "T-70-X-Flügler",
      text: 'Solange du nicht gestresst bist, darfst du deine %TROLLLEFT% und %TROLLRIGHT% Manöver als weiße Manöver behandeln.'
    },
    '"Omega Ace"': {
      ship: "TIE/EO-Jäger",
      name: '"Ass Omega"',
      text: "Sobald du angreifst, kannst du einen Fokusmarker und eine deiner Zielerfassungen auf dem Verteidiger ausgeben, um alle deine Würfelergebnisse in %KRIT% zu ändern."
    },
    '"Epsilon Leader"': {
      ship: "TIE/EO-Jäger",
      name: "Epsilon Eins",
      text: "Zu Beginn der Kampfphase entferne je 1 Stressmarker von jedem freundlichen Schiff in Reichweite 1."
    },
    '"Zeta Ace"': {
      ship: "TIE/EO-Jäger",
      name: "Ass Zeta",
      text: "Sobald du eine Fassrolle ausführst, darfst du die (%STRAIGHT% 2) Manöverschablone verwenden anstatt der (%STRAIGHT% 1) Manöverschablone."
    },
    "Omega Squadron Pilot": {
      ship: "TIE/EO-Jäger",
      name: "Pilot der Omega-Staffel"
    },
    "Zeta Squadron Pilot": {
      ship: "TIE/EO-Jäger",
      name: "Pilot der Zeta-Staffel"
    },
    "Epsilon Squadron Pilot": {
      ship: "TIE/EO-Jäger",
      name: "Pilot der Epsilon-Staffel"
    },
    '"Omega Leader"': {
      ship: "TIE/EO-Jäger",
      name: '"Omega Eins"',
      text: 'Feindliche Schiffe, die du in der Zielerfassung hast, können keine Würfel modifizieren, sobald sie dich angreifen oder sich gegen dich verteidigen.'
    },
    '"Zeta Leader"': {
      ship: "TIE/EO-Jäger",
      name: '"Zeta Eins"',
      text: 'Sobald du angreifst und falls du nicht gestresst bist, darfst du 1 Stressmarker erhalten, um 1 zusätzlichen Würfel zu werfen.'
    },
    '"Epsilon Ace"': {
      ship: "TIE/EO-Jäger",
      name: '"Ass Epsilon"',
      text: 'Solange du keine Schadenskarten hast, behandle deinen Pilotenwert als "12".'
    },
    'Gozanti-class Cruiser': {
      ship: "Kreuzer der Gozanti-Klasse",
      name: "Kreuzer der Gozanti-Klasse",
      text: "Nachdem du ein Manöver ausgeführt hast, darfst du 2 angedockte Schiffe absetzen."
    },
    '"Scourge"': {
      ship: "TIE-Jäger",
      name: "Geissel",
      text: "Sobald du einen Verteidiger angreifst, der 1 oder mehr Schadenskarten hat, wirf 1 zusätzlichen Angriffswürfel."
    },
    '"Youngster"': {
      ship: "TIE-Jäger",
      text: "Freundliche TIE-Jäger in Reichweite 1-3 dürfen die Aktion einer von dir ausgerüsteten %ELITE%-Aufwertung durchführen."
    },
    '"Wampa"': {
      ship: "TIE-Jäger",
      text: "Sobald du angreifst, darfst du alle Würfelergebnisse negieren. Negierst du ein %CRIT%, teile dem Verteidiger 1 verdeckte Schadenskarte zu."
    },
    '"Chaser"': {
      ship: "TIE-Jäger",
      text: "Sobald ein anderes freundliches Schiff in Reichweite 1 einen Fokusmarker ausgibt, wird deinem Schiff ein Fokusmarker zugeteilt."
    },
    'Hera Syndulla': {
      text: 'Sobald du ein grünes oder rotes Manöver aufdeckst, darfst du dein Rad auf ein anderes Manöver mit gleicher Schwierigkeit drehen.'
    },
    "Kanan Jarrus": {
      text: "Sobald ein feindliches Schiff in Reichweite 1-2 angreift, darfst du einen Fokusmarker ausgeben. Tust du das, wirft der Angreifer 1 Angriffswürfel weniger."
    },
    '"Chopper"': {
      text: "Zu Beginn der Kampfphase erhält jedes feindliche Schiff, das du berührst, 1 Stressmarker."
    },
    "Lothal Rebel": {
      name: "Rebell von Lothal"
    },
    'Ezra Bridger': {
      ship: "Jagdshuttle",
      text: "Falls du Stressmarker hast, darfst du, sobald du dich verteidigst, bis zu 2 deiner %FOCUS% in %EVADE% ändern."
    },
    'Hera Syndulla (Attack Shuttle)': {
      ship: "Jagdshuttle",
      name: "Hera Syndulla (Jagdshuttle)",
      text: "Sobald du ein grünes oder rotes Manöver aufdeckst, darfst du dein Rad auf ein anderes Manöver mit gleicher Schwierigkeit drehen."
    },
    'Sabine Wren': {
      ship: "Jagdshuttle",
      text: "Unmittelbar vor dem Aufdecken deines Manövers darfst du als freie Aktion einen Schub oder eine Fassrolle durchführen."
    },
    '"Zeb" Orrelios': {
      ship: "Jagdshuttle",
      text: 'Sobald du dich verteidigst, darfst du %CRIT% vor %HIT% negieren.'
    },
    "Contracted Scout": {
      name: "Angeheuerter Kundschafter"
    },
    "Dengar": {
      text: "Ein Mal pro Runde darfst du nach dem Verteidigen einen Angriff auf den Angreifer durchführen, falls er sich in deinem Feuerwinkel befindet."
    },
    "Tel Trevura": {
      text: "Wenn du zum ersten Mal zerstörst werden würdest, negiere stattdessen alle restlichen Schaden, lege alle Schadenskarten ab und teile diesem Schiff 4 verdeckte Schadenskarten zu."
    },
    "Manaroo": {
      text: "Zu Beginn der Kampfphase darfst du alle dir zugeordneten Fokus-, Ausweich- und Zielerfassungsmarker einem anderen freundlichen Schiff zuordnen."
    },
    "Sienar Test Pilot": {
      ship: "TIE-Turbojäger-Prototyp",
      name: "Sienar-Testpilot"
    },
    "Baron of the Empire": {
      ship: "TIE-Turbojäger-Prototyp",
      name: "Imperialer Baron"
    },
    "Valen Rudor": {
      ship: "TIE-Turbojäger-Prototyp",
      text: "Nachdem du verteidigt hast, darfst du eine freie Aktion durchführen."
    },
    "The Inquisitor": {
      ship: "TIE-Turbojäger-Prototyp",
      name: "Der Inquisitor",
      text: "Sobald du mit deinen Primärwaffen in Reichweite 2-3 angreifst, behandle die Reichweite des Angriffs als Reichweite 1."
    },
    "4-LOM": {
      ship: "G-1A-Sternenjäger",
      text: "Zu Beginn der Endphase darfst du 1 deiner Stressmarker einem anderen Schiff in Reichweite 1 zuordnen."
    },
    "Ruthless Freelancer": {
      ship: "G-1A-Sternenjäger",
      name: "Skrupelloser Söldner"
    },
    "Gand Findsman": {
      ship: "G-1A-Sternenjäger",
      name: "Gand-Finder"
    },
    "Zuckuss": {
      ship: "G-1A-Sternenjäger",
      text: "Sobald du angreifst, darfst du 1 zusätzlichen Angriffswürfel werfen. Falls du das tust, wirft der Verteidiger 1 zusätzlichen Verteidigungswürfel."
    },
    'Tomax Bren': {
      ship: "TIE-Bomber",
      text: 'Once per round, after you discard an %ELITE% Upgrade card, flip that card faceup.'
    },
    '"Deathfire"': {
      text: 'When you reveal your maneuver dial or after you perform an action, you may perform a %BOMB% Upgrade card action as a free action.'
    },
    "Maarek Stele (TIE Defender)": {
      text: "When your attack deals a faceup Damage card to the defender, instead draw 3 Damage cards, choose 1 to deal, and discard the others.",
      ship: "TIE-Jagdbomber"
    },
    "Countess Ryad": {
      text: "When you reveal a %STRAIGHT% maneuver, you may treat it as a %KTURN% maneuver.",
      ship: "TIE-Jagdbomber"
    },
    "Gamma Squadron Veteran": {
      ship: "TIE-Bomber",
      name: "Veteran der Gamma-Staffel"
    },
    "Glaive Squadron Pilot": {
      ship: "TIE-Jagdbomber",
      name: "Pilot der Glaive-Staffel"
    },
    "Poe Dameron (PS9)": {
      text: "When attacking or defending, if you have a focus token, you may change 1 of your %FOCUS% results to a %HIT% or %EVADE% result.",
      ship: "T-70-X-Flügler"
    },
    '"Snap" Wexley': {
      ship: "T-70-X-Flügler"
    },
    'Jess Pava': {
      ship: "T-70-X-Flügler"
    },
    "Rey": {
      text: "When attacking or defending, if the enemy ship is inside of your firing arc, you may reroll up to 2 of your blank results."
    }
  };
  upgrade_translations = {
    "Ion Cannon Turret": {
      name: "Ionengeschütz",
      text: "<strong>Angriff:</strong> Greife 1 Schiff an (es muss nicht in deinem Feuerwinkel sein).<br /><br />Wenn der Angriff trifft, nimmt das verteidigende Schiff 1 Schaden und erhält 1 Ionenmarker. Dann werden alle übrigen Würfelergebnisse negiert."
    },
    "Proton Torpedoes": {
      name: "Protonen-Torpedos",
      text: "<strong>Angriff (Zielerfassung):</strong>Gib deine Zielerfassung aus und lege diese Karte ab, um diesen Angriff durchzuführen.<br /><br />Du darfst eines deiner %FOCUS% in ein %CRIT% ändern."
    },
    "R2 Astromech": {
      name: "R2 Astromechdroide",
      text: "Du darfst alle Manöver mit Geschwindigkeit 1 und 2 wie grüne Manöver behandeln."
    },
    "R2-D2": {
      text: "Nachdem du ein grünes Manöver ausgeführt hast, darfst du 1 Schild wiederaufladen (bis maximal zum Schildwert)."
    },
    "R2-F2": {
      text: "<strong>Aktion:</strong> Erhöhe deinen Wendigkeitswert bis zum Ende der Spielrunde um 1."
    },
    "R5-D8": {
      text: "<strong>Aktion:</strong> Wirf 1 Verteidigungswürfel.<br /><br />Lege bei %EVADE% oder %FOCUS% 1 deiner verdeckten Schadenskarten ab."
    },
    "R5-K6": {
      text: "Wirf 1 Verteidigungswürfel nachdem du deine Zielerfassungsmarker ausgegeben hast.<br /><br />Bei %EVADE% nimmst du dasselbe Schiff sofort wieder in die Zielerfassung. Für diesen Angriff kannst du die Zielerfassungsmarker nicht erneut ausgeben."
    },
    "R5 Astromech": {
      name: "R5 Astromechdroide",
      text: "Wähle während der Endphase 1 deiner offnen Schadenskarte mit dem Attribut <strong>Schiff</strong> und drehe sie um."
    },
    "Determination": {
      name: "Entschlossenheit",
      text: "Wenn du eine offene Schadenskarte mit dem Attribut <b>Pilot</b> erhältst, wird diese sofort abgelegt (ohne dass der Kartentext in Kraft tritt)."
    },
    "Swarm Tactics": {
      name: "Schwarmtaktik",
      text: "Du darfst zu Beginn der Kampfphase 1 freundliches Schiff in Reichweite 1 wählen.<br /><br />Bis zum Ende dieser Phase wird das gewählte Schiff so behandelt, als hätte es denselben Pilotenwert wie du."
    },
    "Squad Leader": {
      name: "Staffelführer",
      text: "<strong>Aktion:</strong> Wähle ein Schiff in Reichweite 1-2 mit einem geringeren Pilotenwert als du.<br /><br />Das gewählte Schiff darf sofort 1 freie Aktion durchführen."
    },
    "Expert Handling": {
      name: "Flugkunst",
      text: "<strong>Aktion:</strong> Führe als freie Aktion eine Fassrolle durch. Wenn du kein %BARRELROLL%-Symbol hast, erhältst du 1 Stressmarker.<br /><br />Dann darfst du 1 feindlichen Zielerfassungsmarker von deinem Schiff entfernen."
    },
    "Marksmanship": {
      name: "Treffsicherheit",
      text: "<strong>Aktion:</strong> Wenn du in dieser Runde angreifst, darfst du eines deiner %FOCUS% in ein %CRIT% und alle anderen %FOCUS% in %HIT% ändern."
    },
    "Concussion Missiles": {
      name: "Erschütterungsraketen",
      text: "<strong>Angriff (Zielerfassung):</strong> Gib eine Zielerfassung aus und lege diese Karte ab, um mit dieser Sekundärwaffe anzugreifen.<br /><br />Du darfst eine deiner Leerseiten in ein %HIT% ändern."
    },
    "Cluster Missiles": {
      name: "Cluster-Raketen",
      text: "<strong>Angriff (Zielerfassung):</strong> Gib eine Zielerfassung aus und lege diese Karte ab, um mit dieser Sekundärwaffe <strong>zwei Mal</strong> anzugreifen"
    },
    "Daredevil": {
      name: "Draufgänger",
      text: "<strong>Aktion:</strong> Führe ein weißes (%TURNLEFT% 1) oder (%TURNRIGHT% 1) Manöver aus. Dann erhältst du einen Stressmarker.<br /><br />Wenn du kein %BOOST%-Aktionssymbol hast, musst du dann 2 Angriffswürfel werfen. Du nimmst allen gewürfelten Schaden (%HIT%) und kritischen Schaden (%CRIT%)."
    },
    "Elusiveness": {
      name: "Schwer zu Treffen",
      text: "Wenn du verteidigst, darfst du 1 Stressmarker nehmen, um 1 Angriffswürfel zu wählen. Diesen muss der Angreifer neu würfeln.<br /><br />Du kannst diese Fähigkeit nicht einsetzen, solange du 1 oder mehrere Stressmarker hast."
    },
    "Homing Missiles": {
      name: "Lenkraketen",
      text: "<strong>Angriff (Zielerfassung):</strong> Lege diese Karte ab, um diesen Angriff durchzuführen.<br /><br />Bei diesem Angriff kann der Verteidiger keine Ausweichmarker ausgeben."
    },
    "Push the Limit": {
      name: "Bis an die Grenzen",
      text: "Einmal pro Runde darfst du nach dem Durchführen einer Aktion eine freie Aktion aus deiner Aktionsleiste durchführen.<br /><br />Dann erhältst du 1 Stressmarker."
    },
    "Deadeye": {
      name: "Meisterschütze",
      text: "Du darfst die Bedingung \"Angriff (Zielerfassung):\" in \"Angriff (Fokussierung):\" ändern.<br /><br />Wenn ein Angriff das Ausgeben von Zielerfassungsmarkern erfordert, darfst du stattdessen auch einen Fokusmarker ausgeben."
    },
    "Expose": {
      name: "Aggressiv",
      text: "<strong>Aktion:</strong> Bis zum Ende der Runde steigt dein Primärwaffenwert um 1, dafür sinkt dein Wendigkeitswert um 1."
    },
    "Gunner": {
      name: "Bordschütze",
      text: "Unmittelbar nachdem du mit einem Angriff verfehlt hast, darfst du einen weiteren Angriff mit deiner Primärwaffe durchführen. Danach kannst du in dieser Runde nicht noch einmal angreifen."
    },
    "Ion Cannon": {
      name: "Ionenkanonen",
      text: "<strong>Angriff:</strong> Greife 1 Schiff mit dieser Sekundärwaffe an.<br /><br />Wenn du triffst, nimmt das verteidigende Schiff 1 Schaden und erhält 1 Ionenmarker. Dann werden <b>alle</b> übrigen Würfelergebnisse negiert."
    },
    "Heavy Laser Cannon": {
      name: "Schwere Laserkanone",
      text: "<strong>Attack:</strong> Greife 1 Schiff mit dieser Sekundärwaffe an.<br /><br />Unmittelbar nach dem Angriffswurf musst du alle %CRIT% in %HIT% ändern."
    },
    "Seismic Charges": {
      name: "Seismische Bomben",
      text: "Nach dem Aufdecken deines Manöverrads darfst du diese Karte ablegen um 1 Seismischen Bomben-Marker zu <strong>legen</strong>.<br /><br />Der Marker <strong>detoniert</strong> am Ende der Aktivierungsphase."
    },
    "Mercenary Copilot": {
      name: "Angeheuerter Kopilot",
      text: "Wenn du ein Ziel in Reichweite 3 angreifst, darfst du eines deiner %HIT%  in ein %CRIT% ändern."
    },
    "Assault Missiles": {
      name: "Angriffsraketen",
      text: "Angriff (Zielerfassung): Gib eine Zielerfassung aus und lege diese Karte ab, um mit dieser Sekundärwaffe anzugreifen.<br /><br />Wenn du triffst, nimmt jedes andere Schiff in Reichweite 1 des verteidigendes Schiffs 1 Schaden."
    },
    "Veteran Instincts": {
      name: "Veteraneninstinkte",
      text: "Dein Pilotenwert steigt um 2."
    },
    "Proximity Mines": {
      name: "Annährungsminen",
      text: "<strong>Aktion:</strong> Lege diese Karte ab, um 1 Annährungsminen-Marker zu <strong>legen</strong>.<br /><br />Der Marker <strong>detoniert</strong>, sobald sich die Basis eines Schiffs oder die Manöverschablone mit dem Marker überschneidet."
    },
    "Weapons Engineer": {
      name: "Waffen-Techniker",
      text: "Du darfst 2 verschiedene Schiffe gleichzeitig in der Zielerfassung haben (maximal 1 Zielerfassung pro feindlichem Schiff).<br /><br />Sobald du eine Zielerfassung durchführst, darfst du zwei verschiedene Schiffe als Ziele erfassen."
    },
    "Draw Their Fire": {
      name: "Das Feuer auf mich ziehen",
      text: "Wenn ein freundliches Schiff in Reichweite 1 durch einen Angriff getroffen wird, darfst du anstelle dieses Schiffs den Schaden für 1 nicht-negiertes %CRIT% auf dich nehmen."
    },
    "Luke Skywalker": {
      text: "%DE_REBELONLY%%LINEBREAK%Unmittelbar nachdem du mit einem Angriff verfehlt hast, darfst du einen weiteren Angriff mit deiner Primärwaffe durchführen. Du darfst ein %FOCUS% in ein %HIT% ändern. Danach kannst du in dieser Runde nicht noch einmal angreifen."
    },
    "Nien Nunb": {
      text: "%DE_REBELONLY%%LINEBREAK%Du darfst alle %STRAIGHT%-Manöver wie grüne Manöver behandeln."
    },
    "Chewbacca": {
      name: "Chewbacca (Crew)",
      text: "%DE_REBELONLY%%LINEBREAK%Wenn du eine Schadenskarte erhältst, darfst du sie sofort ablegen und 1 Schild wiederaufladen.<br /><br />Danach wird diese Aufwertungskarte abgelegt."
    },
    "Advanced Proton Torpedoes": {
      name: "Verstärkte Protonen-Torpedos",
      text: "<strong>Angriff (Zielerfassung):</strong> Gib eine Zielerfassung aus und lege diese Karte ab um mit dieser Sekundärwaffe anzugreifen.<br /><br />Du darfst bis zu 3 deiner Leerseiten in %FOCUS% ändern."
    },
    "Autoblaster": {
      name: "Repetierblaster",
      text: "<strong>Angriff:</strong> Greife 1 Schiff mit dieser Sekundärwaffe an.<br /><br />Deine %HIT% können von Verteidigungswürfeln nicht negiert werden.<br /><br />Der Verteidiger darf %CRIT% negieren, bevor alle %HIT% negiert wurden."
    },
    "Fire-Control System": {
      name: "Feuerkontrollsystem",
      text: "Nachdem du angegriffen hast, darfst du eine Zielerfassung auf den Verteidiger durchführen."
    },
    "Blaster Turret": {
      name: "Blastergeschütz",
      text: "<strong>Angriff (Fokussierung):</strong> Gib 1 Fokusmarker aus, um 1 Schiff mit dieser Sekundärwaffe anzugreifen (es muss nicht in deinem Feuerwinkel sein)."
    },
    "Recon Specialist": {
      name: "Aufklärungs-Experte",
      text: "Wenn du die Aktion Fokussieren durchführst, lege 1 zusätzlichen Fokusmarker neben dein Schiff."
    },
    "Saboteur": {
      text: "<strong>Aktion:</strong> Wähle 1 feindliches Schiff in Reichweite 1 und wirf 1 Angriffswürfel. Bei %HIT% oder %CRIT%, wähle 1 zufällige verdeckte Schadenskarte des Schiffs, decke sie auf und handle sie ab."
    },
    "Intelligence Agent": {
      name: "Geheimagent",
      text: "Wähle zu Beginn der Aktivierungsphase 1 feindliches Schiff in Reichweite 1-2. Du darfst dir das ausgewählte Manöver dieses Schiffs ansehen."
    },
    "Proton Bombs": {
      name: "Protonenbomben",
      text: "Nach dem Aufdecken deines Manöverrads darfst du diese Karte ablegen um 1 Protonenbomben-Marker zu <strong>legen</strong>.<br /><br />Der Marker <strong>detoniert</strong> am Ende der Aktivierungsphase."
    },
    "Adrenaline Rush": {
      name: "Adrenalinschub",
      text: "Wenn du ein rotes Manöver aufdeckst, darfst du diese Karte ablegen, um das Manöver bis zum Ende der Aktivierungsphase wie ein weißes Manöver zu behandeln."
    },
    "Advanced Sensors": {
      name: "Verbesserte Sensoren",
      text: "Unmittelbar vor dem Aufdecken deines Manövers darfst du 1 freie Aktion durchführen.<br /><br />Wenn du diese Fähigkeit nutzt, musst du den Schritt \"Aktion durchführen\" in dieser Runde überspringen."
    },
    "Sensor Jammer": {
      name: "Störsender",
      text: "Beim Verteidigen darfst du eines der %HIT% des Angreifers in ein %FOCUS% ändern.<br /><br />Der Angreifer darf den veränderten Würfel nicht neu würfeln."
    },
    "Darth Vader": {
      name: "Darth Vader (Crew)",
      text: "%DE_IMPERIALONLY%%LINEBREAK%Nachdem du ein feindliches Schiff angegriffen hast, darfst du 2 Schaden nehmen, damit dieses Schiff 1 kritischen Schaden nimmt."
    },
    "Rebel Captive": {
      name: "Gefangener Rebell",
      text: "%DE_IMPERIALONLY%%LINEBREAK%Ein Mal pro Runde erhält das erste Schiff, das einen Angriff gegen dich ansagt, sofort 1 Stressmarker."
    },
    "Flight Instructor": {
      name: "Fluglehrer",
      text: "Beim Verteidigen darfst du 1 deiner %FOCUS% neu würfeln. Hat der Angreifer einen Pilotenwert von 2 oder weniger, darfst du stattdessen 1 deiner Leerseiten neu würfeln."
    },
    "Navigator": {
      name: "Navigator",
      text: "Nach dem Aufdecken deines Manöverrads darfst du das Rad auf ein anderes Manöver mit gleicher Flugrichtung drehen.<br /><br />Wenn du bereits Stressmarker hast, darfst du es nicht auf ein rotes Manöver drehen."
    },
    "Opportunist": {
      name: "Opportunist",
      text: "Wenn du angreifst und der Verteidiger keine Fokusmarker oder Ausweichmarker hat, kannst du einen Stressmarker nehmen, um einen zusätzlichen Angriffswürfel zu erhalten.<br /><br />Du kannst diese Fähigkeit nicht nutzen, wenn du einen Stressmarker hast."
    },
    "Comms Booster": {
      name: "Kommunikationsverstärker",
      text: "<strong>Energie:</strong> Gib 1 Energie aus, um sämtliche Stressmarker von einem freundlichen Schiff in Reichweite 1-3 zu entfernen. Dann erhält jenes Schiff 1 Fokusmarker."
    },
    "Slicer Tools": {
      name: "Hackersoftware",
      text: "<strong>Aktion:</strong> Wähle 1 oder mehrere feindliche Schiffe mit Stressmarker in Reichweite 1-3. Bei jedem gewählten Schiff kannst du 1 Energie ausgeben, damit es 1 Schaden nimmt."
    },
    "Shield Projector": {
      name: "Schildprojektor",
      text: "Wenn ein feindliches Schiff in der Kampfphase an die Reihe kommt, kannst du 3 Energie ausgeben, um das Schiff bis zum Ende der Phase dazu zu zwingen dich anzugreifen, falls möglich."
    },
    "Ion Pulse Missiles": {
      name: "Ionenpuls-Raketen",
      text: "<strong>Angriff (Zielerfassung):</strong> Lege diese Karte ab, um mit dieser Sekundärwaffe anzugreifen.<br /><br />Wenn du triffst, nimmt das verteidigende Schiff 1 Schaden und erhält 2 Ionenmarker. Dann werden <strong>alle<strong> übrigen Würfelergebnisse negiert."
    },
    "Wingman": {
      name: "Flügelmann",
      text: "Entferne zu Beginn der Kampfphase 1 Stressmarker von einem anderen freundlichen Schiff in Reichweite 1."
    },
    "Decoy": {
      name: "Täuschziel",
      text: "Zu Beginn der Kampfphase darfst du 1 freundliches Schiff in Reichweite 1-2 wählen. Bis zum Ende der Phase tauscht du mit diesem Schiff den Pilotenwert."
    },
    "Outmaneuver": {
      name: "Ausmanövrieren",
      text: "Wenn du ein Schiff innerhalb deines Feuerwinkels angreifst und selbst nicht im Feuerwinkel dieses Schiffs bist, wird seine Wendigkeit um 1 reduziert (Minimum 0)"
    },
    "Predator": {
      name: "Jagdinstinkt",
      text: "Wenn du angreifst, darfst du 1 Angriffswürfel neu würfeln. Ist der Pilotenwert des Verteidigers2 oder niedriger, darfst du stattdessen bis zu 2 Angriffswürfel neu würfeln."
    },
    "Flechette Torpedoes": {
      name: "Flechet-Torpedos",
      text: "<strong>Angriff (Zielerfassung):</strong> Gib deine Zielerfassungsmarker aus und lege diese Karte ab, um mit dieser Sekundärwaffe anzugreifen.<br /><br />Nachdem du angegriffen hast, bekommt der Verteidiger 1 Stressmarker, sofern sein Hüllenwert 4 oder weniger beträgt."
    },
    "R7 Astromech": {
      name: "R7-Astromech-Droide",
      text: "Ein Mal pro Runde kannst du beim Verteidigen gegen den Angriff eines Schiffs, das du in Zielerfassung hast, die Zielerfassungsmarker ausgeben, um beliebige (oder alle) Angriffswürfel zu wählen. Diese muss der Angreifer neu würfeln."
    },
    "R7-T1": {
      name: "R7-T1",
      text: "<strong>Aktion:</strong> Wähle ein feindliches Schiff in Reichweite 1-2. Wenn du im Feuerwinkel dieses Schiffs bist, kannst du es in die Zielerfassung nehmen. Dann darfst du als freie Aktion einen Schub durchführen."
    },
    "Tactician": {
      name: "Taktiker",
      text: "Nachdem du ein Schiff in Reichweite 2 und innerhalb deines Feuerwinkels angegriffen hast, erhält es 1 Stressmarker."
    },
    "R2-D2 (Crew)": {
      name: "R2-D2 (Crew)",
      text: "%DE_REBELONLY%%LINEBREAK%Wenn du am Ende der Endphase keine Schilde hast, darfst du 1 Schild wieder aufladen und 1 Angriffswürfel werfen. Bei %HIT% musst du 1 deiner verdeckten Schadenskarten (zufällig gewählt) umdrehen und abhandeln."
    },
    "C-3PO": {
      name: "C-3PO",
      text: "%DE_REBELONLY%%LINEBREAK%Einmal pro Runde darfst du, bevor du 1 oder mehrere Verteidigungswürfel wirfst, laut raten, wie viele %EVADE% du würfeln wirst. Wenn du richtig geraten hast (bevor die Ergebnisse modifiziert werden), wird 1 %EVADE% hinzugefügt."
    },
    "Single Turbolasers": {
      name: "Einzelne Turbolasers",
      text: "<strong>Angriff (Energie):</strong> gib 2 Energie von dieser Karte aus, um mit dieser Sekundärwaffe anzugreifen. Der Verteidiger verwendet zum Verteidigen seinen doppelten Wendigkeitswert. Du darfst 1 deiner %FOCUS% in ein %HIT% ändern."
    },
    "Quad Laser Cannons": {
      name: "Vierlings-Laserkanone",
      text: "<strong>Angriff (Energie):</strong> Gib 1 Energie von dieser Karte aus, um mit dieser Sekundärwaffe anzugreifen. Wenn der Angriff verfehlt, kannst du sofort 1 Energie von dieser Karte ausgeben, um den Angriff zu wiederholen."
    },
    "Tibanna Gas Supplies": {
      name: "Tibanna-Gas-Vorräte",
      text: "<strong>Energie:</strong> Du kannst diese Karte ablegen, um 3 Energie zu erzeugen."
    },
    "Ionization Reactor": {
      name: "Ionenreaktor",
      text: "<strong>Energie:</strong> Gib 5 Energie von dieser Karte aus und lege sie ab, damit jedes andere Schiff in Reichweite 1 einen Schaden nimmt und einen Ionenmarker bekommt."
    },
    "Engine Booster": {
      name: "Nachbrenner",
      text: "Unmittelbar bevor du dein Manöverrad aufdeckst, kannst du 1 Energie ausgeben, um ein weißes (%STRAIGHT% 1)-Manöver auszuführen. Wenn es dadurch zur Überschneidung mit einem anderen Schiff käme, darfst du diese Fähigkeit nicht nutzen."
    },
    "R3-A2": {
      name: "R3-A2",
      text: "Nachdem du das Ziel deines Angriffs angesagt hast, darfst du, wenn der Verteidiger in deinem Feuerwinkel ist, 1 Stressmarker nehmen, damit der Verteidiger auch 1 Stressmarker bekommt."
    },
    "R2-D6": {
      name: "R2-D6",
      text: "Deine Aufwertungsleiste bekommt ein %ELITE%-Symbol.<br /><br />Du kannst diese Aufwertung nicht ausrüsten, wenn du bereits ein %ELITE%-Symbol hast oder dein Pilotenwert 2 oder weniger beträgt."
    },
    "Enhanced Scopes": {
      name: "Verbessertes Radar",
      text: "Behandle in der Aktivierungsphase deinen Pilotenwert als \"0\"."
    },
    "Chardaan Refit": {
      name: "Chardaan-Nachrüstung",
      text: "<span class=\"card-restriction\">Nur für A-Wing</span>%LINEBREAK%Diese Karte hat negative Kommandopunktekosten."
    },
    "Proton Rockets": {
      name: "Protonenraketen",
      text: "<strong>Angriff (Fokussierung):</strong> Lege diese Karte ab, um mit dieser Sekundärwaffe anzugreifen.<br /><br />Du darfst so viele zusätzliche Angriffswürfel werfen, wie du Wendigkeit hast (maximal 3 zusätzliche Würfel)."
    },
    "Kyle Katarn": {
      name: "Kyle Katarn (Crew)",
      text: "%DE_REBELONLY%%LINEBREAK%Nachdem du einen Stressmarker von deinem Schiff entfernt hast, darfst du deinem Schiff einen Fokusmarker geben."
    },
    "Jan Ors": {
      name: "Jan Ors (Crew)",
      text: "%DE_REBELONLY%%LINEBREAK%Sobald ein freundliches Schiff in Reichweite 1-3 eine Aktion Fokussierung durchführt oder ihm ein Fokusmarker zugeordnet werden würde, darfst du diesem Schiff stattdessen ein Mal pro Runde einen Ausweichmarker zuordnen."
    },
    "Toryn Farr": {
      text: "%DE_HUGESHIPONLY%%LINEBREAK%%DE_REBELONLY%%LINEBREAK%<strong>Aktion:</strong> Gib X Energie aus, um X feindliche Schiffe in Reichweite 1-2 zu wählen. Sämtliche Fokus-, Ausweich- und blauen Zielerfassungsmarker dieser Schiffe werden entfernt."
    },
    "R4-D6": {
      text: "Wenn du von einem Angriff getroffen wirst und es mindestens 3 nicht negierte %HIT% gibt, darfst du so viele %HIT% wählen und negieren, bis es nur noch 2 sind. Für jedes auf diese Weise negierte %HIT% bekommst du 1 Stressmarker."
    },
    "R5-P9": {
      text: "Am Ende der Kampfphase kannst du 1 deiner Fokusmarker ausgeben, um 1 Schild wiederaufzuladen (bis maximal zum Schildwert)."
    },
    "WED-15 Repair Droid": {
      name: "WED-15 Reparaturdroide",
      text: "%DE_HUGESHIPONLY%%LINEBREAK%<strong>Aktion:</strong> gib 1 Energie aus, um 1 deiner verdeckten Schadenskarten abzulegen oder gib 3 Energie aus, um 1 deiner offenen Schadenskarten abzulegen."
    },
    "Carlist Rieekan": {
      text: "%DE_HUGESHIPONLY%%LINEBREAK%%DE_REBELONLY%%LINEBREAK%Zu Beginn der Aktivierungsphase kannst du diese Karte ablegen, damit bis zum Ende der Phase der Pilotenwert aller freundlichen Schiffe 12 beträgt."
    },
    "Jan Dodonna": {
      text: "%DE_HUGESHIPONLY%%LINEBREAK%%DE_REBELONLY%%LINEBREAK%Wenn ein anderes freundliches Schiff in Reichweite 1 angreift, darf es 1 seiner gewürfelten %HIT% in ein %CRIT% ändern."
    },
    "Expanded Cargo Hold": {
      name: "Erweiterter Ladebereich",
      text: "Ein Mal pro Runde darfst du, wenn du eine offene Schadenskarte erhältst, frei wählen, ob du sie vom Schadensstapel Bug oder Heck ziehen willst.",
      ship: "Medium-Transporter GR-75"
    },
    "Backup Shield Generator": {
      name: "Sekundärer Schildgenerator",
      text: "Am Ende jeder Runde kannst du 1 Energie ausgeben, um 1 Schild wiederaufzuladen (bis maximal zum Schildwert)."
    },
    "EM Emitter": {
      name: "EM-Emitter",
      text: "Wenn du bei einem Angriff die Schussbahn versperrst, bekommst der Verteidiger 3 zusätzliche Verteidigungswürfel (anstatt 1)."
    },
    "Frequency Jammer": {
      name: "Störsender (Fracht)",
      text: "Wenn du die Aktion Störsignal durchführst, wähle 1 feindliches Schiff ohne Stressmarker in Reichweite 1 des vom Störsignal betroffenen Schiffs. Das gewählte Schiff erhält 1 Stressmarker."
    },
    "Han Solo": {
      name: "Han Solo (Crew)",
      text: "%DE_REBELONLY%%LINEBREAK%Wenn du angreifst und den Verteidiger in Zielerfassung hast, kannst du diese Zielerfassung ausgeben, um all deine gewürfelten %FOCUS% in %HIT% zu ändern."
    },
    "Leia Organa": {
      text: "%DE_REBELONLY%%LINEBREAK%Zu Beginn der Aktivierungsphase kannst du diese Karte ablegen, damit alle freundlichen Schiffe, die ein rotes Manöver aufdecken, dieses bis zum Ende der Phase wie ein weißes Manöver behandeln dürfen."
    },
    "Targeting Coordinator": {
      text: "<strong>Energy:</strong> You may spend 1 energy to choose 1 friendly ship at Range 1-2.  Acquire a target lock, then assign the blue target lock token to the chosen ship."
    },
    "Raymus Antilles": {
      text: "%DE_HUGESHIPONLY%%LINEBREAK%%DE_REBELONLY%%LINEBREAK%Wähle zu Beginn der Aktivierungsphase 1 feindliches Schiff in Reichweite 1-3. Du kannst dir das gewählte Manöver dieses Schiffes ansehen. Wenn es weiß ist, bekommt dieses Schiff 1 Stressmarker."
    },
    "Gunnery Team": {
      name: "Bordschützenteam",
      text: "Einmal pro Runde kannst du beim Angreifen mit einer Sekundärwaffe 1 Energie ausgeben, um 1 gewürfelte Leerseite in ein %HIT% zu ändern."
    },
    "Sensor Team": {
      name: "Sensortechnikerteam",
      text: "Du kannst feindliche Schiffe in Reichweite 1-5 in die Zielerfassung nehmen (anstatt in Reichweite 1-3)."
    },
    "Engineering Team": {
      name: "Ingenieurteam",
      text: "Wenn du in der Aktivierungsphase ein %STRAIGHT% Manöver aufdeckst, bekommst du im Schritt \"Energie gewinnen\" 1 zusätzlichen Energiemarker."
    },
    "Lando Calrissian": {
      name: "Lando Calrissian (Crew)",
      text: "%DE_REBELONLY%%LINEBREAK%<strong>Aktion:</strong> Wirf 2 Verteidigungswürfel. Dein Schiff bekommt 1 Fokusmarker für jedes %FOCUS% und 1 Ausweichmarker für jedes %EVADE%."
    },
    "Mara Jade": {
      text: "%DE_IMPERIALONLY%%LINEBREAK%Am Ende der Kampfphase erhält jedes feindliche Schiff in Reichweite 1, das keine Stressmarker hat, einen Stressmarker."
    },
    "Fleet Officer": {
      name: "Flottenoffizier",
      text: "%DE_IMPERIALONLY%%LINEBREAK%<strong>Aktion:</strong> Wähle bis zu 2 freundliche Schiffe in Reichweite 1-2 und gib ihnen je 1 Fokusmarker. Dann erhältst du 1 Stressmarker."
    },
    "Targeting Coordinator": {
      name: "Zielkoordinator",
      text: "<strong>Energie:</strong> Du kannst 1 Energie ausgeben, um 1 freundliches Schiff in Reichweite1-2 zu wählen. Nimm dann ein Schiff in die Zielerfassung und gibt den blauen Zielerfassungsmarker dem gewählten Schiff."
    },
    "Lone Wolf": {
      name: "Einsamer Wolf",
      text: "Sobald du angreifst oder verteidigst und wenn keine anderen freundlichen Schiffe in Reichweite 1-2 sind, darfst du 1 gewürfelte Leerseite neu würfeln."
    },
    "Stay On Target": {
      name: "Am Ziel bleiben",
      text: "Sobald du ein Manöverrad aufdeckst, darfst du ein anderes Manöver mit gleicher Geschwindigkeit auf deinem Rad einstellen.<br /><br />Dieses Manöver wird wie ein rotes Manöver behandelt."
    },
    "Dash Rendar": {
      name: "Dash Rendar (Crew)",
      text: "%DE_REBELONLY%%LINEBREAK%Du darfst auch angreifen während du dich mit einem Hindernis überschneidest.<br /><br />Deine Schussbahn kann nicht versperrt werden."
    },
    '"Leebo"': {
      name: '"Leebo" (Crew)',
      text: "%DE_REBELONLY%%LINEBREAK%<strong>Aktion:</strong> Führe als freie Aktion einen Schub durch. Dann erhältst du 1 Ionenmarker."
    },
    "Ruthlessness": {
      name: "Erbarmungslos",
      text: "%DE_IMPERIALONLY%%LINEBREAK%Nachdem du mit einem Angriff getroffen hast, <strong>musst</strong> du 1 anderes Schiff in Reichweite 1 des Verteidigers (außer dir selbst) wählen. Das Schiff nimmt 1 Schaden."
    },
    "Intimidation": {
      name: "Furchteinflössend",
      text: "Die Wendigkeit feindlicher Schiffe sinkt um 1, solange du sie berührst."
    },
    "Ysanne Isard": {
      text: "%DE_IMPERIALONLY%%LINEBREAK%Wenn du zu Beginn der Kampfphase keine Schilde und mindestens 1 Schadenskarte hast, darfst du als freie Aktion ausweichen."
    },
    "Moff Jerjerrod": {
      text: "%DE_IMPERIALONLY%%LINEBREAK%Wenn du eine offene Schadenskarte erhältst, kannst du diese Aufwertungskarte oder eine andere %CREW%-Aufwertung ablegen, um die Schadenskarte umzudrehen (ohne dass der Kartentext in Kraft tritt)."
    },
    "Ion Torpedoes": {
      name: "Ionentorpedos",
      text: "<strong>Angriff (Zielerfassung):</strong> Gib deine Zielerfassungsmarker aus und lege diese Karte ab, um mit dieser Sekundärwaffe anzugreifen.<br /><br />Triffst du, erhalten alle Schiffe in Reichweite 1 des Verteidigers und der Verteidiger selbst je 1 Ionenmarker."
    },
    "Bodyguard": {
      name: "Leibwache",
      text: "%DE_SCUMONLY%%LINEBREAK%Zu Beginn der Kampfphase darfst du einen Fokusmarker ausgeben um ein freundliches Schiff in Reichweite 1 zu wählen, dessen Pilotenwert höher ist als deiner. Bis zum Ende der Runde steigt sein Wendigkeitswert um 1."
    },
    "Calculation": {
      name: "Berechnung",
      text: "Sobald du angreifst, darfst du einen Fokusmarker ausgeben, um 1 deiner %FOCUS% in ein %CRIT% zu ändern."
    },
    "Accuracy Corrector": {
      name: "Zielvisor",
      text: "Wenn du angreifst, darfst du während des Schritts \"Angriffswürfel modifizieren\" alle deine Würfelergebnisse negieren. Dann darfst du 2 %HIT% hinzufügen.%LINEBREAK%Deine Würfel können während dieses Angriffs nicht noch einmal modifiziert werden."
    },
    "Inertial Dampeners": {
      name: "Trägheitsdämpfer",
      text: "Sobald du dein Manöverrad aufdeckst, darfst du diese Karte ablegen, um stattdessen ein weißes [0%STOP%]-Manöver auszuführen. Dann erhältst du 1 Stressmarker."
    },
    "Flechette Cannon": {
      name: "Flechettekanonen",
      text: "<strong>Angriff:</strong> Greife 1 Schiffe an.%LINEBREAK%Wenn dieser Angriff trifft, nimmt das verteidigende Schiff 1 Schaden und erhält 1 Stressmarker (falls es noch keinen hat.) Dann werden <strong>alle</strong> Würfelergebnisse negiert."
    },
    '"Mangler" Cannon': {
      name: '"Mangler"-Kanonen',
      text: "<strong>Angriff:</strong> Greife 1 Schiff an.%LINEBREAK%Sobald du angreifst, darfst du 1 deiner %HIT% in ein %CRIT% ändern."
    },
    "Dead Man's Switch": {
      name: "Totmannschalter",
      text: "Sobald du zerstörst wirst, nimmt jedes Schiff in Reichweite 1 einen Schaden."
    },
    "Feedback Array": {
      name: "Rückkopplungsfeld",
      text: "In der Kampfphase darfst du statt einen Angriff durchzuführen 1 Ionenmarker und 1 Schaden nehmen, um ein feindliches Schiff in Reichweite 1 zu wählen. Das gewählte Schiff nimmt 1 Schaden."
    },
    '"Hot Shot" Blaster': {
      text: "<strong>Angriff:</strong> Lege diese Karte ab, um 1 Schiff (auch außerhalb deines Feuerwinkels) anzugreifen."
    },
    "Greedo": {
      text: "%DE_SCUMONLY%%LINEBREAK%In jeder Runde wird bei deinem ersten Angriff und deiner ersten Verteidigung die erste Schadenskarte offen zugeteilt."
    },
    "Salvaged Astromech": {
      name: "Abgewrackter Astromechdroide",
      text: "Sobald du eine Schadenskarte mit dem Attribut <strong>Schiff</strong> erhältst, darfst du sie sofort ablegen (bevor ihr Effekt abgehandelt wird).%LINEBREAK%Danach wird diese Aufwertungskarte abgelegt."
    },
    "Bomb Loadout": {
      name: "Bombenladung",
      text: "<span class=\"card-restriction\">Nur für Y-Wing.</span>%LINEBREAK%Füge deiner Aufwertungsleiste das %BOMB%-Symbol hinzu."
    },
    '"Genius"': {
      name: '"Genie"',
      text: "Wenn du eine Bombe ausgerüstet hast, die gelegt werden kann, sobald du ein Manöver aufdeckst, darfst du die Bombe legen, nachdem du dein Manöver ausgeführt hast."
    },
    "Unhinged Astromech": {
      name: "Ausgeklinkter Astromech-Droide",
      text: "Du darfst alle Manöver mit Geschwindigkeit 3 wie grüne Manöver behandeln."
    },
    "R4-B11": {
      text: "Sobald du angreifst, darfst du, falls du den Verteidiger in der Zielerfassung hast, den Zielerfassungsmarker ausgeben, um beliebig viele Verteidigungswürfel zu wählen. Diese muss der Verteidiger neu würfeln."
    },
    "Autoblaster Turret": {
      name: "Autoblastergeschütz",
      text: "<strong>Angriff:</strong> Greife 1 Schiff (auch außerhalb deines Feuerwinkels) an. %LINEBREAK%Deine %HIT% können von Verteidigungswürfeln nicht negiert werden. Der Verteidiger darf %CRIT% vor %HIT% negieren."
    },
    "R4 Agromech": {
      name: "R4-Agromech-Droide",
      text: "Sobald du angreifst, darfst du, nachdem du einen Fokusmarker ausgegeben hast, den Verteidiger in die Zielerfassung nehmen."
    },
    "K4 Security Droid": {
      name: "K4-Sicherheitsdroide",
      text: "%DE_SCUMONLY%%LINEBREAK%Nachdem du ein grünes Manöver ausgeführt hast, darfst du ein Schiff in die Zielerfassung nehmen."
    },
    "Outlaw Tech": {
      name: "Gesetzloser Techniker",
      text: "%DE_SCUMONLY%%LINEBREAK%Nachdem du ein rotes Manöver ausgeführt hast, darfst du deinem Schiff 1 Fokusmarker zuweisen."
    },
    "Advanced Targeting Computer": {
      name: "Verbesserter Zielcomputer",
      text: "<span class=\"card-restriction\">Nur für TIE Advanced</span>%LINEBREAK%Sobald du mit deiner Primärwaffe angreifst, darfst du deinem Würfelwurf 1 %CRIT% hinzufügen, wenn du den Verteidiger in der Zielerfassung hast. Wenn du das tust, kannst du während dieses Angriffs keine Zielerfassungen ausgeben."
    },
    "Ion Cannon Battery": {
      name: "Ionengeschützbatterie",
      text: "<strong>Angriff (Energie):</strong> Gib 2 Energie von dieser Karte aus, um diesen Angriff durchzuführen. Wenn dieser Angriff trifft, nimmt der Verteidiger 1 kritischen Schaden und erhält 1 Ionenmarker. Dann werden <strong>alle</strong> Würfelergebnisse negiert."
    },
    "Extra Munitions": {
      name: "Ersatzmunition",
      text: "Sobald du diese Karte ausrüstest, lege 1 Munitionsmarker auf jede ausgerüstete %TORPEDO%, %MISSILE% oder %BOMB% Aufwertungskarte. Sobald du angewiesen wirst eine Aufwertungskarte abzulegen, darfst du stattdessen 1 Munitionsmarker von der entsprechenden Karte ablegen."
    },
    "Cluster Mines": {
      name: "Clusterminen",
      text: "<strong>Aktion</strong>: Lege diese Karte ab, um 1 Satz Clusterminenmarker zu <strong>legen</strong>.<br /><br />Ein Clusterminenmarker <strong>detoniert</strong>, sobald sich eine Schiffsbasis oder Manöverschablone mit diesem Marker überschneidet."
    },
    "Glitterstim": {
      name: "Glitzerstim",
      text: "Zu Beginn der Kampfphase darfst du diese Karte ablegen und bekommst 1 Stressmarker. Tust du das , darfst du bis zum Ende der Runde, sobald du angreifst oder verteidigst, alle deine %FOCUS% in %HIT% oder %EVADE% ändern."
    },
    "Grand Moff Tarkin": {
      name: "Grossmoff Tarkin",
      text: "%DE_HUGESHIPONLY% %DE_IMPERIALONLY%%LINEBREAK%Zu Beginn der Kampfphase darfst du ein anderes Schiff in Reichweite 1-4 wählen. Entweder weist du ihm 1 Fokusmarker zu oder du entfernst 1 Fokusmarker von ihm."
    },
    "Captain Needa": {
      text: "%DE_HUGESHIPONLY% %DE_IMPERIALONLY%%LINEBREAK%Wenn du dich in der Aktivierungsphase mit einem Hindernis überschneidest, erhältst du keine offene Schadenskarte. Stattdessen wirfst du 1 Angriffswürfel. Bei %HIT% oder %CRIT% nimmst du 1 Schaden."
    },
    "Admiral Ozzel": {
      text: "%DE_HUGESHIPONLY% %DE_IMPERIALONLY%%LINEBREAK%<strong>Energie:</strong> Du darfst bis zu 3 Schilde von deinem Schiff entfernen. Für jedes entfernte Schild erhältst du 1 Energie."
    },
    "Emperor Palpatine": {
      name: "Imperator Palpatine",
      text: "%DE_IMPERIALONLY%%LINEBREAK%Ein Mal pro Runde darfst du das Ergebnis eines Würfels, den ein freundliches Schiff geworfen hat, in ein beliebiges anderes Ergebnis ändern. Dieses Ergebnis kann nicht nochmal modifiziert werden."
    },
    "Bossk": {
      name: "Bossk (Crew)",
      text: "%DE_SCUMONLY%%LINEBREAK%Nachdem du einen Angriff durchgeführt hast, der nicht geroffen hat, <strong>musst</strong> du 1 Stressmarker bekommen, wenn du keine Stressmarker hast. Weise dann deinem Schiff 1 Fokusmarker zu und nimm den Verteidiger in die Zielerfassung."
    },
    "Lightning Reflexes": {
      name: "Blitzschnelle Reflexe",
      text: "%DE_SMALLSHIPONLY%%LINEBREAK%Nachdem du ein weißes oder grünes Manöver von deinem Rad ausgeführt hast, darfst du diese Karte ablegen, um dein Schiff um 180&deg; zu drehen. Dann erhältst du 1 Stressmarker <strong>nach</strong> dem Schritt \"Stress des Piloten überprüfen\"."
    },
    "Twin Laser Turret": {
      name: "Zwillingslasergeschütz",
      text: "<strong>Angriff:</strong> Führe diesen Angriff zwei Mal durch (auch gegen ein Schiff außerhalb deines Feuerwinkels). Jedes Mal wenn dieser Angriff trifft, nimmt der Verteidiger 1 Schaden. Dann werden <strong>alle</strong> Würfelergebnisse negiert."
    },
    "Plasma Torpedoes": {
      name: "Plasma Torpedos",
      text: "<strong>Angriff (Zielerfassung):</strong> Gib deine Zielerfassung aus und lege diese Karte ab, um diesen Angriff durchzuführen.<br /><br />Falls dieser Angriff trifft, entfernst du nach dem Verursachen von Schaden 1 Schildmarker vom Verteidiger."
    },
    "Ion Bombs": {
      name: "Ionenbomben",
      text: "Sobald du dein Manöverrad aufdeckst, darfst du diese Karte ablegen, um 1 Ionenbombenmarker zu <strong>legen</strong>.<br /><br /> Der Marker <strong>detoniert</strong> am Ende der Aktivierungsphase."
    },
    "Conner Net": {
      name: "Connernetz",
      text: "<strong>Aktion:</strong> Lege diese Karte ab, um 1 Connernetzmarker zu <strong>legen</strong>.<br /><br /> Der Marker <strong>detoniert</strong>, sobald sich eine Schiffsbasis oder Manöverschablone mit dem Marker überschneidet."
    },
    "Bombardier": {
      name: "Bombenschütze",
      text: "Sobald du eine Bombe legst, darfst du die (%STRAIGHT% 2)-Schablone anstatt der (%STRAIGHT% 1)-Schablone verwenden."
    },
    'Crack Shot': {
      name: "Meisterhafter Schuss",
      text: 'Sobald du ein Schiff innerhalb deines Feuerwinkels angreifst, darfst du diese Karte ablegen um 1 gewürfeltes %EVADE% des Verteidigers zu negieren.'
    },
    "Advanced Homing Missiles": {
      name: "Verstärkte Lenkraketen",
      text: "<strong>Angriff (Zielerfassung):</strong> Lege diese Karte ab, um diesen Angriff durchzuführen.%LINEBREAK%Falls dieser Angriff triffst, teile dem Verteidiger 1 offene Schadenskarte zu. Dann werden <strong>alle</strong> Würfelergebnisse negiert."
    },
    'Agent Kallus': {
      text: '%DE_IMPERIALONLY%%LINEBREAK%Wähle zu Beginn der ersten Runde ein kleines oder großes feindliches Schiff. Sobald du dieses Schiff angreifst oder dich gegen dieses Schiff verteidigst, darfst du 1 deiner %FOCUS% in ein %HIT% bzw. %EVADE% ändern.'
    },
    'XX-23 S-Thread Tracers': {
      name: "XX-23-S-Signal-Peilsender",
      text: "<strong>Angriff (Fokussierung):</strong>Lege diese Karte ab, um diesen Angriff auszuführen. Falls dieser Angriff trifft, darf jedes freundliche Schiff in Reichweite 1-2 zu dir den Verteidiger in die Zielerfassung nehmen. Dann werden <strong>alle</strong> Würfelergebnisse negiert."
    },
    "Tractor Beam": {
      name: "Traktorstrahl",
      text: "<strong>Angriff:</strong> Greife 1 Schiff an.%LINEBREAK%Trifft der Angriff, erhält der Verteidiger 1 Traktorstrahlmarker. Dann werden <strong>alle</strong> Würfelergebnisse negiert."
    },
    "Cloaking Device": {
      name: "Tarngerät",
      text: "%DE_SMALLSHIPONLY%%LINEBREAK%<strong>Aktion:</strong> Führe eine freie Aktion Tarnen durch.%LINEBREAK%Falls du getarnt bist, wirfst du am Ende jeder Runde 1 Angriffswürfel. Bei %FOCUS% legst du diese Karte ab, dann enttarnst du dich oder legst deinen Tarnungsmarker ab."
    },
    "Shield Technician": {
      name: "Schildtechniker",
      text: "%DE_HUGESHIPONLY%%LINEBREAK%Sobald du die Aktion Aufladen durchführst, kannst du wählen, wie viel Energie du ausgeben möchtest, anstatt alle Energie auszugeben."
    },
    "Weapons Guidance": {
      name: "Zielführung",
      text: "Sobald du angreifst, darfst du einen Fokus ausgeben, um 1 deiner gewürfelten Leerseiten in %HIT% zu ändern."
    },
    "BB-8": {
      text: "Sobald du eine grünes Manöver aufdeckst, darfst du als freie Aktion eine Fassrolle ausführen."
    },
    "R5-X3": {
      text: "Bevor du dein Manöver aufdeckst, darfst du diese Karte ablegen, um Hindernisse bis zum Ende der Runde zu ignorieren."
    },
    "Wired": {
      name: "Aufgedreht",
      text: "Sobald du angreifst oder verteidigst, und wenn du gestresst bist, darfst du 1 oder mehrere %FOCUS% neu würfeln."
    },
    'Cool Hand': {
      name: "Sichere Hand",
      text: 'Sobald du einen Stressmarker erhältst, darfst du diese Karte ablegen, um deinem Schiff 1 Fokus- oder Ausweichmarker zuzuweisen.'
    },
    'Juke': {
      name: "Finte",
      text: '%DE_SMALLSHIPONLY%%LINEBREAK%Sobald du angreifst und falls du einen Ausweichmarker hast, darfst du 1 %EVADE% des Verteidigers in ein %FOCUS% ändern.'
    },
    'Comm Relay': {
      name: "Kommunikations-Relais",
      text: 'Du kannst nicht mehr als 1 Ausweichmarker haben.%LINEBREAK%Während der Endphase wird ein nicht verwendeter Ausweichmarker nicht entfernt.'
    },
    'Dual Laser Turret': {
      ship: "Kreuzer der Gozanti-Klasse",
      name: "Doppellasergeschütz",
      text: '%DE_GOZANTIONLY%%LINEBREAK%<strong>Angriff (Energie):</strong> Gib 1 Energie von dieser Karte aus, um diesen Angriff gegen 1 Schiff durchzuführen (auch außerhalb deines Feuerwinkels).'
    },
    'Broadcast Array': {
      ship: "Kreuzer der Gozanti-Klasse",
      name: "Sendephalanx",
      text: '%DE_GOZANTIONLY%%LINEBREAK%Deine Aktionsleiste erhält das %JAM%-Aktionssymbol.'
    },
    'Rear Admiral Chiraneau': {
      name: "Konteradmiral Chiraneau",
      text: '%HUGESHIPONLY% %IMPERIALONLY%%LINEBREAK%<strong>Aktion:</strong> Führe ein weißes (%STRAIGHT% 1)-Manöver aus.'
    },
    'Ordnance Experts': {
      name: "Flugkörperexperten",
      text: 'Sobald ein freundliches Schiff in Reichweite 1-3 einen Angriff mit einer %TORPEDO%- oder %MISSILE%-Sekundärwaffe durchführt, darf es ein Mal pro Runde 1 seiner Leerseiten in ein %HIT% ändern.'
    },
    'Docking Clamps': {
      ship: "Kreuzer der Gozanti-Klasse",
      name: "Andockklammern",
      text: '%DE_GOZANTIONLY% %DE_LIMITED%%LINEBREAK%An diesem Schiff können bis zu 4 TIE-Jäger, TIE-Abfangjäger, TIE-Bomber oder TIE-Turbojäger andocken. Alle angedockten Schiffe müssen denselben Schiffstyp haben.'
    },
    '"Zeb" Orrelios': {
      name: '"Zeb" Orrelios (Crew)',
      text: "%REBELONLY%%LINEBREAK%Feindliche Schiffe in deinem Feuerwinkel, deren Basis du berührst, gelten nicht als berührt, sobald du oder sie in der Kampfphase aktiviert werden."
    },
    'Kanan Jarrus': {
      name: "Kanan Jarrus (Crew)",
      text: "%REBELONLY%%LINEBREAK%Ein Mal pro Runde, nachdem ein freundliches Schiff in Reichweite 1-2 ein weißes Manöver ausgeführt hat, darfst du 1 Stressmarker von jenem Schiff entfernen.."
    },
    'Reinforced Deflectors': {
      name: "Verstärkte Deflektoren",
      text: "%LARGESHIPONLY%%LINEBREAK%Nachdem du durch einen Angriff 3 oder mehr Schaden genommen hast, lädst du 1 Schild wieder auf (bis maximal zu deinem Schildwert)."
    },
    'Dorsal Turret': {
      name: "Dorsaler Geschützturm",
      text: "<strong>Angriff:</strong> Greife 1 Schiff an (auch außerhalb deines Feuerwinkels). Falls das Ziel dieses Angriffs in Reichweite 1 ist, wirf 1 zusätzlichen Angriffswürfel."
    },
    'Targeting Astromech': {
      name: "Zielender Astromech",
      text: 'Nachdem du eine rotes Manöver ausgeführt hast, darfst du ein Schiff in die Zielerfassung nehmen.'
    },
    'Hera Syndulla': {
      name: "Hera Syndulla (Crew)",
      text: "%REBELONLY%%LINEBREAK%Du kannst auch rote Manöver aufdecken und ausführen, solange du gestresst bist."
    },
    'Ezra Bridger': {
      name: "Ezra Bridger (Crew)",
      text: "%REBELONLY%%LINEBREAK%Sobald du angreifst und falls du gestresst bist, darfst du 1 deiner %FOCUS% in ein %CRIT% ändern."
    },
    'Sabine Wren': {
      name: "Sabine Wren (Crew)",
      text: "%REBELONLY%%LINEBREAK%Deine Aufwertungsleiste erhält ein %BOMB%-Symbol. Wähle ein Mal pro Runde, vor dem Entfernen eines freundlichen Bombenmarkers, ein feindliches Schiff in Reichweite 1 des Markers. Das gewählte Schiff nimmt 1 Schaden."
    },
    '"Chopper"': {
      name: '"Chopper" (Crew)',
      text: "%REBELONLY%%LINEBREAK%Du darfst auch Aktionen durchführen, solange du gestresst bist.%LINEBREAK%Nachdem du eine Aktion durchgeführt hast, solange du gestresst bist, nimmst du 1 Schaden."
    },
    'Construction Droid': {
      name: "Baudroide",
      text: '%HUGESHIPONLY% %DE_LIMITED%%LINEBREAK%Sobald du die Aktion Aufladen durchführst, darfst du 1 Energie ausgeben, um 1 verdeckte Schadenskarte abzulegen.'
    },
    'Cluster Bombs': {
      name: "Clusterbomben",
      text: 'Nachdem du dich verteidigt hast, darfst du diese Karte ablegen. Wenn du dies tust, wirft jedes andere Schiff in Reichweite 1 der verteidigenden Sektion 2 Angriffswürfel und nimmt allen gewürfelten Schaden (%HIT%) und kritischen Schaden (%CRIT%).'
    },
    "Adaptability": {
      name: "Anpassungsfähig",
      text: "<span class=\"card-restriction\">Doppelseitige Karte.</span>%LINEBREAK%<strong>Seite A:</strong>%LINEBREAK%Dein Pilotwert steigt um 1.%LINEBREAK%<strong>Seite B:</strong>%LINEBREAK%Dein Pilotwert sinkt um 1."
    },
    "Electronic Baffle": {
      name: "Elektronischer Dämpfer",
      text: "Sobald du einen Stressmarker oder Ionenmarker erhältst, darfst du 1 Schaden nehmen, um diesen Marker abzulegen."
    },
    "4-LOM": {
      name: "4-LOM (Crew)",
      text: "%SCUMONLY%%LINEBREAK%Sobald du angreifst, darfst du im Schritt \"Angriffswürfel modifizieren\" 1 Ionenmarker erhalten, um 1 Fokus- oder Ausweichmarker des Verteidigers zu wählen. Der gewählte Marker kann bei diesem Angriff nicht ausgegeben werden."
    },
    "Zuckuss": {
      name: "Zuckuss (Crew)",
      text: "%SCUMONLY%%LINEBREAK%Sobald du angreifst, darfst du beliebig viele Stressmarker erhalten, um ebenso viele Verteidigungswürfel zu wählen. Der Verteidiger muss alle gewählten Würfel neu würfeln."
    },
    'Rage': {
      name: "Wutanfall",
      text: "<strong>Aktion:</strong> Ordne deinem Schiff 1 Fokusmarker zu und erhalte 2 Stressmarker. Bis zum Ende der runde darfst du bis zu 3 Angriffswürfel neu würfeln, sobald du angreifst."
    },
    "Attanni Mindlink": {
      name: "Attanni-Implantat",
      text: "%SCUMONLY%%LINEBREAK%Immer wenn dir ein Fokus- oder Stressmarker zugeordnet wird, muss jedem anderen freundlichen Schiff mit Attanni-Implantat ein Marker desselben Typs zugeordnet werden, falls es diesen nicht schon hat."
    },
    "Boba Fett": {
      name: "Boba Fett (Crew)",
      text: "%SCUMONLY%%LINEBREAK%Nachdem du einen Angriff durchgeführt hast und falls dem Verteidiger eine offene Schadenskarte zugeteilt worden ist, darfst du diese Karte ablegen, um 1 der Aufwertungskarten des Verteidigers zu wählen und abzulegen."
    },
    "Dengar": {
      name: "Dengar (Crew)",
      text: "%SCUMONLY%%LINEBREAK%Sobald du angreifst, darfst du 1 Angriffswürfel neu würfeln. Falls der Verteidiger ein einzigartiger Pilot ist, darfst du stattdessen bis zu 2 Angriffswürfel neu würfeln."
    },
    '"Gonk"': {
      name: '"Gonk" (Crew)',
      text: "%SCUMONLY%%LINEBREAK%<strong>Aktion:</strong> Lege 1 Schildmarker auf diese Karte.%LINEBREAK%<strong>Aktion:</strong> Entferne 1 Schildmarker von dieser Karte, um 1 Schild wieder aufzuladen (bis maximal zu deinem Schildwert)."
    },
    "R5-P8": {
      text: "Ein Mal pro Runde darfst du nach dem Verteidigen 1 Angriffswürfel werfen. Bei %HIT% nimmt der Angreifer 1 Schaden. Bei %CRIT% nehmen du und der Angreifer je 1 Schaden."
    },
    'Thermal Detonators': {
      name: "Thermaldetonatoren",
      text: "Sobald du dein Manöverrad aufdeckst, darfst du diese Karte <strong>ablegen</strong>, um 1 Thermaldetonatormarker zu legen.%LINEBREAK%Der Marker <strong>detoniert</strong> am ende der Aktivierungsphase."
    },
    "Overclocked R4": {
      name: "Übertakteter R4",
      text: "Sobald du in der Kampfphase einen Fokusmarker ausgibst, darfst du 1 Stressmarker erhalten, um deinem Schiff 1 Fokusmarker zuzuordnen."
    },
    'Systems Officer': {
      text: '%IMPERIALONLY%%LINEBREAK%After you execute a green maneuver, choose another friendly ship at Range 1.  That ship may acquire a target lock.'
    }
  };
  modification_translations = {
    "Stealth Device": {
      name: "Tarnvorrichtung",
      text: "Dein Wendigkeitswert steigt um 1. Lege diese Karte ab, wenn du von einem Angriff getroffen wirst."
    },
    "Shield Upgrade": {
      name: "Verbesserte Schilde",
      text: "Dein Schildwert steigt um 1."
    },
    "Engine Upgrade": {
      name: "Verbessertes Triebwerk",
      text: "Füge deiner Aktionsleiste ein %BOOST%-Symbol hinzu."
    },
    "Anti-Pursuit Lasers": {
      name: "Kurzstreckenlaser",
      text: "%DE_LARGESHIPONLY%%LINEBREAK%Nachdem ein feindliches Schiff ein Manöver ausgeführt hat, das zur Überschneidung mit deinem Schiff führt, wirf 1 Angriffswürfel. Bei %HIT% oder %CRIT% nimmt das feindliche Schiff 1 Schaden."
    },
    "Targeting Computer": {
      name: "Zielerfassungssystem",
      text: "Deine Aktionsleiste erhält das %TARGETLOCK%-Symbol."
    },
    "Hull Upgrade": {
      name: "Verbesserte Hülle",
      text: "Erhöhe deinen Hüllenwert um 1."
    },
    "Munitions Failsafe": {
      name: "Ausfallsichere Munition",
      text: "Wenn du mit einer Sekundärwaffe angreifst, deren Kartentext besagt, dass sie zum Angriff abgelegt werden muss, legst du sie nur ab, falls du triffst."
    },
    "Stygium Particle Accelerator": {
      name: "Stygium-Teilchen-Beschleuniger",
      text: "immer wenn du dich enttarnst oder die Aktion Tarnen durchführst, darfst du als freie Aktion ausweichen."
    },
    "Advanced Cloaking Device": {
      ship: "TIE-Phantom",
      name: "Verbesserte Tarnvorrichtung",
      text: '<span class="card-restriction">Nur für TIE-Phantom.</span>%LINEBREAK%Nachdem du angegriffen hast, darfst du dich als freie Aktion tarnen.'
    },
    "Combat Retrofit": {
      name: "Umrüstung für den Kampfeinsatz",
      ship: "Medium-Transporter GR-75",
      text: "Erhöhe deinen Hüllenwert um 2 und deinen Schildwert um 1."
    },
    "B-Wing/E2": {
      text: "Füge deiner Aufwertungsleiste das %CREW%-Symbol hinzu."
    },
    "Countermeasures": {
      name: "Gegenmassnahmen",
      text: "%DE_LARGESHIPONLY%%LINEBREAK%Zu Beginn der Kampfphase kannst du diese Karte ablegen, um deine Wendigkeit bis zum Ende der Runde um 1 zu erhöhen. Dann darfst du 1 feindliche Zielerfassung von deinem Schiff entfernen."
    },
    "Experimental Interface": {
      name: "Experimentelles Interface",
      text: "Ein Mal pro Runde darfst du nach dem Durchführen einer Aktion 1 ausgerüstete Aufwertungskarte mit dem Stichwort \"<strong>Aktion:</strong>\" benutzen (dies zählt als freie Aktion). Dann erhältst du 1 Stressmarker."
    },
    "Tactical Jammer": {
      name: "Taktischer Störsender",
      text: "%DE_LARGESHIPONLY%%LINEBREAK%Dein Schiff kann die feindliche Schussbahn versperren."
    },
    "Autothrusters": {
      name: "Automatische Schubdüsen",
      text: "Sobald du verteidigst und jenseits von Reichweite 2 oder außerhalb des Feuerwinkels des Angreifers bist, darfst du 1 deiner Leerseiten in ein %EVADE% ändern. Du darfst diese Karte nur ausrüsten, wenn du das %BOOST%-Aktionssymbol hast."
    },
    "Advanced SLAM": {
      name: "Verbesserter SLAM",
      text: "Nachdem du die Aktion SLAM durchgeführt hast, darfst du 1 freie Aktion durchführen, falls du dich nicht mit einem Hindernis oder anderen Schiff überschnitten hast."
    },
    "Twin Ion Engine Mk. II": {
      name: "Zwillings-Ionenantrieb MK. II",
      text: "Du darfst alle Drehmanöver (%BANKLEFT% oder %BANKRIGHT%) als grüne Manöver behandeln."
    },
    "Maneuvering Fins": {
      name: "Steuertragflächen",
      text: "Sobald du ein Wendemanöver (%TURNLEFT% oder %TURNRIGHT%) aufdeckst, darfst du das entsprechende Drehmanöver (%BANKLEFT% oder %BANKRIGHT%) mit gleicher Geschwindigkeit auf deinem Manöverrad einstellen."
    },
    "Ion Projector": {
      name: "Ionenprojektor",
      text: "%DE_LARGESHIPONLY%%LINEBREAK%Nachdem ein feindliches Schiff ein Manöver ausgeführt hat, das zur Überschneidung mit deinem Schiff führte, wirf 1 Angriffswürfel. Bei %HIT% oder %CRIT% bekommt das feindliche Schiff 1 Ionenmarker."
    },
    'Integrated Astromech': {
      name: "Integrierter Astromech",
      text: '<span class="card-restriction">Nur für X-Flügler.</span>%LINEBREAK%Sobald dir eine Schadenskarte zugeteilt wird, darfst du 1 deiner %ASTROMECH%-Aufwertungskarten ablegen, um jene Schadenskarte abzulegen (ohne ihren Effekt abzuhandeln).'
    },
    'Optimized Generators': {
      name: "Optimierte Generatoren",
      text: '%HUGESHIPONLY%%LINEBREAK%Ein Mal pro Runde erhältst du 2 Energie, sobald du Energie auf einer ausgerüsteten Aufwertung zuordnest.'
    },
    'Automated Protocols': {
      name: "Vollautomatische Protokolle",
      text: '%HUGESHIPONLY%%LINEBREAK%Ein Mal pro Runde darfst du, nachdem du eine Aktion durchgeführt hast (außer Aufladen und Verstärken), 1 Energie ausgeben, um Aufladen oder Verstärken als freie Aktion durchzuführen.'
    },
    'Ordnance Tubes': {
      name: "Abschussrohre",
      text: '%HUGESHIPONLY%%LINEBREAK%Du darfst jedes deiner %HARDPOINT%-Aufwertungssymbole wie ein %TORPEDO%- oder %MISSILE%- Symbol behandeln.%LINEBREAK%Sobald du angewiesen wirst eine %TORPEDO%- oder %MISSILE%-Aufwertung abzulegen, lege sie nicht ab.'
    },
    'Long-Range Scanners': {
      text: 'You can acquire target locks on ships at Range 3 and beyond.  You cannot acquire target locks on ships at Range 1-2.  You can equip this card only if you have %TORPEDO% and %MISSILE% in your upgrade bar.'
    },
    "Guidance Chips": {
      name: "Steuerungschips",
      text: "Ein Mal pro Runde darfst du, sobald du mit einer %TORPEDO%- oder %MISSILE%-Sekundärwaffe angreifst, 1 Würfelergebnis in ein %HIT% ändern (oder in ein %CRIT%, falls dein Primärwaffenwert 3 oder höher ist)."
    }
  };
  title_translations = {
    "Slave I": {
      name: "Sklave I",
      text: '<span class="card-restriction">Nur für Firespray-31.</span>%LINEBREAK%Füge deiner Aktionsleiste ein %TORPEDO%-Symbol hinzu.'
    },
    "Millennium Falcon": {
      name: "Millennium Falke",
      text: '<span class="card-restriction">Nur für YT-1300.</span>%LINEBREAK%Füge deiner Aktionsleiste ein %EVADE%-Symbol hinzu.'
    },
    "Moldy Crow": {
      text: '<span class="card-restriction">Nur für HWK-290.</span>%LINEBREAK%In der Endphase werden von diesem Schiff keine unbenutzen Fokusmarker entfernt.'
    },
    "ST-321": {
      ship: "Raumfähre der Lambda-Klasse",
      text: '<span class="card-restriction">Nur für Raumfähren der Lamda-Klasse.</span>%LINEBREAK%Wenn du eine Zielerfassung durchführst, darfst du ein beliebiges feindliches Schiff auf der Spielfläche als Ziel erfassen.'
    },
    "Royal Guard TIE": {
      name: "TIE der Roten Garde",
      ship: "TIE-Abfangjäger",
      text: '<span class="card-restriction">Nur für TIE-Abfangjäger.</span>%LINEBREAK%Du kannst bis zu 2 verschiedene Modifikationen verwenden (statt einer).<br /><br />Du kannst diese Karte nicht verwenden, wenn der Pilotenwert "4" oder kleiner ist.'
    },
    "Dodonna's Pride": {
      name: "Dodonnas Stolz",
      ship: "CR90-Korvette (Bug)",
      text: '<span class="card-restriction">Nur für CR90-Korvette (Bug).</span>%LINEBREAK%Wenn du die Aktion Koordination durchführst, kannst du 2 freundliche Schiffe wählen (anstatt 1). Jedes dieser Schiffe darf 1 freie Aktion durchführen.'
    },
    "A-Wing Test Pilot": {
      name: "Erfahrener Testpilot",
      text: '<span class="card-restriction">Nur für A-Wing.</span>%LINEBREAK%Füge deiner Aufwertungsleiste 1 %ELITE%-Symbol hinzu.<br /><br />Du darfst jede %ELITE%-Aufwertung nur ein Mal ausrüsten. Du kannst diese Karte nicht verwenden, wenn dein Pilotenwert "1" oder niedriger ist.'
    },
    "Tantive IV": {
      ship: "CR90-Korvette (Bug)",
      text: '<span class="card-restriction">Nur für CR90-Korvette (Bug).</span>%LINEBREAK%Die Aufwertungsleiste deiner Bugsektion erhält 1 zusätzliches %CREW% und 1 zusätzliches %TEAM% .'
    },
    "Bright Hope": {
      ship: "Medium-Transporter GR-75",
      text: '<span class="card-restriction">Nur für Medium-Transporter GR-75.</span>%LINEBREAK%Wenn neben deiner Bugsektion ein Verstärkungsmarker liegt, fügt er 2 %EVADE% hinzu (anstatt 1).'
    },
    "Quantum Storm": {
      ship: "Medium-Transporter GR-75",
      text: '<span class="card-restriction">Nur für Medium-Transporter GR-75.</span>%LINEBREAK%Wenn du zu Beginn der Endphase 1 Energiemarker oder weniger hast, gewinnst du 1 Energiemarker.'
    },
    "Dutyfree": {
      ship: "Medium-Transporter GR-75",
      text: '<span class="card-restriction">Nur für Medium-Transporter GR-75.</span>%LINEBREAK%Bei der Aktion Störsignal kannst du ein feindliches Schiff in Reichweite 1-3 (statt 1-2) wählen.'
    },
    "Jaina's Light": {
      name: "Jainas Licht",
      ship: "CR90-Korvette (Bug)",
      text: '<span class="card-restriction">Nur für CR90-Korvette (Bug).</span>%LINEBREAK%Wenn du verteidigst, darfst du einmal pro Angriff eine soeben erhaltene, offene Schadenskarte ablegen und dafür eine neue offene Schadenskarte ziehen.'
    },
    "Outrider": {
      text: '<span class="card-restriction">Nur für YT-2400.</span>%LINEBREAK%Solange du eine %CANNON%-Aufwertung ausgerüstet hast, kannst du deine Primärwaffen <strong>nicht</strong> verwenden. Dafür darfst du mit %CANNON%-Sekundärwaffen auch Ziele außerhalb deines Feuerwinkels angreifen.'
    },
    "Dauntless": {
      text: '<span class="card-restriction">Nur für VT-49 Decimator.</span>%LINEBREAK%Nach dem Ausführen eines Manövers, das zur Überschneidung mit einem anderen Schiff geführt hat, darfst du 1 freie Aktion durchführen. Dann erhältst du 1 Stressmarker.'
    },
    "Virago": {
      ship: "SternenViper",
      text: '<span class="card-restriction">Nur für SternenViper.</span>%LINEBREAK%Füge deiner Aufwertungsleiste ein %SYSTEM%- und ein %ILLICIT%-Symbol hinzu.%LINEBREAK%Du kannst diese Karte nicht ausrüsten, wenn dein Pilotenwert "3" oder niedriger ist.'
    },
    '"Heavy Scyk" Interceptor (Cannon)': {
      ship: "M3-A Abfangjäger",
      name: '"Schwerer Scyk"-Abfangjäger (Kannone)',
      text: '<span class="card-restriction">Nur für M3-A-Abfangjäger.</span>%LINEBREAK%Füge deiner Aufwertungsleiste eines der folgenden Symbole hinzu: %CANNON%, %TORPEDO%, oder %MISSILE%.'
    },
    '"Heavy Scyk" Interceptor (Torpedo)': {
      ship: "M3-A Abfangjäger",
      name: '"Schwerer Scyk"-Abfangjäger (Torpedo)',
      text: '<span class="card-restriction">Nur für M3-A-Abfangjäger.</span>%LINEBREAK%Füge deiner Aufwertungsleiste eines der folgenden Symbole hinzu: %CANNON%, %TORPEDO%, oder %MISSILE%.'
    },
    '"Heavy Scyk" Interceptor (Missile)': {
      ship: "M3-A Abfangjäger",
      name: '"Schwerer Scyk"-Abfangjäger (Rakete)',
      text: '<span class="card-restriction">Nur für M3-A-Abfangjäger.</span>%LINEBREAK%Füge deiner Aufwertungsleiste eines der folgenden Symbole hinzu: %CANNON%, %TORPEDO%, oder %MISSILE%.'
    },
    "IG-2000": {
      text: '<span class="card-restriction">Nur für Aggressor.</span>%LINEBREAK%Du bekommst die Pilotenfähigkeiten aller anderen freundlichen Schiffe mit der Aufwertungskarte <em>IG-2000</em> (zusätzlich zu deiner eigenen Pilotenfähigkeit).'
    },
    "BTL-A4 Y-Wing": {
      name: "BTL-A4-Y-Wing",
      text: '<span class="card-restriction">Nur für Y-Wing.</span>%LINEBREAK%Du darfst Schiffe außerhalb deines Feuerwinkels nicht angreifen. Nachdem du einen Angriff mit deinen Primärwaffen durchgeführt hast, darfst du sofort einen weiteren Angriff mit einer %TURRET%-Sekundärwaffe durchführen.'
    },
    "Andrasta": {
      text: '<span class="card-restriction">Nur für Firespray-31.</span>%LINEBREAK%Füge deiner Aufwertungsleiste zwei weitere %BOMB%-Symbole hinzu.'
    },
    "TIE/x1": {
      text: '<span class="card-restriction">Nur für TIE Advanced.</span>%LINEBREAK%Füge deiner Aufwertungsleiste ein %SYSTEM%-Symbol hinzu.%LINEBREAK%Wenn du eine %SYSTEM%-Aufwertung ausrüstest, sinken deren Kommandopunkte um 4 (Minimum 0).'
    },
    "Hound's Tooth": {
      name: "Reisszahn",
      text: '<span class="card-restriction">Nur für YV-666.</span>%LINEBREAK%Nachdem du zerstörst worden bist, darfst du das Schiff <em>Nashtahwelpe</em> <strong>absetzen</strong>, bevor du von der Spielfläche entfernt wirst.%LINEBREAK%Es darf diese Runde nicht angreifen.'
    },
    "Ghost": {
      text: '<span class="card-restriction">Nur für VCX-100.</span>%LINEBREAK%Rüste ein freundlichen Jagdshuttle mit dem Titel <em>Phantom</em> aus und docke es an diesem Schiff an.%LINEBREAK%Nachdem du ein Manöver ausgeführt hast, darfst du das Shuttle von deinen Heck-Stoppern aus starten lassen.'
    },
    "Phantom": {
      ship: "Jagdshuttle",
      text: '<span class="card-restriction">Nur für Jagdshuttle.</span>%LINEBREAK%Solange du angedockt bist, kann die <em>Ghost</em> mit ihren Primärwaffen auch Ziele in ihrem Spezial-Feuerwinkel angreifen und darf am Ende der Kampfphase einen zusätzlichen Angriff mit einer ausgerüsteten %TURRET% durchführen. Falls sie diesen Angriff durchführt kann sie in dieser Runde nicht noch einmal angreifen.'
    },
    "TIE/v1": {
      name: "TIE-V1",
      ship: "TIE-Turbojäger-Prototyp",
      text: '<span class="card-restriction">Nur für TIE-Turbojäger-Prototyp.</span>%LINEBREAK%Nachdem du ein Ziel erfasst hast, darfst du eine freie Aktion Ausweichen durchführen.'
    },
    "Mist Hunter": {
      name: "Nebeljäger",
      ship: "G-1A-Sternenjäger",
      text: '<span class="card-restriction">Nur für G-1A-Sternenjäger.</span>%LINEBREAK%Deine Aktionsleiste erhält ein %BARRELROLL%-Symbol.%LINEBREAK%Du <strong>musst</strong> 1 Aufwertungskarte "Traktorstrahl" ausrüsten (und ihre normalen Kommandopunktekosten bezahlen).'
    },
    "Punishing One": {
      name: "Vollstrecker Eins",
      text: '<span class="card-restriction">Nur für JumpMaster 5000.</span>%LINEBREAK%Erhöhe deinen Primärwaffenwert um 1.'
    },
    "Assailer": {
      ship: "Korv. der Sturm-Klasse (Heck)",
      name: "Sturmbringer",
      text: '<span class="card-restriction">Nur für Korvetten der <em>Sturm</em>-Klasse (Heck).</span>%LINEBREAK%Sobald du verteidigst und wenn die als Ziel bestimmten Sektion einen Verstärkungsmarker hat, darfst du 1 %FOCUS% in ein %EVADE% ändern.'
    },
    "Instigator": {
      ship: "Korv. der Sturm-Klasse (Heck)",
      name: "Hetzer",
      text: '<span class="card-restriction">Nur für Korvetten der <em>Sturm</em>-Klasse (Heck).</span>%LINEBREAK%Nachdem du die Aktion Aufladen durchgeführt hast, lade 1 weiteres Schild wieder auf.'
    },
    "Impetuous": {
      ship: "Korv. der Sturm-Klasse (Heck)",
      name: "Ungestüm",
      text: '<span class="card-restriction">Nur für Korvetten der <em>Sturm</em>-Klasse (Heck).</span>%LINEBREAK%Nachdem du einen Angriff durchgeführt hast, der ein feindliches Schiff zerstört hat, darfst du ein Schiff in die Zielerfassung nehmen..'
    },
    'TIE/x7': {
      ship: "TIE-Jagdbomber",
      text: '<span class="card-restriction">TIE Defender only.</span>%LINEBREAK%Your upgrade bar loses the %CANNON% and %MISSILE% upgrade icons.%LINEBREAK%After executing a 3-, 4-, or 5-speed maneuver, you may assign 1 evade token to your ship.'
    },
    'TIE/D': {
      ship: "TIE-Jagdbomber",
      text: '<span class="card-restriction">TIE Defender only.</span>%LINEBREAK%Once per round, after you perform an attack with a %CANNON% secondary weapon that costs 3 or fewer squad points, you may perform a primary weapon attack.'
    },
    'TIE Shuttle': {
      ship: "TIE-Bomber",
      text: '<span class="card-restriction">TIE Bomber only.</span>%LINEBREAK%Your upgrade bar loses all %TORPEDO%, %MISSILE%, and %BOMB% upgrade icons and gains 2 %CREW% upgrade icons.  You cannot equip a %CREW% Upgrade card that costs more than 4 squad points.'
    },
    'Requiem': {
      ship: "Kreuzer der Gozanti-Klasse",
      text: '%DE_GOZANTIONLY%%LINEBREAK%Sobald du ein Schiff startest, wird es bis zum Ende der Runde behandelt, als hätte es einen Pilotenwert von 8.'
    },
    'Vector': {
      ship: "Kreuzer der Gozanti-Klasse",
      name: "Vektor",
      text: '%DE_GOZANTIONLY%%LINEBREAK%Nachdem du ein Manöver ausgeführt hast, darfst du bis zu 4 angedockte Schiffe starten (anstatt 2).'
    },
    'Suppressor': {
      ship: "Kreuzer der Gozanti-Klasse",
      name: "Unterdrücker",
      text: '%DE_GOZANTIONLY%%LINEBREAK%Ein Mal pro Runde darfst du, nachdem du ein feindliches Schiff in die Zielerfassung genommen hast, 1 Fokus-, Ausweich- oder blaue Zielerfassungsmarker von dem Schiff entfernen.'
    },
    'Black One': {
      text: 'After you perform a boost or barrel roll action, you may remove 1 enemy target lock from a friendly ship at Range 1.  You cannot equip this card if your pilot skill is "6" or lower.'
    },
    'Millennium Falcon (TFA)': {
      text: 'After you execute a 3-speed bank maneuver (%BANKLEFT% or %BANKRIGHT%), if you are not touching another ship and you are not stressed, you may receive 1 stress token to rotate your ship 180&deg;.'
    }
  };
  return exportObj.setupCardData(basic_cards, pilot_translations, upgrade_translations, modification_translations, title_translations);
};

exportObj = typeof exports !== "undefined" && exports !== null ? exports : this;

if (exportObj.codeToLanguage == null) {
  exportObj.codeToLanguage = {};
}

exportObj.codeToLanguage.en = 'English';

if (exportObj.translations == null) {
  exportObj.translations = {};
}

exportObj.translations.English = {
  action: {
    "Barrel Roll": "Barrel Roll",
    "Boost": "Boost",
    "Evade": "Evade",
    "Focus": "Focus",
    "Target Lock": "Target Lock",
    "Recover": "Recover",
    "Reinforce": "Reinforce",
    "Jam": "Jam",
    "Coordinate": "Coordinate",
    "Cloak": "Cloak",
    "SLAM": "SLAM"
  },
  slot: {
    "Astromech": "Astromech",
    "Bomb": "Bomb",
    "Cannon": "Cannon",
    "Crew": "Crew",
    "Elite": "Elite",
    "Missile": "Missile",
    "System": "System",
    "Torpedo": "Torpedo",
    "Turret": "Turret",
    "Cargo": "Cargo",
    "Hardpoint": "Hardpoint",
    "Team": "Team",
    "Illicit": "Illicit",
    "Salvaged Astromech": "Salvaged Astromech"
  },
  sources: {
    "Core": "Core",
    "A-Wing Expansion Pack": "A-Wing Expansion Pack",
    "B-Wing Expansion Pack": "B-Wing Expansion Pack",
    "X-Wing Expansion Pack": "X-Wing Expansion Pack",
    "Y-Wing Expansion Pack": "Y-Wing Expansion Pack",
    "Millennium Falcon Expansion Pack": "Millennium Falcon Expansion Pack",
    "HWK-290 Expansion Pack": "HWK-290 Expansion Pack",
    "TIE Fighter Expansion Pack": "TIE Fighter Expansion Pack",
    "TIE Interceptor Expansion Pack": "TIE Interceptor Expansion Pack",
    "TIE Bomber Expansion Pack": "TIE Bomber Expansion Pack",
    "TIE Advanced Expansion Pack": "TIE Advanced Expansion Pack",
    "Lambda-Class Shuttle Expansion Pack": "Lambda-Class Shuttle Expansion Pack",
    "Slave I Expansion Pack": "Slave I Expansion Pack",
    "Imperial Aces Expansion Pack": "Imperial Aces Expansion Pack",
    "Rebel Transport Expansion Pack": "Rebel Transport Expansion Pack",
    "Z-95 Headhunter Expansion Pack": "Z-95 Headhunter Expansion Pack",
    "TIE Defender Expansion Pack": "TIE Defender Expansion Pack",
    "E-Wing Expansion Pack": "E-Wing Expansion Pack",
    "TIE Phantom Expansion Pack": "TIE Phantom Expansion Pack",
    "Tantive IV Expansion Pack": "Tantive IV Expansion Pack",
    "Rebel Aces Expansion Pack": "Rebel Aces Expansion Pack",
    "YT-2400 Freighter Expansion Pack": "YT-2400 Freighter Expansion Pack",
    "VT-49 Decimator Expansion Pack": "VT-49 Decimator Expansion Pack",
    "StarViper Expansion Pack": "StarViper Expansion Pack",
    "M3-A Interceptor Expansion Pack": "M3-A Interceptor Expansion Pack",
    "IG-2000 Expansion Pack": "IG-2000 Expansion Pack",
    "Most Wanted Expansion Pack": "Most Wanted Expansion Pack",
    "Imperial Raider Expansion Pack": "Imperial Raider Expansion Pack",
    "Hound's Tooth Expansion Pack": "Hound's Tooth Expansion Pack",
    "Kihraxz Fighter Expansion Pack": "Kihraxz Fighter Expansion Pack",
    "K-Wing Expansion Pack": "K-Wing Expansion Pack",
    "TIE Punisher Expansion Pack": "TIE Punisher Expansion Pack",
    "The Force Awakens Core Set": "The Force Awakens Core Set"
  },
  ui: {
    shipSelectorPlaceholder: "Select a ship",
    pilotSelectorPlaceholder: "Select a pilot",
    upgradePlaceholder: function(translator, language, slot) {
      return "No " + (translator(language, 'slot', slot)) + " Upgrade";
    },
    modificationPlaceholder: "No Modification",
    titlePlaceholder: "No Title",
    upgradeHeader: function(translator, language, slot) {
      return "" + (translator(language, 'slot', slot)) + " Upgrade";
    },
    unreleased: "unreleased",
    epic: "epic",
    limited: "limited"
  },
  byCSSSelector: {
    '.xwing-card-browser .translate.sort-cards-by': 'Sort cards by',
    '.xwing-card-browser option[value="name"]': 'Name',
    '.xwing-card-browser option[value="source"]': 'Source',
    '.xwing-card-browser option[value="type-by-points"]': 'Type (by Points)',
    '.xwing-card-browser option[value="type-by-name"]': 'Type (by Name)',
    '.xwing-card-browser .translate.select-a-card': 'Select a card from the list at the left.',
    '.info-well .info-ship td.info-header': 'Ship',
    '.info-well .info-skill td.info-header': 'Skill',
    '.info-well .info-actions td.info-header': 'Actions',
    '.info-well .info-upgrades td.info-header': 'Upgrades',
    '.info-well .info-range td.info-header': 'Range',
    '.clear-squad': 'New Squad',
    '.save-list': 'Save',
    '.save-list-as': 'Save as…',
    '.delete-list': 'Delete',
    '.backend-list-my-squads': 'Load squad',
    '.view-as-text': '<span class="hidden-phone"><i class="icon-print"></i>&nbsp;Print/View as </span>Text',
    '.randomize': 'Random!',
    '.randomize-options': 'Randomizer options…',
    '.notes-container > span': 'Squad Notes',
    '.bbcode-list': 'Copy the BBCode below and paste it into your forum post.<textarea></textarea><button class="btn btn-copy">Copy</button>',
    '.html-list': '<textarea></textarea><button class="btn btn-copy">Copy</button>',
    '.vertical-space-checkbox': "Add space for damage/upgrade cards when printing <input type=\"checkbox\" class=\"toggle-vertical-space\" />",
    '.color-print-checkbox': "Print color <input type=\"checkbox\" class=\"toggle-color-print\" />",
    '.print-list': '<i class="icon-print"></i>&nbsp;Print',
    '.do-randomize': 'Randomize!',
    '#empireTab': 'Galactic Empire',
    '#rebelTab': 'Rebel Alliance',
    '#scumTab': 'Scum and Villainy',
    '#browserTab': 'Card Browser',
    '#aboutTab': 'About'
  },
  singular: {
    'pilots': 'Pilot',
    'modifications': 'Modification',
    'titles': 'Title'
  },
  types: {
    'Pilot': 'Pilot',
    'Modification': 'Modification',
    'Title': 'Title'
  }
};

if (exportObj.cardLoaders == null) {
  exportObj.cardLoaders = {};
}

exportObj.cardLoaders.English = function() {
  var basic_cards, modification_translations, pilot_translations, title_translations, upgrade_translations;
  exportObj.cardLanguage = 'English';
  basic_cards = exportObj.basicCardData();
  exportObj.canonicalizeShipNames(basic_cards);
  exportObj.ships = basic_cards.ships;
  pilot_translations = {
    "Wedge Antilles": {
      text: "When attacking, reduce the defender's agility value by 1 (to a minimum of \"0\")."
    },
    "Garven Dreis": {
      text: "After spending a focus token, you may place that token on any other friendly ship at Range 1-2 (instead of discarding it)."
    },
    "Biggs Darklighter": {
      text: "Other friendly ships at Range 1 cannot be targeted by attacks if the attacker could target you instead."
    },
    "Luke Skywalker": {
      text: "When defending, you may change 1 of your %FOCUS% results to a %EVADE% result."
    },
    '"Dutch" Vander': {
      text: "After acquiring a target lock, choose another friendly ship at Range 1-2.  The chosen ship may immediately acquire a target lock."
    },
    "Horton Salm": {
      text: "When attacking at Range 2-3, you may reroll any of your blank results."
    },
    '"Winged Gundark"': {
      text: "When attacking at Range 1, you may change 1 of your %HIT% results to a %CRIT% result."
    },
    '"Night Beast"': {
      text: "After executing a green maneuver, you may perform a free focus action."
    },
    '"Backstabber"': {
      text: "When attacking from outside the defender's firing arc, roll 1 additional attack die."
    },
    '"Dark Curse"': {
      text: "When defending, ships attacking you cannot spend focus tokens or reroll attack dice."
    },
    '"Mauler Mithel"': {
      text: "When attacking at Range 1, roll 1 additional attack die."
    },
    '"Howlrunner"': {
      text: "When another friendly ship at Range 1 is attacking with its primary weapon, it may reroll 1 attack die."
    },
    "Maarek Stele": {
      text: "When your attack deals a faceup Damage card to the defender, instead draw 3 Damage cards, choose 1 to deal, and discard the others."
    },
    "Darth Vader": {
      text: "During your \"Perform Action\" step, you may perform 2 actions."
    },
    "\"Fel's Wrath\"": {
      text: "When the number of Damage cards assigned to you equals or exceeds your hull value, you are not destroyed until the end of the Combat phase."
    },
    "Turr Phennir": {
      text: "After you perform an attack, you may perform a free boost or barrel roll action."
    },
    "Soontir Fel": {
      text: "When you receive a stress token, you may assign 1 focus token to your ship."
    },
    "Tycho Celchu": {
      text: "You may perform actions even while you have stress tokens."
    },
    "Arvel Crynyd": {
      text: "You may declare an enemy ship inside your firing arc that you are touching as the target of your attack."
    },
    "Chewbacca": {
      text: "When you are dealt a faceup Damage card, immediately flip it facedown (without resolving its ability)."
    },
    "Lando Calrissian": {
      text: "After you execute a green maneuver, choose 1 other friendly ship at Range 1.  That ship may perform 1 free action shown on its action bar."
    },
    "Han Solo": {
      text: "When attacking, you may reroll all of your dice.  If you choose to do so, you must reroll as many of your dice as possible."
    },
    "Kath Scarlet": {
      text: "When attacking, the defender receives 1 stress token if he cancels at least 1 %CRIT% result."
    },
    "Boba Fett": {
      text: "When you reveal a bank maneuver (%BANKLEFT% or %BANKRIGHT%), you may rotate your dial to the other bank maneuver of the same speed."
    },
    "Krassis Trelix": {
      text: "When attacking with a secondary weapon, you may reroll 1 attack die."
    },
    "Ten Numb": {
      text: "When attacking, 1 of your %CRIT% results cannot be canceled by defense dice."
    },
    "Ibtisam": {
      text: "When attacking or defending, if you have at least 1 stress token, you may reroll 1 of your dice."
    },
    "Roark Garnet": {
      text: 'At the start of the Combat phase, choose 1 other friendly ship at Range 1-3.  Until the end of the phase, treat that ship\'s pilot skill value as "12."'
    },
    "Kyle Katarn": {
      text: "At the start of the Combat phase, you may assign 1 of your focus tokens to another friendly ship at Range 1-3."
    },
    "Jan Ors": {
      text: "When another friendly ship at Range 1-3 is attacking, if you have no stress tokens, you may receive 1 stress token to allow that ship to roll 1 additional attack die."
    },
    "Captain Jonus": {
      text: "When another friendly ship at Range 1 attacks with a secondary weapon, it may reroll up to 2 attack dice."
    },
    "Major Rhymer": {
      text: "When attacking with a secondary weapon, you may increase or decrease the weapon range by 1 to a limit of Range 1-3."
    },
    "Captain Kagi": {
      text: "When an enemy ship acquires a target lock, it must lock onto your ship if able."
    },
    "Colonel Jendon": {
      text: "At the start of the Combat phase, you may assign 1 of your blue target lock tokens to a friendly ship at Range 1 if it does not have a blue target lock token."
    },
    "Captain Yorr": {
      text: "When another friendly ship at Range 1-2 would receive a stress token, if you have 2 or fewer stress tokens, you may receive that token instead."
    },
    "Lieutenant Lorrir": {
      text: "When performing a barrel roll action, you may receive 1 stress token to use the (%BANKLEFT% 1) or (%BANKRIGHT% 1) template instead of the (%STRAIGHT% 1) template."
    },
    "Tetran Cowall": {
      text: "When you reveal a %UTURN% maneuver, you may treat the speed of that maneuver as \"1,\" \"3,\" or \"5\"."
    },
    "Kir Kanos": {
      text: "When attacking at Range 2-3, you may spend 1 evade token to add 1 %HIT% result to your roll."
    },
    "Carnor Jax": {
      text: "Enemy ships at Range 1 cannot perform focus or evade actions and cannot spend focus or evade tokens."
    },
    "Lieutenant Blount": {
      text: "When attacking, the defender is hit by your attack, even if he does not suffer any damage."
    },
    "Airen Cracken": {
      text: "After you perform an attack, you may choose another friendly ship at Range 1.  That ship may perform 1 free action."
    },
    "Colonel Vessery": {
      text: "When attacking, immediately after you roll attack dice, you may acquire a target lock on the defender if it already has a red target lock token."
    },
    "Rexler Brath": {
      text: "After you perform an attack that deals at least 1 Damage card to the defender, you may spend a focus token to flip those cards faceup."
    },
    "Etahn A'baht": {
      text: "When an enemy ship inside your firing arc at Range 1-3 is defending, the attacker may change 1 of its %HIT% results to a %CRIT% result."
    },
    "Corran Horn": {
      text: "At the start of the End phase, you may perform one attack.  You cannot attack during the next round."
    },
    '"Echo"': {
      text: "When you decloak, you must use the (%BANKLEFT% 2) or (%BANKRIGHT% 2) template instead of the (%STRAIGHT% 2) template."
    },
    '"Whisper"': {
      text: "After you perform an attack that hits, you may assign 1 focus to your ship."
    },
    "Wes Janson": {
      text: "After you perform an attack, you may remove 1 focus, evade, or blue target lock token from the defender."
    },
    "Jek Porkins": {
      text: "When you receive a stress token, you may remove it and roll 1 attack die.  On a %HIT% result, deal 1 facedown Damage card to this ship."
    },
    '"Hobbie" Klivian': {
      text: "When you acquire or spend a target lock, you may remove 1 stress token from your ship."
    },
    "Tarn Mison": {
      text: "When an enemy ship declares you as the target of an attack, you may acquire a target lock on that ship."
    },
    "Jake Farrell": {
      text: "After you perform a focus action or are assigned a focus token, you may perform a free boost or barrel roll action."
    },
    "Gemmer Sojan": {
      text: "While you are at Range 1 of at least 1 enemy ship, increase your agility value by 1."
    },
    "Keyan Farlander": {
      text: "When attacking, you may remove 1 stress token to change all of your %FOCUS% results to %HIT%results."
    },
    "Nera Dantels": {
      text: "You can perform %TORPEDO% secondary weapon attacks against enemy ships outside your firing arc."
    },
    "CR90 Corvette (Fore)": {
      text: "When attacking with your primary weapon, you may spend 1 energy to roll 1 additional attack die."
    },
    "Dash Rendar": {
      text: "You may ignore obstacles during the Activation phase and when performing actions."
    },
    '"Leebo"': {
      text: "When you are dealt a faceup Damage card, draw 1 additional Damage card, choose 1 to resolve, and discard the other."
    },
    "Eaden Vrill": {
      text: "When performing a primary weapon attack against a stressed ship, roll 1 additional attack die."
    },
    "Rear Admiral Chiraneau": {
      text: "When attacking at Range 1-2, you may change 1 of your %FOCUS% results to a %CRIT% result."
    },
    "Commander Kenkirk": {
      text: "If you have no shields and at least 1 Damage card assigned to you, increase your agility value by 1."
    },
    "Captain Oicunn": {
      text: "After executing a maneuver, each enemy ship you are touching suffers 1 damage."
    },
    "Prince Xizor": {
      text: "When defending, a friendly ship at Range 1 may suffer 1 uncanceled %HIT% or %CRIT% result instead of you."
    },
    "Guri": {
      text: "At the start of the Combat phase, if you are at Range 1 of an enemy ship, you may assign 1 focus token to your ship."
    },
    "Serissu": {
      text: "When another friendly ship at Range 1 is defending, it may reroll 1 defense die."
    },
    "Laetin A'shera": {
      text: "After you defend against an attack, if the attack did not hit, you may assign 1 evade token to your ship."
    },
    "IG-88A": {
      text: "After you perform an attack that destroys the defender, you may recover 1 shield."
    },
    "IG-88B": {
      text: "Once per round, after you perform an attack that does not hit, you may perform an attack with an equipped %CANNON% secondary weapon."
    },
    "IG-88C": {
      text: "After you perform a boost action, you may perform a free evade action."
    },
    "IG-88D": {
      text: "You may execute the (%SLOOPLEFT% 3) or (%SLOOPRIGHT% 3) maneuver using the corresponding (%TURNLEFT% 3) or (%TURNRIGHT% 3) template."
    },
    "Boba Fett (Scum)": {
      text: "When attacking or defending, you may reroll 1 of your dice for each enemy ship at Range 1."
    },
    "Kath Scarlet (Scum)": {
      text: "When attacking a ship inside your auxiliary firing arc, roll 1 additional attack die."
    },
    "Emon Azzameen": {
      text: "When dropping a bomb, you may use the [%TURNLEFT% 3], [%STRAIGHT% 3], or [%TURNRIGHT% 3] template instead of the [%STRAIGHT% 1] template."
    },
    "Kavil": {
      text: "When attacking a ship outside your firing arc, roll 1 additional attack die."
    },
    "Drea Renthal": {
      text: "After you spend a target lock, you may receive 1 stress token to acquire a target lock."
    },
    "Dace Bonearm": {
      text: "When an enemy ship at Range 1-3 receives at least 1 ion token, if you are not stressed, you may receive 1 stress token to cause that ship to suffer 1 damage."
    },
    "Palob Godalhi": {
      text: "At the start of the Combat phase, you may remove 1 focus or evade token from an enemy ship at Range 1-2 and assign it to yourself."
    },
    "Torkil Mux": {
      text: "At the end of the Activation phase, choose 1 enemy ship at Range 1-2. Until the end of the Combat phase, treat that ship's pilot skill value as \"0\"."
    },
    "N'Dru Suhlak": {
      text: "When attacking, if there are no other friendly ships at Range 1-2, roll 1 additional attack die."
    },
    "Kaa'To Leeachos": {
      text: "At the start of the Combat phase, you may remove 1 focus or evade token from another friendly ship at Range 1-2 and assign it to yourself."
    },
    "Commander Alozen": {
      text: "At the start of the Combat phase, you may acquire a target lock on an enemy ship at Range 1."
    },
    "Raider-class Corvette (Fore)": {
      text: "Once per round, after you perform a primary weapon attack, you may spend 2 energy to perform another primary weapon attack."
    },
    "Bossk": {
      text: "When you perform an attack that hits, before dealing damage, you may cancel 1 of your %CRIT% results to add 2 %HIT% results."
    },
    "Talonbane Cobra": {
      text: "When attacking or defending, double the effect of your range combat bonuses."
    },
    "Miranda Doni": {
      text: "Once per round when attacking, you may either spend 1 shield to roll 1 additional attack die <strong>or</strong> roll 1 fewer attack die to recover 1 shield."
    },
    '"Redline"': {
      text: "You may maintain 2 target locks on the same ship.  When you acquire a target lock, you may acquire a second lock on that ship."
    },
    '"Deathrain"': {
      text: "When dropping a bomb, you may use the front guides of your ship.  After dropping a bomb, you may perform a free barrel roll action."
    },
    "Juno Eclipse": {
      text: "When you reveal your maneuver, you may increase or decrease its speed by 1 (to a minimum of 1)."
    },
    "Zertik Strom": {
      text: "Enemy ships at Range 1 cannot add their range combat bonus when attacking."
    },
    "Lieutenant Colzet": {
      text: "At the start of the End phase, you may spend a target lock you have on an enemy ship to flip 1 random facedown Damage card assigned to it faceup."
    },
    "Latts Razzi": {
      text: "When a friendly ship declares an attack, you may spend a target lock you have on the defender to reduce its agility by 1 for that attack."
    },
    "Graz the Hunter": {
      text: "When defending, if the attacker is inside your firing arc, roll 1 additional defense die."
    },
    "Esege Tuketu": {
      text: "When another friendly ship at Range 1-2 is attacking, it may treat your focus tokens as its own."
    },
    "Moralo Eval": {
      text: "You can perform %CANNON% secondary attacks against ships inside your auxiliary firing arc."
    },
    'Gozanti-class Cruiser': {
      text: "After you execute a maneuver, you may deploy up to 2 attached ships."
    },
    '"Scourge"': {
      text: "When attacking a defender that has 1 or more Damage cards, roll 1 additional attack die."
    },
    "The Inquisitor": {
      text: "When attacking with your primary weapon at Range 2-3, treat the range of the attack as Range 1."
    },
    "Zuckuss": {
      text: "When attacking, you may roll 1 additional attack die.  If you do, the defender rolls 1 additional defense die."
    },
    "Dengar": {
      text: "Once per round after defending, if the attacker is inside your firing arc, you may perform an attack against that ship."
    },
    "Poe Dameron": {
      text: "When attacking or defending, if you have a focus token, you may change 1 of your %FOCUS% results to a %HIT% or %EVADE% result."
    },
    '"Blue Ace"': {
      text: "When performing a boost action, you may use the (%TURNLEFT% 1) or (%TURNRIGHT% 1) template."
    },
    '"Omega Ace"': {
      text: "When attacking, you may spend a focus token and a target lock you have on the defender to change all of your results to %CRIT% results."
    },
    '"Epsilon Leader"': {
      text: "At the start of the Combat phase, remove 1 stress token from each friendly ship at Range 1."
    },
    '"Zeta Ace"': {
      text: "When performing a barrel roll you may use the (%STRAIGHT% 2) template instead of the (%STRAIGHT% 1) template."
    },
    '"Red Ace"': {
      text: 'The first time you remove a shield token from your ship each round, assign 1 evade token to your ship.'
    },
    '"Omega Leader"': {
      text: 'Enemy ships that you have locked cannot modify any dice when attacking you or defending against your attacks.'
    },
    'Hera Syndulla': {
      text: 'When you reveal a green or red maneuver, you may rotate your dial to another maneuver of the same difficulty.'
    },
    '"Youngster"': {
      text: "Friendly TIE fighters at Range 1-3 may perform the action on your equipped %ELITE% Upgrade card."
    },
    '"Wampa"': {
      text: "When attacking, you may cancel all die results.  If you cancel a %CRIT% result, deal 1 facedown Damage card to the defender."
    },
    '"Chaser"': {
      text: "When another friendly ship at Range 1 spends a focus token, assign a focus token to your ship."
    },
    'Ezra Bridger': {
      text: "When defending, if you are stressed, you may change up to 2 of your %FOCUS% results to %EVADE% results."
    },
    '"Zeta Leader"': {
      text: 'When attacking, if you are not stressed, you may receive 1 stress token to roll 1 additional die.'
    },
    '"Epsilon Ace"': {
      text: 'While you do not have any Damage cards, treat your pilot skill value as "12."'
    },
    "Kanan Jarrus": {
      text: "When an enemy ship at Range 1-2 is attacking, you may spend a focus token.  If you do, the attacker rolls 1 fewer attack die."
    },
    '"Chopper"': {
      text: "At the start of the Combat phase, each enemy ship you are touching receives 1 stress token."
    },
    'Hera Syndulla (Attack Shuttle)': {
      text: "When you reveal a green or red maneuver, you may rotate your dial to another maneuver of the same difficulty."
    },
    'Sabine Wren': {
      text: "Immediately before you reveal your maneuver, you may perform a free boost or barrel roll action."
    },
    '"Zeb" Orrelios': {
      text: 'When defending, you may cancel %CRIT% results before %HIT% results.'
    },
    'Tomax Bren': {
      text: 'Once per round, after you discard an %ELITE% Upgrade card, flip that card faceup.'
    },
    'Ello Asty': {
      text: 'While you are not stressed, you may treat your %TROLLLEFT% and %TROLLRIGHT% maneuvers as white maneuvers.'
    },
    "Valen Rudor": {
      text: "After defending, you may perform a free action."
    },
    "4-LOM": {
      text: "At the start of the End phase, you may assign 1 of your stress tokens to another ship at Range 1."
    },
    "Tel Trevura": {
      text: "The first time you would be destroyed, instead cancel any remaining damage, discard all Damage cards, and deal 4 facedown Damage cards to this ship."
    },
    "Manaroo": {
      text: "At the start of the Combat phase, you may assign all focus, evade, and target lock tokens assigned to you to another friendly ship."
    },
    '"Deathfire"': {
      text: 'When you reveal your maneuver dial or after you perform an action, you may perform a %BOMB% Upgrade card action as a free action.'
    },
    "Maarek Stele (TIE Defender)": {
      text: "When your attack deals a faceup Damage card to the defender, instead draw 3 Damage cards, choose 1 to deal, and discard the others."
    },
    "Countess Ryad": {
      text: "When you reveal a %STRAIGHT% maneuver, you may treat it as a %KTURN% maneuver."
    },
    "Poe Dameron (PS9)": {
      text: "When attacking or defending, if you have a focus token, you may change 1 of your %FOCUS% results to a %HIT% or %EVADE% result."
    },
    "Rey": {
      text: "When attacking or defending, if the enemy ship is inside of your firing arc, you may reroll up to 2 of your blank results."
    },
    'Norra Wexley': {
      text: 'When attacking or defending, you may spend a target lock you have on the enemy ship to add 1 %FOCUS% result to your roll.'
    },
    'Shara Bey': {
      text: 'When another friendly ship at Range 1-2 is attacking, it may treat your blue target lock tokens as its own.'
    },
    '"Quickdraw"': {
      text: 'Once per round, when you lose a shield token, you may perform a primary weapon attack.'
    },
    'Fenn Rau': {
      text: 'When attacking or defending, if the enemy ship is at Range 1, you may roll 1 additional die.'
    },
    'Kad Solus': {
      text: 'After you execute a red maneuver, assign 2 focus tokens to your ship.'
    },
    'Ketsu Onyo': {
      text: 'At the start of the Combat phase, you may choose a ship at Range 1.  If it is inside your primary <strong>and</strong> mobile firing arcs, assign 1 tractor beam token to it.'
    },
    'Sabine Wren': {
      text: 'When defending against an enemy ship inside your mobile firing arc at Range 1-2, you may add 1 %FOCUS% result to your roll.'
    }
  };
  upgrade_translations = {
    "Ion Cannon Turret": {
      text: "<strong>Attack:</strong> Attack 1 ship (even a ship outside your firing arc).%LINEBREAK%If this attack hits the target ship, the ship suffers 1 damage and receives 1 ion token.  Then cancel all dice results."
    },
    "Proton Torpedoes": {
      text: "<strong>Attack (target lock):</strong> Spend your target lock and discard this card to perform this attack.%LINEBREAK%You may change 1 of your %FOCUS% results to a %CRIT% result."
    },
    "R2 Astromech": {
      text: "You may treat all 1- and 2-speed maneuvers as green maneuvers."
    },
    "R2-D2": {
      text: "After executing a green maneuver, you may recover 1 shield (up to your shield value)."
    },
    "R2-F2": {
      text: "<strong>Action:</strong> Increase your agility value by 1 until the end of this game round."
    },
    "R5-D8": {
      text: "<strong>Action:</strong> Roll 1 defense die.%LINEBREAK%On a %EVADE% or %FOCUS% result, discard 1 of your facedown Damage cards."
    },
    "R5-K6": {
      text: "After spending your target lock, roll 1 defense die.%LINEBREAK%On a %EVADE% result, immediately acquire a target lock on that same ship.  You cannot spend this target lock during this attack."
    },
    "R5 Astromech": {
      text: "During the End phase, you may choose 1 of your faceup Damage cards with the Ship trait and flip it facedown."
    },
    "Determination": {
      text: "When you are dealt a faceup Damage card with the Pilot trait, discard it immediately without resolving its effect."
    },
    "Swarm Tactics": {
      text: "At the start of the Combat phase, you may choose 1 friendly ship at Range 1.%LINEBREAK%Until the end of this phase, treat the chosen ship as if its pilot skill were equal to your pilot skill."
    },
    "Squad Leader": {
      text: "<strong>Action:</strong> Choose 1 ship at Range 1-2 that has a lower pilot skill than you.%LINEBREAK%The chosen ship may immediately perform 1 free action."
    },
    "Expert Handling": {
      text: "<strong>Action:</strong> Perform a free barrel roll action.  If you do not have the %BARRELROLL% action icon, receive 1 stress token.%LINEBREAK%You may then remove 1 enemy target lock from your ship."
    },
    "Marksmanship": {
      text: "<strong>Action:</strong> When attacking this round, you may change 1 of your %FOCUS% results to a %CRIT% result and all of your other %FOCUS% results to %HIT% results."
    },
    "Concussion Missiles": {
      text: "<strong>Attack (target lock):</strong>  Spend your target lock and discard this card to perform this attack.%LINEBREAK%You may change 1 of your blank results to a %HIT% result."
    },
    "Cluster Missiles": {
      text: "<strong>Attack (target lock):</strong> Spend your target lock and discard this card to perform this attack twice."
    },
    "Daredevil": {
      text: "<strong>Action:</strong> Execute a white (%TURNLEFT% 1) or (%TURNRIGHT% 1) maneuver.  Then, receive 1 stress token.%LINEBREAK%Then, if you do not have the %BOOST% action icon, roll 2 attack dice.  Suffer any damage (%HIT%) and any critical damage (%CRIT%) rolled."
    },
    "Elusiveness": {
      text: "When defending, you may receive 1 stress token to choose 1 attack die.  The attacker must reroll that die.%LINEBREAK%If you have at least 1 stress token, you cannot use this ability."
    },
    "Homing Missiles": {
      text: "<strong>Attack (target lock):</strong> Discard this card to perform this attack.%LINEBREAK%The defender cannot spend evade tokens during this attack."
    },
    "Push the Limit": {
      text: "Once per round, after you perform an action, you may perform 1 free action shown in your action bar.%LINEBREAK%Then receive 1 stress token."
    },
    "Deadeye": {
      text: "You may treat the <strong>Attack (target lock):</strong> header as <strong>Attack (focus):</strong>.%LINEBREAK%When an attack instructs you to spend a target lock, you may spend a focus token instead."
    },
    "Expose": {
      text: "<strong>Action:</strong> Until the end of the round, increase your primary weapon value by 1 and decrease your agility value by 1."
    },
    "Gunner": {
      text: "After you perform an attack that does not hit, you may immediately perform a primary weapon attack.  You cannot perform another attack this round."
    },
    "Ion Cannon": {
      text: "<strong>Attack:</strong> Attack 1 ship.%LINEBREAK%If this attack hits, the defender suffers 1 damage and receives 1 ion token.  Then cancel all dice results."
    },
    "Heavy Laser Cannon": {
      text: "<strong>Attack:</strong> Attack 1 ship.%LINEBREAK%Immediately after rolling your attack dice, you must change all of your %CRIT% results to %HIT% results."
    },
    "Seismic Charges": {
      text: "When you reveal your maneuver dial, you may discard this card to drop 1 seismic charge token.%LINEBREAK%This token detonates at the end of the Activation phase.%LINEBREAK%<strong>Seismic Charge Token:</strong> When this bomb token detonates, each ship at Range 1 of the token suffers 1 damage.  Then discard this token."
    },
    "Mercenary Copilot": {
      text: "When attacking at Range 3, you may change 1 of your %HIT% results to a %CRIT% result."
    },
    "Assault Missiles": {
      text: "<strong>Attack (target lock):</strong> Spend your target lock and discard this card to perform this attack.%LINEBREAK%If this attack hits, each other ship at Range 1 of the defender suffers 1 damage."
    },
    "Veteran Instincts": {
      text: "Increase your pilot skill value by 2."
    },
    "Proximity Mines": {
      text: "<strong>Action:</strong> Discard this card to <strong>drop</strong> 1 proximity mine token.%LINEBREAK%When a ship's base or maneuver template overlaps this token, this token <strong>detonates</strong>.%LINEBREAK%<strong>Proximity Mine Token:</strong> When this bomb token detonates, the ship that moved through or overlapped this token rolls 3 attack dice and suffers all damage (%HIT%) and critical damage (%CRIT%) rolled.  Then discard this token."
    },
    "Weapons Engineer": {
      text: "You may maintain 2 target locks (only 1 per enemy ship).%LINEBREAK%When you acquire a target lock, you may lock onto 2 different ships."
    },
    "Draw Their Fire": {
      text: "When a friendly ship at Range 1 is hit by an attack, you may suffer 1 of the uncanceled %CRIT% results instead of the target ship."
    },
    "Luke Skywalker": {
      text: "%REBELONLY%%LINEBREAK%After you perform an attack that does not hit, you may immediately perform a primary weapon attack.  You may change 1 %FOCUS% result to a %HIT% result.  You cannot perform another attack this round."
    },
    "Nien Nunb": {
      text: "%REBELONLY%%LINEBREAK%You may treat all %STRAIGHT% maneuvers as green maneuvers."
    },
    "Chewbacca": {
      text: "%REBELONLY%%LINEBREAK%When you are dealt a Damage card, you may immediately discard that card and recover 1 shield.%LINEBREAK%Then, discard this Upgrade card."
    },
    "Advanced Proton Torpedoes": {
      text: "<strong>Attack (target lock):</strong> Spend your target lock and discard this card to perform this attack.%LINEBREAK%You may change up to 3 of your blank results to %FOCUS% results."
    },
    "Autoblaster": {
      text: "<strong>Attack:</strong> Attack 1 ship.%LINEBREAK%Your %HIT% results cannot be canceled by defense dice.%LINEBREAK%The defender may cancel %CRIT% results before %HIT% results."
    },
    "Fire-Control System": {
      text: "After you perform an attack, you may acquire a target lock on the defender."
    },
    "Blaster Turret": {
      text: "<strong>Attack (focus):</strong> Spend 1 focus token to perform this attack against 1 ship (even a ship outside your firing arc)."
    },
    "Recon Specialist": {
      text: "When you perform a focus action, assign 1 additional focus token to your ship."
    },
    "Saboteur": {
      text: "<strong>Action:</strong> Choose 1 enemy ship at Range 1 and roll 1 attack die.  On a %HIT% or %CRIT% result, choose 1 random facedown Damage card assigned to that ship, flip it faceup, and resolve it."
    },
    "Intelligence Agent": {
      text: "At the start of the Activation phase, choose 1 enemy ship at Range 1-2.  You may look at that ship's chosen maneuver."
    },
    "Proton Bombs": {
      text: "When you reveal your maneuver dial, you may discard this card to <strong>drop</strong> 1 proton bomb token.%LINEBREAK%This token <strong>detonates</strong> at the end of the Activation phase.%LINEBREAK%<strong>Proton Bomb Token:</strong> When this bomb token detonates, deal 1 <strong>faceup</strong> Damage card to each ship at Range 1 of the token.  Then discard this token."
    },
    "Adrenaline Rush": {
      text: "When you reveal a red maneuver, you may discard this card to treat that maneuver as a white maneuver until the end of the Activation phase."
    },
    "Advanced Sensors": {
      text: "Immediately before you reveal your maneuver, you may perform 1 free action.%LINEBREAK%If you use this ability, you must skip your \"Perform Action\" step during this round."
    },
    "Sensor Jammer": {
      text: "When defending, you may change 1 of the attacker's %HIT% results into a %FOCUS% result.%LINEBREAK%The attacker cannot reroll the die with the changed result."
    },
    "Darth Vader": {
      text: "%IMPERIALONLY%%LINEBREAK%After you perform an attack against an enemy ship, you may suffer 2 damage to cause that ship to suffer 1 critical damage."
    },
    "Rebel Captive": {
      text: "%IMPERIALONLY%%LINEBREAK%Once per round, the first ship that declares you as the target of an attack immediately receives 1 stress token."
    },
    "Flight Instructor": {
      text: "When defending, you may reroll 1 of your %FOCUS% results.  If the attacker's pilot skill value is \"2\" or lower, you may reroll 1 of your blank results instead."
    },
    "Navigator": {
      text: "When you reveal a maneuver, you may rotate your dial to another maneuver with the same bearing.%LINEBREAK%You cannot rotate to a red maneuver if you have any stress tokens."
    },
    "Opportunist": {
      text: "When attacking, if the defender does not have any focus or evade tokens, you may receive 1 stress token to roll 1 additional attack die.%LINEBREAK%You cannot use this ability if you have any stress tokens."
    },
    "Comms Booster": {
      text: "<strong>Energy:</strong> Spend 1 energy to remove all stress tokens from a friendly ship at Range 1-3.  Then assign 1 focus token to that ship."
    },
    "Slicer Tools": {
      text: "<strong>Action:</strong> Choose 1 or more ships at Range 1-3 that have a stress token.  For each ship chosen, you may spend 1 energy to cause that ship to suffer 1 damage."
    },
    "Shield Projector": {
      text: "When an enemy ship is declaring either a small or large ship as the target of its attack, you may spend 3 energy to force that ship to target you if possible."
    },
    "Ion Pulse Missiles": {
      text: "<strong>Attack (target lock):</strong> Discard this card to perform this attack.%LINEBREAK%If this attack hits, the defender suffers 1 damage and receives 2 ion tokens.  Then cancel <strong>all</strong> dice results."
    },
    "Wingman": {
      text: "At the start of the Combat phase, remove 1 stress token from another friendly ship at Range 1."
    },
    "Decoy": {
      text: "At the start of the Combat phase, you may choose 1 friendly ship at Range 1-2.  Exchange your pilot skill with that ship's pilot skill until the end of the phase."
    },
    "Outmaneuver": {
      text: "When attacking a ship inside your firing arc, if you are not inside that ship's firing arc, reduce its agility value by 1 (to a minimum of 0)."
    },
    "Predator": {
      text: "When attacking, you may reroll 1 attack die.  If the defender's pilot skill value is \"2\" or lower, you may instead reroll up to 2 attack dice."
    },
    "Flechette Torpedoes": {
      text: "<strong>Attack (target lock):</strong> Discard this card and spend your target lock to perform this attack.%LINEBREAK%After you perform this attack, the defender receives 1 stress token if its hull value is \"4\" or lower."
    },
    "R7 Astromech": {
      text: "Once per round when defending, if you have a target lock on the attacker, you may spend the target lock to choose any or all attack dice.  The attacker must reroll the chosen dice."
    },
    "R7-T1": {
      text: "<strong>Action:</strong> Choose an enemy ship at Range 1-2.  If you are inside that ship's firing arc, you may acquire a target lock on that ship.  Then, you may perform a free boost action."
    },
    "Tactician": {
      text: "After you perform an attack against a ship inside your firing arc at Range 2, that ship receives 1 stress token."
    },
    "R2-D2 (Crew)": {
      text: "%REBELONLY%%LINEBREAK%At the end of the End phase, if you have no shields, you may recover 1 shield and roll 1 attack die.  On a %HIT% result, randomly flip 1 of your facedown Damage cards faceup and resolve it."
    },
    "C-3PO": {
      text: "%REBELONLY%%LINEBREAK%Once per round, before you roll 1 or more defense dice, you may guess aloud a number of %EVADE% results.  If you roll that many %EVADE% results (before modifying dice), add 1 %EVADE% result."
    },
    "Single Turbolasers": {
      text: "<strong>Attack (Energy):</strong> Spend 2 energy from this card to perform this attack.  The defender doubles his agility value against this attack.  You may change 1 of your %FOCUS% results to a %HIT% result."
    },
    "Quad Laser Cannons": {
      text: "<strong>Attack (Energy):</strong> Spend 1 energy from this card to perform this attack.  If this attack does not hit, you may immediately spend 1 energy from this card to perform this attack again."
    },
    "Tibanna Gas Supplies": {
      text: "<strong>Energy:</strong> You may discard this card to gain 3 energy."
    },
    "Ionization Reactor": {
      text: "<strong>Energy:</strong> Spend 5 energy from this card and discard this card to cause each other ship at Range 1 to suffer 1 damage and receive 1 ion token."
    },
    "Engine Booster": {
      text: "Immediately before you reveal your maneuver dial, you may spend 1 energy to execute a white (%STRAIGHT% 1) maneuver.  You cannot use this ability if you would overlap another ship."
    },
    "R3-A2": {
      text: "When you declare the target of your attack, if the defender is inside your firing arc, you may receive 1 stress token to cause the defender to receive 1 stress token."
    },
    "R2-D6": {
      text: "Your upgrade bar gains the %ELITE% upgrade icon.%LINEBREAK%You cannot equip this upgrade if you already have a %ELITE% upgrade icon or if your pilot skill value is \"2\" or lower."
    },
    "Enhanced Scopes": {
      text: "During the Activation phase, treat your pilot skill value as \"0\"."
    },
    "Chardaan Refit": {
      text: "<span class=\"card-restriction\">A-Wing only.</span>%LINEBREAK%This card has a negative squad point cost."
    },
    "Proton Rockets": {
      text: "<strong>Attack (Focus):</strong> Discard this card to perform this attack.%LINEBREAK%You may roll additional attack dice equal to your agility value, to a maximum of 3 additional dice."
    },
    "Kyle Katarn": {
      text: "%REBELONLY%%LINEBREAK%After you remove a stress token from your ship, you may assign a focus token to your ship."
    },
    "Jan Ors": {
      text: "%REBELONLY%%LINEBREAK%Once per round, when a friendly ship at Range 1-3 performs a focus action or would be assigned a focus token, you may assign it an evade token instead."
    },
    "Toryn Farr": {
      text: "%HUGESHIPONLY% %REBELONLY%%LINEBREAK%<strong>Action:</strong> Spend any amount of energy to choose that many enemy ships at Range 1-2.  Remove all focus, evade, and blue target lock tokens from those ships."
    },
    "R4-D6": {
      text: "When you are hit by an attack and there are at least 3 uncanceled %HIT% results, you may choose to cancel those results until there are 2 remaining.  For each result canceled this way, receive 1 stress token."
    },
    "R5-P9": {
      text: "At the end of the Combat phase, you may spend 1 of your focus tokens to recover 1 shield (up to your shield value)."
    },
    "WED-15 Repair Droid": {
      text: "%HUGESHIPONLY%%LINEBREAK%<strong>Action:</strong> Spend 1 energy to discard 1 of your facedown Damage cards, or spend 3 energy to discard 1 of your faceup Damage cards."
    },
    "Carlist Rieekan": {
      text: "%HUGESHIPONLY% %REBELONLY%%LINEBREAK%At the start of the Activation phase, you may discard this card to treat each friendly ship's pilot skill value as \"12\" until the end of the phase."
    },
    "Jan Dodonna": {
      text: "%HUGESHIPONLY% %REBELONLY%%LINEBREAK%When another friendly ship at Range 1 is attacking, it may change 1 of its %HIT% results to a %CRIT%."
    },
    "Expanded Cargo Hold": {
      text: "<span class=\"card-restriction\">GR-75 only.</span>%LINEBREAK%Once per round, when you would be dealt a faceup Damage card, you may draw that card from either the fore or aft Damage deck."
    },
    "Backup Shield Generator": {
      text: "At the end of each round, you may spend 1 energy to recover 1 shield (up to your shield value)."
    },
    "EM Emitter": {
      text: "When you obstruct an attack, the defender rolls 3 additional defense dice (instead of 1)."
    },
    "Frequency Jammer": {
      text: "When you perform a jam action, choose 1 enemy ship that does not have a stress token and is at Range 1 of the jammed ship.  The chosen ship receives 1 stress token."
    },
    "Han Solo": {
      text: "%REBELONLY%%LINEBREAK%When attacking, if you have a target lock on the defender, you may spend that target lock to change all of your %FOCUS% results to %HIT% results."
    },
    "Leia Organa": {
      text: "%REBELONLY%%LINEBREAK%At the start of the Activation phase, you may discard this card to allow all friendly ships that reveal a red maneuver to treat that maneuver as a white maneuver until the end of the phase."
    },
    "Targeting Coordinator": {
      text: "<strong>Energy:</strong> You may spend 1 energy to choose 1 friendly ship at Range 1-2.  Acquire a target lock, then assign the blue target lock token to the chosen ship."
    },
    "Raymus Antilles": {
      text: "%HUGESHIPONLY% %REBELONLY%%LINEBREAK%At the start of the Activation phase, choose 1 enemy ship at Range 1-3.  You may look at that ship's chosen maneuver.  If the maneuver is white, assign that ship 1 stress token."
    },
    "Gunnery Team": {
      text: "Once per round, when attacking with a secondary weapon, you may spend 1 energy to change 1 of your blank results to a %HIT% result."
    },
    "Sensor Team": {
      text: "When acquiring a target lock, you may lock onto an enemy ship at Range 1-5 instead of 1-3."
    },
    "Engineering Team": {
      text: "During the Activation phase, when you reveal a %STRAIGHT% maneuver, gain 1 additional energy during the \"Gain Energy\" step."
    },
    "Lando Calrissian": {
      text: "%REBELONLY%%LINEBREAK%<strong>Action:</strong> Roll 2 defense dice.  For each %FOCUS% result, assign 1 focus token to your ship.  For each %EVADE% result, assign 1 evade token to your ship."
    },
    "Mara Jade": {
      text: "%IMPERIALONLY%%LINEBREAK%At the end of the Combat phase, each enemy ship at Range 1 that does not have a stress token receives 1 stress token."
    },
    "Fleet Officer": {
      text: "%IMPERIALONLY%%LINEBREAK%<strong>Action:</strong> Choose up to 2 friendly ships at Range 1-2 and assign 1 focus token to each of those ships.  Then receive 1 stress token."
    },
    "Lone Wolf": {
      text: "When attacking or defending, if there are no other friendly ships at Range 1-2, you may reroll 1 of your blank results."
    },
    "Stay On Target": {
      text: "When you reveal a maneuver, you may rotate your dial to another maneuver with the same speed.%LINEBREAK%Treat that maneuver as a red maneuver."
    },
    "Dash Rendar": {
      text: "%REBELONLY%%LINEBREAK%You may perform attacks while overlapping an obstacle.%LINEBREAK%Your attacks cannot be obstructed."
    },
    '"Leebo"': {
      text: "%REBELONLY%%LINEBREAK%<strong>Action:</strong> Perform a free boost action.  Then receive 1 ion token."
    },
    "Ruthlessness": {
      text: "%IMPERIALONLY%%LINEBREAK%After you perform an attack that hits, you <strong>must</strong> choose 1 other ship at Range 1 of the defender (other than yourself).  That ship suffers 1 damage."
    },
    "Intimidation": {
      text: "While you are touching an enemy ship, reduce that ship's agility value by 1."
    },
    "Ysanne Isard": {
      text: "%IMPERIALONLY%%LINEBREAK%At the start of the Combat phase, if you have no shields and at least 1 Damage card assigned to your ship, you may perform a free evade action."
    },
    "Moff Jerjerrod": {
      text: "%IMPERIALONLY%%LINEBREAK%When you are dealt a faceup Damage card, you may discard this Upgrade card or another %CREW% Upgrade card to flip that Damage card facedown (without resolving its effect)."
    },
    "Ion Torpedoes": {
      text: "<strong>Attack (target lock):</strong> Spend your target lock and discard this card to perform this attack.%LINEBREAK%If this attack hits, the defender and each ship at Range 1 of it receives 1 ion token."
    },
    "Bodyguard": {
      text: "%SCUMONLY%%LINEBREAK%At the start of the Combat phase, you may spend a focus token to choose a friendly ship at Range 1 with higher pilot skill than you. Increase its agility value by 1 until the end of the round."
    },
    "Calculation": {
      text: "When attacking, you may spend a focus token to change 1 of your %FOCUS% results to a %CRIT% result."
    },
    "Accuracy Corrector": {
      text: "When attacking, during the \"Modify Attack Dice\" step, you may cancel all of your dice results. Then, you may add 2 %HIT% results to your roll.%LINEBREAK%Your dice cannot be modified again during this attack."
    },
    "Inertial Dampeners": {
      text: "When you reveal your maneuver, you may discard this card to instead perform a white [0%STOP%] maneuver. Then receive 1 stress token."
    },
    "Flechette Cannon": {
      text: "<strong>Attack:</strong> Attack 1 ship.%LINEBREAK%If this attack hits, the defender suffers 1 damage and, if the defender is not stressed, it also receives 1 stress token.  Then cancel <strong>all</strong> dice results."
    },
    '"Mangler" Cannon': {
      text: "<strong>Attack:</strong> Attack 1 ship.%LINEBREAK%When attacking, you may change 1 of your %HIT% results to a %CRIT% result."
    },
    "Dead Man's Switch": {
      text: "When you are destroyed, each ship at Range 1 suffers 1 damage."
    },
    "Feedback Array": {
      text: "During the Combat phase, instead of performing any attacks, you may receive 1 ion token and suffer 1 damage to choose 1 enemy ship at Range 1.  That ship suffers 1 damage."
    },
    '"Hot Shot" Blaster': {
      text: "<strong>Attack:</strong> Discard this card to attack 1 ship (even a ship outside your firing arc)."
    },
    "Greedo": {
      text: "%SCUMONLY%%LINEBREAK%The first time you attack each round and the first time you defend each round, the first Damage card dealt is dealt faceup."
    },
    "Salvaged Astromech": {
      text: "When you are dealt a faceup Damage card with the <strong>Ship</strong> trait, you may immediately discard that card (before resolving its effect).%LINEBREAK%Then, discard this Upgrade card."
    },
    "Bomb Loadout": {
      text: "<span class=\"card-restriction\">Y-Wing only.</span>%LINEBREAK%Your upgrade bar gains the %BOMB% icon."
    },
    '"Genius"': {
      text: "If you are equipped with a bomb that can be dropped when you reveal your maneuver, you may drop the bomb <strong>after</strong> you execute your maneuver instead."
    },
    "Unhinged Astromech": {
      text: "You may treat all 3-speed maneuvers as green maneuvers."
    },
    "R4-B11": {
      text: "When attacking, if you have a target lock on the defender, you may spend the target lock to choose any or all defense dice. The defender must reroll the chosen dice."
    },
    "Autoblaster Turret": {
      text: "<strong>Attack:</strong> Attack 1 ship (even a ship outside your firing arc).%LINEBREAK%Your %HIT% results cannot be canceled by defense dice. The defender may cancel %CRIT% results before %HIT% results."
    },
    "R4 Agromech": {
      text: "When attacking, after you spend a focus token, you may acquire a target lock on the defender."
    },
    "K4 Security Droid": {
      text: "%SCUMONLY%%LINEBREAK%After executing a green maneuver, you may acquire a target lock."
    },
    "Outlaw Tech": {
      text: "%SCUMONLY%%LINEBREAK%After you execute a red maneuver, you may assign 1 focus token to your ship."
    },
    "Advanced Targeting Computer": {
      text: "<span class=\"card-restriction\">TIE Advanced only.</span>%LINEBREAK%When attacking with your primary weapon, if you have a target lock on the defender, you may add 1 %CRIT% result to your roll.  If you do, you cannot spend target locks during this attack."
    },
    "Ion Cannon Battery": {
      text: "<strong>Attack (energy):</strong> Spend 2 energy from this card to perform this attack.  If this attack hits, the defender suffers 1 critical damage and receives 1 ion token.  Then cancel <strong>all</strong> dice results."
    },
    "Extra Munitions": {
      text: "When you equip this card, place 1 ordnance token on each equipped %TORPEDO%, %MISSILE%, and %BOMB% Upgrade card.  When you are instructed to discard an Upgrade card, you may discard 1 ordnance token on that card instead."
    },
    "Cluster Mines": {
      text: "<strong>Action:</strong> Discard this card to <strong>drop</strong> 3 cluster mine tokens.<br /><br />When a ship's base or maneuver template overlaps a cluster mine token, that token <strong>detonates</strong>.<br /><br /><strong>Cluster Mines Tokens:</strong> When one of these bomb tokens detonates, the ship that moved through or overlapped this token rolls 2 attack dice and suffers all damage (%HIT%) rolled.  Then discard this token."
    },
    "Glitterstim": {
      text: "At the start of the Combat phase, you may discard this card and receive 1 stress token.  If you do, until the end of the round, when attacking  or defending, you may change all of your %FOCUS% results to %HIT% or %EVADE% results."
    },
    "Grand Moff Tarkin": {
      text: "%HUGESHIPONLY% %IMPERIALONLY%%LINEBREAK%At the start of the Combat phase, you may choose another ship at Range 1-4.  Either remove 1 focus token from the chosen ship or assign 1 focus token to that ship."
    },
    "Captain Needa": {
      text: "%HUGESHIPONLY% %IMPERIALONLY%%LINEBREAK%If you overlap an obstacle during the Activation phase, do not suffer 1 faceup damage card.  Instead, roll 1 attack die.  On a %HIT% or %CRIT% result, suffer 1 damage."
    },
    "Admiral Ozzel": {
      text: "%HUGESHIPONLY% %IMPERIALONLY%%LINEBREAK%<strong>Energy:</strong> You may remove up to 3 shields from your ship.  For each shield removed, gain 1 energy."
    },
    "Emperor Palpatine": {
      text: "%IMPERIALONLY%%LINEBREAK%Once per round, you may change a friendly ship's die result to any other die result.  That die result cannot be modified again."
    },
    "Bossk": {
      text: "%SCUMONLY%%LINEBREAK%After you perform an attack that does not hit, if you are not stressed, you <strong>must</strong> receive 1 stress token. Then assign 1 focus token to your ship and acquire a target lock on the defender."
    },
    "Lightning Reflexes": {
      text: "%SMALLSHIPONLY%%LINEBREAK%After you execute a white or green maneuver on your dial, you may discard this card to rotate your ship 180&deg;.  Then receive 1 stress token <strong>after</strong> the \"Check Pilot Stress\" step."
    },
    "Twin Laser Turret": {
      text: "<strong>Attack:</strong> Perform this attack <strong>twice</strong> (even against a ship outside your firing arc).<br /><br />Each time this attack hits, the defender suffers 1 damage.  Then cancel <strong>all</strong> dice results."
    },
    "Plasma Torpedoes": {
      text: "<strong>Attack (target lock):</strong> Spend your target lock and discard this card to perform this attack.<br /><br />If this attack hits, after dealing damage, remove 1 shield token from the defender."
    },
    "Ion Bombs": {
      text: "When you reveal your maneuver dial, you may discard this card to <strong>drop</strong> 1 ion bomb token.<br /><br />This token <strong>detonates</strong> at the end of the Activation phase.<br /><br /><strong>Ion Bombs Token:</strong> When this bomb token detonates, each ship at Range 1 of the token receives 2 ion tokens.  Then discard this token."
    },
    "Conner Net": {
      text: "<strong>Action:</strong> Discard this card to <strong>drop</strong> 1 Conner Net token.<br /><br />When a ship's base or maneuver template overlaps this token, this token <strong>detonates</strong>.<br /><br /><strong>Conner Net Token:</strong> When this bomb token detonates, the ship that moved through or overlapped this token suffers 1 damage, receives 2 ion tokens, and skips its \"Perform Action\" step.  Then discard this token."
    },
    "Bombardier": {
      text: "When dropping a bomb, you may use the (%STRAIGHT% 2) template instead of the (%STRAIGHT% 1) template."
    },
    'Crack Shot': {
      text: 'When attacking a ship inside your firing arc, at the start of the "Compare Results" step, you may discard this card to cancel 1 of the defender\'s %EVADE% results.'
    },
    "Advanced Homing Missiles": {
      text: "<strong>Attack (target lock):</strong> Discard this card to perform this attack.%LINEBREAK%If this attack hits, deal 1 faceup Damage card to the defender.  Then cancel <strong>all</strong> dice results."
    },
    'Agent Kallus': {
      text: '%IMPERIALONLY%%LINEBREAK%At the start of the first round, choose 1 enemy small or large ship.  When attacking or defending against that ship, you may change 1 of your %FOCUS% results to a %HIT% or %EVADE% result.'
    },
    'XX-23 S-Thread Tracers': {
      text: "<strong>Attack (focus):</strong> Discard this card to perform this attack.  If this attack hits, each friendly ship at Range 1-2 of you may acquire a target lock on the defender.  Then cancel <strong>all</strong> dice results."
    },
    "Tractor Beam": {
      text: "<strong>Attack:</strong> Attack 1 ship.%LINEBREAK%If this attack hits, the defender receives 1 tractor beam token.  Then cancel <strong>all</strong> dice results."
    },
    "Cloaking Device": {
      text: "%SMALLSHIPONLY%%LINEBREAK%<strong>Action:</strong> Perform a free cloak action.%LINEBREAK%At the end of each round, if you are cloaked, roll 1 attack die.  On a %FOCUS% result, discard this card, then decloak or discard your cloak token."
    },
    "Shield Technician": {
      text: "%HUGESHIPONLY%%LINEBREAK%When you perform a recover action, instead of spending all of your energy, you can choose any amount of energy to spend."
    },
    "Weapons Guidance": {
      text: "When attacking, you may spend a focus token to change 1 of your blank results to a %HIT% result."
    },
    "BB-8": {
      text: "When you reveal a green maneuver, you may perform a free barrel roll action."
    },
    "R5-X3": {
      text: "Before you reveal your maneuver, you may discard this card to ignore obstacles until the end of the round."
    },
    "Wired": {
      text: "When attacking or defending, if you are stressed, you may reroll 1 or more of your %FOCUS% results."
    },
    'Cool Hand': {
      text: 'When you receive a stress token, you may discard this card to assign 1 focus or evade token to your ship.'
    },
    'Juke': {
      text: '%SMALLSHIPONLY%%LINEBREAK%When attacking, if you have an evade token, you may change 1 of the defender\'s %EVADE% results into a %FOCUS% result.'
    },
    'Comm Relay': {
      text: 'You cannot have more than 1 evade token.%LINEBREAK%During the End phase, do not remove an unused evade token from your ship.'
    },
    'Dual Laser Turret': {
      text: '%GOZANTIONLY%%LINEBREAK%<strong>Attack (energy):</strong> Spend 1 energy from this card to perform this attack against 1 ship (even a ship outside your firing arc).'
    },
    'Broadcast Array': {
      text: '%GOZANTIONLY%%LINEBREAK%Your action bar gains the %JAM% action icon.'
    },
    'Rear Admiral Chiraneau': {
      text: '%HUGESHIPONLY% %IMPERIALONLY%%LINEBREAK%<strong>Action:</strong> Execute a white (%STRAIGHT% 1) maneuver.'
    },
    'Ordnance Experts': {
      text: 'Once per round, when a friendly ship at Range 1-3 performs an attack with a %TORPEDO% or %MISSILE% secondary weapon, it may change 1 of its blank results to a %HIT% result.'
    },
    'Docking Clamps': {
      text: '%GOZANTIONLY% %LIMITED%%LINEBREAK%You may attach 4 up to TIE fighters, TIE interceptors, TIE bombers, or TIE Advanced to this ship.  All attached ships must have the same ship type.'
    },
    '"Zeb" Orrelios': {
      text: "%REBELONLY%%LINEBREAK%Enemy ships inside your firing arc that you are touching are not considered to be touching you when either you or they activate during the Combat phase."
    },
    'Kanan Jarrus': {
      text: "%REBELONLY%%LINEBREAK%Once per round, after a friendly ship at Range 1-2 executes a white maneuver, you may remove 1 stress token from that ship."
    },
    'Reinforced Deflectors': {
      text: "%LARGESHIPONLY%%LINEBREAK%After you suffer 3 or more damage from an attack, recover one shield (up to your shield value)."
    },
    'Dorsal Turret': {
      text: "<strong>Attack:</strong> Attack 1 ship (even a ship outside your firing arc).%LINEBREAK%If the target of this attack is at Range 1, roll 1 additional attack die."
    },
    'Targeting Astromech': {
      text: 'After you execute a red maneuver, you may acquire a target lock.'
    },
    'Hera Syndulla': {
      text: "%REBELONLY%%LINEBREAK%You may reveal and execute red maneuvers even while you are stressed."
    },
    'Ezra Bridger': {
      text: "%REBELONLY%%LINEBREAK%When attacking, if you are stressed, you may change 1 of your %FOCUS% results to a %CRIT% result."
    },
    'Sabine Wren': {
      text: "%REBELONLY%%LINEBREAK%Your upgrade bar gains the %BOMB% upgrade icon.  Once per round, before a friendly bomb token is removed, choose 1 enemy ship at Range 1 of that token. That ship suffers 1 damage."
    },
    '"Chopper"': {
      text: "%REBELONLY%%LINEBREAK%You may perform actions even while you are stressed.%LINEBREAK%After you perform an action while you are stressed, suffer 1 damage."
    },
    'Construction Droid': {
      text: '%HUGESHIPONLY% %LIMITED%%LINEBREAK%When you perform a recover action, you may spend 1 energy to discard 1 facedown Damage card.'
    },
    'Cluster Bombs': {
      text: 'After defending, you may discard this card.  If you do, each other ship at Range 1 of the defending section rolls 2 attack dice, suffering all damage (%HIT%) and critical damage (%CRIT%) rolled.'
    },
    "Adaptability": {
      text: "<span class=\"card-restriction\">Dual card.</span>%LINEBREAK%<strong>Side A:</strong>%LINEBREAK%Increase your pilot skill value by 1.%LINEBREAK%<strong>Side B:</strong>%LINEBREAK%Decrease your pilot skill value by 1."
    },
    "Electronic Baffle": {
      text: "When you receive a stress token or an ion token, you may suffer 1 damage to discard that token."
    },
    "4-LOM": {
      text: "%SCUMONLY%%LINEBREAK%When attacking, during the \"Modify Attack Dice\" step, you may receive 1 ion token to choose 1 of the defender's focus or evade tokens.  That token cannot be spent during this attack."
    },
    "Zuckuss": {
      text: "%SCUMONLY%%LINEBREAK%When attacking, you may receive any number of stress tokens to choose an equal number of defense dice.  The defender must reroll those dice."
    },
    'Rage': {
      text: "<strong>Action:</strong> Assign 1 focus token to your ship and receive 2 stress tokens.  Until the end of the round, when attacking, you may reroll up to 3 attack dice."
    },
    "Attanni Mindlink": {
      text: "%SCUMONLY%%LINEBREAK%Each time you are assigned a focus or stress token, each other friendly ship with Attanni Mindlink must also be assigned the same type of token if it does not already have one."
    },
    "Boba Fett": {
      text: "%SCUMONLY%%LINEBREAK%After performing an attack, if the defender was dealt a faceup Damage card, you may discard this card to choose and discard 1 of the defender's Upgrade cards."
    },
    "Dengar": {
      text: "%SCUMONLY%%LINEBREAK%When attacking, you may reroll 1 attack die.  If the defender is a unique pilot, you may instead reroll up to 2 attack dice."
    },
    '"Gonk"': {
      text: "%SCUMONLY%%LINEBREAK%<strong>Action:</strong> Place 1 shield token on this card.%LINEBREAK%<strong>Action:</strong> Remove 1 shield token from this card to recover 1 shield (up to your shield value)."
    },
    "R5-P8": {
      text: "Once per round, after defending, you may roll 1 attack die.  On a %HIT% result, the attacker suffers 1 damage.  On a %CRIT% result, you and the attacker each suffer 1 damage."
    },
    'Thermal Detonators': {
      text: "When you reveal your maneuver dial, you may discard this card to <strong>drop</strong> 1 thermal detonator token.%LINEBREAK%This token <strong>detonates</strong> at the end of the Activation phase.%LINEBREAK%<strong>Thermal Detonator Token:</strong> When this bomb token detonates, each ship at Range 1 of the token suffers 1 damage and receives 1 stress token.  Then discard this token."
    },
    "Overclocked R4": {
      text: "During the Combat phase, when you spend a focus token, you may receive 1 stress token to assign 1 focus token to your ship."
    },
    'Systems Officer': {
      text: '%IMPERIALONLY%%LINEBREAK%After you execute a green maneuver, choose another friendly ship at Range 1.  That ship may acquire a target lock.'
    }
  };
  modification_translations = {
    "Stealth Device": {
      text: "Increase your agility value by 1.  If you are hit by an attack, discard this card."
    },
    "Shield Upgrade": {
      text: "Increase your shield value by 1."
    },
    "Engine Upgrade": {
      text: "Your action bar gains the %BOOST% action icon."
    },
    "Anti-Pursuit Lasers": {
      text: "%LARGESHIPONLY%%LINEBREAK%After an enemy ship executes a maneuver that causes it to overlap your ship, roll 1 attack die.  On a %HIT% or %CRIT% result, the enemy ship suffers 1 damage."
    },
    "Targeting Computer": {
      text: "Your action bar gains the %TARGETLOCK% action icon."
    },
    "Hull Upgrade": {
      text: "Increase your hull value by 1."
    },
    "Munitions Failsafe": {
      text: "When attacking with a secondary weapon that instructs you to discard it to perform the attack, do not discard it unless the attack hits."
    },
    "Stygium Particle Accelerator": {
      text: "When you either decloak or perform a cloak action, you may perform a free evade action."
    },
    "Advanced Cloaking Device": {
      text: "<span class=\"card-restriction\">TIE Phantom only.</span>%LINEBREAK%After you perform an attack, you may perform a free cloak action."
    },
    "Combat Retrofit": {
      text: "<span class=\"card-restriction\">GR-75 only.</span>%LINEBREAK%Increase your hull value by 2 and your shield value by 1."
    },
    "B-Wing/E2": {
      text: "<span class=\"card-restriction\">B-Wing only.</span>%LINEBREAK%Your upgrade bar gains the %CREW% upgrade icon."
    },
    "Countermeasures": {
      text: "%LARGESHIPONLY%%LINEBREAK%At the start of the Combat phase, you may discard this card to increase your agility value by 1 until the end of the round.  Then you may remove 1 enemy target lock from your ship."
    },
    "Experimental Interface": {
      text: "Once per round, after you perform an action, you may perform 1 free action from an equipped Upgrade card with the \"<strong>Action:</strong>\" header.  Then receive 1 stress token."
    },
    "Tactical Jammer": {
      text: "%LARGESHIPONLY%%LINEBREAK%Your ship can obstruct enemy attacks."
    },
    "Autothrusters": {
      text: "When defending, if you are beyond Range 2 or outside the attacker's firing arc, you may change 1 of your blank results to a %EVADE% result. You can equip this card only if you have the %BOOST% action icon."
    },
    "Advanced SLAM": {
      text: "After performing a SLAM action, if you did not overlap an obstacle or another ship, you may perform a free action."
    },
    "Twin Ion Engine Mk. II": {
      text: "<span class=\"card-restriction\">TIE only.</span>%LINEBREAK%You may treat all bank maneuvers (%BANKLEFT% and %BANKRIGHT%) as green maneuvers."
    },
    "Maneuvering Fins": {
      text: "When you reveal a turn maneuver (%TURNLEFT% or %TURNRIGHT%), you may rotate your dial to the corresponding bank maneuver (%BANKLEFT% or %BANKRIGHT%) of the same speed."
    },
    "Ion Projector": {
      text: "%LARGESHIPONLY%%LINEBREAK%After an enemy ship executes a maneuver that causes it to overlap your ship, roll 1 attack die.  On a %HIT% or %CRIT% result, the enemy ship receives 1 ion token."
    },
    'Integrated Astromech': {
      text: '<span class="card-restriction">X-wing only.</span>%LINEBREAK%When you are dealt a Damage card, you may discard 1 of your %ASTROMECH% Upgrade cards to discard that Damage card.'
    },
    'Optimized Generators': {
      text: '%HUGESHIPONLY%%LINEBREAK%Once per round, when you assign energy to an equipped Upgrade card, gain 2 energy.'
    },
    'Automated Protocols': {
      text: '%HUGESHIPONLY%%LINEBREAK%Once per round, after you perform an action that is not a recover or reinforce action, you may spend 1 energy to perform a free recover or reinforce action.'
    },
    'Ordnance Tubes': {
      text: '%HUGESHIPONLY%%LINEBREAK%You may treat each of your %HARDPOINT% upgrade icons as a %TORPEDO% or %MISSILE% icon.%LINEBREAK%When you are instructed to discard a %TORPEDO% or %MISSILE% Upgrade card, do not discard it.'
    },
    'Long-Range Scanners': {
      text: 'You can acquire target locks on ships at Range 3 and beyond.  You cannot acquire target locks on ships at Range 1-2.  You can equip this card only if you have %TORPEDO% and %MISSILE% in your upgrade bar.'
    },
    "Guidance Chips": {
      text: "Once per round, when attacking with a %TORPEDO% or %MISSILE% secondary weapon, you may change 1 die result to a %HIT% result (or a %CRIT% result if your primary weapon value is \"3\" or higher)."
    }
  };
  title_translations = {
    "Slave I": {
      text: "<span class=\"card-restriction\">Firespray-31 only.</span>%LINEBREAK%Your upgrade bar gains the %TORPEDO% upgrade icon."
    },
    "Millennium Falcon": {
      text: "<span class=\"card-restriction\">YT-1300 only.</span>%LINEBREAK%Your action bar gains the %EVADE% action icon."
    },
    "Moldy Crow": {
      text: "<span class=\"card-restriction\">HWK-290 only.</span>%LINEBREAK%During the End phase, do not remove unused focus tokens from your ship."
    },
    "ST-321": {
      text: "<span class=\"card-restriction\"><em>Lambda</em>-class Shuttle only.</span>%LINEBREAK%When acquiring a target lock, you may lock onto any enemy ship in the play area."
    },
    "Royal Guard TIE": {
      text: "<span class=\"card-restriction\">TIE Interceptor only.</span>%LINEBREAK%You may equip up to 2 different Modification upgrades (instead of 1).%LINEBREAK%You cannot equip this card if your pilot skill value is \"4\" or lower."
    },
    "Dodonna's Pride": {
      text: "<span class=\"card-restriction\">CR90 fore section only.</span>%LINEBREAK%When you perform a coordinate action, you may choose 2 friendly ships (instead of 1).  Those ships may each perform 1 free action."
    },
    "A-Wing Test Pilot": {
      text: "<span class=\"card-restriction\">A-Wing only.</span>%LINEBREAK%Your upgrade bar gains 1 %ELITE% upgrade icon.%LINEBREAK%You cannot equip 2 of the same %ELITE% Upgrade cards.  You cannot equip this if your pilot skill value is \"1\" or lower."
    },
    "Tantive IV": {
      text: "<span class=\"card-restriction\">CR90 fore section only.</span>%LINEBREAK%Your fore section upgrade bar gains 1 additional %CREW% and 1 additional %TEAM% upgrade icon."
    },
    "Bright Hope": {
      text: "<span class=\"card-restriction\">GR-75 only.</span>%LINEBREAK%A reinforce action assigned to your fore section adds 2 %EVADE% results (instead of 1)."
    },
    "Quantum Storm": {
      text: "<span class=\"card-restriction\">GR-75 only.</span>%LINEBREAK%At the start of the End phase, if you have 1 or fewer energy tokens, gain 1 energy token."
    },
    "Dutyfree": {
      text: "<span class=\"card-restriction\">GR-75 only.</span>%LINEBREAK%When performing a jam action, you may choose an enemy ship at Range 1-3 (instead of at Range 1-2)."
    },
    "Jaina's Light": {
      text: "<span class=\"card-restriction\">CR90 fore section only.</span>%LINEBREAK%When defending, once per attack, if you are dealt a faceup Damage card, you may discard it and draw another faceup Damage card."
    },
    "Outrider": {
      text: "<span class=\"card-restriction\">YT-2400 only.</span>%LINEBREAK%While you have a %CANNON% Upgrade card equipped, you <strong>cannot</strong> perform primary weapon attacks and you may perform %CANNON% secondary weapon attacks against ships outside your firing arc."
    },
    "Dauntless": {
      text: "<span class=\"card-restriction\">VT-49 Decimator only.</span>%LINEBREAK%After you execute a maneuver that causes you to overlap another ship, you may perform 1 free action.  Then receive 1 stress token."
    },
    "Virago": {
      text: "<span class=\"card-restriction\">StarViper only.</span>%LINEBREAK%Your upgrade bar gains the %SYSTEM% and %ILLICIT% upgrade icons.%LINEBREAK%You cannot equip this card if your pilot skill value is \"3\" or lower."
    },
    '"Heavy Scyk" Interceptor (Cannon)': {
      text: "<span class=\"card-restriction\">M3-A Interceptor only.</span>%LINEBREAK%Your upgrade bar gains the %CANNON%, %TORPEDO%, or %MISSILE% upgrade icon."
    },
    '"Heavy Scyk" Interceptor (Torpedo)': {
      text: "<span class=\"card-restriction\">M3-A Interceptor only.</span>%LINEBREAK%Your upgrade bar gains the %CANNON%, %TORPEDO%, or %MISSILE% upgrade icon."
    },
    '"Heavy Scyk" Interceptor (Missile)': {
      text: "<span class=\"card-restriction\">M3-A Interceptor only.</span>%LINEBREAK%Your upgrade bar gains the %CANNON%, %TORPEDO%, or %MISSILE% upgrade icon."
    },
    "IG-2000": {
      text: "<span class=\"card-restriction\">Aggressor only.</span>%LINEBREAK%You have the pilot ability of each other friendly ship with the <em>IG-2000</em> Upgrade card (in addition to your own pilot ability)."
    },
    "BTL-A4 Y-Wing": {
      text: "<span class=\"card-restriction\">Y-Wing only.</span>%LINEBREAK%You cannot attack ships outside your firing arc. After you perform a primary weapon attack, you may immediately perform an attack with a %TURRET% secondary weapon."
    },
    "Andrasta": {
      text: "Your upgrade bar gains two additional %BOMB% upgrade icons."
    },
    "TIE/x1": {
      text: "<span class=\"card-restriction\">TIE Advanced only.</span>%LINEBREAK%Your upgrade bar gains the %SYSTEM% upgrade icon.%LINEBREAK%If you equip a %SYSTEM% upgrade, its squad point cost is reduced by 4 (to a minimum of 0)."
    },
    "Hound's Tooth": {
      text: "<span class=\"card-restriction\">YV-666 only.</span>%LINEBREAK%After you are destroyed, before you are removed from the play area, you may <strong>deploy</strong> the <em>Nashtah Pup</em> ship.%LINEBREAK%It cannot attack this round."
    },
    "Ghost": {
      text: "<span class=\"card-restriction\">VCX-100 only.</span>%LINEBREAK%Equip the <em>Phantom</em> title card to a friendly Attack Shuttle and dock it to this ship.%LINEBREAK%After you execute a maneuver, you may deploy it from your rear guides."
    },
    "Phantom": {
      text: "While you are docked, the <em>Ghost</em> can perform primary weapon attacks from its special firing arc, and, at the end of the Combat phase, it may perform an additional attack with an equipped %TURRET%. If it performs this attack, it cannot attack again this round."
    },
    "TIE/v1": {
      text: "<span class=\"card-restriction\">TIE Advanced Prototype only.</span>%LINEBREAK%After you acquire a target lock, you may perform a free evade action."
    },
    "Mist Hunter": {
      text: "<span class=\"card-restriction\">G-1A starfighter only.</span>%LINEBREAK%Your action bar gains the %BARRELROLL% action icon.%LINEBREAK%You <strong>must</strong> equip 1 \"Tractor Beam\" Upgrade card (paying its squad point cost as normal)."
    },
    "Punishing One": {
      text: "<span class=\"card-restriction\">JumpMaster 5000 only.</span>%LINEBREAK%Increase your primary weapon value by 1."
    },
    "Assailer": {
      text: "<span class=\"card-restriction\"><em>Raider</em>-class corvette aft section only.</span>%LINEBREAK%When defending, if the targeted section has a reinforce token, you may change 1 %FOCUS% result to a %EVADE% result."
    },
    "Instigator": {
      text: "<span class=\"card-restriction\"><em>Raider</em>-class corvette aft section only.</span>%LINEBREAK%After you perform a recover action, recover 1 additional shield."
    },
    "Impetuous": {
      text: "<span class=\"card-restriction\"><em>Raider</em>-class corvette aft section only.</span>%LINEBREAK%After you perform an attack that destroys an enemy ship, you may acquire a target lock."
    },
    'TIE/x7': {
      text: '<span class="card-restriction">TIE Defender only.</span>%LINEBREAK%Your upgrade bar loses the %CANNON% and %MISSILE% upgrade icons.%LINEBREAK%After executing a 3-, 4-, or 5-speed maneuver, you may assign 1 evade token to your ship.'
    },
    'TIE/D': {
      text: '<span class="card-restriction">TIE Defender only.</span>%LINEBREAK%Once per round, after you perform an attack with a %CANNON% secondary weapon that costs 3 or fewer squad points, you may perform a primary weapon attack.'
    },
    'TIE Shuttle': {
      text: '<span class="card-restriction">TIE Bomber only.</span>%LINEBREAK%Your upgrade bar loses all %TORPEDO%, %MISSILE%, and %BOMB% upgrade icons and gains 2 %CREW% upgrade icons.  You cannot equip a %CREW% Upgrade card that costs more than 4 squad points.'
    },
    'Requiem': {
      text: '%GOZANTIONLY%%LINEBREAK%When you deploy a ship, treat its pilot skill value as "8" until the end of the round.'
    },
    'Vector': {
      text: '%GOZANTIONLY%%LINEBREAK%After you execute a maneuver, you may deploy up to 4 attached ships (instead of 2).'
    },
    'Suppressor': {
      text: '%GOZANTIONLY%%LINEBREAK%Once per round, after you acquire a target lock, you may remove 1 focus, evade, or blue target lock token from that ship.'
    },
    'Black One': {
      text: 'After you perform a boost or barrel roll action, you may remove 1 enemy target lock from a friendly ship at Range 1.  You cannot equip this card if your pilot skill is "6" or lower.'
    },
    'Millennium Falcon (TFA)': {
      text: 'After you execute a 3-speed bank maneuver (%BANKLEFT% or %BANKRIGHT%), if you are not touching another ship and you are not stressed, you may receive 1 stress token to rotate your ship 180&deg;.'
    },
    'Alliance Overhaul': {
      text: '<span class="card-restriction">ARC-170 only.</span>%LINEBREAK%When attacking with a primary weapon from your primary firing arc, you may roll 1 additional attack die.  When attacking from your auxiliary firing arc, you may change 1 of your %FOCUS% results to a %CRIT% result.'
    },
    'Special Ops Training': {
      text: '<span class="card-restriction">TIE/sf only.</span>%LINEBREAK%When attacking with a primary weapon from your primary firing arc, you may roll 1 additional attack die.  If you do not, you may perform an additional attack from your auxiliary firing arc.'
    },
    'Concord Dawn Protector': {
      text: '<span class="card-restriction">Protectorate Starfighter only.</span>%LINEBREAK%When defending, if you are inside the attacker\'s firing arc and at Range 1 and the attacker is inside your firing arc, add 1 %EVADE% result.'
    },
    'Shadow Caster': {
      text: '<span class="card-restriction">Lancer-class Pursuit Craft only.</span>%LINEBREAK%After you perform an attack that hits, if the defender is inside your mobile firing arc and at Range 1-2, you may assign the defender 1 tractor beam token.'
    }
  };
  return exportObj.setupCardData(basic_cards, pilot_translations, upgrade_translations, modification_translations, title_translations);
};
