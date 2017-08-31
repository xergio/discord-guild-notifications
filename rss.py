#! /usr/bin/python3

import feedparser
import redis
import time
import traceback
import webhook
import conf

now = time.time()

wh = webhook.Webhook(conf.url_discord_webhook_news)

r = redis.StrictRedis(host='localhost', charset="utf-8", decode_responses=True, db=1)
r.zremrangebyscore("bot:rss", "-inf", now-(60*60*24*30*3)) # 3 meses de caché

url_feeds = [
	"http://www.wowhead.com/news&rss", 
	"http://www.mmo-champion.com/external.php?do=rss&type=newcontent&sectionid=1&days=120&count=5"
]

for url in url_feeds:
	try:
		feed = feedparser.parse(url)

		if "items" not in feed or len(feed["items"]) < 3:
			continue

		for i in [0, 1, 2]: # 3 últimas noticias
			entry = feed["items"][i]
			fid = "{} {}".format(feed["feed"]["title"][0:20], entry["published"])
			if r.zadd("bot:rss", now, fid) == 0:
				continue

			if "wowhead.com/" in entry["link"]:
				icon = conf.icon_wowhead
			elif "mmo-champion.com/" in entry["link"]:
				icon = conf.icon_mmoc
			else:
				icon = ":newspaper2:"

			wh.send("{2} [{0}](<{1}>)".format(entry["title"], entry["link"], icon))
			time.sleep(2)

	except:
		print(url)
		traceback.print_exc()
