import os

from PIL import Image, ImageFont, ImageDraw, ImageOps, ImageFilter

stat_ranges = {
    'skill': ([str(num) for num in range(0, 10)], '#CD6D2D'),
    'attack': (['-'] + [str(num) for num in range(0, 7)], '#EF232B'),
    'energy': ([str(num) for num in range(0, 17)], '#C7B5E2'),
    'agility': ([str(num) for num in range(0, 5)], '#6BBE44'),
    'hull': ([str(num) for num in range(0, 17)], '#B6B335'),
    'shield': ([str(num) for num in range(0, 17)], '#7ED3E5'),
}

size = (128, 128)

if not os.path.exists('numbers'):
    os.mkdir('numbers')

font = ImageFont.truetype('kimberley bl.ttf', 128)
for stat, bits in stat_ranges.items():
    numbers, colour = bits
    for number in numbers:
        im = Image.new("RGBA", (300, 300), (255, 255, 255, 0))

        draw = ImageDraw.Draw(im)
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
        background.save("numbers/{}.png".format('{}{}'.format(stat, number)))
