import os

from PIL import Image, ImageFont, ImageDraw, ImageOps


class Colour:
    default = ('', (0, 0, 0))

    def __init__(self, letter):
        try:
            self.colours = letter.colours
            self.letter = letter.letter
        except AttributeError:
            self.letter = letter
            self.colours = [self.default]

    @staticmethod
    def factory(name, colour):
        class Temp(Colour):
            def __init__(self, letter):
                super().__init__(letter)
                self.colours.append((name, colour))
        return Temp

Red = Colour.factory('red', "#EF232B")
Green = Colour.factory('green', "#6BBE44")
Yellow = Colour.factory('yellow', "#B6B335")
Blue = Colour.factory('blue', "#7ED3E5")
Orange = Colour.factory('orange', "#E5B922")
Purple = Colour.factory('purple', "#C39DC9")

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
        'team': "T",
        'tech': 'X',
        'talent': "E",
        'title': "t",
        'torpedo': "P",
        'turret': "U",
        # Actions
        'barrelroll': Red("r"),
        'boost': Red("b"),
        'calculate': Red('a'),
        'cloak': Red("k"),
        'coordinate': Red("o"),
        'evade': Red("e"),
        'focus': Red("f"),
        'jam': Red("j"),
        'lock': Red("l"),
        'recover': Red("v"),
        'reinforce': Red("i"),
        'reload': Red("="),
        'rotatearc': Red("R"),
        'slam': Red("s"),
        # Other
        #TODO make this smaller so it matches the cards
        'linked': '>',
        'crit': "c",
        'hit': "d",
        'rangebonusindicator': Red('?'),
        'recurring': Orange(Purple('`')),
        # 'condition': '\u00B0',
    },
    "xwing-miniatures-ships.ttf": {
        'aggressorassaultfighter': "i",
        'alphaclassstarwing': "&",
        'arc170starfighter': "c",
        'attackshuttle': "g",
        'auzituckgunship': "@",
        'rz1awing': "a",
        'asf01bwing': "b",
        'mg100starfortresssf17': "Z",
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
        'tieinterceptor': "I",
        'tiephphantom': "P",
        'tiecapunisher': "N",
        'tiereaper': "V",
        'tiesffighter': "S",
        'tiesilencer': "$",
        'tieskstriker': "T",
        'upsilonclassshuttle': "U",
        'ut60duwing': "u",
        'vcx100lightfreighter': "G",
        'vt49decimator': "d",
        't65xwing': "x",
        'modifiedyt1300lightfreighter': "m",
        'yt2400lightfreighter': "o",
        'yv666lightfreighter': "t",
        'btla4ywing': "y",
        'z95af4headhunter': "z",
    }
}

size = (128, 128)

def main():
    if not os.path.exists('emoji'):
        os.mkdir('emoji')

    for font, glyphs in fonts.items():
        font = ImageFont.truetype(font, 128)
        for name, glyph in glyphs.items():
            try:
                colours = glyph.colours
                glyph = glyph.letter
            except AttributeError:
                colours = [Colour.default]

            for colour_name, colour in colours:
                im = Image.new("RGBA", (300, 300), (255, 255, 255, 0))

                draw = ImageDraw.Draw(im)
                draw.text((50, 50), glyph, font=font, fill=colour)

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
