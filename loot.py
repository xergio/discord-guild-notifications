#! /usr/bin/python3

import redis
import time
import json
import requests
import traceback
import os
import webhook
import conf

now = time.time()

wh = webhook.Webhook(conf.url_discord_webhook)

r = redis.StrictRedis(host='localhost', charset="utf-8", decode_responses=True)

bnet_member = "https://{1}.api.battle.net/wow/character/dun%20modr/{0}?fields=feed,items&locale=es_ES&apikey={2}"

# legends database
items = {}
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "items_legend.json"), 'r') as f:
	js = json.load(f)

	for item in js:
		items[item["item_id"]] = item


members = r.smembers("bot:members") # i need all guild members
request = requests.Session()

for m in members:
	try:
		member = request.get(url=bnet_member.format(m, conf.battle_net_region, conf.battle_net_apikey)).json()

		if "feed" not in member:
			continue
		
		for feed in member["feed"]:
			if feed["type"] != "LOOT":
				continue
			
			fid = "{}-{}".format(m, feed["itemId"])

			if feed["itemId"] in items and r.sadd("bot:legends", fid):
				#r.rpush("bot:rss:new", ":unicorn: **{0}** pilla legendario! **{1}**! <http://es.wowhead.com/item={2}>".format(member["name"], items[feed["itemId"]]["name_eses"], feed["itemId"]) )
				wh.send(":unicorn: **{0}** pilla legendario! **[{1}](<http://es.wowhead.com/item={2}>)**".format(member["name"], items[feed["itemId"]]["name_eses"], feed["itemId"]))

	except:
		traceback.print_exc()

"""
Vamos a generar el archivo items_legend.json
Sacar la lista de legends de aquí: view-source:http://es.wowhead.com/items/quality:5/slot:16:5:8:11:10:1:7:2:3:12:6:9?filter=166;7;0
Buscar: 'var _ = {};' y copiar toda la línea siguiente
Reemplazar: '_\[(\d+)\]=\{' por '\n{"item_id": \1, '
Reemplazar: ';$' por ','
Añadir los [ ... ]
"""
