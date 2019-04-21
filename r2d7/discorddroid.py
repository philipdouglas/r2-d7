from r2d7.slackdroid import SlackDroid


class DiscordDroid(SlackDroid):
    """
    Discord is similar enough to Slack that we subclass that and then modify.
    """

    @staticmethod
    def bold(text):
        return f"**{text}**"

    @staticmethod
    def italics(text):
        return f"*{text}*"

    @staticmethod
    def link(url, name):
        """
        Discord doesn't allow inline links.
        """
        return f"[{name}]({url})"
