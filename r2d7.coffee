BotKit = require('botkit')
BeepBoop = require('beepboop-botkit')

controller = BotKit.slackbot({debug: false})
beepboop = BeepBoop.start(controller, {debug: false})


#Help
help_text = "I am R2-D7, xwingtmg.slack.com's bot.\n
    *List Printing:* If you paste a (Yet Another) Squad Builder, Fab's or
    xwing-builder.co.uk permalink into a channel I'm in (or direct
    message me one), I will print a summary of the list.\n
    *Card Lookup:* Say something to me (_<@r2-d7>: something_) and I will describe any upgrades,
    ships or pilots that match what you said.\n
    You can also lookup a card by enclosing its name in double square brackets. (Eg. Why not try
    [[Engine Upgrade]])\n
    If you only want cards in a particular slot or ship, begin your lookup with the emoji for
    that ship or slot. (eg. _<@r2-d7>: :crew: rey_)\n
    You can also search for cards by points value in a particular slot. Eg. _<@r2-d7> :crew: <=3_.
    =, <, >, <= and >= are supported.
"
controller.hears(['^help$'], ["direct_mention", "direct_message"], (bot, message) ->
    bot.reply(message, help_text))
controller.on('team_join', (bot, message) ->
    bot.api.im.open({user: message.user.id}, (err, response) ->
        if response.channel.id
            dm_channel = response.channel.id
            bot.say({channel: dm_channel, text: 'Welcome to xwingtmg.slack.com!'})
            bot.say({channel: dm_channel, text: help_text})
    )
)

# Set up handler classes
XWSPrinter = require('./xwslistprinter')
xws_printer = new XWSPrinter()
CardLookup = require('./cardlookup')
card_lookup = new CardLookup()
ShipLister = require('./shiplister')
ship_lister = new ShipLister()
card_lookup_cb = card_lookup.make_callback()
ship_lister_cb = ship_lister.make_callback()

multi_callback = (bot, message) ->
    if not ship_lister_cb(bot, message)
        card_lookup_cb(bot, message)

controller.hears(
    # slack wraps URLs in <>
    [
        '<(https?://(geordanr)\\.github\\.io/xwing/\\?(.*))>',
        '<(https?://(xwing-builder)\\.co\\.uk/view/(\\d+)[^>|]*)[>|]',
        '<(https?://x-wing\\.(fabpsb)\\.net/permalink\\.php\\?sq=([a-z0-9]+))>',
        '({.*})',
    ]
    ["ambient", "direct_mention", "direct_message"],
    xws_printer.make_callback()
)

controller.hears('(.*)', ['direct_message', 'direct_mention', 'mention'], multi_callback)
controller.hears([
    '^[rR]2-[dD](?:7|test):? +(.*)$',  # Non @ mentions
    '\\[\\[(.*)\\]\\]',  # [[]] syntax
], ['ambient'], multi_callback)

# Fake the environment xwing.js expects
require('./xwing-shim')
global['window'] = require('mock-browser').mocks.MockBrowser.createWindow()
global['$'] = require('jquery')

# Set up the download from github
fs = require('fs')
process = require('process')
request = require('request')
reload = require('require-reload')(require)
yasb_hash = null
yasb_url = 'https://raw.githubusercontent.com/geordanr/xwing/gh-pages/javascripts/xwing.js'
download_yasb = () ->
    request.get(yasb_url).on('response', (response) ->
        yasb_hash = response.headers['etag']
        console.log("New YASB hash: #{yasb_hash}")
    ).pipe(fs.createWriteStream('xwing.js')).on('finish', () ->
        try
            exportObj = reload('./xwing')
        catch error
            console.error('Failed to reload xwing.js')
            process.exit()
        exportObj.cardLoaders.English()
        xws_printer.set_data(exportObj)
        card_lookup.set_data(exportObj)
        ship_lister.set_data(exportObj)
    )
download_yasb()

ticks = 0
controller.on('tick', (bot, event) ->
    ticks += 1
    if ticks % 600 != 0
        return
    if yasb_hash is null
        return
    request.head(yasb_url).on('response', (response) ->
        if yasb_hash != response.headers['etag']
            console.log("New xwing.js detected.")
            download_yasb()
    )
)
