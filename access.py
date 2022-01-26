import os

print("HELLO, " + os.getlogin().upper())
print("CHECKING FOR THE NECESSARY PYTHON MODULES...")

try:
    import PySimpleGUI as sg

    print("YOU HAVE ALL THE REQUIREMENTS TO RUN THIS PROJECT.\n"
          "CONTINUING...")

except ImportError as err:
    print("CRITICAL_ERROR://   ", str(err))
    print("FIXING...")
    print("INSTALLING THE LATEST PIP3 VERSION...")
    os.system("pip3 install --upgrade pip")
    print("INSTALLING MODULES...")

    try:
        os.system("pip3 install -r requirements.txt")

    except:
        print("COULDN'T INSTALL PACKAGES. PLEASE RUN 'pip3 install -r requirements.txt' IN YOUR TERMINAL.")


def encrypt():  # encrypt all files in the 'src' folder.
    import rsa


def decrypt():  # decrypt all files in the 'src' folder.
    import rsa


def reset_encryption():  # revert all files to the GitHub default and create new keys
    import rsa, json
    sure = input("THIS PROCESS IS IRREVERSIBLE, ALL DATA WITHIN THE 'src' FOLDER WILL BE ERASED. "
                 "YOU WILL HAVE A NEW SET OF PUBLIC AND PRIVATE KEYS GENERATED FOR YOU. "
                 "\nCONTINUE? (Y/N): ")

    if sure == "Y":
        print("TYPE 'A1B2C3' TO CONTINUE\n(A1B2C3): ")
        abc = input()

        if abc == "A1B2C3":
            print("PROMPT CORRECT")
            print("FINDING FOLDER...")
            with open('../settings.json', 'r') as settingsFile:
                # understand settings data
                data = settingsFile.read()
                obj = json.loads(data)

                srcFolderLocation = obj['src_folder_location']

            print("FOLDER FOUND.")
            print("DELETING...")
