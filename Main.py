import os #Module qui va permettre de passer des commandes systèmes.
import pyfiglet # On importe le module qui permet de faire un menu sympa
import requests # Module qui va permettre de faire des requêtes à l'API URLscan.io
import json # Module permettant de manipuler des fichiers json. (proche du XML)
import time # Nécessaire pour faire attendre le code quelques secondes pour récupérer le résultat de URLSCAN
import yaml # On importe le module yaml pour manipuler les fichier du même nom.
# Installation de tous les paquets nécessaires au script dans un autre fichier pour être sûr et certain que la machine va être capable de lire le script.

BOLD = '\033[1m' # Code couleur qui nous permet de rendre le script un peu plus joli
BLUE = '\033[94m' # La couleur bleue
GREEN = '\033[92m' # La couleur verte
RED = '\033[31m' # La couleur rouge
RESET = '\033[0m' # La couleur normale.

""" 
Ceci est une proposition de menu, il y a plusieurs propositions faites a l'utilisteurs, le programme se stoppe uniquement
quand l'utilisateur selectionne la commande "q", de cette maniere il peut lancer, un scan, puis un autre, relancer la premier scan etc...
L'utilisateur n'a ainsi pas besoin de relancer le programme a chaque fois.
Si l'utilisteur entre une mauvaise commande, le programme ne se bloque pas, il indique juste que la commande n'est pas bonne et ainsi 
l'utilisateur peut entrer une nouvelle commande.
Si ce dernier sélectionne help, le menu s'affiche de nouveau.
Effectuer un scan rapide integrant touts les outils avec les parametres les plus rapide (par exemple dnscan avec une wordlist de 500 mots"),
un scan lent (par exemple dnscan avec une wordlist de 10000 mots"), et un custom scan qui permet a l'utilisateur de lancer un outil precis.
Tout cela rends le programme modulable sans changer la complexite de celui-ci, grace a l'utilisation de fonctions specifiques.

"""

def verif_dependance (a) : # Fonction qui vérifie l'entrée utilisateur demandée pour l'installation des dépendances nécessaires au script.
	while a != "1" and a != "2" : # Si différent des deux options qu'on propose on redemande en boucle.
		print("Veuillez saisir une valeur accepté, 1 ou 2")
		a = str(input(BOLD + BLUE + ">>> "))
		print(RESET, end='')
	return a


titre0 = pyfiglet.figlet_format("Installation des outils nécessaires", font = "slant" )
print(titre0)
print("="*50)
print("Voulez-vous installer toutes dépendances nécessaires pour le script ? \n")
print("1. Oui")
print("2. Non")
print("="*50)
print("\n")
Rps = str(input(BOLD + BLUE + ">>> "))
print(RESET, end='')
apres_verif = verif_dependance(Rps)
#On va installer tout les paquets nécessaires pour que le script fonctionne correctement.
# on met à jour le système et on installe tous les outils nécessaires.
# Pour que ce script soit utilisable sur l'ensemble des postes.


if apres_verif == "1" :
	#Installation de Python3
	os.system("apt-get install python3")

	#Installation du module pyfiglet
	os.system("python3 -m pip install pyfiglet")

	# Installation de l'outil curl qui va être utile avec URLscan.io pour récupérer les résultats des scans.
	os.system("apt-get install curl")

	#Installation du module yaml
	os.system("python3 -m pip install pyyaml")

	#Ci-dessous, installation de shodan et initialisation de l'API avec la clé API que l'on a récupérée sur le site shodan.
	os.system("python3 -m pip install shodan")
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

elif apres_verif == "2" :
	print("\0")

print("="*50)
print("\n")


def verif_IP (a) :
	nb = a.count(".")
	while nb != 3 :
		print("Veuillez saisir une adresse IP ! Exemple : 8.8.8.8")
		a = str(input(BLUE + BOLD + ">>> (Default Scan) "))
		print(RESET, end='')
		nb = a.count(".")
	return a

def verif_domain (a) :
	nb = a.count(".")
	while nb != 2 :
		print("Veuillez saisir un nom de domaine acceptable ! Exemple : www.nomdedomaine.org")
		a = str(input(BOLD + BLUE + ">>> (Default Scan) "))
		print(RESET, end='')
		nb = a.count(".")
	return a

