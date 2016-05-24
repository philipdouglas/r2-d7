exportObj = require('./cards-combined')
exportObj.cardLoaders.English()

BotKit = require('botkit')
controller = BotKit.slackbot({debug: false})
bot = controller.spawn({token: process.env.SLACK_TOKEN})
bot.startRTM((err, bot, payload) ->
    if err
        throw new Error('Could not connect to slack!')
)

name_to_emoji = (name) ->
    return name.toLowerCase().replace(/\ \(.*\)$/, '').replace(/[ -\/]/g, '')

ship_to_icon = (pilot) ->
    return ":#{name_to_emoji(pilot.ship)}:"

faction_to_emoji = (faction) ->
    switch faction
        when 'Scum and Villainy' then return ':scum:'
        when 'Rebel Alliance' then return ':rebel:'
        when 'Galactic Empire' then return ':empire:'
        when 'Galactic Empire' then return ':empire:'
        when 'Resistance' then return ':resistance:'
        when 'First Order' then return ':first_order:'


#http://geordanr.github.io/xwing/?f=Rebel%20Alliance&d=v4!s!162:-1,-1:-1:-1:&sn=Unnamed%20Squadron

# For some reason there's a > at the end of the message
controller.hears('geordanr\.github\.io\/xwing\/\?(.*)>', ["ambient", "direct_mention", "direct_message"], (bot, message) ->
    url = require('url')
    Entities = require('html-entities').XmlEntities
    entities = new Entities();
    parsed = url.parse(entities.decode(message.match[1]), parseQueryString=true)
    data = parsed.query.d

    for data_chunk in data.split('!')
        if /^\d/.test(data_chunk)
            ships = data_chunk.split(';')
    faction = faction_to_emoji(parsed.query.f)
    output = ["*#{parsed.query.sn or 'Nameless Squadron'}* #{faction}"]
    total_points = 0
    for ship in ships
        if not ship then continue
        points = 0
        ship = ship.split(':')
        pilot = exportObj.pilotsById[ship[0]]
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
            add_upgrade(exportObj.upgradesById[upgrade_id])
        for title_id in ship[2].split(',')
            title_id = parseInt(title_id)
            add_upgrade(exportObj.titlesById[title_id])
        for mod_id in ship[3].split(',')
            mod_id = parseInt(mod_id)
            add_upgrade(exportObj.modificationsById[mod_id])
        for extra in ship[4].split(',')
            extra = extra.split('.')
            extra_id = parseInt(extra[1])
            switch extra[0].toLowerCase()
                when 'u'
                    # Hacked support for Tie/X1
                    upgrade = exportObj.upgradesById[extra_id]
                    if upgrade and upgrade.slot == 'System' and 'TIE/x1' in upgrades
                        points -= Math.min(4, upgrade.points)
                    add_upgrade(upgrade)
                when 't' then add_upgrade(exportObj.titlesById[extra_id])
                when 'm' then add_upgrade(exportObj.modificationsById[extra_id])

        output.push("_#{pilot.name}_ #{ship_to_icon(pilot)}: #{upgrades.join(', ')} *[#{points}]*")
        total_points += points

    output[0] += " *[#{total_points}]*"
    return bot.reply(message, output.join('\n'))
)

fixIcons = (data) ->
    if data.text?
        data.text = data.text
            .replace(/<i class="xwing-miniatures-font xwing-miniatures-font-/g, ':')
            .replace(/"><\/i>/g, ':')
            .replace(/:bomb:/g, ':xbomb:')  # bomb is already an emoji
            .replace(/<br \/><br \/>/g, '\n')
            .replace(/<strong>/g, '*')
            .replace(/<\/strong>/g, '*')
            .replace(/<em>/g, '')
            .replace(/<\/em>/g, '')
            .replace(/<span class="card-restriction">/g, '_')
            .replace(/<\/span>/g, '_')

strip_name = (name) ->
    return name.toLowerCase().replace(/[-]/g, ' ').replace(/\ \(.*\)$/, '').replace(/[^a-z0-9]/g, '')
strip_name_say = (name) ->
    return name.replace(/\ \(.*\)$/, '')

# Build a lookup object
card_lookup = {}
add_card_name = (name, data) ->
    card_lookup[name] = card_lookup[name] || []
    card_lookup[name].push(data)
add_card = (data) ->
    name = strip_name(data.name)
    add_card_name(name, data)
for upgrade_name, upgrade of exportObj.upgrades
    fixIcons(upgrade)
    add_card(upgrade)
for modification_name, modification of exportObj.modifications
    modification.slot = 'Modification'
    fixIcons(modification)
    add_card(modification)
for title_name, title of exportObj.titles
    title.slot = 'Title'
    fixIcons(title)
    add_card(title)
for pilot_name, pilot of exportObj.pilots
    pilot.slot = 'Pilot'
    fixIcons(pilot)
    add_card(pilot)

alias_map = {
    'fcs': 'fire control system',
    'apl': 'anti pursuit lasers',
    'atc': 'advanced targeting computer',
    'ptl': 'push the limit',
    'hlc': 'heavy laser cannon',
    'tlt': 'twin laser turret',
    'vi': 'veteran instincts',
    'at': 'autothrusters',
    'as': 'advanced sensors',
    'acd': 'advanced cloaking device',
    'eu': 'engine upgrade',
}

# Card Lookup
card_lookup_cb = (bot, message) ->
    lookup = strip_name(message.match[1])
    matches = []
    if lookup.length > 2
        matches = matches.concat(Object.keys(card_lookup).filter((key) ->
            return ///#{lookup}///.test(key))
        )
    if alias_map[lookup] and alias_map[lookup] not in matches
        matches.push(alias_map[lookup])

    if matches.length < 1
        return
    text = []
    for match in matches
        for card in card_lookup[match]
            unique = if card.unique then ':unique:' else ' '
            slot = if card.slot == 'Pilot' then ship_to_icon(card) else ":#{name_to_emoji(card.slot)}:"
            if card.name == 'Emperor Palpatine'
                slot += ":crew:"
            text.push("#{slot}#{unique}*#{strip_name_say(card.name)}* [#{card.points}]")
            if card.limited
                text.push("_Limited._")
            if card.skill  # skill field is (hopefully) unique to pilots
                ship = exportObj.ships[card.ship]
                line = ["#{faction_to_emoji(card.faction)} #{card.ship}"]

                stats = ":skill#{card.skill}:"
                if ship.attack
                    stats += ":attack#{ship.attack}:"
                if ship.energy
                    stats += ":energy#{ship.energy}:"
                stats += ":agility#{ship.agility}::hull#{ship.hull}::shield#{ship.shields}:"
                line.push(stats)
                if ship.attack_icon
                    line.push(":#{ship.attack_icon.replace(/xwing-miniatures-font-/, '')}:")

                line.push((":#{name_to_emoji(action)}:" for action in ship.actions).join(' '))
                if card.slots.length > 0
                    slots = (":#{name_to_emoji(slot)}:" for slot in card.slots).join('')
                    slots = slots.replace(/:bomb:/g, ':xbomb:')
                    line.push(slots)
                text.push(line.join(' | '))
            text.push(card.text)
    return bot.reply(message, text.join('\n'))

controller.hears('(.*)', ['direct_message', 'direct_mention'], card_lookup_cb)
# Handle non-@ mentions
controller.hears('^[rR]2-[dD]7: +(.*)$', ['ambient'], card_lookup_cb)
