#! /usr/bin/python3
"""
Affixes Cron
"""

import requests
import webhook
import conf

wh = webhook.Webhook(conf.url_discord_webhook_news)

rio_api = "https://raider.io/api/v1/mythic-plus/affixes?region=eu&locale=es"
api = requests.get(url=rio_api).json()

if api is not None and "affix_details" in api:
    fields = []

    for d in api["affix_details"]:
        name = d["name"]
        fields.append(webhook.field("{1} {0}".format(name, conf.affixes[name]), conf.affix_human[name], True))

    wh.add_embed(webhook.embed(color=0x3f89ff, fields=fields))
    wh.send("**[Affixes de esta semana](<https://mythicpl.us/>)**")
