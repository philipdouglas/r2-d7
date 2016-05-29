BotKit = require('botkit')
controller = BotKit.slackbot({debug: false})
bot = controller.spawn({token: process.env.SLACK_TOKEN})
bot.startRTM((err, bot, payload) ->
    if err
        throw new Error('Could not connect to slack!')
)

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
controller.hears('(.*)', ['direct_message', 'direct_mention'], card_lookup_cb)
# Handle non-@ mentions
controller.hears('^[rR]2-[dD]7: +(.*)$', ['ambient'], card_lookup_cb)
