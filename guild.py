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

bnet_guild = conf.battle_net_url("https://{0}.api.battle.net/wow/guild/dun%20modr/vagrant%20story?fields=news,members,achievements&locale=es_ES&apikey={1}")

g = requests.get(url=bnet_guild).json()


if "members" not in g:
	print("'members' not in g")
	sys.exit()

members = r.smembers("bot:members") # members database, used by other scripts
chars = set()

# how join the guild, how leaves

for member in g["members"]:
	chars.add(member["character"]["name"])

for new in chars.difference(members):
	r.sadd("bot:members", new)
	members.add(new)
	wh.send(":inbox_tray: **{0}** ha entrado a la guild! 🎉".format(new))

for kick in members.difference(chars):
	r.srem("bot:members", kick)
	wh.send(":outbox_tray: **{0}** ha salido a la guild :confused:".format(kick))


if "news" not in g:
	print("'news' not in g")
	sys.exit()

g["news"].reverse()
r.zremrangebyscore("bot:guild", "-inf", now-(60*60*24*2))

for news in g["news"]:
	fid = None
	push = None

	if news["timestamp"]/1000 < now-(60*60*24): # oooold, check 1 day only
		continue

	if news["type"] in ["playerAchievement", "guildAchievement"]:
		fid = "{} {} {}".format(news["type"], news["character"], news["achievement"]["title"])
		push =  ":medal: **{0}** gana el logro **{1}**!".format(news["character"], news["achievement"]["title"])

	if fid is None or r.zadd("bot:guild", now, fid) == 0 or push is None:
		continue

	wh.send(push)
	
	time.sleep(2) # prevent rate limit, for example with boss FK
