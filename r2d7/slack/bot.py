"""
Stolen from https://github.com/BeepBoopHQ/starter-python-bot/

MIT Licensed
"""
import time
import logging
import threading
import traceback

from websocket._exceptions import WebSocketConnectionClosedException

from r2d7.core import UserError
from r2d7.slack.clients import SlackClients
from r2d7.slack.event_handler import RtmEventHandler

logger = logging.getLogger(__name__)


class Messager():
    def __init__(self, clients):
        self.clients = clients

    def send_message(self, channel_id, msg, thread=None):
        # in the case of Group and Private channels, RTM channel payload is a complex dictionary
        if isinstance(channel_id, dict):
            channel_id = channel_id['id']
        logger.debug('Sending msg: %s to channel: %s' % (msg, channel_id))
        self.clients.web.chat.post_message(
            channel_id, msg, as_user=True, unfurl_links=False, thread_ts=thread)

    def write_error(self, channel_id, err_msg):
        self.send_message(channel_id, ':alarm: ' + err_msg)


class SlackBot(threading.Thread):
    def __init__(self, droid, name=None, token=None, debug=False):
        """Creates Slacker Web and RTM clients with API Bot User token.

        Args:
            token (str): Slack API Bot User token (for development token set in env)
        """
        super().__init__()
        self.last_ping = 0
        self.keep_running = True
        self.debug = debug
        self.name = name
        if token is not None:
            self.clients = SlackClients(token)
        self.droid = droid

    def run(self):
        logger.info('Running bot for: {}'.format(self.name))

        if self.clients.rtm.rtm_connect():
            try:
                team_name = self.clients.rtm.server.login_data['team']['name']
                logging.info(u'Connected {} to {} team at https://{}.slack.com'.format(
                    self.clients.rtm.server.username,
                    team_name,
                    self.clients.rtm.server.domain))
            except TypeError:
                logger.error(
                    f"Failed to connect to {resource['resource']['SlackTeamName']}")
                return

            messager = Messager(self.clients)
            event_handler = RtmEventHandler(
                self.clients,
                self.droid,
                messager,
                debug=self.debug
            )

            while self.keep_running:
                try:
                    for event in self.clients.rtm.rtm_read():
                        try:
                            event_handler.handle(event)
                        except UserError as error:
                            logging.debug(
                                'User error generated', exc_info=True)
                            err_msg = f"Error: {error}"
                            messager.send_message(event['channel'], err_msg)
                            continue
                        except Exception:
                            logging.exception('Unexpected error:')
                            if self.debug:
                                err_msg = "I crashed, look at the log!"
                                messager.write_error(event['channel'], err_msg)
                            continue
                except WebSocketConnectionClosedException:
                    self.clients.rtm.rtm_connect()
                    continue

                self._auto_ping()
                time.sleep(.1)

        else:
            logger.error('Failed to connect to RTM client with token: {}'.format(self.clients.token))

    def _auto_ping(self):
        # hard code the interval to 3 seconds
        now = int(time.time())
        if now > self.last_ping + 3:
            self.clients.rtm.server.ping()
            self.last_ping = now

    def stop(self, timeout=False):
        """Stop any polling loops on clients, clean up any resources,
        close connections if possible.

        Args:
            resource (dict of Resource JSON): See message payloads - https://beepboophq.com/docs/article/resourcer-api
        """
        self.keep_running = False
