#coding: utf-8
import itertools
import os

from PIL import Image, ImageFont, ImageDraw, ImageOps, ImageFilter

plusminus = list(itertools.chain(
    *[[f"+{num}", f"-{num}"] for num in range(1, 3)]))
stat_ranges = {
    'initiative': ([str(num) for num in range(0, 8)], '#CD6D2D'),
    'attack': (['-'] + [str(num) for num in range(0, 6)] + plusminus, '#EF232B'),
    'agility': ([str(num) for num in range(0, 5)] + plusminus, '#6BBE44'),
    'hull': ([str(num) for num in range(0, 13)] + plusminus, '#B6B335'),
    'shield': ([str(num) for num in range(0, 7)] + plusminus, '#7ED3E5'),
    'charge': (
        list(itertools.chain( *[[str(num), f"{num}`"] for num in range(0, 9)])),
    '#E5B922'),
    'forcecharge': (
        list(itertools.chain(
            *[[str(num), f"{num}`", f"+{num}", f"+{num}`"] for num in range(0, 5)])),
    '#C39DC9'),
}

size = (128, 128)

def main():
    if not os.path.exists('emoji'):
        os.mkdir('emoji')

    font = ImageFont.truetype('kimberley bl.ttf', 128)
    xwingfont = ImageFont.truetype('xwing-miniatures.ttf', 128)
    for stat, bits in stat_ranges.items():
        numbers, colour = bits
        for number in numbers:
            im = Image.new("RGBA", (300, 300), (255, 255, 255, 0))

            draw = ImageDraw.Draw(im)
            if number.endswith('`'):
                draw.text((0, 0), number[:-1], font=font, fill=colour)
                width = draw.textsize(number[:-1], font=font)[0]
                draw.text((width, 36), '`', font=xwingfont, fill=colour)
            else:
                draw.text((0, 0), number, font=font, fill=colour)

            # remove unneccessory whitespaces if needed
            im = im.crop(ImageOps.invert(im.convert('RGB')).getbbox())

            # im = ImageOps.invert(im)
            im.thumbnail(size, Image.ANTIALIAS)

            background = Image.new('RGBA', size, (255, 255, 255, 0))
            background.paste(
                im,
                ((size[0] - im.size[0]) // 2, (size[1] - im.size[1]) // 2))
            # background.paste(
            #     im.filter(ImageFilter.FIND_EDGES).convert('1'),
            #     ((size[0] - im.size[0]) // 2, (size[1] - im.size[1]) // 2))

            # write into file
            number = number.replace('±', '_')
            number = number.replace('-', 'minus')
            number = number.replace('+', 'plus')
            number = number.replace('`', 'recurring')
            background.save("emoji/{}.png".format('{}{}'.format(stat, number)))

if __name__ == '__main__':
    main()
