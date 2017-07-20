
url_discord_webhook = "https://discordapp.com/api/webhooks/???/???????"

battle_net_region = "eu"
battle_net_apikey = "????"

twitch_token = "?????"

warcraftlogs_token = "???????"

icon_wowhead = "<:wowhead:283900950379233280>"
icon_mmoc = "<:mmochampion:283900921694650368>"
icon_twitch = "<:twitch:332609778285019137>"
icon_warcraftlogs = "<:warcraftlogs:283906655484379138>"

affixes = {
	"Bullente": "<:m_teeming:278565188410802176>",
	"Detonante": "<:m_bursting:327109581048250369>",
	"Dolorosa": "<:m_grievous:327109581132136449>",
	"Explosiva": "<:m_explosive:327109581249576960>",
	"Furibunda": "<:m_raging:278565187986915328>",
	"Inquieta": "<:m_skittish:278565188087840768>",
	"Necrótica": "<:m_necro:278565187634593795>",
	"Potenciante": "<:m_bolstering:278565187987046400>",
	"Rebosante": "<:m_over:278565188033314816>",
	"Reforzada": "<:m_forti:278565187588456450>",
	"Sanguina": "<:m_sanguine:278565188020469760>",
	"Sísmica": "<:m_quaking:327109581236862976>",
	"Tiránica": "<:m_tyra:278565187852828674>",
	"Volcánica": "<:m_volcanic:278565188125458432>"
}

affix_human = {
	"Bullente": "+ bichos",
	"Detonante": "= Il'gynoth",
	"Dolorosa": "Sangrado 90%",
	"Explosiva": "Orbes de mierda",
	"Furibunda": "Enrage 30%",
	"Inquieta": "- Aggro",
	"Necrótica": "- Sanación",
	"Potenciante": "Se buffan al morir",
	"Rebosante": "Overheal",
	"Reforzada": "Bichos :muscle:",
	"Sanguina": "Pozo al morir",
	"Sísmica": "El puto quake",
	"Tiránica": "Bosses :muscle:",
	"Volcánica": "El puto volcanic"
}

affix_rotation = [
	["Furibunda", "Volcánica", "Tiránica"],
	["Bullente", "Explosiva", "Reforzada"],
	["Potenciante", "Dolorosa", "Tiránica"],
	["Sanguina", "Volcánica", "Reforzada"],
	["Detonante", "Inquieta", "Tiránica"],
	["Bullente", "Sísmica", "Reforzada"],
	["Furibunda", "Necrótica", "Tiránica"],
	["Potenciante", "Inquieta", "Reforzada"],
	["Bullente", "Necrótica", "Tiránica"],
	["Sanguina", "Dolorosa", "Reforzada"],
	["Potenciante", "Explosiva", "Tiránica"],
	["Detonante", "Sísmica", "Reforzada"]
]

zones = {
	"darkheart-thicket": "Arboleda Corazón Oscuro", 
	"court-of-stars": "Corte de las Estrellas", 
	"vault-of-the-wardens": "Cámara de las Celadoras", 
	"halls-of-valor": "Cámaras del Valor", 
	"maw-of-souls": "Fauce de Almas", 
	"neltharions-lair": "Guarida de Neltharion", 
	"the-arcway": "La Arquería", 
	"eye-of-azshara": "Ojo de Azshara", 
	"black-rook-hold": "Torreón Grajo Negro", 
	"cathedral-of-eternal-night": "Catedral de la Noche Eterna", 
	"return-to-karazhan-lower": "Regreso a Karazhan: inferior", 
	"return-to-karazhan-upper": "Regreso a Karazhan: superior"
}

timers = {
	"black-rook-hold": ["38:00", "30:24", "22:48"],
	"court-of-stars": ["30:00", "24:00", "18:00"],
	"darkheart-thicket": ["30:00", "24:00", "18:00"],
	"eye-of-azshara": ["35:00", "28:00", "21:00"],
	"halls-of-valor": ["45:00", "36:00", "27:00"],
	"maw-of-souls": ["24:00", "19:12", "14:24"],
	"neltharions-lair": ["33:00", "27:24", "19:48"],
	"the-arcway": ["45:00", "36:00", "27:00"],
	"vault-of-the-wardens": ["33:00", "26:24", "19:48"],
	"cathedral-of-eternal-night": ["33:00", "27:24", "19:48"],
	"return-to-karazhan-lower": ["39:00", "31:12", "23:24"],
	"return-to-karazhan-upper": ["39:00", "31:12", "23:24"]
}

class_icons = {
	"Character--WARRIOR": "<:class_warrior:278565187257237505>",
	"Character--DRUID": "<:class_druid:278565188381442048>",
	"Character--HUNTER": "<:class_hunter:278565187605364737>",
	"Character--DEATHKNIGHT": "<:class_deathknight:278565187903029248>",
	"Character--MAGE": "<:class_mage:278565187919937537>",
	"Character--DEMONHUNTER": "<:class_demonhunter:278565187500376065>",
	"Character--PRIEST": "<:class_priest:278565187970269184>",
	"Character--PALADIN": "<:class_paladin:278565187588587521>",
	"Character--SHAMAN": "<:class_shaman:278565187831726081>",
	"Character--ROGUE": "<:class_rogue:278565187940909056>",
	"Character--WARLOCK": "<:class_warlock:278565187596976130>",
	"Character--MONK": "<:class_monk:278565187618078722>"
}

#stop here!

def battle_net_url(pattern):
	return pattern.format(battle_net_region, battle_net_apikey)
