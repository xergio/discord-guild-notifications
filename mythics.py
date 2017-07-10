#! /usr/bin/python3

import redis
import time
import requests
import traceback
import datetime
from lxml import html
from lxml import etree
import webhook
import conf

now = time.time()

wh = webhook.Webhook(conf.url_discord_webhook)

r = redis.StrictRedis(host='localhost', charset="utf-8", decode_responses=True)

warcraft_api = "https://worldofwarcraft.com/es-es/game/pve/leaderboards/dun-modr/{}"

members = r.smembers("bot:members")
r.zremrangebyscore("bot:m+", "-inf", now-(60*60*24*7*2)) # 2 semanas

for zone, instance in conf.zones.items():
	try:
		page = requests.get(warcraft_api.format(zone))
		hp = etree.HTMLParser(encoding=page.encoding)
		tree = html.fromstring(page.content, parser=hp) # .decode(page.encoding)

		top = tree.xpath('//div[@class="Media-text"]/div[@class="font-semp-medium-white"]/text()')
		if len(top) < 3:
			print("no affix?")
			continue
			
		affix  = "" if top[0] not in conf.affixes else conf.affixes[top[0]]
		affix += "" if top[1] not in conf.affixes else conf.affixes[top[1]]
		affix += "" if top[2] not in conf.affixes else conf.affixes[top[2]]

		rows = tree.xpath('//div[@class="SortTable-body"]/div[@class="SortTable-row"]')
		#print("rows", len(rows))

		for row in rows:
			#print("tiempo", row.xpath('./div[5]/text()'))
			#print("row", html.tostring(row))
			pos = row.xpath('./div[1]/text()')[0]
			lvl = int(row.xpath('./div[2]/text()')[0])
			record = row.xpath('./div[3]/text()')[0]
			datee = row.xpath('./div[5]/text()')[0] #row.xpath('./div[5]/@data-value')[0]
			team = row.xpath('./div[4]/div/div[@class="List-item gutter-tiny"]')
			#print("row", pos, lvl, time, datee, len(team))

			k = "{0}.{1}.{2}.{3}".format(zone, lvl, record, datee)
			inguild = False
			party = []

			if lvl < 15 or r.zadd("bot:m+", now, k) == 0:
				continue

			for player in team:
				#print("player", html.tostring(player))
				name = player.xpath('.//div[@class="Character-name"]/text()')[0]
				url = str(player.xpath('./a/@href')[0])
				clss = str(player.xpath('./a/@class')[0])
				spec = ""
				for key in conf.class_icons.keys():
					if key in clss:
						spec = conf.class_icons[key]
				#party.append("{2}{0}{1}".format(name, "" if "dun-modr" in url else " *({})*".format(url.split("/")[6]), roles[len(party)]))
				party.append("{1}{0}".format(name if "dun-modr" in url else "*{}*".format(name), spec))

				for member in members:
					if "/{}".format(member).lower() in url and "dun-modr" in url:
						inguild = True
			
			if inguild:
				chests = 0
				for timer in conf.timers[zone]:
					delta = datetime.datetime.strptime(record, '%H:%M:%S') - datetime.datetime.strptime(timer, '%M:%S')
					if delta.total_seconds() > 0:
						break
					chests += 1
				if chests == 3:
					delta = datetime.datetime.strptime(timer, '%M:%S') - datetime.datetime.strptime(record, '%H:%M:%S')

				#tip = "(piedra +{0} por {1})".format(chests, delta)
				tip = "(piedra +{0})".format(chests, delta)
				msg = "{6} **[{0}](<{7}>) +{1}** hecha en **{2}** {3} por {4} / **rank {5}** de Dun Modr".format(instance, lvl, record, tip, " ".join(party), pos, affix, warcraft_api.format(zone))
				#r.rpush("bot:rss:new", msg)
				#print(msg)
				wh.send(msg)

	except:
		traceback.print_exc()
	time.sleep(1)
