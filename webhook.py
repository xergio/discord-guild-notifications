
# https://github.com/Derpolino/discord-webhooks-python/blob/master/discordWebhooks.py

import requests
import json
import time

now = time.time()

# https://discordapp.com/developers/docs/resources/webhook#execute-webhook
class Webhook():

	def __init__(self, url, **kwargs):
		self.url = url
		self.wh = {
			#"username": kwargs.get("username", None),
			#"avatar_url": kwargs.get("avatar_url", None),
			"content": None,
			"embeds": []
		}

		self.requests = requests.Session()

	def add_embed(self, embed):
		self.wh["embeds"].append(embed)

	def clear_embeds(self):
		self.wh["embeds"] = []

	def send(self, content=None, tts=False):
		self.wh["content"] = content
		self.wh["tts"] = tts
		#print(self.wh)
		#return True # BORRAR ESTO
		r = self.requests.post(self.url, json=self.wh)

		if "X-RateLimit-Remaining" in r.headers and int(r.headers["X-RateLimit-Remaining"]) <= 1:
			wait = int(r.headers["X-RateLimit-Reset"])-int(now)
			raise Exception("RateLimit {0}/{1}, reset in ~{2}s".format(r.headers["X-RateLimit-Remaining"], r.headers["X-RateLimit-Limit"], wait))

			"""rl = "RateLimit {0}/{1}, reset in ~{2}s".format(r.headers["X-RateLimit-Remaining"], r.headers["X-RateLimit-Limit"], wait)
			if wait < 600:
				print(rl)
				time.sleep(wait+1)
			else:
				raise Exception(rl)"""

		if r.text != "":
			raise Exception("Webhook error: {0}".format(r.text))
		return True


# https://discordapp.com/developers/docs/resources/channel#embed-object
def embed(**kwargs):
	return {
		"title": kwargs.get("title", None),
		"description": kwargs.get("description", None),
		"url": kwargs.get("url", None),
		"color": kwargs.get("color", None),
		"image": kwargs.get("image", None),
		"thumbnail": kwargs.get("thumbnail", None),
		"footer": kwargs.get("footer", None),
		"fields": kwargs.get("fields", [])
	}


def field(name, value, inline=False):
	return {
		"name": name,
		"value": value,
		"inline": inline
	}


def image(url, w=50, h=50):
	return {
		"url": url,
		"width": w,
		"height": h
	}


def thumbnail(url, w=50, h=50):
	return {
		"url": url,
		"width": w,
		"height": h
	}


def footer(text, icon_url):
	return {
		"text": text,
		"icon_url": icon_url
	}


__all__ = ["Webhook", "embed", "field", "footer"]
