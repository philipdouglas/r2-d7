url = require('url')
Entities = require('html-entities').XmlEntities
entities = new Entities();

utils = require('./utils')

class ListPrinter
    constructor: (data) ->
        @data = data

    make_callback: ->
        # Frigging Javascript
        self = this
        return (bot, message) ->
            parsed = url.parse(entities.decode(message.match[1]), parseQueryString=true)
            data = parsed.query.d

            for data_chunk in data.split('!')
                if /^\d/.test(data_chunk)
                    ships = data_chunk.split(';')
            faction = utils.faction_to_emoji(parsed.query.f)
            output = ["*#{parsed.query.sn or 'Nameless Squadron'}* #{faction}"]
            total_points = 0
            for ship in ships
                if not ship then continue
                points = 0
                ship = ship.split(':')
                pilot = self.data.pilotsById[ship[0]]
                if pilot is undefined
                    output.push(":question: *_Unrecognised Ship ID_*")
                    continue
                points += pilot.points
                upgrades = []

                add_upgrade = (cards, card_id) ->
                    if card_id == -1 or card_id == ''
                        return
                    upgrade = cards[card_id]
                    if upgrade is undefined
                        upgrades.push("*Unrecognised Upgrade*")
                        return
                    upgrades.push(upgrade.name)
                    points += upgrade.points

                # Upgrade : Titles : Modifications : Extra Slots
                for upgrade_id in ship[1].split(',')
                    upgrade_id = parseInt(upgrade_id)
                    add_upgrade(self.data.upgradesById, upgrade_id)
                for title_id in ship[2].split(',')
                    title_id = parseInt(title_id)
                    add_upgrade(self.data.titlesById, title_id)
                for mod_id in ship[3].split(',')
                    mod_id = parseInt(mod_id)
                    add_upgrade(self.data.modificationsById, mod_id)
                for extra in ship[4].split(',')
                    extra = extra.split('.')
                    extra_id = parseInt(extra[1])
                    switch extra[0].toLowerCase()
                        when 'u'
                            # Hacked support for Tie/X1
                            upgrade = self.data.upgradesById[extra_id]
                            if upgrade and upgrade.slot == 'System' and 'TIE/x1' in upgrades
                                points -= Math.min(4, upgrade.points)
                            add_upgrade(self.data.upgradesById, extra_id)
                        when 't' then add_upgrade(self.data.titlesById, extra_id)
                        when 'm' then add_upgrade(self.data.modificationsById, extra_id)

                output.push("#{utils.ship_to_icon(pilot)} _#{pilot.name}_: #{upgrades.join(', ')} *[#{points}]*")
                total_points += points

            output[0] += " *[#{total_points}]*"
            return bot.reply(message, output.join('\n'))

module.exports = ListPrinter
