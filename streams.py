#! /usr/bin/python3

import redis
import time
import requests
import sys
import webhook
import conf

now = time.time()

wh = webhook.Webhook(conf.url_discord_webhook)

r = redis.StrictRedis(host='localhost', charset="utf-8", decode_responses=True)

twitch_api = "https://api.twitch.tv/kraken/streams/followed?oauth_token={0}".format(conf.twitch_token)

r.zremrangebyscore("bot:twitch", "-inf", now-(60*15))

t = requests.get(url=twitch_api).json()

if "streams" not in t:
	print(t)
	sys.exit()

for stream in t["streams"]:
	if r.zadd("bot:twitch", now, stream["channel"]["name"]) == 0:
		continue

	#r.rpush("bot:rss:new", ":projector: **{0}** está stremeando <{1}>".format(stream["channel"]["name"], stream["channel"]["url"]))
	wh.send("{3} **{0}** está stremeando! **[{2}](<{1}>)**".format(stream["channel"]["name"], stream["channel"]["url"], stream["channel"]["status"], conf.icon_twitch))
