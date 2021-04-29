#!/bin/python
import os  

def write_lang():
    lang = input("Type the language of the program (fr or en) >> ")

def start():
    print(" _____ _____ _   _   _____  _      _____  ___  ______ ")
    print("|  __ \  _  | \ | | /  __ \| |    |  ___|/ _ \ | ___ \ ")
    print("| |  \/ | | |  \| | | /  \/| |    | |__ / /_\ \| |_/ /")
    print("| | __| | | | . ` | | |    | |    |  __||  _  ||    / ")
    print("| |_\ \ \_/ / |\  | | \__/\| |____| |___| | | || |\ \ ")
    print(" \____/\___/\_| \_/  \____/\_____/\____/\_| |_/\_| \_|")
    print(" ")
    print("Version 1.1")
    print(" ")

def input_lang():
    lang = input("Type the language of the program (fr or en) >> ")

def help_fr():
    print("Voice la liste des commandes executables:")
    print("- cleardisk")
    print("cleardisk permet de supprimés,optimisés tout les fichiers indélérisables et inutiles de Windows (Beta)")
    print("- resetws")
    print("resetws permet de réinitialiser le cache du Windows Store (EN BETA !!)")
    print("(peut causer le disfonctionnement du Windows Store)")

def help_en():
    print("Voice the list of executable commands:")
    print("- cleardisk")
    print("cleardisk allows to delete, optimize all the undeliverable and useless files of Windows (Beta)")
    print("- resetws")
    print("resetws allows to reset the cache of the Windows Store (IN BETA!!)")
    print("(peut causer le disfonctionnement du Windows Store)")

def repeat_command_in_french():
    command_in_french()

def repeat_command_in_english():
    command_in_english()

def command_in_french():
    print(" ")
    print(" ")
    command = input("Veuillez tappez la commande >> ")
    if command == "cleardisk":
        print("Nettoyage du disque principal en cours...")
        os.system("cleanmgr /sagerun:65535")
        print("Nettoyage du disque fini !")
        print("Suppression des fichiers temporaires en cours ...")
        os.system("del /S /F /Q %temp%")
        print("Nettoyage des fichiers temporaires fini !")
        print("Défragmentation de tout les disques en cours...")
        os.system("defrag C: D: /M")
        print("Défragmentation fini !")
        print(" ")
        repeat_command_in_french()
    elif command == "resetws":
        print("Nettoyage du cache du Windows store en cours ...")
        os.system("wsreset")
        print("Fini !")
        repeat_command_in_french()
        
def command_in_english():
    print(" ")
    print(" ")
    command = input("Please type the command >> ")
    if command == "cleardisk":
        print("Main disk cleaning in progress...")
        os.system("cleanmgr /sagerun:65535")
        print("Cleaning of the finished disk!")
        print("Deleting temporary files in progress ...")
        os.system("del /S /F /Q %temp%")
        print("Temporary files cleaning finished!")
        print("Defragmentation of all the disks in progress...")
        os.system("defrag C: D: /M")
        print("Defragmentation finished!")
        print(" ")
        repeat_command_in_english()
    elif command == "resetws":
        print("Cleaning the cache of the Windows store in progress ...")
        os.system("wsreset")
        print("Done !")
        repeat_command_in_english()
     
start()        
lang = input("Type the language of the program (fr or en) >> ")
if lang == "fr":
    help_fr()
    command_in_french()
elif lang == "en":
    help_en()
    command_in_english()
elif lang != "en" or "fr":
    print("Please write correctly the chosen language / Veuillez écrire correctement la langue choisi")
    input_lang()
    
# ACTIVE ADMINISTRATOR SESSION,NOT WORK
#    for _ in range(10):
#        print(" ")
#    os.system("net user administrator /active")
#    for _ in range(10):
#       print(" ") 
