import re

from r2d7.core import BotCore


class SlackPrinter(BotCore):
    @staticmethod
    def name_to_icon(name):
        if name in ['bomb', 'shield']:
            name = 'x' + name
        return f":{name.lower()}:"

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
        return text
