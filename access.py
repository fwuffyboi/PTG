# get username, run commands
import os, sys
import json


# check if required modules are installed
try:
	print("CHECKING FOR THE NECESSARY PYTHON MODULES...")
	# encryption, decryption
	import rsa

	# logging
	from zenlog import log

	# internet
	import requests

	# translation service
	import googletrans

	# os/platform detection
	import platform

	log.info("All requirements installed.")

	try:
		# testing API keys
		with open('settings.json', 'r') as settingsFile:
			# understand settings data
			data = settingsFile.read()
			obj = json.loads(data)
			APIKey = obj['openWeatherMapAPIKey']
			url = f'http://api.openweathermap.org/geo/1.0/direct?q=atlanta&limit=1&appid={APIKey}'
			r = requests.get(url)
			results = r.json()
			# print(results)

		if results[0]['state'] == "Georgia":
			log.info("OpenWeatherMap API key test successful.")
		if results[0]['state'] != "Georgia":
			log.error(f"\nThe weather service is unavailable. \nPotential reason: {results['message']}\n")

	except Exception as error:
		if results['cod'] == 401:
			log.error(f"\nThe weather service is unavailable. \nPotential reason: {results['message']}\n")

		else:
			log.error(error)
			sys.exit()

except ImportError as err:
	log.critical("CRITICAL_ERROR://   ", str(err))
	log.debug("FIXING...")
	log.info("INSTALLING THE LATEST PIP3 VERSION...")
	os.system("pip3 install --upgrade pip")
	log.info("INSTALLING MODULES...")

	try:
	        os.system("pip3 install -r requirements.txt")

	except:
		log.critical("COULD NOT INSTALL PACKAGES. PLEASE RUN 'pip3 install -r requirements.txt' IN YOUR TERMINAL.")
		sys.exit()

# Greet the user by profile name
try:
	pc_username = os.getlogin().upper()
	log.info(f"Got profile username. pc_username set to \"{pc_username}\"")
	print(f"Hello, {pc_username}.")
	
	with open('settings.json', 'r') as settingsFile:
		# understand settings data
		data = settingsFile.read()
		obj = json.loads(data)
		
		robotName = str(obj['robotName'])
		OS = obj['openWeatherMapAPIKey']
		

	print(f"Your robot's name is {robotName}.")
	log.debug("Booting...")
	
except Exception:
	pc_username = "Unknown"
	log.error("Could not get profile username")
	log.debug(f"pc_username set to \"{pc_username}\"")
	print(f"Hello, {pc_username}.")
	
	with open('settings.json', 'r') as settingsFile:
		# understand settings data
		data = settingsFile.read()
		obj = json.loads(data)
		
		robotName = str(obj['robotName'])
		OS = obj['operatingSystem'].lower()
	
	
	print(f"Your robot's name is {robotName}.")
	
	if OS == "linux":
		if str(platform.machine).lower() == "linux":
			log.info(f"Settings says your pc's operating system is {OS}. \nThis is correct.")
			clearCmd = "clear"
		else:
			log.critical(f"Settings says your pc's operating system is {OS}. \nYour pc's operating system is {str(platform.system()).lower}.")
			sys.exit()

	if OS == "macos":
		if str(platform.machine).lower() == "darwin":
			log.info(f"Settings says your pc's operating system is {OS}. \nThis is correct.")
			clearCmd = "clear"
		else:
			log.critical(f"Settings says your pc's operating system is {OS}. \nYour pc's operating system is {str(platform.system()).lower}(MacOS).")
			sys.exit()

	if OS == "windows":
		print(platform.system())
		if str(platform.machine).lower() == "windows":
			log.info(f"Settings says your pc's operating system is {OS}. \nThis is correct.")
			clearCmd = "clear"
		else:
			log.critical(f"Settings says your pc's operating system is {OS}. \nYour pc's operating system is {str(platform.system()).lower}.")
			sys.exit()
		
	
	log.debug("Booting...")


# def encrypt():  # encrypt all files in the 'src' folder.
# 	log.info("Commence encrypting the 'src' folder...")
# 	log.info("Looking for public and private keys...")
# 	try:
# 		with open("keys.json", "r") as pubPrivKeysFile:
			

# def decrypt():  # decrypt all files in the 'src' folder.
    # import rsa


# reset encryption keys and reinstall the 'src' folder.
def reset_encryption():
	# encrypt()
	sure = input("THIS PROCESS IS IRREVERSIBLE, ALL DATA WITHIN THE 'src' FOLDER WILL BE ERASED.\n"
                 "YOU WILL HAVE A NEW SET OF PUBLIC AND PRIVATE KEYS GENERATED FOR YOU. "
                 "\nCONTINUE? (Y/N): ")

	if sure == "Y":
		print("TYPE 'A1B2C3' TO CONTINUE\n(A1B2C3): ")
		abc = input()

	if abc == "A1B2C3":
		# finish this
		print("finish this")
