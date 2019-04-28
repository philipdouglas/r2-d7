from multiprocessing import Process

from r2d7.slack.__main__ import main as slack_main
from r2d7.discord.__main__ import main as discord_main


def main():
    slack = Process(target=slack_main)
    slack.start()
    discord = Process(target=discord_main)
    discord.start()

    slack.join()
    discord.join()

if __name__ == "__main__":
    main()
