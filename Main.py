import os 
import pyfiglet as pfg # On importe le module qui permet de faire un menu sympa

#Module qui va permettre de passer des commandes systèmes.
# Pour moi (Raphaël), le script doit être exécutée sour tous les systèmes Linux.
# Donc première chose, c'est de passer les commandes pour installer tous les paquets.
# On va pas encombrer le code avec ça autant faire ça avec un autre script à part.

# Faudrait commenter cette partie ! Pas compris l'objectif et quel outil tu utilises !
#Essyer de faire un petit menu sympa avec la bibliothèque pyfiglet
#On a installer le module précèdement dans l'autre fichier (pre-script.py)

print("h - help")
print("do - tout faire sur le future DNS donné ")
Souhait = input("Que  souhaitez vous faire ? : ")

if Souhait == "h" :
    print("Voici ce que vous pouvez faire avec ce script")
    os.system("theHarvester")
elif Souhait == "do" : 
    DNS = input("veuillez saisir l'adresse DNS à Scanner ")
    os.system("theHarvester -d "+DNS+" -b all")
else : 
    print("Vous n'avez rien saisi.")
