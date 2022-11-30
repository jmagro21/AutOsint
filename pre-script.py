import os 
#On va installer tout les paquets nécessaires pour que le script fonctionne correctement.
# on met à jour le système et on installe tous les outils nécessaires.
# Pour que ce script soit utilisable sur l'ensemble des postes. 

#Installation de Python3
os.system("apt-get install python3")

#Installation du module pyfiglet
os.system("pip install pyfiglet")


#Ci-dessous, installation de shodan et initialisation de l'API avec la clé API que l'on a récupérée sur le site shodan.
os.system("python3 -m pip install -U --user shodan")
os.system("shodan")
os.system("shodan init mcctQG1Pu7vfFoHKWGAUeB9X4SSrNN9q")

#DNSSCAN
os.system("https://github.com/rbsec/dnscan")


#theHarvester
os.system("git clone https://github.com/laramies/theHarvester")
os.system("cd theHarvester")
os.system("python3.7 -m pip install -r requirements/dev.txt")
os.system("python3.7 -m pip install -r requirements/base.txt")

#urlscan.io



#Ci-dessous, on met à jour le système et tous les paquets
os.system("apt-get update")
os.system("apt-get upgrade -y")

#Script principal qui s'exécute
exec(open("Main.py").read())


