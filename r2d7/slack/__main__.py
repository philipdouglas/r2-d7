#!/usr/bin/env python
"""
Stolen from https://github.com/BeepBoopHQ/starter-python-bot/

MIT Licensed
"""
import logging
import os

import redis
import flask
from slackclient import SlackClient

from r2d7.slack.bot import SlackBot

from r2d7.listformatter import ListFormatter
from r2d7.cardlookup import CardLookup
from r2d7.wavelister import WaveLister
from r2d7.factionlister import FactionLister
from r2d7.slackdroid import SlackDroid

logger = logging.getLogger(__name__)


class Droid(
        SlackDroid,
        ListFormatter,
        WaveLister,
        CardLookup,
        FactionLister,
    ):
    pass


def main():
    debug = os.getenv('DEBUG', False)
    log_level = 'DEBUG' if debug else 'INFO'
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s: %(message)s',
        level=log_level
    )

    slack_token = os.getenv("SLACK_TOKEN", None)
    store = redis.from_url(os.environ["REDIS_URL"])
    logging.info("token: {}".format(slack_token))

    droid = Droid()
    if not slack_token:
        logging.info("SLACK_TOKEN env var not set, connecting to Redis")
        for teamname in store.keys():
            SlackBot(
                droid,
                name=teamname,
                token=store.get(teamname),
                debug=debug
            ).start()
    else:
        # Run a single instance of the bot in dev mode
        bot = SlackBot(droid, "test", slack_token, debug)
        bot.start()

    # Handle new installs
    if "SLACK_CLIENT_ID" not in os.environ:
        logger.info("No SLACK_CLIENT_ID env var found, not starting flask.")
        return
    client_id = os.environ["SLACK_CLIENT_ID"]
    client_secret = os.environ["SLACK_CLIENT_SECRET"]
    oauth_scope = "bot"

    app = flask.Flask(__name__)

    @app.route("/install", methods=["GET"])
    def install():
        url = f"https://slack.com/oauth/authorize?scope={oauth_scope}&client_id={client_id}"
        return flask.redirect(url, code=302)

    @app.route("/finish", methods=["GET", "POST"])
    def finish():
        # Retrieve the auth code from the request params
        auth_code = flask.request.args['code']

        # An empty string is a valid token for this request
        sc = SlackClient("")

        # Request the auth tokens from Slack
        auth_response = sc.api_call(
          "oauth.access",
          client_id=client_id,
          client_secret=client_secret,
          code=auth_code
        )
        team_name = auth_response["team_id"]
        bot_token = auth_response["bot"]["bot_access_token"]
        logger.info(f"New Team: {team_name}")
        logger.debug(auth_response)
        store.set(team_name, bot_token)

        SlackBot(
            droid,
            name=team_name,
            token=bot_token,
            debug=debug
        ).start()

        return "R2-D7 has been added! Follow the instructions <a href=\"https://github.com/FreakyDug/r2-d7\">here</a> to add the icons."

    app.run(host='0.0.0.0', port=80)

if __name__ == "__main__":
    main()
