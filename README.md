# first of all

Take in mind that the first execution of each script will cause a bit of spam on your server.

More info (in spanish) [here](https://sergio.am/post/discord-webhooks-guild-notifications.html).

# configuration

You should rename and edit the `tokens-sample.py` file to `tokens.py`, and you can edit the `conf.py` file. `tokens` file contains tokens (ofc) and api keys for services. `conf` file contains a mix of icons and strings.

To get your Discord Webhook URL go [here](https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks)

To get your Battle.net API Key go [here](https://dev.battle.net/)

# dependencies

* python3
* redis-server
* redis-py

# crontab

```*/15 * * * * timeout 890 /path/guild.py >> /path/log/guild.log 2>&1
*/15 * * * * timeout 890 /path/mythics.py >> /path/log/mythics.log 2>&1
*/30 * * * * timeout 1790 /path/loot.py >> /path/log/loot.log 2>&1
* * * * * timeout 58 /path/rss.py >> /path/log/rss.log 2>&1
* * * * * timeout 58 /path/streams.py >> /path/log/streams.log 2>&1
* * * * * timeout 58 /path/warcraftlogs.py >> /path/cron/log/warcraftlogs.log 2>&1
0 9 * * 3 timeout 60 /path/wowprogress.py >> /path/cron/log/wowprogress.log 2>&1
0 8 * * 3 timeout 60 /path/affixes.py >> /path/log/affixes.log 2>&1
```

# credits

- Readme writted with [stackedit](https://stackedit.io/editor).
- Coded with [Sublime Text 3](https://www.sublimetext.com/3).
- Scripts running under [Gigabyte Brix](https://www.gigabyte.com/Mini-PcBarebone/GB-BXi3-5010-rev-10#ov) + [Ubuntu](https://www.ubuntu.com/).
- Originally did it for [Vagrant Story](https://vagrantstory.eu/) (EU-Dun Modr) guild.
