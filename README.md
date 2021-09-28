# R2-D7
A bot for xwingtmg.slack.com.

Support Slack and Discord!

<a href="https://slack.com/oauth/authorize?client_id=22172116449.94722582676&scope=bot"><img alt="Add to Slack" height="40" width="139" src="https://platform.slack-edge.com/img/add_to_slack.png" srcset="https://platform.slack-edge.com/img/add_to_slack.png 1x, https://platform.slack-edge.com/img/add_to_slack@2x.png 2x" /></a>

<a href="https://discordapp.com/oauth2/authorize?client_id=569554290331353088&permissions=2048&scope=bot">Add to Discord</a>

## Features
- Detects links to lists from <http://geordanr.github.io/xwing/>, <http://xwing-builder.co.uk/build> and <http://x-wing.fabpsb.net> and print them in chat
- Card lookup via [[]] queries
- Card image lookup via {{}} queries
- Basic dice rolls with stats from http://gateofstorms.net/2/multi/

To add the icons:
- Download the latest emoji.zip from https://github.com/FreakyDug/r2-d7/releases
- Install https://chrome.google.com/webstore/detail/slack-emoji-tools/anchoacphlfbdomdlomnbbfhcmcdmjej
- Go to your slack's add emoji page
- Then drag all the files in the emoji folder into Bulk section. (You'll need to do it in a couple of goes, there's a 100 file limit)

Written in Python. (Requires version 3.6 or later)

Uses card data from <a href="https://github.com/guidokessels/xwing-data">guidokessels/xwing-data</a>.

# Required Permissions
## Slack
- View information about a user’s identity,
- Add the ability for people to direct message or mention @r2-d7
- Add shortcuts and/or slash commands that people can use

## Discord
- Text channel permissions:
  - Send messages
  - Manage messages (optional, enables prompt to delete a bot trigger message)

# Running locally
## Setup
Set up a virtual env and install requirements. Standard python stuff, but
easy to forget so it's written here for convenience.
```
mkdir env               # only needed 1st time
python3 -m venv env     # only needed 1st time
source env/bin/activate
pip3 install -r requirements.txt
```

## Run
First, create or obtain a slack (or discord) token (see slack API documentation).
Then set your token as an environment variable and launch r2d7:
```
export SLACK_TOKEN="123456-your-slack-token-here"
python -m r2d7.slack
```
Or for discord:
```
export DISCORD_TOKEN="123456-your-discord-token-here"
python -m r2d7.discord
```

