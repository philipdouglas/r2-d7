import os

from PIL import Image, ImageFont, ImageDraw, ImageOps

fonts = {
    'xwing-miniatures.ttf': {
        'attack-turret': "$",
        'attack-frontback': '<',
        'attack-180': '>',
        'attack': '%',
        'energy': '(',
        'epic': ')',
        'agility': 'e',
        'hull': '&',
        'xshield': '*',
        'astromech': "A",
        'xbomb': "B",
        'cannon': "C",
        'elite': "E",
        'cargo': "G",
        'hardpoint': "H",
        'illicit': "I",
        'missile': "M",
        'torpedo': "P",
        'rotatearc': "R",
        'system': "S",
        'team': "T",
        'turret': "U",
        'salvagedastromech': "V",
        'crew': "W",
        'tech': 'X',
        'boost': "b",
        'crit': "c",
        'hit': "d",
        'evade': "e",
        'focus': "f",
        'reinforce': "i",
        'jam': "j",
        'cloak': "k",
        'targetlock': "l",
        'modification': "m",
        'coordinate': "o",
        'barrelroll': "r",
        'slam': "s",
        'title': "t",
        'unique': "u",
        'recover': "v",
        # 'condition': '\u00B0',
    },
    "xwing-miniatures-ships.ttf": {
        'gr75mediumtransport': "1",
        'cr90corvette': "2",
        'raiderclasscorvette': "3",
        'gozanticlasscruiser': "4",
        'croccruiser': "5",
        'tieadvanced': "A",
        'tiebomber': "B",
        'tiedefender': "D",
        'tiefighter': "F",
        'vcx100': "G",
        'scurrgh6bomber': "H",
        'tieinterceptor': "I",
        'lancerclasspursuitcraft': "L",
        'protectoratestarfighter': "M",
        'tiepunisher': "N",
        'tiefofighter': "O",
        'tiephantom': "P",
        'tieadvprototype': "R",
        'tiesffighter': "S",
        'tiestriker': 'T',
        'upsilonclassshuttle': 'U',
        'awing': "a",
        'bwing': "b",
        'arc170': "c",
        'vt49decimator': "d",
        'ewing': "e",
        'firespray31': "f",
        'attackshuttle': "g",
        'hwk290': "h",
        'ig2000': "i",
        'aggressor': "i",
        'kwing': "k",
        'lambdaclassshuttle': "l",
        'yt1300': "m",
        'g1astarfighter': "n",
        'yt2400': "o",
        'jumpmaster5000': "p",
        'quadjumper': "q",
        'kihraxzfighter': "r",
        'm3ainterceptor': "s",
        'yv666': "t",
        'uwing': 'u',
        'starviper': "v",
        't70xwing': "w",
        'xwing': "x",
        'ywing': "y",
        'z95headhunter': "z",
        'auzituckgunship': '@',
        'tieaggressor': '`',
    }
}

size = (128, 128)

def main():
    if not os.path.exists('emoji'):
        os.mkdir('emoji')

    for font, glyphs in fonts.items():
        font = ImageFont.truetype(font, 128)
        for name, glyph in glyphs.items():
            im = Image.new("RGBA", (300, 300), (255, 255, 255, 0))

            draw = ImageDraw.Draw(im)
            draw.text((50, 50), glyph, font=font, fill=(0, 0, 0))

            # remove unneccessory whitespaces if needed
            im = im.crop(ImageOps.invert(im.convert('RGB')).getbbox())

            # im = ImageOps.invert(im)
            im.thumbnail(size, Image.ANTIALIAS)

            background = Image.new('RGBA', size, (255, 255, 255, 0))
            background.paste(
                im,
                ((size[0] - im.size[0]) // 2, (size[1] - im.size[1]) // 2))

            # write into file
            background.save("emoji/{}.png".format(name))

if __name__ == '__main__':
    main()
