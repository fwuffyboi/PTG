import os

print("HELLO, " + os.getlogin().upper())
print("CHECKING FOR THE NECESSARY PYTHON MODULES...")

try:
    import PySimpleGUI as sg

except ImportError as err:
    print("CRITICAL_ERROR://   ", str(err))
    print("FIXING...")
    print("INSTALLING MODULES...")

    try:
        os.system("pip3 install -r requirements.txt")


def encrypt():  # encrypt all files in the 'src' folder.
    import rsa



def decrypt():  # decrypt all files in the 'src' folder.
    import rsa


def reset_encryption():  # revert all files to the GitHub default and create new keys
    sure = input("THIS PROCESS IS IRREVERSIBLE, ALL DATA WITHIN THE 'src' FOLDER WILL BE ERASED. "
                 "YOU WILL HAVE A NEW SET OF PUBLIC AND PRIVATE KEYS GENERATED FOR YOU. "
                 "\nCONTINUE? (Y/N): ")

    if sure == "Y":
        print("TYPE 'A1B2C3' TO CONTINUE\n(A1B2C3): ")