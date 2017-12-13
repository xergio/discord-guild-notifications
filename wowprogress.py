#! /usr/bin/python3

import redis
import requests
import webhook
import conf

now = time.time()

wh = webhook.Webhook(conf.url_discord_webhook_guild)

r = redis.StrictRedis(host='localhost', charset="utf-8", decode_responses=True, db=1)

wp_api = "http://www.wowprogress.com/guild/eu/dun-modr/Mirrors/json_rank"

rank = requests.get(url=wp_api).json()

if rank is not None and "realm_rank" in rank:
    last = r.get("bot:wowprogress")
    realm = rank["realm_rank"]
    msg = None

    if last is None:
        msg = ":arrow_right: La guild entra en el ranking de Dun Modr: **{0}**".format(realm)

    elif int(last) > int(rank["realm_rank"]):
        msg = ":arrow_up: La guild sube en el ranking de Dun Modr: **{0}** (+{1})".format(realm, int(last)-int(realm))

    elif int(last) < int(realm):
        msg = ":arrow_down: La guild baja en el ranking de Dun Modr: **{0}** (-{1})".format(realm, int(realm)-int(last))

    elif int(last) == int(realm):
        msg = ":ok_hand: La guild se mantiene en el ranking de Dun Modr: **{0}**".format(realm)

    r.set("bot:wowprogress", realm)

    if msg:
        wh.send(msg)
