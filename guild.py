#! /usr/bin/python3

import redis
import time
import requests
import sys
import webhook
import conf

now = time.time()

wh = webhook.Webhook(conf.url_discord_webhook_guild)

r = redis.StrictRedis(host='localhost', charset="utf-8", decode_responses=True, db=1)

bnet_achs = conf.battle_net_url("https://{0}.api.battle.net/wow/data/guild/achievements?locale=es_ES&apikey={1}")

bnet_guild = conf.battle_net_url("https://{0}.api.battle.net/wow/guild/dun%20modr/farm%20and%20furious?fields=news,members,achievements&locale=es_ES&apikey={1}")

a = requests.get(url=bnet_achs).json()
g = requests.get(url=bnet_guild).json()



if "members" not in g:
	print("'members' not in g")
	sys.exit()

members = r.smembers("bot:members") # members database, used by other scripts
chars = set()

# who join the guild, who leaves

for member in g["members"]:
	chars.add(member["character"]["name"])

for new in chars.difference(members):
	r.sadd("bot:members", new)
	members.add(new)
	wh.send(":inbox_tray: **{0}** ha entrado a la guild! 🎉".format(new))
	time.sleep(2)

for kick in members.difference(chars):
	r.srem("bot:members", kick)
	wh.send(":outbox_tray: **{0}** ha salido a la guild :confused:".format(kick))
	time.sleep(2)



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



if "achievements" not in g:
	print("'achievements' not in g")
	sys.exit()

def ach_to_list(data):
	ret = []

	for d in data:
		if "categories" in d:
			ret.extend(ach_to_list(d["categories"]))

		elif "achievements" in d:
			ret.extend(ach_to_list(d["achievements"]))

		else:
			ret.append(d)

	return ret

a = ach_to_list(a["achievements"])

achievements = [int(x) for x in r.smembers("bot:guild-ach")]

for new in set(g["achievements"]["achievementsCompleted"]).difference(achievements):
	r.sadd("bot:guild-ach", new)

	ach = next((item for item in a if item["id"] == new), None)
	if not ach or "title" not in ach:
		continue

	title = ach["title"]
	desc = ach["description"]
	url = "http://es.wowhead.com/achievement={0}".format(new)
	icon = "https://wow.zamimg.com/images/wow/icons/large/{0}.jpg".format(ach["icon"])

	wh.clear_embeds()
	wh.add_embed(webhook.embed(title=ach["title"], url="http://es.wowhead.com/achievement={0}".format(new), description=ach["description"], thumbnail=webhook.image(icon)))
	wh.send(":clap: La guild ha ganado un logro!")

	time.sleep(2)
