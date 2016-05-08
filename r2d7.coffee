BotKit = require('botkit')
controller = BotKit.slackbot({debug: false})
bot = controller.spawn({token: process.env.SLACK_TOKEN})
bot.startRTM((err, bot, payload) ->
    if err
        throw new Error('Could not connect to slack!')
)

cards = require('./cards-common').basicCardData()
icon_map = {
    "Lambda-Class Shuttle":":lambda:",
    "Firespray-31":":firespray:",
    "A-Wing":":awing:",
    "TIE Advanced":":advanced:",
    "TIE Bomber":":bomber:",
    "B-Wing":":bwing:",
    "YT-1300":":falcon:",
    "TIE Fighter":":fighter:",
    "HWK-290":":hwk:",
    "TIE Interceptor":":interceptor:",
    "X-Wing":":xwing:",
    "Y-Wing":":ywing:",
}

# For some reason there's a > at the end of the message
controller.hears('geordanr\.github\.io\/xwing\/\?(.*)>$', ["ambient"], (bot, message) ->
    pieces = message.match[1].split('&amp;')
    serialized = pieces[1].split('=')[1]
    if not /v4!s!/.test(serialized)
        return bot.reply(message, "I don't understand URLs before v4.")

    serialized = serialized.slice(5)
    ships = serialized.split(';')
    console.log(message.match[1])
    switch decodeURI(pieces[0].split('=')[1])
        when 'Scum and Villainy' then faction = ':scum:'
        when 'Rebel Alliance' then faction = ':rebels:'
        when 'Galactic Empire' then faction = ':imperials:'
    output = ["*#{decodeURI(pieces[2].split('=')[1])}* #{faction}"]
    total_points = 0
    for ship in ships
        if not ship then continue
        points = 0
        ship = ship.split(':')
        pilot = cards.pilotsById[ship[0]]
        points += pilot.points
        upgrades = []

        add_upgrade = (upgrade) ->
            if upgrade is undefined
                return
            upgrades.push(upgrade.name)
            points += upgrade.points

        # Upgrade : Titles : Modifications : Extra Slots
        for upgrade_id in ship[1].split(',')
            upgrade_id = parseInt(upgrade_id)
            add_upgrade(cards.upgradesById[upgrade_id])
        for title_id in ship[2].split(',')
            title_id = parseInt(title_id)
            add_upgrade(cards.titlesById[title_id])
        for mod_id in ship[3].split(',')
            mod_id = parseInt(mod_id)
            add_upgrade(cards.modificationsById[mod_id])
        for extra in ship[4].split(',')
            extra = extra.split('.')
            extra_id = parseInt(extra[1])
            switch extra[0].toLowerCase()
                when 'u'
                    # Hacked support for Tie/X1
                    upgrade = cards.upgradesById[extra_id]
                    if upgrade.slot == 'System' and 'TIE/x1' in upgrades
                        points -= Math.min(4, upgrade.points)
                    add_upgrade(upgrade)
                when 't' then add_upgrade(cards.titlesById[extra_id])
                when 'm' then add_upgrade(cards.modificationsById[extra_id])

        icon = icon_map[pilot.ship] or "(#{pilot.ship})"

        output.push("#{pilot.name} #{icon}: #{upgrades.join(', ')} [#{points}]")
        total_points += points

    output[0] += " *[#{total_points}]*"
    return bot.reply(message, output.join('\n'))
)
