# R2-D7
A bot for xwingtmg.slack.com.

## Features
- Detects links to lists from <http://geordanr.github.io/xwing/>, <http://xwing-builder.co.uk/build> and <http://x-wing.fabpsb.net> and print them in chat
- Card lookup via [[]] queries

Adding the bot to new Slack workspaces is currently broken. I plan to fix it soon.

To add the icons:
- Download the latest emoji.zip from https://github.com/FreakyDug/r2-d7/releases
- Install https://chrome.google.com/webstore/detail/slack-emoji-tools/anchoacphlfbdomdlomnbbfhcmcdmjej
- Go to your slack's add emoji page
- Then drag all the files in the emoji folder into Bulk section. (You'll need to do it in a couple of goes, there's a 100 file limit)

Written in Python. (Requires version 3.6 or later)

Uses card data from <a href="https://github.com/guidokessels/xwing-data">guidokessels/xwing-data</a>.
