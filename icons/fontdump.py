import os

from PIL import Image, ImageFont, ImageDraw, ImageOps


class Icon:
    default_colour = ('', (0, 0, 0))

    def __init__(self, letter):
        try:
            self.letter = letter.letter
            self.colours = letter.colours
            self.size = letter.size
        except AttributeError:
            self.letter = letter
            self.colours = [self.default_colour]
            self.size = 128

    @staticmethod
    def factory(name=None, colour=None, size=None):
        class Temp(Icon):
            def __init__(self, letter):
                super().__init__(letter)
                if colour and name:
                    self.colours.append((name, colour))
                if size:
                    self.size = size
        return Temp

Red = Icon.factory('red', "#EF232B")
Green = Icon.factory('green', "#6BBE44")
Yellow = Icon.factory('yellow', "#B6B335")
Blue = Icon.factory('blue', "#7ED3E5")
Orange = Icon.factory('orange', "#E5B922")
Purple = Icon.factory('purple', "#B590D3")

Medium = Icon.factory(size=100)

fonts = {
    'xwing-miniatures.ttf': {
        # Stats
        'agility': Green('^'),
        'attack': Red('%'),
        'charge': Orange('g'),
        'hull': Yellow('&'),
        'forcecharge': Purple('h'),
        'shield': Blue('*'),
        # Arcs
        'bullseyearc': Red("}"),
        'doubleturretarc': Red('q'),
        'frontarc': Red('{'),
        'fullfrontarc': Red('~'),
        'fullreararc': Red('¡'),
        'leftarc': Red('£'),
        'reararc': Red('|'),
        'rightarc': Red('¢'),
        'singleturretarc': Red('p'),
        # Slots
        'astromech': "A",
        'device': "B",
        'cannon': "C",
        'cargo': "G",
        'configuration': 'n',
        'crew': "W",
        'forcepower': 'F',
        'gunner': 'Y',
        'hardpoint': "H",
        'illicit': "I",
        'missile': "M",
        'modification': "m",
        'sensor': "S",
        'tacticalrelay': 'Z',
        'talent': "E",
        'team': "T",
        'tech': 'X',
        'title': "t",
        'torpedo': "P",
        'turret': "U",
        # Actions
        'barrelroll': Purple(Red("r")),
        'boost': Purple(Red("b")),
        'calculate': Purple(Red('a')),
        'cloak': Purple(Red("k")),
        'coordinate': Purple(Red("o")),
        'evade': Purple(Red("e")),
        'focus': Purple(Red("f")),
        'jam': Purple(Red("j")),
        'targetlock': Purple(Red("l")),
        'lock': Purple(Red("l")),
        'recover': Purple(Red("v")),
        'reinforce': Purple(Red("i")),
        'reload': Purple(Red("=")),
        'rotatearc': Purple(Red("R")),
        'slam': Purple(Red("s")),
        # Other
        #TODO make this smaller so it matches the cards
        'linked': '>',
        'crit': "c",
        'hit': "d",
        'rangebonusindicator': Red('?'),
    },
    "xwing-miniatures-ships.ttf": {
        'aggressorassaultfighter': "i",
        'alphaclassstarwing': "&",
        'arc170starfighter': "c",
        'attackshuttle': "g",
        'auzituckgunship': "@",
        'rz1awing': "a",
        'asf01bwing': "b",
        'mg100starfortress': "Z",
        'cr90corvette': "2",
        'croccruiser': "5",
        'ewing': "e",
        'firesprayclasspatrolcraft': "f",
        'g1astarfighter': "n",
        'gozanticlasscruiser': "4",
        'gr75mediumtransport': "1",
        'hwk290lightfreighter': "h",
        'ig2000': "i",
        'jumpmaster5000': "p",
        'kihraxzfighter': "r",
        'btls8kwing': "k",
        'm12lkimogilafighter': "K",
        'lambdaclasst4ashuttle': "l",
        'lancerclasspursuitcraft': "L",
        'm3ainterceptor': "s",
        'fangfighter': "M",
        'quadrijettransferspacetug': "q",
        'raiderclasscorvette': "3",
        'scurrgh6bomber': "H",
        'sheathipedeclassshuttle': "%",
        'starviperclassattackplatform': "v",
        't70xwing': "w",
        'tieadvancedx1': "A",
        'tieadvancedv1': "R",
        'tieagaggressor': "`",
        'tiesabomber': "B",
        'tieddefender': "D",
        'tielnfighter': "F",
        'tiefofighter': "O",
        'tieininterceptor': "I",
        'tiephphantom': "P",
        'tiecapunisher': "N",
        'tiereaper': "V",
        'tiesffighter': "S",
        'tievnsilencer': "$",
        'tieskstriker': "T",
        'upsilonclasscommandshuttle': "U",
        'ut60duwing': "u",
        'vcx100lightfreighter': "G",
        'vt49decimator': "d",
        't65xwing': "x",
        'modifiedyt1300lightfreighter': "m",
        'yt2400lightfreighter': "o",
        'yv666lightfreighter': "t",
        'btla4ywing': "y",
        'z95af4headhunter': "z",
        'customizedyt1300lightfreighter': 'W',
        'escapecraft': 'X',
        'modifiedtielnfighter': 'C',
        'rz2awing': 'E',
        'scavengedyt1300': 'Y',
        'belbullab22starfighter': '[',
        'delta7aethersprite': '\\',
        'sithinfiltrator': ']',
        'v19torrentstarfighter': '^',
        'vultureclassdroidfighter': '_',
        'resistancetransport': '>',
        'resistancetransportpod': '?',
        'hyenaclassdroidbomber': '=',
        'nabooroyaln1starfighter': '<',
        'btlbywing': ':',
        'nantexclassstarfighter': ';',
        'fireball': '|',
        'tiebainterceptor': '{',
        'xiclasslightshuttle': 'Q',
        'laatigunship': '/',
        'hmpdroidgunship': '.',
    }
}

