import os #Module qui va permettre de passer des commandes systèmes.
import pyfiglet # On importe le module qui permet de faire un menu sympa
import requests # Module qui va permettre de faire des requêtes à l'API URLscan.io
import json # Module permettant de manipuler des fichiers json. (proche du XML)
import time # Nécessaire pour faire attendre le code quelques secondes pour récupérer le résultat de URLSCAN

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
		os.system("theHarvester -d " + domain + " " + "-b all > OutputHarvester")# On lance le scan avec le nom de domaine donné par l'utilisateur. On récupère l'intégralité de la sortie dans un fichier.
		#Ci-dessous il faudrat appeler la fonction 'tri_result_harvester' pour trier le fichier de résultat et peut être faire un affichage plus propre.
		

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
		os.system("curl https://urlscan.io/api/v1/result/" + uuid + "/ > OutputURLScan")#On récupère le résultat du scan dans un fichier.
		#On stocke le fichier de sortie dans un tableau en attendant

		
		os.system("mkdir DefaultScanResult/")
		os.system("chmod -R 700 DefaultScanResult/")
		if Rps2 == "1":
			os.system("mv OutputShodanIP DefaultScanResult/")
		elif Rps2 == "2":
			os.system("mv OutputShodanDomain DefaultScanResult/")

		os.system("mv OutputHarvester DefaultScanResult/")
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
		print(BOLD + BLUE + "Veuillez choisir une option : " + RESET)
		print("="*50)
		print("A : Dnscan")
		print("B : TheHarvester")
		print("C : Shodan")
		print("D : Urlscan")
		print("q : Quit")
		print("="*50)
		
		Rps = str(input(BOLD + BLUE + ">>> (Custom scan) "))
		print(RESET, end = '')
		while Rps != "q" :
		
			if (Rps == "A" or Rps == "a") :
				print("blabla")
				
			if (Rps == "B" or Rps == "b") :
				print("blabla")
			
			if (Rps == "C" or Rps == "c") :
				print("blabla")
				
			if (Rps == "D" or Rps == "d") :
				print("blabla")
	
      #Si l'utilisateur est con ou s'il rentre une mauvaise commande
			if(Rps != "A" and Rps != "B" and Rps != "C" and Rps != "D" and Rps != "a" and Rps != "b" and Rps != "c" and Rps != "d") :
				print(RED + BOLD + "La commande que vous avez saisie n'existe pas" + RESET)		
		
			Rps = str(input(BOLD + BLUE + ">>> (Custom scan) "))
			print(RESET, end = '')
		
	#Help, cela affiche le menu
	if Rps == "h" :
		FirstSummary()
	#Si l'utilisateur est con ou s'il rentre une mauvaise commande
	if(Rps != "1" and Rps != "2" and Rps != "3" and Rps != "4" and Rps != "h") :
		print(RED + BOLD + "La commande que vous avez saisie n'existe pas" + RESET)

	Rps = str(input(BOLD + BLUE + ">>> "))
	print(RESET, end = '')
