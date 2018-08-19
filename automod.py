import json 
import requests
from time import sleep

TOKEN = "" # Telegram bot API access token
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    url = URL + "getUpdates?offset=" + str(prev_uid)
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_text_and_time(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    last_update_id = updates["result"][last_update]["update_id"]
    #print("after update", last_update_id)
    #print(updates["result"])
    if "message" in updates["result"][last_update]:
        if "text" in updates["result"][last_update]["message"]:
            text = updates["result"][last_update]["message"]["text"].lower()
        else:
            text = ""
        time = updates["result"][last_update]["message"]["date"]
        chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    else:
        text = ""
        time = 0
        chat_id = 0
    #print(updates)
    return (text, chat_id, time, last_update_id)


def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

	
def dontdoshit():
	return
	

response_map = {
	"good automod": "ayy, danks m88",
	"ayy": "lmao",
	"lmao": "m88",
	"ati": "hey, automoderator here, watch out, you mentioned ati. ati was consumed by eternal glory amd so you should correct your post to glorious amd.",
	"nvidia": "That's a strange way to spell novideo",
	"<--": "\U0001f440\U0001f44c \U0001f440\U0001f44c\U0001f440\U0001f44c\U0001f440\U0001f44c\U0001f440 good shit go౦ԁ sHit\U0001f44c thats \U00002714 some good\U0001f44c\U0001f44cshit right\U0001f44c\U0001f44cthere\U0001f44c\U0001f44c\U0001f44c right\U00002714there \U00002714\U00002714if i do Saү so my self \U0001f4af i say so \U0001f4af thats what im talking about right there right there (chorus: ʳIᵍʰᵗ ᵗʰᵉʳᵉ) mMMMMmМ\U0001f4af \U0001f44c\U0001f44c \U0001f44cНO0ОଠOOOOOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ \U0001f44c \U0001f44c\U0001f44c \U0001f44c \U0001f4af \U0001f44c \U0001f440 \U0001f440 \U0001f440 \U0001f44c\U0001f44cGood shit",
	"m88":"m89",
	"m90":"m91",
	"evga":"you mean an IED maker",	
	"bad automod":"​u wot? i will fucking rek your mii at wii party because wii is dank bec- What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces...If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo.",
	"intel":"that's a strange way to spell shintel",
	"shit automod":"​WHAT THE FUCK DID YOU JUST FUCKING SAY ABOUT ME, YOU НO0ОଠOOOOOОଠଠOOOOᵒᵒᵒᵒᵒᵒᵒᵒᵒ? I’LL HAVE YOU KNOW I GRADUATED TOP OF MY CLASS IN THE GOOD SHIT GO౦Ԁ SHIT ACADEMY, AND I’VE BEEN INVOLVED IN NUMEROUS SECRET RAIDS ON BAADDD SHIT, AND I HAVE OVER 300 CONFIRMED (CHORUS: ʳᶦᵍʰᵗ ᵗʰᵉʳᵉ). I AM TRAINED IN GOOD SHIT WARFARE AND I’M THE TOP SHITER IN THE ENTIRE US ARMED MMMMMᎷМ. YOU ARE NOTHING TO ME BUT JUST ANOTHER BAAA AAAADDDDD SH1T. I WILL WIPE YOU THE FUCK OUT WITH PRECISION THE LIKES OF WHICH HAS NEVER BEEN SEEN BEFORE ON THIS EARTH, THATS WHAT IM TALKING ABOUT RIGHT THERE RIGHT THERE . YOU THINK YOU CAN GET AWAY WITH SAYING THAT SHIT TO ME OVER THE INTERNET? THINK AGAIN, FUCKER. AS WE SPEAK I AM CONTACTING MY SECRET NETWORK OF GO౦Ԁ SHIT ACROSS THE USA AND YOUR IP IS BEING TRACED RIGHT THERE RIGHT THERE, SO IF I DO ƼAҮ SO MY SELF I SAY SO, YOU BETTER PREPARE FOR THE STORM, НO0ОଠOOOOOОଠଠOOOOᵒᵒᵒᵒᵒᵒᵒᵒᵒ. THE STORM THAT WIPES OUT THE PATHETIC LITTLE THING YOU CALL YOUR LIFE. YOU’RE FUCKING DEAD, KID. I CAN BE ANYWHERE, ANYTIME, I COULD BE RIGHT THERE RIGHT THERE AND I CAN KILL YOU IN OVER SEVEN HUNDRED WAYS, AND THAT’S JUST WITH MY BARE (CHORUS: ʳᶦᵍʰᵗ ᵗʰᵉʳᵉ). NOT ONLY AM I EXTENSIVELY TRAINED IN MMMMMᎷМ COMBAT, BUT I HAVE ACCESS TO THE ENTIRE ARSENAL OF THE UNITED STATES GOOD SHIT CORPS AND I WILL USE IT TO ITS FULL EXTENT TO WIPE YOUR MISERABLE ASS OFF THE FACE OF THE CONTINENT, YOU LITTLE BAAAAAAAAD SHIT. IF ONLY YOU COULD HAVE KNOWN WHAT UNHOLY RETRIBUTION YOUR LITTLE “CLEVER” COMMENT WAS ABOUT TO BRING DOWN UPON YOU, MAYBE YOU WOULD HAVE HELD YOUR FUCKING SHIT. BUT YOU COULDN’T, YOU DIDN’T, AND NOW YOU’RE PAYING THE PRICE, YOU GODDAMN IDIOT. I WILL SHIT FURY ALL OVER YOU AND YOU WILL DROWN IN IT. YOU’RE FUCKING DEAD, НO0ОଠOOOOOОଠଠOOOOᵒᵒᵒᵒᵒᵒᵒᵒᵒ.",
	"amd": "don't u mean AyyMD? ヽ༼▀̿̿Ĺ̯̿̿▀̿ ̿༽ﾉ",
	"silvy":"dankness with silvy\n<--[❄️]------------------->\ndankness without silvy\n<-------------------[🔥]-->",
	"rip automod":"intel is rip after ryzen release",
	"ryzen":"RGB STOCK COOLER",
	"kkk":"fukken racist"
}

prev_uid = 0
prev_uid = get_last_chat_id_and_text_and_time(get_updates())[3]
while True:
	text, chat, time, uid = get_last_chat_id_and_text_and_time(get_updates())

	if uid == prev_uid:
		dontdoshit()
	else:
		for q, a in response_map.items():
			if q in text:
				send_message(a, chat)
		prev_uid = uid
	sleep(1)