def verif_domain_harvester (a) :
	nb = a.count(".")
	while nb != 1 :
		print("Veuillez saisir un nom de domaine comme ceci : le-pointcom.fr")
		a = str(input(BOLD + BLUE + ">>> (Default Scan) "))
		print(RESET, end='')
		nb = a.count(".")
	return a

def verif_domain_dnscan (a) :
	nb = a.count(".")
	while nb != 2 :
		print("Veuillez saisir un nom de domaine comme ceci : www.le-pointcom.fr")
		a = str(input(BOLD + BLUE + ">>> (Default Scan) "))
		print(RESET, end='')
		nb = a.count(".")
	return a

def verif_urlscan_lien(a) :
	nb = a.count(".")
	nb1 = a.count("/")
	nb2 = a.count(":")
	while nb != 2 and nb1 != 3 and nb2 != 1 :
		print("Veuillez saisir un nom de domaine comme ceci : www.le-pointcom.fr")
		a = str(input(BOLD + BLUE + ">>> (Default Scan) "))
		print(RESET, end='')
		nb = a.count(".")
	return a

def FirstSummary () :
	print(BOLD + BLUE + "Veuillez choisir une option : " + RESET)
	print("="*50)
	print("1 : Default scan") # Mettre en place une configuration de scan prédéfinie pour l'utilisateur
	print("2 : Custom scan") # Mettre en place une solution pour ce scan où l'utilisateur peut choisir les types de scan qu'il souhaite effectué aves les différents outils.
	print("h : Help") # Permet à l'utilisateur d'avoir des informations sur les outils et comment s'en servir.
	print("q : Quit") # Permet à l'utilisateur de quitter le script.
	print("="*50)

def SummaryTools () :
	print(BOLD + BLUE + "Veuillez choisir une option : " + RESET)
	print("="*50)
	print("a : Dnscan")
	print("b : TheHarvester")
	print("c : Shodan")
	print("d : Urlscan")
	print("q : Quit")
	print("="*50)

def verif_tools (a) :
	while a != "a" and a != "b" and a != "c" and a != "d" and a != "q":
		print("Veuillez saisir une réponse acceptée !")
		a = str(input(BOLD + BLUE + ">>> (Custom Scan) "))
		print(RESET, end='')
	return a

def autre_outil () :
	print("="*50)
	print("Voulez-vous utilisez un autre outil ?")
	print("1. Oui")
	print("2. Non, passer à l'execution")
	print("="*50)

def verif_souhait (a) :
	while a != "h" and a != "ggl" and a != "do" and a != "p" and a != "ex" :
		print("Veuillez saisir une réponse parmi celle proposées ! Exemple : ggl")
		a = str(input(BOLD + BLUE + ">>> (Custom Scan) "))
		print(RESET, end='')
	return a

def verif_souhait_shodan (a) :
	nb = a.count(".")
	while nb != 2 and nb != 3 :
		print("Veuillez saisir un nom de domaine ou une adresse IP dans le format suivant ! IP : 8.8.8.8 ; domaine : www.test.fr")
		a = str(input(BOLD + BLUE + ">>> (Custom Scan) "))
		print(RESET, end='')
	return a

def verif_choix_shodan_IP (a) :
	while a != "1" and a != "2" and a != "3" and a != "4" and a != "5" :
		print("Veuillez saisir une réponse acceptée : 1,2,3,4 ou 5")
		a = str(input(BOLD + BLUE + ">>> (Custom Scan) "))
		print(RESET, end='')
	return a

def verif_cible (a) :
	x = isinstance(a, str)
	while x != True :
		print("Veuillez saisir une chaîne de caractères !")
		a = str(input(BOLD + BLUE + ">>> (Custom Scan) "))
		print(RESET, end='')
		x = isinstance(a, str)
	return x

def verif_choix_shodan_domain (a) :
	while a != "1" and a != "2" and a != "3" and a != "4" :
		print("Veuillez saisir une réponse acceptée : 1,2,3,4 ou 5")
		a = str(input(BOLD + BLUE + ">>> (Custom Scan) "))
		print(RESET, end='')
	return a

def verif_choice_dnscan (a) :
	while a != "1" and a != "2" :
		print("Veuillez sélectionner l'une des deux options qui vous est offert par le chiffre indiqué : 1 ou 2")
		a = str(input(BOLD + BLUE + ">>> (Custom Scan) "))
		print(RESET, end='')
	return a

