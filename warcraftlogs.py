#! /usr/bin/python3

import redis
import time
import requests
import webhook
import conf

now = time.time()

wh = webhook.Webhook(conf.url_discord_webhook)

r = redis.StrictRedis(host='localhost', charset="utf-8", decode_responses=True)
r.zremrangebyscore("bot:warcraftlogs", "-inf", now-(60*60*24*30*12)) # 12 meses

wl_api = "https://www.warcraftlogs.com/v1/reports/guild/vagrant%20story/dun-modr/eu?api_key={0}".format(conf.warcraftlogs_token)

wl = requests.get(url=wl_api).json()

for report in wl:
	if report["start"]/1000 < now-(60*60*24*7): # oooold, 7 day only
		continue

	if not r.zadd("bot:warcraftlogs", now, report["id"]):
		continue

	url = "https://www.warcraftlogs.com/reports/{0}".format(report["id"])
	#r.rpush("bot:rss:new", "<:Warcraftlogs:283906655484379138> Log en vivo! **{2}** por **{0}** en <{1}>".format(report["owner"], url, report["title"]))
	wh.send("{3} Logs! **[{2}](<{1}>)** por **{0}**".format(report["owner"], url, report["title"], conf.icon_warcraftlogs))
