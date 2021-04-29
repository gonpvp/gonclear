#!/bin/python
import os

print(" _____ _____ _   _   _____  _      _____  ___  ______ ")
print("|  __ \  _  | \ | | /  __ \| |    |  ___|/ _ \ | ___ \ ")
print("| |  \/ | | |  \| | | /  \/| |    | |__ / /_\ \| |_/ /")
print("| | __| | | | . ` | | |    | |    |  __||  _  ||    / ")
print("| |_\ \ \_/ / |\  | | \__/\| |____| |___| | | || |\ \ ")
print(" \____/\___/\_| \_/  \____/\_____/\____/\_| |_/\_| \_|")
print(" ")
print("Version 1.0 (Beta)")
print(" ")
print("Commandes disponibles:")
print("- cleardisk")
print("cleardisk permet de supprimés,optimisés tout les fichiers indélérisables et inutiles de Windows (Beta)")
print("- resetws")
print("resetws permet de réinitialiser le cache du Windows Store (EN BETA !!)")
print("(peut causer le disfonctionnement du Windows Store)")

def command():
    print(" ")
    print(" ")
    command = input("Veuillez tappez la commande :  ")
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
        print("Relancer le programme pour executer une autre commande !")
#        print("Défragmentation de tout les disques en cours...")
#        os.system("chkdsk c: /f")
    elif command == "resetws":
        print("Nettoyage du cache du Windows store en cours ...")
        os.system("wsreset")

command()
