url = require('url')
request = require('request')
Entities = require('html-entities').XmlEntities
entities = new Entities()
utils = require('./utils')
x1_link = utils.wiki_link('TIE/x1', false)


class XWSPrinter
    set_data: (data) ->
        @data = data

    print_xws: (list_url, list) ->
        if not list.name and 'yasb' of list.vendor
            decoded = entities.decode(list_url)
            parsed = url.parse(decoded, parseQueryString=true)
            list.name = parsed.query.sn
        list_url = utils.make_link(list_url, list.name or 'Nameless Squadron')
        output = [":#{list.faction}: *#{list_url}*"]
        total_points = 0
        pilots = @data.pilotsByFactionCanonicalName[utils.unxws_faction(list.faction)]
        for pilot in list.pilots
            points = 0
            if pilots[pilot.name].length > 1
                console.log(pilots[pilot.name])
            pilot_card = pilots[pilot.name][0]
            points += pilot_card.points
            skill = pilot_card.skill
            ship = if pilot.ship == 'sabinestiefighter' then 'tiefighter' else pilot.ship

            cards = []
            for slot, upgrades of pilot.upgrades
                for upgrade in upgrades
                    if slot == 'mod'
                        cards.push(@data.modificationsByCanonicalName[upgrade])
                    else if slot == 'title'
                        if upgrade == 'heavyscykinterceptor'
                            cards.push(@data.titlesByCanonicalName[upgrade][0])
                        else
                            cards.push(@data.titlesByCanonicalName[upgrade])
                    else
                        slot_cards = @data.upgradesBySlotCanonicalName[utils.unxws_slot(slot)]
                        cards.push(slot_cards[upgrade])

            upgrades = []
            for upgrade in cards
                if upgrade is undefined
                    upgrades.push("*Unrecognised Upgrade*")
                    return
                if upgrade.name == 'Veteran Instincts'
                    skill += 2
                if upgrade.slot.toLowerCase() == 'system' and x1_link in upgrades
                    points -= Math.min(4, upgrade.points)
                upgrade_link = utils.wiki_link(
                    upgrade.name,
                    upgrade.slot.toLowerCase() == 'crew' and upgrade.name of @data.pilots
                )
                if upgrade.name == 'Adaptability'
                    upgrade_link += ":skill_1:"
                upgrades.push(upgrade_link)
                points += upgrade.points

            output.push(
                ":#{ship}::skill#{skill}:" +
                " _#{utils.wiki_link(pilot_card.name)}_:" +
                " #{upgrades.join(', ')}" +
                " *[#{points}]*"
            )
            total_points += points

        output[0] += " *[#{total_points}]*"
        return output

    main: (bot, message) ->
        self = this
        if message.match[2] == 'geordanr'
            xws_url = "https://yasb-xws.herokuapp.com/?#{message.match[3]}"
        else if message.match[2] == 'xwing-builder'
            xws_url = "http://xwing-builder.co.uk/xws/#{message.match[3]}?dl=1"
        else if message.match[2]
            xws_url = "http://x-wing.fabpsb.net/permalink.php?sq=#{message.match[3]}&xws=1"
        else
            try
                xws = JSON.parse(message.match[1])
            catch e
                return

        if xws_url
            xws_url = entities.decode(xws_url)

            request({url: xws_url, json: true}, (error, response, body) ->
                if error || response.statusCode != 200 || 'message' of body
                    bot.reply(message, "Error retrieving XWS: #{body['message']}")
                    return

                bot.reply(message, {
                    text: self.print_xws(message.match[1], body).join('\n'),
                    # A fudge to get botkit to use postMessage which supports link formatting
                    attachments: [],
                    unfurl_links: false,
                })
            )
        else
            link = xws.vendor[Object.keys(xws.vendor)[0]].link
            bot.reply(message, {
                text: self.print_xws(link, xws).join('\n'),
                # A fudge to get botkit to use postMessage which supports link formatting
                attachments: [],
                unfurl_links: false,
            })

    make_callback: ->
        # Frigging Javascript
        self = this
        return (bot, message) ->
            self.main(bot, message)


module.exports = XWSPrinter
