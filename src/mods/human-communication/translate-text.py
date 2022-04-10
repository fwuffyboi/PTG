def translateTextGOOG(fromLang, toLang: str, toTrans: str):
	from googletrans import Translator
	from zenlog import log
	import sys

	# init the Google API translator
	translator = Translator()

	if toLang == "":
		log.error("The 'toLang' variable cannot be empty.")
		sys.exit()

	elif toTrans == "":
		log.error("The 'toTrans' variable cannot be empty.")
		sys.exit()


	log.debug("Variable 'fromLang' set to 'en'.")
	log.info("Translating from english.")

	translation = translator.translate(toTrans, dest=toLang)
	log.info(f"Translated '{translation.origin}' to '{translation.text}' ({translation.src} -> {translation.dest})")

	return {
		"translatedFromLang": translation.src,
		"translatedToLang": translation.dest,
		"translatedFromText": translation.origin,
		"translatedToText": translation.text,
		"confidence": translation.extra_data['confidence']
	}

# print(translateText(toLang="sv", toTrans="Hello bro")['translatedToText'])

def translateTextDDGO(fromLang: str, toLang: str, toTrans: str):
	import requests
	from zenlog import log
	import sys
	
	if toLang == "":
		log.error("The 'toLang' variable cannot be empty.")
		sys.exit()

	elif toTrans == "":
		log.error("The 'toTrans' variable cannot be empty.")
		sys.exit()


	log.debug("Variable 'fromLang' set to 'en'.")
	log.info("Translating from english.")

	TDPayload = bytes(toTrans, 'utf-8')

	TD = requests.post(f"https://duckduckgo.com/translation.js?vqd=3-219300495395415285450569426735018914512-288366996005856944283776176404510835301&query=hej%20in%20english&from={fromLang}&to={toLang}", 
			   data=TDPayload
	)

	

	log.info(f"Translated '{toTrans}' to '{TD.json()['translated']}' ({fromLang} -> {toLang})")

	return {
		"translatedFromLang": fromLang,
		"translatedToLang": toLang,
		"translatedFromText": toTrans,
		"translatedToText": TD.json()['translated'],
		"DDGODetectedLang": TD.json()['detected_language'],
		"confidence": "Unavailable due to DuckDuckGo's service not providing this information."
	}

# print(translateTextDDGO(fromLang="en", toLang="sv", toTrans="Biscuit is a cute cat.")['translatedToText'])
# print(translateTextGOOG(fromLang="en", toLang="sv", toTrans="Biscuit is a cute cat.")['translatedToText'])

def translate(fromLang="en", toLang="", toTrans="", prefer="google"):
	from zenlog import log
	import sys

	if toLang == "":
		log.error("The 'toLang' variable cannot be empty.")
		sys.exit()

	elif toTrans == "":
		log.error("The 'toTrans' variable cannot be empty.")
		sys.exit()

	if prefer != "google":
		if prefer == "ddgo":
			pass
		else:
			log.error("The 'prefer' variable must be 'google' or 'ddgo'.")
			sys.exit()

	if prefer == "google":
		try:
			googlet = translateTextGOOG(fromLang=fromLang, toLang=toLang, toTrans=toTrans)
			return googlet

		except Exception as err:
			log.error(err)

			try:
				log.warn("Could not get GOOGLE translation, trying DDGO..")
				ddgot = translateTextDDGO(fromLang=fromLang, toLang=toLang, toTrans=toTrans)
				return ddgot

			except Exception as err:
				log.error(err)
				sys.exit()

	elif prefer == "ddgo":
		try:
			ddgot = translateTextDDGO(fromLang=fromLang, toLang=toLang, toTrans=toTrans)
			return ddgot

		except Exception as err:
			log.error(err)

			try:
				log.warn("Could not get DDGO translation, trying GOOG..")
				googlet = translateTextGOOG(fromLang=fromLang, toLang=toLang, toTrans=toTrans)
				return googlet

			except Exception as err:
				log.error(err)
				sys.exit()
		

# print(translate(fromLang="en", toLang="sv", toTrans="Biscuit is a cute cat.", prefer="google"))