needsCreamCircle = {
    'astromech',
    'device',
    'cannon',
    'cargo',
    'condition',
    'configuration',
    'crew',
    'forcepower',
    'gunner',
    'hardpoint',
    'illicit',
    'missile',
    'modification',
    'sensor',
    'tacticalrelay',
    'talent',
    'team',
    'tech',
    'title',
    'torpedo',
    'turret'
}

needsBlackBackground = {
    'linked',
    'crit',
    'hit',
    'rangebonusindicator',
    'barrelroll',
    'boost',
    'calculate',
    'cloak',
    'coordinate',
    'evade',
    'focus',
    'jam',
    'targetlock',
    'lock',
    'recover',
    'reinforce',
    'reload',
    'rotatearc',
    'slam'
}

needsSizeBoost = {
    'linked',
    'crit',
    'hit',
    'boost',
    'cloak',
    'coordinate',
    'evade',
    'targetlock',
    'lock',
    'recover',
    'reinforce',
    'reload',
    'rotatearc',
    'slam'
}

noBackground = {
    'agility',
    'attack',
    'charge',
    'hull',
    'forcecharge',
    'shield'
}


size = (128, 128)

def main():
    if not os.path.exists('emoji'):
        os.mkdir('emoji')

    for font, glyphs in fonts.items():
        for name, glyph in glyphs.items():
            try:
                colours = glyph.colours
                glyph = glyph.letter
            except AttributeError:
                colours = [Icon.default_colour]

            fontSize = 130

            if name in needsCreamCircle or ('arc' in name and '170' not in name and 'rotate' not in name):
                fontSize = 155

            if name in needsBlackBackground:
                fontSize = 200

            if name in needsSizeBoost:
                fontSize = 240

            if font == "xwing-miniatures-ships.ttf":
                fontSize = 200

            imfont = ImageFont.truetype(font, fontSize)
            for colour_name, colour in colours:
                im = Image.new("RGBA", (300, 300), (255, 255, 255, 0))

                if name in needsBlackBackground:
                    im = Image.new("RGB", (300, 300))

                draw = ImageDraw.Draw(im)

                if name in needsCreamCircle or font == "xwing-miniatures-ships.ttf":
                    draw.arc((75, 75, 225, 225), start=0, end=360, fill="#F2F3F5", width=100)

                if name in needsBlackBackground and colour == (0, 0, 0):
                    colour = (255, 255, 255)

                draw.text((151, 152), glyph, font=imfont, fill=colour, anchor='mm')

                # remove unneccessory whitespaces if needed
                im = im.crop(ImageOps.invert(im.convert('RGB')).getbbox())

                # im = ImageOps.invert(im)
                im.thumbnail(size, Image.ANTIALIAS)

                background = Image.new('RGBA', size, (255, 255, 255, 0))


                background.paste(
                    im,
                    ((size[0] - im.size[0]) // 2, (size[1] - im.size[1]) // 2))

                # write into file
                background.save(f"emoji/{colour_name}{name}.png")

if __name__ == '__main__':
    main()
