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
    }

    constructor: (data) ->
        @data = data
        @card_lookup = {}
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
            @add_card(title)
        for pilot_name, pilot of @data.pilots
            pilot.slot = 'Pilot'
            @fix_icons(pilot)
            @add_card(pilot)
        for ship_name, ship of @data.ships
            ship.slot = ship.name
            @add_card(ship)

    add_card_name: (name, data) ->
        @card_lookup[name] = @card_lookup[name] || []
        @card_lookup[name].push(data)

    add_card: (data) ->
        name = @strip_name(data.name)
        @add_card_name(name, data)

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

    strip_name: (name) ->
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

    make_callback: ->
        # Frigging Javascript
        self = this
        return (bot, message) ->
            lookup = self.strip_name(message.match[1])
            matches = []
            if lookup.length > 2
                matches = matches.concat(Object.keys(self.card_lookup).filter((key) ->
                    return ///#{lookup}///.test(key))
                )
            if self.alias_map[lookup] and self.alias_map[lookup] not in matches
                matches.push(self.alias_map[lookup])

            if matches.length < 1
                return
            text = []
            for match in matches
                for card in self.card_lookup[match]
                    unique = if card.unique then ':unique:' else ' '
                    slot = if card.slot == 'Pilot' then utils.ship_to_icon(card) else utils.name_to_emoji(card.slot)
                    if card.name == 'Emperor Palpatine'
                        slot += ":crew:"
                    points = if card.points is undefined then '' else "[#{card.points}]"
                    text.push("#{slot}#{unique}*#{self.strip_name_say(card.name)}* #{points}")

                    if card.skill  # skill field is (hopefully) unique to pilots
                        text.push(self.build_ship_stats(self.data.ships[card.ship], card))

                    else if card.maneuvers  # Ship
                        text.push(self.build_ship_stats(card))
                        for line in self.build_maneuver(card)
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
            return bot.reply(message, text.join('\n'))

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
        # check for blank columns
        cols = []
        for bearing in [0..(ship.maneuvers[0].length - 1)]
            empty = true
            for distance in [(ship.maneuvers.length - 1)..0]
                if ship.maneuvers[distance][bearing]
                    empty = false
            if not empty
                cols.push(bearing)
        console.log(cols)

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
