# R2-D7
A bot for xwingtmg.slack.com.

Support Slack and Discord!

<a href="https://slack.com/oauth/authorize?client_id=22172116449.94722582676&scope=bot"><img alt="Add to Slack" height="40" width="139" src="https://platform.slack-edge.com/img/add_to_slack.png" srcset="https://platform.slack-edge.com/img/add_to_slack.png 1x, https://platform.slack-edge.com/img/add_to_slack@2x.png 2x" /></a>

<a href="https://discordapp.com/oauth2/authorize?client_id=569554290331353088&permissions=309237967936&scope=bot">Add to Discord</a>

# Features
## Detects links to lists 
-  <http://raithos.github.io/> and <https://launchbaynext.app/> and prints the lists in chat
- Just paste the list URL into chat, and let the bot handle it! (on Windows, you can press F6 then CTRL+C, and paste into chat)
## Card lookup via [[]] queries
  - [[:t65xwing:luke]] will trigger a response with Luke Skywalker's pilot details
  - [[luke]] will trigger a response letting you choose between the Pilot and the Gunner cards.
  - [[marksmanship]] will trigger a response with the Marksmanship card's details
  - [[fang]] will show the Fang Fighter ship chassis information (stats, maneuvers, ship ability), and list the pilots that exist for that ship.
  - Try looking up [[hellothere]] or [[squid]] ;)
## Card Image Lookup via {{}} queries
## Basic dice rolls with stats from http://gateofstorms.net/2/multi/

To add the icons:
- Download the latest emoji.zip from https://github.com/FreakyDug/r2-d7/releases
- Install https://chrome.google.com/webstore/detail/slack-emoji-tools/anchoacphlfbdomdlomnbbfhcmcdmjej
- Go to your slack's add emoji page
- Then drag all the files in the emoji folder into Bulk section. (You'll need to do it in a couple of goes, there's a 100 file limit)

Written in Python. (Requires version 3.6 or later)

Uses card data from <a href="https://github.com/guidokessels/xwing-data2">guidokessels/xwing-data2</a>.

# Required Permissions
## Slack
- View information about a user’s identity,
- Add the ability for people to direct message or mention @r2-d7
- Add shortcuts and/or slash commands that people can use

## Discord
- Text channel permissions:
  - View Channels
  - Send Messages
  - Access Public Threads (future-proofing for potential new features)
  - Send Messages in Threads (future-proofing for potential new features)
  - Manage Messages (enables prompt to delete a user's data query message)
  - Embed Links
  - Attach Files
  - Use External Emojis
  - Add Reactions

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

