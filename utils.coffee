exports.strip_name = (name) ->
    return name.toLowerCase().replace(/\ \(.*\)$/, '').replace(/[ -\/]/g, '')

exports.name_to_emoji = (name) ->
    name = ":#{exports.strip_name(name)}:"
    return name.replace(/:bomb:/g, ':xbomb:')

exports.ship_to_icon = (pilot) ->
    return exports.name_to_emoji(pilot.ship)

exports.faction_to_emoji = (faction) ->
    switch faction
        when 'Scum and Villainy' then return ':scum:'
        when 'Rebel Alliance' then return ':rebel:'
        when 'Galactic Empire' then return ':empire:'
        when 'Resistance' then return ':resistance:'
        when 'First Order' then return ':first_order:'

exports.emoji_to_faction = (emoji) ->
    switch emoji
        when ':scum:' then return ['Scum and Villainy']
        when ':rebel:' then return ['Rebel Alliance', 'Resistance']
        when ':empire:' then return ['Galactic Empire', 'First Order']
        when ':resistance:' then return ['Resistance']
        when ':first_order:' then return ['First Order']
        else false
