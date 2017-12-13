#! /usr/bin/python3
"""
Raider.IO progress
"""

import redis
import requests
import webhook
import conf

# Every wednesday 9am
# 0 9 * * 3 timeout 58 /mnt/raid10/cron/raiderio.py >> /var/log/crons/raiderio.log 2>&1

wh = webhook.Webhook(conf.url_discord_webhook_guild)

r = redis.StrictRedis(host='localhost', charset="utf-8", decode_responses=True, db=1)

rio_api = "https://raider.io/api/v1/guilds/profile?region=eu&realm=dun%20modr&name=mirrors&fields=raid_progression%2Craid_rankings"
slug = "antorus-the-burning-throne"

api = requests.get(url=rio_api).json()

if api is not None and "raid_rankings" in api and "raid_progression" and slug in api["raid_rankings"]:
    prev_rank = r.get("bot:raiderio")

    rank = api["raid_rankings"][slug]["mythic"]["realm"]
    progress = api["raid_progression"][slug]["summary"]
    msg = None

    if prev_rank is None:
        msg = ":arrow_right: La guild entra en el ranking de Dun Modr: #**{0}**, {1}".format(rank, progress)

    elif int(prev_rank) > int(rank):
        msg = ":arrow_up: La guild sube en el ranking de Dun Modr: #**{0}** (+{1}), {2}".format(rank, int(prev_rank)-int(rank), progress)

    elif int(prev_rank) < int(rank):
        msg = ":arrow_down: La guild baja en el ranking de Dun Modr: #**{0}** (-{1}), {2}".format(rank, int(rank)-int(prev_rank), progress)

    elif int(prev_rank) == int(rank):
        msg = ":ok_hand: La guild se mantiene en el ranking de Dun Modr: #**{0}**, {1}".format(rank, progress)

    r.set("bot:raiderio", rank)

    if msg:
        msg += " - [Raider.IO](<https://raider.io/guilds/eu/dun-modr/Mirrors>) - [WoWProgress](<https://www.wowprogress.com/guild/eu/dun-modr/Mirrors>)"
        wh.send(msg)
