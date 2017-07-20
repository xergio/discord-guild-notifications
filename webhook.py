
# https://github.com/Derpolino/discord-webhooks-python/blob/master/discordWebhooks.py

import requests
import json

# https://discordapp.com/developers/docs/resources/webhook#execute-webhook
class Webhook():

	def __init__(self, url, **kwargs):
		self.url = url
		self.wh = {
			"username": kwargs.get("username", None),
			"avatar_url": kwargs.get("avatar_url", None),
			"content": None,
			"embeds": []
		}

	def add_embed(self, embed):
		self.wh["embeds"].append(embed)

	def clear_embeds(self):
		self.wh["embeds"] = []

	def send(self, content=None, tts=False):
		self.wh["content"] = content
		self.wh["tts"] = tts
		#print(self.wh)

		r = requests.post(self.url, json=self.wh)

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
