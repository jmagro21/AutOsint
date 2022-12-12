import os
#On va installer tout les paquets nécessaires pour que le script fonctionne correctement.
# on met à jour le système et on installe tous les outils nécessaires.
# Pour que ce script soit utilisable sur l'ensemble des postes.

#Installation de Python3
os.system("apt-get install python3")

#Installation du module pyfiglet
os.system("python3 -m pip install pyfiglet")

# Installation de l'outil curl qui va être utile avec URLscan.io pour récupérer les résultats des scans.
os.system("apt-get install curl")

#Ci-dessous, installation de shodan et initialisation de l'API avec la clé API que l'on a récupérée sur le site shodan.
os.system("python3 -m pip install -U --user shodan")
os.system("shodan")
os.system("shodan init mcctQG1Pu7vfFoHKWGAUeB9X4SSrNN9q")

#DNSSCAN
os.system("git clone https://github.com/rbsec/dnscan") # On récupère l'outil sur github
os.system("python3 -m pip install dnspython") # Les dépendances nécessaires à cet outil ci-dessous.
os.system("python3 -m pip install netaddr")
os.system("python3 -m pip install cryptography")
os.system("python3 -m pip install pip install packaging")
os.system("mv dnscan/* ../*") # On donne les tous les droits à root et rien au reste des utilisateurs.
os.system("rm -r dnscan/")
os.system("chmod -R 700 ../*")

#theHarvester
os.system("apt-get install theharvester")

#urlscan.io
os.system("python3 -m pip install requests") # On installe les modules nécessaires pour manipuler l'API.

#Ci-dessous, on met à jour le système et tous les paquets
# os.system("apt-get update")
# os.system("apt-get upgrade -y")
