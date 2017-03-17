clone = require('clone')
Entities = require('html-entities').XmlEntities
entities = new Entities()
fs = require('fs')
utils = require('./utils')

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
        'snuggling': 'smugglingcompartment',
        'snugglingcompartment': 'smugglingcompartment',
    }

    set_data: (data) ->
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
            title.slot = 'Title'
            @fix_icons(title)
            # Purge 2 of the Heavy Scyk copies
            if /\"Heavy Scyk\" Interceptor \((Torpedo|Missile)\)/.exec(title_name)
                continue
            @add_card(title)
        for ship_name, ship of @data.ships
            ship.slot = ship.name
            ship.pilots = []
            @add_card(ship)
        for pilot_name, pilot of @data.pilots
            pilot.ship_card = @data.ships[pilot.ship]

            # Add pilot to it's ship so we can list pilots for ships
            pilot.ship_card.pilots.push(pilot)

            if pilot.ship_override
                pilot.ship_card = Object.assign({}, pilot.ship_card)
                pilot.ship_card = Object.assign(pilot.ship_card, pilot.ship_override)
            pilot.slot = pilot.ship_card.name
            @fix_icons(pilot)
            @add_card(pilot)

        # Add damage cards
        @add_damage_cards(
            JSON.parse(fs.readFileSync('./damage-deck-core.json')), 'Original')
        @add_damage_cards(
            JSON.parse(fs.readFileSync('./damage-deck-core-tfa.json')), 'TFA')

    add_card_name: (name, data) ->
        @card_lookup[name] = @card_lookup[name] || []
        @card_lookup[name].push(data)

    add_card: (card) ->
        name = @strip_card_name(card.name)
        card.slot = utils.strip_name(card.slot)
        @add_card_name(name, card)

    add_damage_cards: (cards, deck) ->
        for card in cards
            card.slot = 'crit'
            card.deck = deck
            @fix_icons(card)
            @add_card(card)

    fix_icons: (data) ->
        if data.text?
            data.text = data.text
                .replace(/<i class="xwing-miniatures-font xwing-miniatures-font-/g, ':')
                .replace(/"><\/i>/g, ':')
                .replace(/:bomb:/g, ':xbomb:')  # bomb is already an emoji
                .replace(/:shield:/g, ':xshield:')  # shield is already an emoji as well
                .replace(/<br \/><br \/>/g, '\n')
                .replace(/<strong>/g, '*')
                .replace(/<\/strong>/g, '*')
                .replace(/<em>/g, '')
                .replace(/<\/em>/g, '')
                .replace(/<span class="card-restriction">/g, '_')
                .replace(/<\/span>/g, '_')
                .replace(/__/g, ' ')  # When italics are next to each, slack gets confused
                .replace(/&deg;/g, '°')
                # Guido's data syntax
                .replace(/\[Hit\]/g, ':hit:')
                .replace(/\[Critical Hit\]/g, ':crit:')
                .replace(/\[Turn Left\]/g, ':turnleft:')
                .replace(/\[Turn Right\]/g, ':turnright:')
                .replace(/\[Straight\]/g, ':straight:')

    strip_card_name: (name) ->
        return name.toLowerCase().replace(/\ \(.*\)$/, '').replace(/[^a-z0-9]/g, '')

    energy_to_emoji: (energy) ->
        return ":energy#{String(energy).replace(/\+/g, 'plus')}:"

    build_ship_stats: (ship, pilot) ->
        line = []
        if pilot
            line.push(utils.faction_to_emoji(pilot.faction))

        stats = ''
        if pilot
            stats += ":skill#{pilot.skill}:"
        if ship.attack
            stats += ":attack#{ship.attack}:"
        if ship.energy
            stats += @energy_to_emoji(ship.energy)
        stats += ":agility#{ship.agility}::hull#{ship.hull}::shield#{ship.shields}:"
        line.push(stats)

        if ship.attack_icon
            line.push(":#{ship.attack_icon.replace(/xwing-miniatures-font-/, '')}:")

        line.push((utils.name_to_emoji(action) for action in ship.actions).join(' '))
        if pilot
            slots = pilot.slots
        else
            slots = ship.pilots.sort(@pilot_compare)[0].slots
        if slots
            slots = (utils.name_to_emoji(slot) for slot in slots).join('')
            line.push(slots)

        if ship.epic_points
            line.push(":epic:#{ship.epic_points}")

        return line.join(' | ')

    pilot_compare: (a, b) ->
        if b.skill > a.skill
            return -1
        else if a.skill > b.skill
            return 1
        else
            return 0

    short_pilot: (pilot) ->
        unique = if pilot.unique then '• ' else ''
        elite = if "Elite" in pilot.slots then ' :elite:' else ''
        return ":skill#{pilot.skill}:#{unique}#{@format_name(pilot)}#{elite}"

    list_pilots: (ship) ->
        factions = {}
        pilots = ship.pilots.sort(@pilot_compare)
        for pilot in ship.pilots
            if pilot.faction not of factions
                factions[pilot.faction] = []
            factions[pilot.faction].push(@short_pilot(pilot))
        return ("#{utils.faction_to_emoji(faction)} #{pilots.join(', ')}" for faction, pilots of factions)

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

    format_name: (card) ->
        if card.actions or card.slot == 'crit'
            return card.name
        return utils.wiki_link(
            card.name,
            card.slot.toLowerCase() == 'crew' and card.name of @data.pilots
        )

    print_card: (card) ->
        text = []
        unique = if card.unique then ' • ' else ' '
        slot = utils.name_to_emoji(card.slot)
        for extra_slot in (card.also_occupies_upgrades or [])
            if extra_slot not in (card.unequips_upgrades or [])
                slot += utils.name_to_emoji(extra_slot)
        points = if card.points is undefined then '' else "[#{card.points}]"
        deck = if card.deck then "(#{card.deck})" else ''
        text.push("#{slot}#{unique}*#{@format_name(card)}* #{points}#{deck}")

        if card.ship_card
            text.push(@build_ship_stats(card.ship_card, card))

        else if card.pilots  # Ship
            text.push(@build_ship_stats(card))
            Array::push.apply(text, @build_maneuver(card))
            Array::push.apply(text, @list_pilots(card))

        else if card.attack or card.energy  # secondary weapon and energy stuff
            line = []
            if card.attack
                line.push(":attack::attack#{card.attack}:")
            if card.range
                line.push("Range: #{card.range}")
            if card.energy
                line.push(":energy:#{@energy_to_emoji(card.energy)}")
            text.push(line.join(' | '))

        if card.limited and not /Limited/.test(card.text)
            if /^\_/.exec(card.text)
                card.text = card.text.replace(/^(_[^_]+)(_.*)/, '$1 Limited.$2')
            else
                text.push("_Limited._")

        if card.type  # Damage card
            text.push("_*#{card.type}*_")

        if card.text
            text.push(card.text)

        return text

    lookup: (term) ->
        matches = []
        pattern = /\ *(?::([^:]+):)? *(?:([^=><:]*[^=><: ][^=><:]*)|([=><][=><]?) *(\d+)) *(?::([^:]+):)? */
        match = pattern.exec(term)
        slot_filter = match[1] or match[5]
        if slot_filter
            slot_filter = slot_filter.toLowerCase()
        if slot_filter == 'xbomb'
            slot_filter = 'bomb'

        if match[2]
            lookup = @strip_card_name(match[2])
            if lookup.length > 2 or /[a-z]\d/.exec(lookup)
                self = this
                regex = ///\b#{lookup}(?:'s)?\b///
                matches = matches.concat(Object.keys(@card_lookup).filter((key) ->
                    for card in self.card_lookup[key]
                        return regex.test(card.name.toLowerCase()))
                )
                if matches.length == 0
                    regex = ///#{lookup}///
                    matches = matches.concat(Object.keys(@card_lookup).filter((key) ->
                        return regex.test(key))
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

        cards = []
        for match in matches
            for card in @card_lookup[match]
                if slot_filter and card.slot != slot_filter
                    continue
                if points_filter and not points_filter(card.points)
                    continue

                cards.push(card)

                if card.applies_condition
                    condition = @data.conditionsByCanonicalName[card.applies_condition]
                    cards.push(condition)
        return cards

    main: (bot, message) ->
        incoming = entities.decode(message.match[1])
        cards = []
        # Handle multiple [[]]s in one message
        for lookup in incoming.split(/\]\][^\[]*\[\[/)
            for card in @lookup(lookup)
                # CoffeeScript doesn't play nicely with the ES6 Set
                if card not in cards
                    cards.push(card)

        if cards.length > 10
            bot.reply(message, 'Your search matched more than 10 cards, please be more specific.')
            return

        text = []
        for card in cards
            text = text.concat(@print_card(card))

        if text
            bot.reply(message, {
                text: text.join('\n'),
                # A fudge to get botkit to use postMessage which supports link formatting
                attachments: [],
                unfurl_links: false,
            })

    make_callback: ->
        self = this
        return (bot, message) ->
            self.main(bot, message)

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
        10: 'reversebankleft',
        11: 'reversestraight',
        12: 'reversebankright',
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
