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
        'shield': '*',
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
    },
    "xwing-miniatures-ships.ttf": {
        'gr75mediumtransport': "1",
        'cr90corvette': "2",
        'raiderclasscorvette': "3",
        'gozanticlasscruiser': "4",
        'tieadvanced': "A",
        'tiebomber': "B",
        'tiedefender': "D",
        'tiefighter': "F",
        'vcx100': "G",
        'tieinterceptor': "I",
        'lancerclasspursuitcraft': "L",
        'protectoratestarfighter': "M",
        'tiepunisher': "N",
        'tiefofighter': "O",
        'tiephantom': "P",
        'tieadvancedprototype': "R",
        'tiesffighter': "S",
        'awing': "a",
        'bwing': "b",
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
        'yt2400freighter': "o",
        'jumpmaster5000': "p",
        'kihraxzfighter': "r",
        'm3ainterceptor': "s",
        'yv666': "t",
        'starviper': "v",
        't70xwing': "w",
        'xwing': "x",
        'ywing': "y",
        'z95headhunter': "z",
    }
}

size = (128, 128)

if not os.path.exists('fonticons'):
    os.mkdir('fonticons')

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
        background.save("fonticons/{}.png".format(name))
