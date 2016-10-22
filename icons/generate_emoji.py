import pathlib

import fontdump
import maneuvers
import stat_icons

def main():
    fontdump.main()
    maneuvers.main()
    stat_icons.main()

    manual = pathlib.Path('manual')
    emojidir = pathlib.Path('emoji')

    for emoji in manual.rglob('*.png'):
        with (emojidir / emoji.name).open('wb') as to_file:
            with emoji.open('rb') as from_file:
                to_file.write(from_file.read())

if __name__ == '__main__':
    main()
