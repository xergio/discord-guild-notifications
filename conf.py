"""
config module
"""

from tokens import *

icon_wowhead = "<:wowhead:352756406925000704>"
icon_mmoc = "<:MMOChampion:352756407109681153>"
icon_twitch = "<:twitch:352756406904160257>"
icon_warcraftlogs = "<:Warcraftlogs:352756407164076034>"

min_mythic = 15

affixes = {
    "Bullente": "<:m_teeming:352756406514089994>",
    "Detonante": "<:m_bursting:352760092397010944>",
    "Dolorosa": "<:m_grievous:352760092472377344>",
    "Explosiva": "<:m_explosive:352760091981905932>",
    "Furibunda": "<:m_raging:352756406492987394>",
    "Inquieta": "<:m_skittish:352756406497181698>",
    "Necrótica": "<:m_necro:352756406333472769>",
    "Potenciante": "<:m_bolstering:352756406509633536>",
    "Rebosante": "<:m_over:352756406463758337>",
    "Reforzada": "<:m_forti:352756406497050624>",
    "Sanguina": "<:m_sanguine:352756406153379844>",
    "Sísmica": "<:m_quaking:352760093118300160>",
    "Tiránica": "<:m_tyra:352756406279208964>",
    "Volcánica": "<:m_volcanic:352756406341992449>"
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
    "return-to-karazhan-upper": "Regreso a Karazhan: superior",
    "seat-of-the-triumvirate": "Trono del Triunvirato"
}

timers = {
    "black-rook-hold": ["39:00", "31:12", "23:25"],
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
    "return-to-karazhan-upper": ["39:00", "31:12", "23:24"],
    "seat-of-the-triumvirate": ["35:00", "28:00", "21:00"]
}

class_icons = {
    "Character--WARRIOR": "<:class_warrior:352756406232809483>",
    "Character--DRUID": "<:class_druid:352756406421815296>",
    "Character--HUNTER": "<:class_hunter:352756406278946827>",
    "Character--DEATHKNIGHT": "<:class_deathknight:352756406408970240>",
    "Character--MAGE": "<:class_mage:352756406035808258>",
    "Character--DEMONHUNTER": "<:class_demonhunter:352756406425878528>",
    "Character--PRIEST": "<:class_priest:352756406299918337>",
    "Character--PALADIN": "<:class_paladin:352756406446981130>",
    "Character--SHAMAN": "<:class_shaman:352756406459432960>",
    "Character--ROGUE": "<:class_rogue:352756406455107584>",
    "Character--WARLOCK": "<:class_warlock:352756406476341248>",
    "Character--MONK": "<:class_monk:352756406337798145>"
}

#stop here!

def battle_net_url(pattern):
    return pattern.format(battle_net_region, battle_net_apikey)
