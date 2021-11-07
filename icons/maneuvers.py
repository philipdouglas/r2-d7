import os

from PIL import Image, ImageFont, ImageDraw, ImageOps

fonts = {
    'xwing-miniatures.ttf': {
        'sloopleft': "1",
        'kturn': "2",
        'sloopright': "3",
        'turnleft': "4",
        'stop': "5",
        'turnright': "6",
        'bankleft': "7",
        'straight': "8",
        'bankright': "9",
        'trollleft': ":",
        'trollright': ";",
        'reversebankleft': "J",
        'reversestraight': "K",
        'reversebankright': "L",
    },
}
colours = {
    '': (255, 255, 255),
    'blue': '#00a8f3',
    'red': '#E61713',
    'purple': '#B590D3'
}


def main():
    size = (128, 128)

    if not os.path.exists('emoji'):
        os.mkdir('emoji')

    for font, glyphs in fonts.items():
        font = ImageFont.truetype(font, 280)
        for name, glyph in glyphs.items():
            for colour_name, colour in colours.items():
                im = Image.new("RGB", (300, 300))

                draw = ImageDraw.Draw(im)
                draw.text(
                    xy=(150, 165 if 'straight' not in name else 175),
                    text=glyph,
                    font=font,
                    fill=colour,
                    anchor='mm',
                    stroke_width=3
                )

                # remove unnecessary whitespaces if needed
                im = im.crop(ImageOps.invert(im.convert('RGB')).getbbox())

                # im = ImageOps.invert(im)
                im.thumbnail(size, Image.ANTIALIAS)

                background = Image.new('RGBA', size)
                background.paste(
                    im,
                    ((size[0] - im.size[0]) // 2, (size[1] - im.size[1]) // 2))

                # write into file
                background.save("emoji/{}{}.png".format(colour_name, name))

if __name__ == '__main__':
    main()
