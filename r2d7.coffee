BotKit = require('botkit')
controller = BotKit.slackbot({debug: false})
bot = controller.spawn({token: process.env.SLACK_TOKEN})
bot.startRTM((err, bot, payload) ->
    if err
        throw new Error('Could not connect to slack!')
)

#Help
controller.hears('^help$', ["ambient", "direct_mention", "direct_message"], (bot, message) ->
    bot.reply(message, "I am R2-D7, xwingtmg.slack.com's bot.\n
        *List Printing:* If you paste a (Yet Another) X-Wing Miniatures Squad Builder permalink into
        a channel I'm in (or direct message me one), I will print a summary of the list.\n
        *Card Lookup:* Say something to me (_<@r2-d7>: something_) and I will describe any upgrades,
        ships or pilots that match what you said.\n
        You can also lookup a card by enlosing its name in double square brackets. (Eg. Why not try
        [[Engine Upgrade]])\n
        If you only want cards in a particular slot or ship, begin your lookup with the emoji for
        that ship or slot. (eg. _<@r2-d7>: :crew: rey_)\n
        You can also search for cards by points value in a particular slot. Eg. _<@r2-d7> :crew: <=3_.
        =, <, >, <= and >= are supported.
    ")
)

require('./xwing-shim')
exportObj = require('./cards-combined')
exportObj.cardLoaders.English()

ListPrinter = require('./listprinter')
listprinter_cb = new ListPrinter(exportObj).make_callback()
controller.hears(
    # http://geordanr.github.io/xwing/?f=Rebel%20Alliance&d=v4!s!162:-1,-1:-1:-1:&sn=Unnamed%20Squadron
    # slack wraps URLs in <>
    'geordanr\.github\.io\/xwing\/\?(.*)>',
    ["ambient", "direct_mention", "direct_message"],
    listprinter_cb
)

CardLookup = require('./cardlookup')
card_lookup_cb = new CardLookup(exportObj).make_callback()
controller.hears('(.*)', ['direct_message', 'direct_mention', 'mention'], card_lookup_cb)
controller.hears([
    '^[rR]2-[dD](7|test):? +(.*)$',  # Non @ mentions
    '\\[\\[(.*)\\]\\]',  # [[]] syntax
], ['ambient'], card_lookup_cb)
