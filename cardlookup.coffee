utils = require('./utils')
Entities = require('html-entities').XmlEntities
entities = new Entities();

class CardLookup
    alias_map: {
        'fcs': 'firecontrolsystem',
        'apl': 'antipursuitlasers',
        'atc': 'advancedtargetingcomputer',
        'ptl': 'pushthelimit',
        'hlc': 'heavylasercannon',
        'tlt': 'twinlaserturret',
        'vi': 'veteraninstincts',
        'at': 'autothrusters',
        'as': 'advancedsensors',
        'acd': 'advancedcloakingdevice',
        'eu': 'engineupgrade',
        'tap': 'tieadvancedprototype',
        'ac': 'accuracycorrector',
        'abt': 'autoblasterturret',
        'sd': 'stealthdevice',
        'ei': 'experimentalinterface',
        'k4': 'k4securitydroid',
        'stressbot': 'r3a2',
        'countesskturn': 'countessryad',
        'countesskturns': 'countessryad',
        'countessgreenkturn': 'countessryad',
        'bmst': 'blackmarketslicertools',
    }

    constructor: (data) ->
        @data = data
        @card_lookup = {}
        for condition_name, condition of @data.conditions
            condition.slot = 'Condition'
            @fix_icons(condition)
            @add_card(condition)
        for upgrade_name, upgrade of @data.upgrades
            @fix_icons(upgrade)
            @add_card(upgrade)
        for modification_name, modification of @data.modifications
            modification.slot = 'Modification'
            @fix_icons(modification)
            @add_card(modification)
        for title_name, title of @data.titles
            # Purge 2 of the Heavy Scyk copies
            if /\"Heavy Scyk\" Interceptor \((Torpedo|Missile)\)/.exec(title_name)
                continue
            title.slot = 'Title'
            @fix_icons(title)
            @add_card(title)
        for pilot_name, pilot of @data.pilots
            pilot.ship_card = @data.ships[pilot.ship]
            if pilot.ship_override
                pilot.ship_card = Object.assign({}, pilot.ship_card)
                pilot.ship_card = Object.assign(pilot.ship_card, pilot.ship_override)
            pilot.slot = pilot.ship_card.name
            @fix_icons(pilot)
            @add_card(pilot)
        for ship_name, ship of @data.ships
            ship.slot = ship.name
            @add_card(ship)

    add_card_name: (name, data) ->
        @card_lookup[name] = @card_lookup[name] || []
        @card_lookup[name].push(data)

    add_card: (card) ->
        name = @strip_card_name(card.name)
        card.slot = utils.strip_name(card.slot)
        @add_card_name(name, card)

    fix_icons: (data) ->
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
                .replace(/__/g, ' ')  # When italics are next to each, slack gets confused
                .replace(/&deg;/g, '°')

    strip_card_name: (name) ->
        return name.toLowerCase().replace(/\ \(.*\)$/, '').replace(/[^a-z0-9]/g, '')

    strip_name_say: (name) ->
        return name.replace(/\ \(.*\)$/, '')

    build_ship_stats: (ship, pilot) ->
        line = []
        if pilot
            ship.factions = [pilot.faction]
        line.push((utils.faction_to_emoji(faction) for faction in ship.factions).join(''))

        stats = ''
        if pilot
            stats += ":skill#{pilot.skill}:"
        if ship.attack
            stats += ":attack#{ship.attack}:"
        if ship.energy
            stats += ":energy#{ship.energy}:"
        stats += ":agility#{ship.agility}::hull#{ship.hull}::shield#{ship.shields}:"
        line.push(stats)

        if ship.attack_icon
            line.push(":#{ship.attack_icon.replace(/xwing-miniatures-font-/, '')}:")

        line.push((utils.name_to_emoji(action) for action in ship.actions).join(' '))
        if pilot and pilot.slots.length > 0
            slots = (utils.name_to_emoji(slot) for slot in pilot.slots).join('')
            line.push(slots)

        if ship.epic_points
            line.push(":epic:#{ship.epic_points}")

        return line.join(' | ')

    make_points_filter: (operator, filter) ->
        filter = parseInt(filter)
        return (value) ->
            if value is undefined
                return false
            switch operator
                when '=', '==' then return value == filter
                when '>' then return value > filter
                when '<' then return value < filter
                when '>=' then return value >= filter
                when '<=' then return value <= filter

    print_card: (card) ->
        text = []
        unique = if card.unique then ':unique:' else ' '
        slot = utils.name_to_emoji(card.slot)
        if card.name == 'Emperor Palpatine'
            slot += ":crew:"
        points = if card.points is undefined then '' else "[#{card.points}]"
        text.push("#{slot}#{unique}*#{@strip_name_say(card.name)}* #{points}")

        if card.ship_card
            text.push(@build_ship_stats(card.ship_card, card))

        else if card.maneuvers  # Ship
            text.push(@build_ship_stats(card))
            for line in @build_maneuver(card)
                text.push(line)

        else if card.attack or card.energy  # secondary weapon and energy stuff
            line = []
            if card.attack
                line.push(":attack::attack#{card.attack}:")
            if card.range
                line.push("Range: #{card.range}")
            if card.energy
                line.push(":energy::energy#{card.energy}:")
            text.push(line.join(' | '))

        if card.limited
            text.push("_Limited._")

        if card.text
            text.push(card.text)

        return text

    main: (bot, message) ->
        incoming = entities.decode(message.match[1])
        # If the mention was mid line, we need to extract the search
        match = /<@U16V61GP6>(.*)/.exec(incoming)
        # Warning: This hard codes the id of r2-d7, so it will break on other slacks
        if match
            incoming = match[1]
        pattern = /(?::([^:]+):)? *(?:([^=><].+)|([=><][=><]?) *(\d+))/
        match = pattern.exec(incoming)
        slot_filter = match[1]
        if slot_filter
            slot_filter = slot_filter.toLowerCase()
        if slot_filter == 'xbomb'
            slot_filter = 'bomb'

        if match[2]
            # Handle multiple [[]]s in one message
            lookups = (@strip_card_name(lookup) for lookup in incoming.split(/\]\][^\[]*\[\[/))
            matches = []
            for lookup in lookups
                if lookup.length > 2 or /r\d/.exec(lookup)
                    matches = matches.concat(Object.keys(@card_lookup).filter((key) ->
                        return ///#{lookup}///.test(key))
                    )
                if @alias_map[lookup] and @alias_map[lookup] not in matches
                    matches.push(@alias_map[lookup])
                    points_filter = undefined
        else
            if not slot_filter
                return bot.reply(message,
                    "You need to specify a slot to search by points value.")
            matches = Object.keys(@card_lookup)
            points_filter = @make_points_filter(match[3], match[4])

        if matches.length < 1
            return
        cards = []
        for match in matches
            for card in @card_lookup[match]
                if slot_filter and card.slot != slot_filter
                    continue
                if points_filter and not points_filter(card.points)
                    continue

                # CoffeeScript doesn't play nicely with the ES6 Set
                if card not in cards
                    cards.push(card)

                if card.applies_condition
                    condition = @data.conditionsByCanonicalName[card.applies_condition]
                    if condition not in cards
                        cards.push(condition)

        text = []
        for card in cards
            text = text.concat(@print_card(card))

        return bot.reply(message, text.join('\n'))

    make_callback: ->
        self = this
        return (bot, message) ->
            return self.main(bot, message)

    difficulties: {
        0: 'blank',
        1: '', # Default black icons are white for our purposes
        2: 'green',
        3: 'red',
    }

    bearings: {
        0: 'turnleft',
        1: 'bankleft',
        2: 'straight',
        3: 'bankright',
        4: 'turnright',
        5: 'kturn',
        6: 'sloopleft',
        7: 'sloopright',
        8: 'trollleft',
        9: 'trollright',
    }

    build_maneuver: (ship) ->
        if ship.maneuvers is undefined or ship.maneuvers.length == 0
            return []
        # check for blank columns
        cols = []
        for bearing in [0..(ship.maneuvers[0].length - 1)]
            empty = true
            for distance in [(ship.maneuvers.length - 1)..0]
                if ship.maneuvers[distance][bearing]
                    empty = false
            if not empty
                cols.push(bearing)

        lines = []
        for distance in [(ship.maneuvers.length - 1)..0]
            line = ["#{distance} "]
            no_bearings = true
            for bearing in cols
                difficulty = ship.maneuvers[distance][bearing]
                if difficulty == 0
                    line.push(':blank:')
                else
                    no_bearings = false
                    bearing = if distance == 0 then 'stop' else @bearings[bearing]
                    line.push(":#{@difficulties[difficulty]}#{bearing}:")
            if not no_bearings
                lines.push(line.join(''))
        return lines

module.exports = CardLookup
