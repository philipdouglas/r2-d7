"""
Stolen from https://github.com/BeepBoopHQ/starter-python-bot/

MIT Licensed
"""
import json
import logging
import re

logger = logging.getLogger(__name__)


class RtmEventHandler(object):
    def __init__(self, slack_clients, droid, messager, debug):
        self.clients = slack_clients
        self.droid = droid
        self.messager = messager
        self.debug = debug

    def handle(self, event):

        if 'type' in event:
            self._handle_by_type(event['type'], event)

    def _handle_by_type(self, event_type, event):
        # See https://api.slack.com/rtm for a full list of events
        if event_type == 'error':
            # error
            self.messager.write_error(event['channel'], json.dumps(event))
        elif event_type == 'message':
            # message was sent to channel
            self._handle_message(event)
        elif event_type == 'channel_joined':
            # you joined a channel
            self.messager.write_help_message(event['channel'])
        elif event_type == 'group_joined':
            # you joined a private group
            self.messager.write_help_message(event['channel'])
        else:
            pass

    def _handle_message(self, event):
        # Filter out messages from the bot itself, and from non-users (eg. webhooks)
        if ('user' in event) and (not self.clients.is_message_from_me(event['user'])):
            msg_txt = event['text']

            # Check for new data
            if self.droid.needs_update():
                self.droid.load_data()

            # Direct responses
            response = []
            if self.clients.is_bot_mention(msg_txt) or self._is_direct_message(event['channel']):
                droid_id = self.clients.rtm.server.login_data['self']['id']
                msg_txt = re.sub(f"<@{droid_id}>", '', msg_txt)
                if self.debug and msg_txt == '!crash':
                    raise Exception('Crashy crash!')
                if 'help' in msg_txt:
                    self.message.write_help_message(event['channel'])
                else:
                    for regex, handle_method in self.droid._dm_handlers.items():
                        match = regex.search(msg_txt)
                        if match:
                            response += handle_method(match[1])

            # Don't handle if the dm_handlers have already got it
            if not response:
                # Watches
                for regex, handle_method in self.droid._handlers.items():
                    match = regex.search(msg_txt)
                    if match:
                        response += handle_method(match[1])

            if response:
                self.messager.send_message(event['channel'], '\n'.join(response))

    def _is_direct_message(self, channel):
        """Check if channel is a direct message channel

        Args:
            channel (str): Channel in which a message was received
        """
        return channel.startswith('D')
