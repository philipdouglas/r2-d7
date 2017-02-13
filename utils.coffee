capitalize = require('capitalize')

exports.strip_name_say = (name) ->
    return name.replace(/\ \(.*\)$/, '')

exports.strip_name = (name) ->
    return exports.strip_name_say(name.toLowerCase()).replace(/[ -\/]/g, '')

exports.name_to_emoji = (name) ->
    name = ":#{exports.strip_name(name)}:"
    return name.replace(/:bomb:/g, ':xbomb:').replace(/:shield:/g, ':xshield:')

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

exports.unxws_faction = (xws) ->
    switch xws
        when 'scum' then return 'Scum and Villainy'
        when 'rebel' then return 'Rebel Alliance'
        when 'imperial' then return 'Galactic Empire'
        else false

exports.unxws_slot = (xws) ->
    switch xws
        when 'turret' then return 'Turret'
        when 'torpedo' then return 'Torpedo'
        when 'amd' then return 'Astromech'
        when 'ept' then return 'Elite'
        when 'missile' then return 'Missile'
        when 'crew' then return 'Crew'
        when 'cannon' then return 'Cannon'
        when 'bomb' then return 'Bomb'
        when 'system' then return 'System'
        when 'cargo' then return 'Cargo'
        when 'hardpoint' then return 'Hardpoint'
        when 'team' then return 'Team'
        when 'illicit' then return 'Illicit'
        when 'samd' then return 'Salvaged Astromech'
        when 'tech' then return 'Tech'
        when 'mod' then return 'Modification'
        when 'title' then return 'Title'
        else false

exports.wiki_link = (card_name, crew_of_pilot, wiki_name = false) ->
    if not wiki_name
        wiki_name = card_name
    fudged_name = capitalize.words(wiki_name)
        # YASB and the wiki use different name conventions
        .replace(/\ /g, '_')
        .replace(/\(Scum\)/, '(S&V)')
        .replace(/\((PS9|TFA)\)/, '(HOR)')
        .replace(/-Wing/, '-wing')
        .replace(/\/V/, '/v')
        .replace(/\/X/, '/x')
    if crew_of_pilot
        fudged_name += '_(Crew)'
    # Stupid Nien Nunb is a stupid special case
    else if fudged_name == 'Nien_Nunb'
        fudged_name += '_(T-70_X-Wing)'
    # All Hera's are suffixed on the wiki
    else if fudged_name == 'Hera_Syndulla'
        fudged_name += '_(VCX-100)'
    else if /"Heavy_Scyk"_Interceptor/.test(fudged_name)
        fudged_name = '"Heavy_Scyk"_Interceptor'
    url = "http://xwing-miniatures.wikia.com/wiki/#{fudged_name}"
    return exports.make_link(url, card_name)

exports.make_link = (url, name) ->
    name = name
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
    return "<#{url}|#{exports.strip_name_say(name)}>"
