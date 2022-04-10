def trainIt(chatbot):
	from chatbot import chatbot
	from chatterbot.trainers import ChatterBotCorpusTrainer
	from zenlog import log
	import json


	with open('../../../settings.json', 'r') as settingsFile:
                # understand settings data
                data = settingsFile.read()
                obj = json.loads(data)

                robotName = str(obj['robotName'])
                languagesToTrain = obj['robotLanguages']

	log.info(f"Training chatbot (name: {robotName})..")
	
	trainer = ChatterBotCorpusTrainer(chatbot)
	
	trainer.train(languagesToTrain)


def useChatbot(input="", trainChatbot=False):
	from chatterbot import ChatBot
	import json
	from zenlog import log
	import sys


	log.debug("Init Chatbot..")
	with open('../../../settings.json', 'r') as settingsFile:
                # understand settings data
                data = settingsFile.read()
                obj = json.loads(data)

                robotName = str(obj['robotName'])


	chatbot = ChatBot(robotName)
	# train chatbot if user wishes.
	if trainChatbot:
		trainIt(chatbot)

	else:
		if input == "":
			if input == " ":
				log.error("Variable 'input' cannot be empty if getting response.")
				sys.exit()

		if input != "":
			if input != " ":
				chatbot.get_response(input)
	

useChatbot(input="", trainChatbot=True)
