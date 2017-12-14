#! /usr/bin/python3
"""
Streams Cron
"""

import time
import sys
import redis
import requests
import webhook
import conf

now = time.time()

wh = webhook.Webhook(conf.url_discord_webhook_news)

r = redis.StrictRedis(host='localhost', charset="utf-8", decode_responses=True, db=1)

twitch_api = "https://api.twitch.tv/kraken/streams/followed?oauth_token={0}".format(conf.twitch_token)

r.zremrangebyscore("bot:twitch", "-inf", now-(60*15))

t = requests.get(url=twitch_api).json()

if "streams" not in t:
    print(t)
    sys.exit()

for stream in t["streams"]:
    if r.zadd("bot:twitch", now, stream["channel"]["name"]) == 0:
        continue

    game = stream["channel"]["game"] if "game" in stream["channel"] else "ahora"

    wh.send("{3} **{0}** está stremeando {4}: [{2}](<{1}>)".format(stream["channel"]["name"], stream["channel"]["url"], stream["channel"]["status"], conf.icon_twitch, game))
    time.sleep(2)
