#! /usr/bin/python3

import datetime
import time
import webhook
import conf

wh = webhook.Webhook(conf.url_discord_webhook_news)

week = (int(datetime.datetime.now().strftime("%V")) % len(conf.affix_rotation)) - 1

f = []
for s in conf.affix_rotation[week]:
	f.append(webhook.field("{1} {0}".format(s, conf.affixes[s]), conf.affix_human[s], True))

wh.add_embed(webhook.embed(color=0x3f89ff, fields=f))
wh.send("**[Affixes de esta semana](<https://mythicpl.us/>)**")
time.sleep(2)
