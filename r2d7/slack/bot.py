"""
Stolen from https://github.com/BeepBoopHQ/starter-python-bot/

MIT Licensed
"""
import time
import logging
import traceback

from r2d7.slack.clients import SlackClients
from r2d7.slack.event_handler import RtmEventHandler

logger = logging.getLogger(__name__)


def spawn_bot():
    return SlackBot()


class SlackBot(object):
    def __init__(self, droid, token=None, debug=False):
        """Creates Slacker Web and RTM clients with API Bot User token.

        Args:
            token (str): Slack API Bot User token (for development token set in env)
        """
        super().__init__()
        self.last_ping = 0
        self.keep_running = True
        self.debug = debug
        if token is not None:
            self.clients = SlackClients(token)
        self.droid = droid

    def start(self, resource):
        """Creates Slack Web and RTM clients for the given Resource
        using the provided API tokens and configuration, then connects websocket
        and listens for RTM events.

        Args:
            resource (dict of Resource JSON): See message payloads - https://beepboophq.com/docs/article/resourcer-api
        """
        logger.debug('Starting bot for resource: {}'.format(resource))
        if 'resource' in resource and 'SlackBotAccessToken' in resource['resource']:
            res_access_token = resource['resource']['SlackBotAccessToken']
            self.clients = SlackClients(res_access_token)
        else:
            logger.debug("No resource or access token found.")

        self.droid.set_clients(self.clients)

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

            event_handler = RtmEventHandler(self.clients, self.droid, debug=self.debug)

            while self.keep_running:
                for event in self.clients.rtm.rtm_read():
                    try:
                        event_handler.handle(event)
                    except Exception:
                        logging.exception('Unexpected error:')
                        if self.debug:
                            err_msg = "I crashed, look at the log!"
                            self.droid.write_error(event['channel'], err_msg)
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

    def stop(self, resource):
        """Stop any polling loops on clients, clean up any resources,
        close connections if possible.

        Args:
            resource (dict of Resource JSON): See message payloads - https://beepboophq.com/docs/article/resourcer-api
        """
        self.keep_running = False