#Affichage de ma baniere
titre = pyfiglet.figlet_format("AutOsint", font = "slant" )
print(titre)

FirstSummary()

Rps = str(input(BOLD + BLUE + ">>> "))
print(RESET, end = '')

while Rps != "q" :

	#On lance tous les outils les uns après le autres avec les paramètres les plus rapides pour fournir des résultats à l'utilisateur sans personnalisation.
	#Il va nous manquer l'outil urlscanio à ajouter plus tard !
	if Rps == "1" :
		print("Nous allons dans un premier temps utiliser l'outil Shodan qui permet de récupèrer des informations sur une cible bien définie !")
		print("A la base cet outil est un moteur de recherche qui référence le balayage massif des ports sur internet !")
		print("Il est possible de l'utiliser en ligne de commande et dans cette situation le script se charge de tout !")
		print("Voulez-vous scanner une IP ou un domaine ?")
		print("="*50) # On laisse le choix à l'utilsiateur si la cible
		print("1. IP") # Une IP 
		print("2. Domaine") # Un domaine
		print("="*50)
		Rps2 = str(input(BOLD + BLUE + ">>> (Default Scan) ")) # On récupère la réponse de l'utilisateur
		print(RESET, end='')
		
		while Rps2 != "1" and Rps2 != "2" :
			print(RED + "Veuillez saisir une commande valide !")
			Rps2 = str(input(BOLD + BLUE + ">>> (Default Scan)")) # On récupère la réponse de l'utilisateur
			print(RESET, end='')

		if Rps2 == "1" :
			print("Veuillez saisir l'IP que vous voulez scanner !")
			Rps3 = str(input(BOLD + BLUE + ">>> (Default Scan) ")) # On récupère l'IP cible
			print(RESET, end='')
			IP = verif_IP(Rps3)
			os.system("shodan host " + IP + " > OutputShodanIP") # On scan et on enregistre dans un fichier de sortie.
		if Rps2 == "2" :
			print("Veuille saisir le domaine que vous voulez scanner !")
			Rps3 = str(input(BOLD + BLUE + ">>> (Default Scan) ")) # On récupère le domaine cible
			print(RESET, end='')
			DOMAIN = verif_domain(Rps3)
			os.system("shodan domain " + DOMAIN + " > OutputShodanDomain") # On scan et on enregistre dans un fichier de sortie


		print("\n")


		print("Nous allons effectuer un scan également sur un nom de domaine avec l'outil theHarvester !")
		print("Veuillez simplement indiquer le nom de domaine que vous voulez cibler !")
		print("Attention ne pas saisir le 'www' du nom de domaine !!!! Exemple : test.fr ")
		Rps = str(input(BOLD + BLUE + ">>> (Default Scan) "))
		print(RESET, end='')
		domain = verif_domain_harvester(Rps) # On vérifie que le nom de domaine entré est valide.
		results = os.popen("theHarvester -d " + domain + " " + "-b all > OutputHarvester").read()#On lance le scan avec le nom de domaine donné par l'utilisateur.
		print("Veuillez patienter quelque seconde...")
		# Trier les résultats
		results_list = results.split("\n")
		results_list = [result for result in results_list if result]  # retirer les éléments vides
		results_list.sort()
		# Afficher les résultats triés
		for result in results_list:
			print(result)
			with open("DefaultScanTheHarvester.txt","w") as file :
				file.write(results)

		print("\n")


		print("Nous allons maintenant lancer un scan avec l'outil dnscan pour récupérer des informations liés au DNS !")
		print("Veuillez simplement saisir le domaine que vous voulez visez et le script se charge du reste !")
		print("Pour ce script, vous devez utilisez l'intégralité du nom de dommaine. Exemple : www.test.fr ")
		Rps = str(input(BOLD + BLUE + ">>> (Default Scan) "))
		print(RESET, end='')
		domaine = verif_domain_dnscan(Rps)
		os.system("python3 dnscan.py -d " + domaine + " -o OutputDNScan")
		
		
		print("\n")


		print("Nous allons maintenant utiliser l'outil urlscan.io qui permet de récupérer des informations sur des URL")
		print("Il vous suffit d'indiquer l'url que vous voulez scanner !")
		print("Vous devez donner l'intégralité du lien !! Exemple : https://www.instagram.com/")
		Rps = str(input(BOLD + BLUE + ">>> (Default Scan) "))
		print(RESET, end='')
		FQDN = verif_urlscan_lien(Rps)
		headers = {'API-Key':'27a5f4bf-340a-47dd-a710-7a3038a97321','Content-Type':'application/json'}
		data = {"url": Rps, "visibility": "public"}
		response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))

		os.system("touch ResultURLScanIo.txt")
		fichier = open('ResultURLScanIo.txt', 'w')
		for ligne in response :
			fichier.write(str(ligne))
		fichier.close()
		#Extraction de l'UUID
		lF = [] #liste tampon qui va accueillir le contenu du fichier
		#On ouvre le fichier et on ajoute son contenu a la liste
		fileInput = open("ResultURLScanIo.txt", "r")
		lignes = fileInput.readlines()
		for ligne in lignes :
			lF.append(ligne)
		fileInput.close()

		texte = str(lF) #On convertie la liste en une string
		#On cherche dans le fichier le mot uuid qui nous indique l'emplacement de celui-ci
		emplUUID = texte.find("uuid") + 8 #emplacement de l'uuid
		#uuid se trouve 4 caracteres apres "uuid", on ajoute la longueur du mot "uuid" ce qui fait 8.
		#uuid fait 36 caracteres de long, par consequent 
		uuid = texte[emplUUID : emplUUID + 36]		
	
		time.sleep(22) # On fige le code pendant 22 secondes pour atteindre que le scan soit terminé
		# et que le résulat puisse être récupéré.
		os.system("curl https://urlscan.io/api/v1/result/" + uuid + "/ > OutputURLScan.json")#On récupère le résultat du scan dans un fichier.
		#On va convertir le fichier de sortie en yaml pour que ce soit plus simple à trier.
		with open('OutputURLScan.json', 'r') as file:
			configuration = json.load(file)

		with open('OutputURLScan.yaml', 'w') as yaml_file:
			yaml.dump(configuration, yaml_file)
		

		os.system("mkdir DefaultScanResult/")
		os.system("chmod -R 700 DefaultScanResult/")
		if Rps2 == "1":
			os.system("mv OutputShodanIP DefaultScanResult/")
		elif Rps2 == "2":
			os.system("mv OutputShodanDomain DefaultScanResult/")

		os.system("mv DefaultScanTheHarvester.txt DefaultScanResult/")
		os.system("rm OutputHarvester")
		os.system("mv OutputDNScan DefaultScanResult/")
		os.system("rm ResultURLScanIo.txt")
		
		print("Nous avons exécuter l'ensemble des outils avec les paramètres par défaut !")
		print("Vous pouvez retrouver l'ensemble des résultats dans le fichier DefaultScanResult \n")
		print("Voulez-vous continuer le script ou quitter ce dernier ?")
		print("="*50)
		print("q. Quitter le script ")
		print("h. Revenir au menu principal ")
		print("="*50)
		Rps = str(input(BOLD + BLUE + ">>> (Default Scan) "))
		print(RESET, end='')

		if Rps == "q" or Rps == "Q" :
			exit()

	#L'utilisateur peut choisir un outil ou un autre 
	if Rps == "2" :

		os.system("mkdir CustomScanOutput/")

		print("Avant de démarrer il est important de préciser que cette partie ne vous expliquera pas le fonctionnement de chaque outil !")
		print("Il est de votre fait de vous renseigner sur chaque outil avant d'utiliser cette partie du script !")
		print("Enjoyyyy !")
		#On prévient l'utilisateur que nous n'allons pas le renseigner sur chaque outil car ce n'est pas le but de l'outil.

		with open('config.yml', 'r') as file :
			service = yaml.safe_load(file)
		
		SummaryTools()

		Tool_Rps = str(input(BOLD + BLUE + ">>> (Custom scan) "))
		print(RESET, end = '')
		Tool_Rps.rstrip("\n")
		Tools1 = verif_tools(Tool_Rps)
		if Tools1 == "a" :
			service['Dnscan'] = 'Vraie'
		elif Tools1 == "b" :
			service['Harvester'] = 'Vraie'
		elif Tools1 == "c" :
			service['shodan'] = 'Vraie'
		elif Tools1 == "d" :
			service['urlscan'] = 'Vraie'
		elif Tools1 == "q" :
			exit()

		print("\n")
	
		autre_outil()
		Autre_outil = str(input(BOLD + BLUE + ">>> (Custom Scan) "))
		verif_autreOutil = verif_dependance(Autre_outil)
		if verif_autreOutil == "1" :
			SummaryTools()
			Tool_Rps = str(input(BOLD + BLUE + ">>> (Custom scan) "))
			print(RESET, end = '')
			Tool_Rps.rstrip("\n")
			Tools2 = verif_tools(Tool_Rps)
			if Tools2 == "a" :
				service['Dnscan'] = 'Vraie'
			elif Tools2 == "b" :
				service['Harvester'] = 'Vraie'
			elif Tools2 == "c" :
				service['shodan'] = 'Vraie'
			elif Tools2 == "d" :
				service['urlscan'] = 'Vraie'
			elif Tools2 == "q" :
				exit()

			autre_outil()
			Autre_outil = str(input(BOLD + BLUE + ">>> (Custom Scan) "))
			verif_autreOutil = verif_dependance(Autre_outil)
			if verif_autreOutil == "1" :
				SummaryTools()
				Tool_Rps = str(input(BOLD + BLUE + ">>> (Custom scan) "))
				print(RESET, end = '')
				Tool_Rps.rstrip("\n")
				Tools3 = verif_tools(Tool_Rps)
				if Tools3 == "a" :
					service['Dnscan'] = 'Vraie'
				elif Tools3 == "b" :
					service['Harvester'] = 'Vraie'
				elif Tools3 == "c" :
					service['shodan'] = 'Vraie'
				elif Tools3 == "d" :
					service['urlscan'] = 'Vraie'
				elif Tools3 == "q" :
					exit()
				
				autre_outil()
				Autre_outil = str(input(BOLD + BLUE + ">>> (Custom Scan) "))
				verif_autreOutil = verif_dependance(Autre_outil)
				if verif_autreOutil == "1" :
					SummaryTools()
					Tool_Rps = str(input(BOLD + BLUE + ">>> (Custom scan) "))
					print(RESET, end = '')
					Tool_Rps.rstrip("\n")
					Tools4 = verif_tools(Tool_Rps)
					if Tools4 == "a" :
						service['Dnscan'] = 'Vraie'
					elif Tools4 == "b" :
						service['Harvester'] = 'Vraie'
					elif Tools4 == "c" :
						service['shodan'] = 'Vraie'
					elif Tools4 == "d" :
						service['urlscan'] = 'Vraie'
					elif Tools4 == "q" :
						exit()

		else :
			print("\0")
		
		print("\n")

		with open('config.yml', 'w') as dump_file :
			yaml.dump(service, dump_file)

		print("\n")
		print(RESET + "Maintenant que vous avez choisi vos outils, nous allons vous demandez les différentes options que vous souhaitez utiliser avec ces derniers !")
		print(RESET + "Allons-y !")
		print("\n")

		with open('config.yml', 'r') as file :
			service = yaml.safe_load(file)
		
		if service['Dnscan'] == 'Vraie' :
			print("Vous allez paramétrer DnScan !")
			print("DnsScan peut fonctionner soit avec un seul domaine soit avec une liste de domaine !")
			print("Votre premier choix va être de choisir entre une liste de domaine à scanner ou un seul !")
			print(RED + "ATTENTION : Si vous voulez attaquer plusieurs domaines, ces derniers doivent se trouver dans un fichier avec un domaine par ligne.")
			print(RED + "Si vous ne savez pas manipuler cette option le script ne fonctionnera pas ! Renseignez-vous au préalable.")
			print(RED + "Il faut placer le fichier contenant tous les domaines à la racine du script pour que ça fonctionne !")
			print(RESET, end='')
			print("="*50)
			print("1. Un seul domaine")
			print("2. Plusieurs domaines")
			print("="*50)
			choix = str(input(BOLD + BLUE + ">>> (Custom Scan) "))
			print(RESET, end='')
			verification = verif_choice_dnscan(choix)

			if verification == "1" :
				print("Nous allons donc scanner un seul domaine.")
				print("Voici les options qui sont à votre disposition.")
				print("="*50)
				print("="*50)

			if verification == "2" :
				print("Nous allons donc scanner une liste de domaine.")
				print("Voici les options qui sont à votre disposition.")
				print("="*50)
				print("="*50)
		
		if service['Harvester'] == 'Vraie' :
			print("Vous allez paramétrer theHarvester !")
			end=" "
			Option1="all"
			Perso="False"
			CommandHarvester=""
			while end != "do" :
				print("="*50)
				print("ggl - scanez via google")
				print("lk - scanez via Linkedin")
				print("do - tout faire sur le future DNS donné ")
				print("p - Personaliser la commande")
				print("ex - quitter theHarvester")
				print("="*50)
				Souhait = str(input(BOLD + BLUE + ">>> (Custom Scan) "))
				print(RESET, end='')
				Souhait.rstrip("\n")
				VERIF_SOUHAIT = verif_souhait(Souhait)
				#verification de la demande 
				if VERIF_SOUHAIT == "ggl" :
					Perso = "true"
					print("L'option 'google' est enregistré")
					Option1 = "ggl"
					input("Appuyez sur Entree pour continuer...")
				elif VERIF_SOUHAIT == "lk" :
					Perso = "true"
					print("L'option 'linkedin' est enregistré")
					Option1 = "linkedin"
					input("Appuyez sur Entree pour continuer...")
				elif VERIF_SOUHAIT == "p" :
					Perso = "true"
					print("Veuillez saisir la commande au complet")
					CommandHarvester=input()
					print("Votre commande à été personalisé, voulez vous lancer TheHarvester avec celle-ci ?")
					QuestionHarvester=input("O (OUI), n (non)")
					if QuestionHarvester == "O" or QuestionHarvester == "o" :
						Souhait="do"
						end = "do"
				elif VERIF_SOUHAIT == "ex" :
					print("Vous quittez TheHarvester")
					print(RED + "ATTENTION, le scan ne sera pas exécuté !")
					print(RESET, end='')
					end = "do"
				elif VERIF_SOUHAIT == "do" :
					end = "do"
      
			if Souhait == end : 
				if Perso == "true" :
					print("Veuillez patienter quelque seconde...")
					results = os.popen(CommandHarvester).read()
				else : 
					#on lui demande l'adresse
					DNS = str(input(BOLD + BLUE + "veuillez saisir l'adresse DNS à Scanner ! Exemple : test.fr et pas www.test.fr"))
					print(RESET, end='')
					#on fait tourner la command de façon non visible pour l'utilisateur
					verif_DNS = verif_domain_harvester(DNS)
					print("Veuillez patienter quelque seconde...")
					results = os.popen("theHarvester -d "+verif_DNS+" -b "+Option1).read()

				# Trier les résultats
				results_list = results.split("\n")
				results_list = [result for result in results_list if result]  # retirer les éléments vides
				results_list.sort()

				# Afficher les résultats triés
				for result in results_list:
					print(result)
					with open("ResultatTheHarvesterCustomScan.txt","w") as file :
						file.write(results)
				print("Les résulats sont enregistrés dans le fichier ResultatTheHArvester.txt qui sera stocké dans le dossier CustomScanOutput")
				os.system("mv ResultatTheHarvesterCustomScan.txt CustomScanOutput/")
			input("Appuyez sur Entree pour continuer...")

		if service['shodan'] == 'Vraie' :
			print("\n")
			print("Vous allez paramétrer shodan !")
			print("La première chose à faire est de choisir la cible : IP ou domaine !")
			print("Veuillez indiquer la cible que vous voulez scaner ! Exemple IP : 8.8.8.8 ; Exemple domaine : www.test.fr")
			Souhait = str(input(BOLD + BLUE + ">>> (Custom Scan) "))
			print(RESET, end='')
			Souhait.rstrip("\n")
			verif_souhait = verif_souhait_shodan(Souhait)

			if verif_souhait.count(".") == 3 :
				print("Vous avez décidé de scaner une IP.")
				print("Voila ce que nous vous proposons d'effectuer sur une IP.")
				print("="*50)
				print("1. Honeypot - Permet de savoir si la cible est un pot de miel.")
				print("2. Host - Avoir toutes les informations disponibles sur une adresse IP.")
				print("3. MyIP - Permet d'afficher votre IP publique.")
				print("4. Search - Permet de faire une recherche dans la base de données Shodan.")
				print("5. Commande - Choisir la commande que vous souhaitez exécuter.")
				print("="*50)
				Choix = str(input(BOLD + BLUE + ">>> (Custom Scan) "))
				print(RESET, end='')
				Choix.rstrip("\n")
				verif_choix = verif_choix_shodan_IP(Choix)
				if verif_choix == "1" :
					print("Nous allons maintenant scaner l'adresse IP choisie pour voir si c'est un pot de miel ou non.")
					print("L'intégralité des résultats récupérés seront stockés dans un fichier récupérable dans le répertoire CustomScanOutput")
					print(RED + "Le HoneyPot est une option qui n'est pas totalement aboutie, il est possible que cette dernière ne fonctionne pas à tous les coups !!")
					print(RESET, end='')
					os.system("shodan honeyscore " + verif_souhait + " > OutputShodanHoneyPot")
					print("Le scan est terminé !")
					os.system("mv OutputShodanHoneyPot CustomScanOutput/ ")
					input("Appuyer pour continuer....")

				if verif_choix == "2" :
					print("Nous allons maintenant scaner l'adresse IP choisie pour obtenir toutes les informations disponible à son sujet.")
					print("L'intégralité des résultats récupérés seront stockés dans un fichier récupérable dans le répertoire CustomScanOutput")
					os.system("shodan host " + verif_souhait + " > OutputShodanHost")
					print("Le scan est terminé !")
					os.system("mv OutputShodanHost CustomScanOutput/ ")
					input("Appuyer pour continuer....")

				if verif_choix == "3" :
					print("Cette option permet simplement de récupérer votre adresse IP publique")
					print("Nous n'allons donc pas utiliser la cible que vous avez renseigné ci-dessus.")
					print("L'intégralité des résultats récupérés seront stockés dans un fichier récupérable dans le répertoire CustomScanOutput")
					os.system("shodan myip > OutputShodanMyPublicIP")
					print("Le scan est terminé !")
					os.system("mv OutputShodanMyPublicIP CustomScanOutput/ ")
					input("Appuyer pour continuer....")

				if verif_choix == "4" :
					print("Nous allons réaliser une recherche dans la bases de données Shodan.")
					print("Nous n'allons pas utiliser la cible que vous avez donnée ci-dessus.")
					print("Pour effecetuer cette recherche, nous allons avoir besoin d'un élément à chercher.")
					print("L'intégralité des résultats récupérés seront stockés dans un fichier récupérable dans le répertoire CustomScanOutput")
					print("Dans notre recherche nous allons utiliser des filtres pour avoir l'IP, le port, l'organisme, et le nom d'hôte.")
					print(RED + "Le choix de la cible vous appartient seulement si vous utilisez une mauvaise cible, le résultat du scan sera forcément erroné.")
					print(RESET, end = '')
					cible = str(input(BOLD + BLUE + ">>> (Custom Scan) "))
					print(RESET, end='')
					cible.rstrip("\n")
				
					if verif_cible(cible) == True : 
						os.system("shodan search --fields ip_str,port,org,hostnames " + cible + " > OutputShodanSearch")

					print("Le scan est terminé !")
					os.system("mv OutputShodanSearch CustomScanOutput/ ")
					input("Appuyer pour continuer....")

				if verif_choix == "5" :
					print("Vous êtes libre de choisir la commande que vous voulez utiliser")
					print("L'intégralité des résultats récupérés seront stockés dans un fichier récupérable dans le répertoire CustomScanOutput")
					print(RED + "Aucune indication ne vous sera donnée, si la commande n'est pas bonne, le fichier de sortie affichera l'erreur !")
					print(RESET, end='')
					commande = str(input(BOLD + BLUE + ">>> (Custom Scan) "))
					print(RESET, end='')
					commande.rstrip("\n")
					os.system(commande + " > OutputShodanFreeCommand")
					print("Le scan est terminé !")
					os.system("mv OutputShodanFreeCommand CustomScanOutput/ ")
					input("Appuyer pour continuer....")

			if verif_souhait.count(".") == 2 :
				print("Vous avez décidé de scaner un domaine.")
				print("Voila ce que nous vous proposons d'effectuer sur un domaine.")
				print("="*50)
				print("1. Domain - Avoir toutes les informations disponibles sur un nom de domaine.")
				print("2. MyIP - Permet d'afficher votre IP public.")
				print("3. Search - Permet de faire une recherche dans la base de données Shodan.")
				print("4. Commande - Choisir la commande que vous souhaitez exécuter.")
				print("="*50)
				Choix = str(input(BOLD + BLUE + ">>> (Custom Scan) "))
				print(RESET, end='')
				Choix.rstrip("\n")
				verif_choix_ = verif_choix_shodan_domain(Choix)
				if verif_choix_ == "1" :
					print("Nous allons scanner le domaine cible que nous avons récupéré ci-dessus.")
					print("Ce scan va permettre de récupérer toutes les infos relatives à la cible choisie")
					os.system("shodan domain " + verif_souhait + " > OutputShodanDomain")
					print("Le scan est terminé !")
					os.system("mv OutputShodanDomain CustomScanOutput/ ")
					input("Appuyer pour continuer....")

				if verif_choix_ == "2" : 
					print("Nous n'allons pas vraiment exécuter de scan dans cette situation.")
					print("Nous allons simplement récupérer votre IP public")
					os.system("shodan myip > OutputShodanPublicIP")
					print("L' IP a été récupérée")
					os.system("mv OutputShodanPublicIP CustomScanOutput/ ")
					input("Appuyer pour continuer....")

				if verif_choix_ == "3" :
					print("Nous allons réaliser une recherche dans la bases de données Shodan.")
					print("Nous n'allons pas utiliser la cible que vous avez donnée ci-dessus.")
					print("Pour effecetuer cette recherche, nous allons avoir besoin d'un élément à chercher.")
					print("L'intégralité des résultats récupérés seront stockés dans un fichier récupérable dans le répertoire CustomScanOutput")
					print("Dans notre recherche nous allons utiliser des filtres pour avoir l'IP, le port, l'organisme, et le nom d'hôte.")
					print(RED + "Le choix de la cible vous appartient seulement si vous utilisez une mauvaise cible, le résultat du scan sera forcément erroné.")
					print(RESET, end = '')
					cible = str(input(BOLD + BLUE + ">>> (Custom Scan) "))
					print(RESET, end='')
					cible.rstrip("\n")
				
					if verif_cible(cible) == True : 
						os.system("shodan search --fields ip_str,port,org,hostnames " + cible + " > OutputShodanSearch")

					print("Le scan est terminé !")
					os.system("mv OutputShodanSearch CustomScanOutput/ ")
					input("Appuyer pour continuer....")

				if verif_choix_ == "4" :
					print("Vous êtes libre de choisir la commande que vous voulez utiliser")
					print("L'intégralité des résultats récupérés seront stockés dans un fichier récupérable dans le répertoire CustomScanOutput")
					print(RED + "Aucune indication ne vous sera donnée, si la commande n'est pas bonne, le fichier de sortie affichera l'erreur !")
					print(RESET, end='')
					commande = str(input(BOLD + BLUE + ">>> (Custom Scan) "))
					print(RESET, end='')
					commande.rstrip("\n")
					os.system(commande + " > OutputShodanFreeCommand")
					print("Le scan est terminé !")
					os.system("mv OutputShodanFreeCommand CustomScanOutput/ ")
					input("Appuyer pour continuer....")

		if service['urlscan'] == 'Vraie' :
			print()




		# while Rps != "q" :
		
		# 	if (Rps == "A" or Rps == "a") :
		# 		print("blabla")
				
		# 	if (Rps == "B" or Rps == "b") :
		# 		print("blabla")
			
		# 	if (Rps == "C" or Rps == "c") :
		# 		print("blabla")
				
		# 	if (Rps == "D" or Rps == "d") :
		# 		print("blabla")
	
      #Si l'utilisateur est con ou s'il rentre une mauvaise commande
			# if(Rps != "A" and Rps != "B" and Rps != "C" and Rps != "D" and Rps != "a" and Rps != "b" and Rps != "c" and Rps != "d") :
			# 	print(RED + BOLD + "La commande que vous avez saisie n'existe pas" + RESET)		
		
			# Rps = str(input(BOLD + BLUE + ">>> (Custom scan) "))
			# print(RESET, end = '')
		
	#Help, cela affiche le menu
	if Rps == "h" :
		FirstSummary()
	#Si l'utilisateur rentre une mauvaise commande
	if(Rps != "1" and Rps != "2" and Rps != "3" and Rps != "4" and Rps != "h") :
		print(RED + BOLD + "La commande que vous avez saisie n'existe pas" + RESET)

	Rps = str(input(BOLD + BLUE + ">>> "))
	print(RESET, end = '')
