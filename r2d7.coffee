BotKit = require('botkit')
BeepBoop = require('beepboop-botkit')

controller = BotKit.slackbot({debug: false})
beepboop = BeepBoop.start(controller, {debug: false})


#Help
help_text = "I am R2-D7, xwingtmg.slack.com's bot.\n
    *List Printing:* If you paste a (Yet Another) X-Wing Miniatures Squad Builder permalink into
    a channel I'm in (or direct message me one), I will print a summary of the list.\n
    *Card Lookup:* Say something to me (_<@r2-d7>: something_) and I will describe any upgrades,
    ships or pilots that match what you said.\n
    You can also lookup a card by enclosing its name in double square brackets. (Eg. Why not try
    [[Engine Upgrade]])\n
    If you only want cards in a particular slot or ship, begin your lookup with the emoji for
    that ship or slot. (eg. _<@r2-d7>: :crew: rey_)\n
    You can also search for cards by points value in a particular slot. Eg. _<@r2-d7> :crew: <=3_.
    =, <, >, <= and >= are supported.
"
controller.hears('^help$', ["ambient", "direct_mention", "direct_message"], (bot, message) ->
    bot.reply(message, help_text))
controller.on('team_join', (bot, message) ->
    bot.api.im.open({user: message.user.id}, (err, response) ->
        if response.channel.id
            dm_channel = response.channel.id
            bot.say({channel: dm_channel, text: 'Welcome to xwingtmg.slack.com!'})
            bot.say({channel: dm_channel, text: help_text})
    )
)

require('./xwing-shim')
global['window'] = require('mock-browser').mocks.MockBrowser.createWindow()
global['$'] = require('jquery')
exportObj = require('./xwing')
exportObj.cardLoaders.English()

ListPrinter = require('./listprinter')
listprinter_cb = new ListPrinter(exportObj).make_callback()
controller.hears(
    # http://geordanr.github.io/xwing/?f=Rebel%20Alliance&d=v4!s!162:-1,-1:-1:-1:&sn=Unnamed%20Squadron
    # slack wraps URLs in <>
    '<(https?://geordanr\.github\.io\/xwing\/\?(.*))>',
    ["ambient", "direct_mention", "direct_message"],
    listprinter_cb
)

CardLookup = require('./cardlookup')
card_lookup_cb = new CardLookup(exportObj).make_callback()
ShipLister = require('./shiplister')
ship_lister_cb = new ShipLister(exportObj).make_callback()

multi_callback = (bot, message) ->
    if not ship_lister_cb(bot, message)
        card_lookup_cb(bot, message)

controller.hears('(.*)', ['direct_message', 'direct_mention', 'mention'], multi_callback)
controller.hears([
    '^[rR]2-[dD](?:7|test):? +(.*)$',  # Non @ mentions
    '\\[\\[(.*)\\]\\]',  # [[]] syntax
], ['ambient'], multi_callback)
