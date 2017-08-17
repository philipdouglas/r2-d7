import re

from r2d7.core import BotCore


class SlackPrinter(BotCore):
    @staticmethod
    def iconify(name, hypens=False):
        name = name.lower()
        if hypens:
            name = re.sub(r'[^a-zA-Z0-9\-]', '', name)
        else:
            name = re.sub(r'[^a-zA-Z0-9]', '', name)
        name = name.replace('+', 'plus')
        if name in ['bomb', 'shield']:
            name = 'x' + name
        elif name == 'rebelalliance':
            name = 'rebel'
        elif name == 'scumandvillainy':
            name = 'scum'
        elif name == 'galacticempire':
            name = 'empire'
        return f":{name}:"

    @staticmethod
    def bold(text):
        return f"*{text}*"

    @staticmethod
    def italics(text):
        return f"_{text}_"

    @staticmethod
    def convert_html(text):
        """
        The data has HTML formatting tags, convert them to slack formatting.
        """
        text = re.sub(r'<\/?strong>', '*', text)
        text = re.sub(r'(<br \/>)+', '\n', text)
        text = re.sub(r'\[Koiogran Turn\]', ':kturn:', text)
        text = re.sub(r'\[([^\]]+)\]', ':\\1:', text)
        return text
