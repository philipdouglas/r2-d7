utils = require('./utils')
Entities = require('html-entities').XmlEntities
entities = new Entities();

class ShipLister
    set_data: (data) ->
        @data = data

    faction_ships: (factions) ->
        ships = []
        for name, ship of @data.ships
            if ship.huge
                continue
            for faction in factions
                if faction in ship.factions
                    if ship not in ships
                        ships.push(ship)
        return (utils.name_to_emoji(ship.name) for ship in ships).join('')

    list: (search) ->
        match = /^ *(:[^:]+:) *$/.exec(search)
        if not match
            return

        factions = utils.emoji_to_faction(match[1].toLowerCase())
        if factions
            return @faction_ships(factions)

        return false

    main: (bot, message) ->
        incoming = entities.decode(message.match[1])
        # If the mention was mid line, we need to extract the search
        match = /<@U16V61GP6>(.*)/.exec(incoming)
        # Warning: This hard codes the id of r2-d7, so it will break on other slacks
        if match
            incoming = match[1]
        # Handle multiple [[]]s in one message
        output = false
        for search in incoming.split(/\]\][^\[]*\[\[/)
            listed = @list(search)
            if listed
                bot.reply(message, listed)
                output = true
        return output

    make_callback: ->
        # Frigging Javascript
        self = this
        return (bot, message) ->
            return self.main(bot, message)


module.exports = ShipLister
