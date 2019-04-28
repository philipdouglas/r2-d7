import pathlib
import json

import generate_emoji


def main():
    generate_emoji.main()

    emojidir = pathlib.Path('emoji')
    outdir = pathlib.Path('discord_emoji')
    outdir.mkdir(exist_ok=True)

    existing_emoji = {}
    try:
        with open('discord_emoji.json', 'r') as tracker_file:
            existing_emoji = json.load(tracker_file)
    except FileNotFoundError:
        pass

    last_server, last_number = 1, 1
    for server, number in existing_emoji.values():
        if server > last_server:
            last_server, last_number = server, number
        elif server == last_server and number > last_number:
            last_number = number

    for emoji in emojidir.rglob('*.png'):
        if emoji.stem in existing_emoji:
            server = existing_emoji[emoji.stem][0]
        else:
            if last_number < 50:
                server = last_server
                last_number += 1
            else:
                last_server += 1
                server = last_server
                last_number = 1
            existing_emoji[emoji.stem] = [server, last_number]

        dest = outdir / f"r2d7_emoji{server:02d}"
        dest.mkdir(exist_ok=True)
        (dest / emoji.name).write_bytes(emoji.read_bytes())

    with open('discord_emoji.json', 'w') as tracker_file:
        json.dump(existing_emoji, tracker_file)



if __name__ == '__main__':
    main()
