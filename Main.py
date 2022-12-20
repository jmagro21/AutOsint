import os #Module qui va permettre de passer des commandes systèmes.
import pyfiglet # On importe le module qui permet de faire un menu sympa
import requests # Module qui va permettre de faire des requêtes à l'API URLscan.io
import json # Module permettant de manipuler des fichiers json. (proche du XML)
import time # Nécessaire pour faire attendre le code quelques secondes pour récupérer le résultat de URLSCAN
import yaml # On importe le module yaml pour manipuler les fichier du même nom.
import csv #On importe csv dont nous allons nous servir par la suite avec URLscan.io
# Installation de tous les paquets nécessaires au script dans un autre fichier pour être sûr et certain que la machine va être capable de lire le script.

BOLD = '\033[1m' # Code couleur qui nous permet de rendre le script un peu plus joli
BLUE = '\033[94m' # La couleur bleue
GREEN = '\033[92m' # La couleur verte
RED = '\033[31m' # La couleur rouge
RESET = '\033[0m' # La couleur normale.

def verif_dependance (a) : # Fonction qui vérifie l'entrée utilisateur demandée pour l'installation des dépendances nécessaires au script et pour les différents outils de la partie Custom Scan.
	while a != "1" and a != "2" : # Si différent des deux options qu'on propose on redemande en boucle.
		print("Veuillez saisir une valeur accepté, 1 ou 2")
		a = str(input(BOLD + BLUE + ">>> "))#On récupère l'entrée utilisateur.
		print(RESET, end='')#On reset la couleur.
	return a#On renvoie l'entrée utilisateur verifiée.


#On demande à l'utilisateur si il veut installer toutes les dépendances et le outils.*
#Il est conseillé dans le read.me d'installer les dépendances avant et de quand même installer tous les outils nécessaires au script.
titre0 = pyfiglet.figlet_format("Installation des outils nécessaires", font = "slant" )#on affiche le titre de l'installation.
print(titre0)
print("="*50)
print("Voulez-vous installer toutes dépendances nécessaires pour le script ? \n")#Menu qui va permettre de récupèrer la réponse utilisateur.
print("1. Oui")
print("2. Non")
print("="*50)
print("\n")
Rps = str(input(BOLD + BLUE + ">>> "))#On récupère l'entrée utilisateur.
print(RESET, end='')#On reset la couleur.
apres_verif = verif_dependance(Rps)#On vérifie la réponse utilisateur.
#On va installer tout les paquets nécessaires pour que le script fonctionne correctement.
#On installe tous les outils nécessaires pour que ce script soit utilisable sur l'ensemble des postes.
#Qu'il soit le plus modulable possible.


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
	os.system("rm -r dnscan/") # On attribue tous les droits à l'utilisateur root.
	os.system("chmod -R 700 ../*")

	#theHarvester
	os.system("apt-get install theharvester") # Install de theHarvester

	#urlscan.io
	os.system("python3 -m pip install requests") # On installe les modules nécessaires pour manipuler l'API.

elif apres_verif == "2" :
	print("\0") # Si l'utilisateur refuse l'installation, il faut afficher quelque chose dans tous les cas alors on affiche un espace vide.

print("="*50)
print("\n")

#Ci-dessous vous allez retrouver l'intégralité des fonctions qui permettent de vérifier les entrées utilisateurs tout au long du script.
#Chacunes d'elles est unique mais elles se ressemblent plus ou moins toutes.
# Vous trouverez des commentaires pour chacunes d'elles pour mieux les comprendre.

def verif_IP (a) :# Permet de vérifier la bonne entrée d'une adresse IP.
	nb = a.count(".") #On compte le nombre de point dans l'entrée
	while nb != 3 : #Si le nombre de point est différent de 3 alors ce n'est pas une adresse IP.
		print("Veuillez saisir une adresse IP ! Exemple : 8.8.8.8") # On redemande en boucle à l'utilisateur.
		a = str(input(BLUE + BOLD + ">>> (Default Scan) ")) # On récupère l'entrée
		print(RESET, end='')# On reset la couleur
		nb = a.count(".") #On recompte le nombre de point pour pouvoir boucler.
	return a # On renvoie la valeur rentrée par l'utilsateur vérifiée.

def verif_domain (a) :
	nb = a.count(".") # On compte le nombre de point.
	while nb != 2 :# Si le nombre de point n'est pas exactement 2 alors on redemande en boucle à l'utilisateur.
		print("Veuillez saisir un nom de domaine acceptable ! Exemple : www.nomdedomaine.org")
		a = str(input(BOLD + BLUE + ">>> (Default Scan) ")) # On récupère la réponse.
		print(RESET, end='')# On reset la couleur.
		nb = a.count(".")# On recompte pour pour pouvoir continuer à boucler.
	return a # On récupère l'entrée utilisateur vérifiée.

def verif_domain_harvester (a) :
	nb = a.count(".")# On compte le nombre de point
	while nb != 1 :# Pour harvester, le nom de domaine ne comprend pas le "www" donc il n'y a plus qu'un point dans le nom de domaine
		print("Veuillez saisir un nom de domaine comme ceci : le-pointcom.fr")#Si on ne retrouve pas qu'un seul point dans l'entrée utilisateur, alors on redemande en boucle.
		a = str(input(BOLD + BLUE + ">>> (Default Scan) "))#On récupère l'entrée utilisateur
		print(RESET, end='')#On reset la couleur.
		nb = a.count(".")#On compte le nombre de point pour pouvoir continuer à boucler.
	return a#On retourne l'entrée utilisateur vérifiée.

def verif_domain_dnscan (a) :
	nb = a.count(".") # On compte le nomnbre de point
	while nb != 2 : #Pour dnscan, le domaine doit contenir le "www", alors il nous faut deux points pour avoir une entrée valide. 
		print("Veuillez saisir un nom de domaine comme ceci : www.le-pointcom.fr")
		a = str(input(BOLD + BLUE + ">>> (Default Scan) ")) #On récupère l'entrée utilisateur. 
		print(RESET, end='')#On reset la couleur
		nb = a.count(".")#On recompte le nombre de point pour boucler.
	return a #On renvoie l'entrée utilisateur vérifiée.

def verif_urlscan_lien(a) :
	nb = a.count(".")#On compte le nombre de point
	nb1 = a.count("/")#On compte le nombre de slash.
	nb2 = a.count(":")#On compte le nomnre de ":".
	while nb != 2 and nb1 != 3 and nb2 != 1 :#Pour URLscan.io, les url fournit doivent posséder 3 "/", 2 "." et 1 ":"
		print("Veuillez saisir un nom de domaine comme ceci : www.le-pointcom.fr")
		a = str(input(BOLD + BLUE + ">>> (Default Scan) "))#On récupère l'entrée utilisateur
		print(RESET, end='')#On reset la couleur
		nb = a.count(".")#On recompte tout les éléments pour pouvoir boucler.
		nb1 = a.count("/")
		nb2 = a.count(":")
	return a#On revoie l'entrée utilisateur vérifiée.

def FirstSummary () :
	print(BOLD + BLUE + "Veuillez choisir une option : " + RESET)
	print("="*50)
	print("1 : Default scan") # Mettre en place une configuration de scan prédéfinie pour l'utilisateur
	print("2 : Custom scan") # Mettre en place une solution pour ce scan où l'utilisateur peut choisir les types de scan qu'il souhaite effectué aves les différents outils.
	print("h : Help") # Permet à l'utilisateur d'avoir des informations sur les outils et comment s'en servir.
	print("q : Quit") # Permet à l'utilisateur de quitter le script.
	print("="*50)
	#Permet d'afficher le menu principal avec les différentes options offertes à l'utilisateur.

def verif_RPS_FirstSummary(a) :
	while a != "1" and a != "2" and a != "h" and a != "q" : # On regarde si l'entrée de l'utilisateur correspond à l'une des options.
		print("Veuillez sélectionner une option valable : 1, 2, h ou q ") 
		a = str(input(BOLD + BLUE + ">>> (Default Scan) ")) # Tant que ce n'est pas le cas, on lui redemande une entrée correcte. 
		print(RESET, end = '') # On reset la couleur du texte.
	return a # Ensuite on retourne la valeur de a qui est l'entrée utilisateur.

def SummaryTools () :
	print(BOLD + BLUE + "Veuillez choisir une option : " + RESET)#On demande à l'utilisateur l'outil qu'il souhaite utiliser.
	print("="*50)
	print("a : Dnscan")
	print("b : TheHarvester")
	print("c : Shodan")
	print("d : Urlscan")
	print("q : Quit")
	print("="*50)

def verif_tools (a) :
	while a != "a" and a != "b" and a != "c" and a != "d" and a != "q":#Si l'entrée utilisateur ne correspond à aucune des options.
		print("Veuillez saisir une réponse acceptée !")
		a = str(input(BOLD + BLUE + ">>> (Custom Scan) "))#On redemande une entrée à l'utilisateur en boucle jusqu'à ce qu'elle remplisse les conditions.
		print(RESET, end='')#On reset la couleur.
	return a#On retourne l'entrée utilisateur vérifiée.

def autre_outil () :
	print("="*50)#Affiche le menu pour savoir si l'utilisateur veut utiliser un autre outil ou passer à l'exécution.
	print("Voulez-vous utilisez un autre outil ?")
	print("1. Oui")
	print("2. Non, passer à l'execution")
	print("="*50)

def verif_souhait (a) :
	while a != "h" and a != "ggl" and a != "do" and a != "p" and a != "ex" :#On vérifie l'entrée utilisateur, si elle ne correspon à aucune des propositions.
		print("Veuillez saisir une réponse parmi celle proposées ! Exemple : ggl")#On redemande à l'utilisateur, en boucle, de choisir une option valide.
		a = str(input(BOLD + BLUE + ">>> (Custom Scan) "))#On récupère l'entrée utilisateur.
		print(RESET, end='')#On reset la couleur
	return a#On retourne l'entrée utilisateur vérifiée.

def verif_souhait_shodan (a) :
	nb = a.count(".")#On compte le nombre de "."
	while nb != 2 and nb != 3 :#Si le nombre de "." n'est pas égal à 2(www.le-pointcom.fr) et à 3 (8.8.8.8), on redemande à l'utilisateur en boucle. 
		print("Veuillez saisir un nom de domaine ou une adresse IP dans le format suivant ! IP : 8.8.8.8 ; domaine : www.test.fr")
		a = str(input(BOLD + BLUE + ">>> (Custom Scan) "))#on récupère l'entrée utilisateur.
		print(RESET, end='')#On reset la couleur.
	return a#On récupère l'entrée utilisateur vérifiée.

def verif_choix_shodan_IP (a) :
	while a != "1" and a != "2" and a != "3" and a != "4" and a != "5" :#Si l'entrée n'est pas égale aux différentes options
		print("Veuillez saisir une réponse acceptée : 1,2,3,4 ou 5")#On redemande à l'utilisateur en boucle.
		a = str(input(BOLD + BLUE + ">>> (Custom Scan) "))#On récupère l'entrée utilisateur.
		print(RESET, end='')#On reset la couleur.
	return a#Renvoie l'entrée utilisateur vérifiée.

def verif_cible (a) :
	x = isinstance(a, str)#Permet de vérifier si une valeur est de type str (Renvoie "True" si c'est une valeur str)
	while x != True :#Tant que l'entrée utilisateur n'est pas de type 'str'
		print("Veuillez saisir une chaîne de caractères !")#On redemande à l'utilisateur une entrée correcte.
		a = str(input(BOLD + BLUE + ">>> (Custom Scan) "))#On récupère la réponse
		print(RESET, end='')#On reset la couleur.
		x = isinstance(a, str)#On revérifie si la valeur est true pour pouvoir boucler.
	return x#On renvoie la valeur stockée dans la variable x (True or False). Forcément True.

def verif_choix_shodan_domain (a) :
	while a != "1" and a != "2" and a != "3" and a != "4" :#Si l'entrée ne correspond à aucunes des options.
		print("Veuillez saisir une réponse acceptée : 1,2,3,4 ou 5")#On redemande en boucle
		a = str(input(BOLD + BLUE + ">>> (Custom Scan) "))#On récupère l'entrée utilisateur 
		print(RESET, end='')#On reset la couleur.
	return a#On retourne la valeur vérifiée.

def verif_choice_dnscan (a) :
	while a != "1" and a != "2" :#Si != 1 et 2 alors on demande à l'utilisateur une autre entrée.
		print("Veuillez sélectionner l'une des deux options qui vous est offert par le chiffre indiqué : 1 ou 2")
		a = str(input(BOLD + BLUE + ">>> (Custom Scan) "))#On récupère l'entrée utilisateur. 
		print(RESET, end='')#On reset la couleur.
	return a#On renvoie l'entrée utilisateur vérifiée.

def verif_option_dnscan (a):
	while a != "1" and a != "2" and a != "3" and a != "4" and a != "5" and a != "6":#Si l'utilisateur ne sélectionne pas une des options proposées, alors on redemande en boucle une valeur acceptée.
		print("Veuillez choisir une des options qui est mises à votre disposition !")
		a = str(input(BOLD + BLUE + ">>> (Custom Scan) "))#On récupère l'entrée utilisateur.
		print(RESET, end='')#On reset la couleur.
	return a#On renvoie l'entrée utilisateur vérifiée.

def verif_list_dnscan(a):#Dans cette fonction, on vérifie que le nom du fichier est acceptable parmis ceux qui sont proposés.
	while a != "subdomains.txt" and a != "subdomains-100.txt" and a != "subdomains-500.txt" and a != "subdomains-1000.txt" and a != "subdomains-10000.txt" and a != "subdomains-uk-500.txt" and a != "subdomains-uk-1000.txt" :
		print("Veuillez saisir un nom de fichier acceptable parmi ceux qui vous sont proposés.")
		a = str(input(BOLD + BLUE + ">>> (Custom Scan) "))#On récupère la réponse utilisateur.
		print(RESET, end='')#On reset la couleur.
	return a#On renvoie la réponse utilisateur vérifiée.

def verif_resolver_dnscan(a):
	nb = a.count(".")#On compte le nombre de "."
	while nb != 3 :#Il nous faut 3 points car dans une adresse IP, on a trois points.
		print("Veuillez saisir une adresse IP ! Exemple : 8.8.8.8")#Si l'utilisateur donne une adresse qui n'est pas de ce format, on redemande en boucle.
		a = str(input(BLUE + BOLD + ">>> (Custom Scan) "))#On récupère l'entrée utilisateur.
		print(RESET, end='')#On reset la couleur.
		nb = a.count(".")#On compte le nombre de "." pour pouvoir boucler.
	return a#On retourne l'entrée utilisateur vérifiée.

def verif_fin_choix(a):
	while a != "1" and a != "2" :#Si la valeur n'est pas 1 ou 2
		print("Veuillez choisir une option autorisée ! 1 ou 2")#On redemande en boucle à l'utilisateur une valeur acceptable.
		a = str(input(BOLD + BLUE + ">>> "))#On récupère la réponse de l'utilisateur. 
		print(RESET, end='')#On reset la couleur.
	return a#Renvoie la valeur vérifiée.

def choix_fin_default_scan(a):
	while a != "q" and a != "h" :#Si réponse != des deux options.
		print("Veuillez sélectionner une option valide ! q ou h")#On redemande en boucle à l'utilisateur une entrée correcte.
		a = str(input(BOLD + BLUE + ">>> "))#On récupère l'entrée utilisateur.
		print(RESET, end='')#On reset la couleur.
	return a#On retourne l'entrée utilisateur vérifiée.

def verif_option_resultat(a) :
	while a != "1" and a != "2" and a != "3" :#Si différents des choix proposés
		print("Veuillez saisir une réponse autorisée ! Exemple : 1, 2 ou 3")#On demande en boucle à l'utilisateur d'entrée une option valide.
		a = str(input(BOLD + BLUE + ">>> (Custom Scan) "))#On récupère l'entrée utilisateur.
		print(RESET, end='')#On reset la couleur.
	return a#Renvoie la valeur vérifiée.

#Affichage de ma baniere
titre = pyfiglet.figlet_format("AutOsint", font = "slant" )
print(titre) # On paramètre le titre que l'on souhaite afficher et on l'affiche.

FirstSummary() # On appel la fonction FirstSummary qui contient le menu principal de notre script.
# Cf. La fonction ci-dessus pour plus de détails.

reponse = str(input(BOLD + BLUE + ">>> ")) # On récupère l'entrée utilisateur avec une certaine mise en forme, plus jolie.
print(RESET, end = '')#On reset la couleur du texte pour ne pas l'appliquer à la suite. On le fera tout au long du code.
Rps = verif_RPS_FirstSummary(reponse) # On vérifie l'entrée utilisateur avant de l'utiliser.
# L'utilisateur doit saisir 1, 2, h ou q et pas une autre entrée.
# Si l'utilisateur choisit l'option "q", il n'exécutera jamais la suite du script.

while Rps != "q" : # Ici, tant que l'utilisateur n'a pas sélectionné "q" comme quitter, alors on exécute la suite.

	#On lance tous les outils les uns après le autres avec les paramètres les plus rapides pour fournir des résultats à l'utilisateur sans personnalisation.
	if Rps == "1" : # Si l'utilisateur choisit la première option, alors on lance le scan par défaut.
		print("Nous allons dans un premier temps utiliser l'outil Shodan qui permet de récupèrer des informations sur une cible bien définie !")
		print("A la base cet outil est un moteur de recherche qui référence le balayage massif des ports sur internet !")
		print("Il est possible de l'utiliser en ligne de commande et dans cette situation le script se charge de tout !")
		print("Voulez-vous scanner une IP ou un domaine ?")
		print("="*50) # On laisse le choix à l'utilsiateur si la cible
		print("1. IP") # Une IP 
		print("2. Domaine") # Un domaine
		print("="*50)
		Rps2 = str(input(BOLD + BLUE + ">>> (Default Scan) ")) # On récupère la cible que l'utilisateur a choisit.
		print(RESET, end='')# On reset la couleur.
		
		while Rps2 != "1" and Rps2 != "2" : # On vérifie l'entrée utilisateur directement dans le code.
			print(RED + "Veuillez saisir une commande valide !")
			Rps2 = str(input(BOLD + BLUE + ">>> (Default Scan)")) # On récupère la réponse de l'utilisateur
			print(RESET, end='')
			# Tant que l'utilisateur ne rentre pas l'une des deux options, il ne passe pas à la suite du script.

		if Rps2 == "1" : # Si il a choisit de scanner une IP, on exécute cette partie.
			print("Veuillez saisir l'IP que vous voulez scanner !")
			Rps3 = str(input(BOLD + BLUE + ">>> (Default Scan) ")) # On récupère l'IP cible
			print(RESET, end='')# On reset la couleur.
			IP = verif_IP(Rps3) # On vérifie l'entrée utilisateur rentre bien une IP. (cf. fonction ci-dessus.)
			os.system("shodan host " + IP + " > OutputShodanIP") # On scan et on enregistre dans un fichier de sortie.

		if Rps2 == "2" : # Si il a choisit de scanner un domaine, on exécute cette partie.
			print("Veuille saisir le domaine que vous voulez scanner !")
			Rps3 = str(input(BOLD + BLUE + ">>> (Default Scan) ")) # On récupère le domaine cible
			print(RESET, end='')#On reset la couleur
			DOMAIN = verif_domain(Rps3) # On vérifie que l'utilisateur a bien rentré un domaine (cf. fonction ci-dessus)
			os.system("shodan domain " + DOMAIN + " > OutputShodanDomain") # On scan et on enregistre dans un fichier de sortie


		print("\n")

		# On passe à l'outil suivant : theHarvester
		print("Nous allons effectuer un scan également sur un nom de domaine avec l'outil theHarvester !")
		print("Veuillez simplement indiquer le nom de domaine que vous voulez cibler !")
		print("Attention ne pas saisir le 'www' du nom de domaine !!!! Exemple : test.fr ")
		Rps = str(input(BOLD + BLUE + ">>> (Default Scan) ")) # On récupère l'entrée utilisateur.
		print(RESET, end='')# On reset la couleur
		domain = verif_domain_harvester(Rps) # On vérifie que le nom de domaine entré est valide.
		os.system("theHarvester -d " + domain + " " + "-b all > OutputHarvester")#On lance le scan avec le nom de domaine donné par l'utilisateur et on stocke ça dans un fichier.
		

		print("\n")

		#On passe à l'outil suivant : Dnscan
		print("Nous allons maintenant lancer un scan avec l'outil dnscan pour récupérer des informations liés au DNS !")
		print("Veuillez simplement saisir le domaine que vous voulez visez et le script se charge du reste !")
		print("Pour ce script, vous devez utilisez l'intégralité du nom de dommaine. Exemple : www.test.fr ")
		Rps = str(input(BOLD + BLUE + ">>> (Default Scan) "))#On récupère l'entrée utilisateur
		print(RESET, end='')# On reset la couleur
		domaine = verif_domain_dnscan(Rps)#On vérifie si le domaine entrée est bien valide.
		os.system("python3 dnscan.py -d " + domaine + " -o OutputDNScan")#On exécute la commande et on stocke le résultat dans un fichier.
		
		
		print("\n")

		#On passe à l'outil suivant : URLscan.io
		print("Nous allons maintenant utiliser l'outil urlscan.io qui permet de récupérer des informations sur des URL")
		print("Il vous suffit d'indiquer l'url que vous voulez scanner !")
		print("Vous devez donner l'intégralité du lien !! Exemple : https://www.instagram.com/")
		Rps = str(input(BOLD + BLUE + ">>> (Default Scan) "))#On récupère l'entrée utilisateur.
		print(RESET, end='')#On reset la couleur.
		FQDN = verif_urlscan_lien(Rps)#On vérifie l'entrée utilisateur pour voir si le lien est acceptable.
		headers = {'API-Key':'27a5f4bf-340a-47dd-a710-7a3038a97321','Content-Type':'application/json'}
		data = {"url": Rps, "visibility": "public"}
		response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
		#Ci-dessus, on retrouve les variables qui vont accueillir les différentes requêtes que l'on va adresser à l'API d'URLscan.io.
		#On y retrouve l'API Key que nous avons décider de laisser en clair dans le code à des finds pédagogiques.
		#Évidemment dans un code professionnel cette dernière ne pourrait apparaitre en clair dans le code.
		os.system("touch ResultURLScanIo.txt")#On créer le fichier qui va reçevoir le résultat de la demande de scan.
		fichier = open('ResultURLScanIo.txt', 'w')
		for ligne in response :
			fichier.write(str(ligne))#On écrit toute la réponse dedans.
		fichier.close()#On ferme le fichier.
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
		#Dans la réponse de l'API, on retrouve l'identifiant unique (UUID) du scan que nous avons demandé.
		#Nous le récupérons pour interroger l'API de résultat et obtenir le résultat du scan.

		time.sleep(22) # On fige le code pendant 22 secondes pour atteindre que le scan soit terminé.
		#Et que le résulat puisse être récupéré.
		
		os.system("curl https://urlscan.io/api/v1/result/" + uuid + "/ > OutputURLScan.json")#On récupère le résultat du scan dans un fichier.
		#On va convertir le fichier de sortie en yaml pour que l'utilisateur est un fichier plus simple à parcourir.
		with open('OutputURLScan.json', 'r') as file:
			configuration = json.load(file) #On charge le fichier "json" 

		with open('OutputURLScan.yaml', 'w') as yaml_file:
			yaml.dump(configuration, yaml_file)#On écrit tout son contenu dans le fichier "yaml"

		os.system("mkdir DefaultScanResult/") # On créer un dossier qui va accueillir tous les résultats du defaultscan.
		os.system("chmod -R 700 DefaultScanResult/")#On lui attribue tous les droits pour l'utilisateur root et rien pour les autres.
		if Rps2 == "1":
			os.system("mv OutputShodanIP DefaultScanResult/")
		elif Rps2 == "2":
			os.system("mv OutputShodanDomain DefaultScanResult/")
		#Pour choisir quel fichier shodan nous allons déplacer, il faut savoir si l'utilisateur a choisit une IP ou un domaine.
		#C'est pour cela que l'on utilise cette fonction "if".
		os.system("mv OutputHarvester DefaultScanResult/")#On déplace le résultat de Harvester
		os.system("mv OutputDNScan DefaultScanResult/")#On déplace le résultat de DNScan
		os.system("rm ResultURLScanIo.txt")#On supprime le résultat de la demande de scan de URLscan.io
		os.system("mv OutputURLScan.yaml DefaultScanResult/")#On déplace le résultat de scan de URLscan.io en json
		os.system("mv OutputURLScan.json DefaultScanResult/")#On déplace le résultat de scan de URLscan.io en yaml
		
		print("Nous avons exécuter l'ensemble des outils avec les paramètres par défaut !")
		print("Vous pouvez retrouver l'ensemble des résultats dans le dossier DefaultScanResult \n")
		print("Voulez-vous continuer le script ou quitter ce dernier ?")
		print("="*50)#Menu permettant à l'utilisateur de quitter le script ou de retourner au menu principal pour continuer à utiliser le script.
		print("q. Quitter le script ")
		print("h. Revenir au menu principal ")
		print("="*50)
		Rps = str(input(BOLD + BLUE + ">>> (Default Scan) "))#On récupère la réponse
		print(RESET, end='')#On reset la couleur.
		VERIF = choix_fin_default_scan(Rps)#On vérifie que l'utilisateur a bien choisit l'une des deux options.

		if VERIF == "q" :
			exit() # Si l'utilisateur sélectionne "q" alors il quitte le script.
		
		if VERIF == "h" :#Si l'utilisateur sélectionne "h" alors il retournera au menu principal pour continuer  d'utiliser le script.
			FirstSummary()#Le FirstSummary, menu du début.
			Rps = str(input(BOLD + BLUE + ">>> "))#On récupère le choix de l'utilisateur sur le menu principal.
			print(RESET, end='')#On reset la couleur. 

	#Si l'utilisateur sélectionne "2", il pourra réaliser un scan personnalisé.
	#Il va pouvoir choisir les différents outils qu'il veut utiliser.
	#Nous allons voir.
	if Rps == "2" :

		os.system("mkdir CustomScanOutput/")#On créer dès le début le répertoire CustomScan qui va permettre de stocker tous les résultats du Custom Scan.

		print("Avant de démarrer il est important de préciser que cette partie ne vous expliquera pas le fonctionnement de chaque outil !")
		print("Il est de votre fait de vous renseigner sur chaque outil avant d'utiliser cette partie du script !")
		print("Enjoyyyy !")
		#On prévient l'utilisateur que nous n'allons pas le renseigner sur chaque outil car ce n'est pas le but de l'outil.

		#Dans les fichiers du script, on retrouve un fichier "config.yaml" avec la liste des outils que nous allons utiliser.
		#Par défaut, ils sont tous à "Faux" pour indiquer qu'ils sont désactivés.
		#Nous allons utiliser ce fichier, le modifier pour activer ou non, en fonction des réponses utlisateurs, les outils.
		with open('config.yml', 'r') as file :
			service = yaml.safe_load(file)#On charge le fichier 
		
		SummaryTools()#On affiche le menu des différents outils (cf. Fonction ci-dessus.)

		Tool_Rps = str(input(BOLD + BLUE + ">>> (Custom scan) "))#On récupère la réponse de l'utilisateur
		print(RESET, end = '')#On reset la couleur.
		Tool_Rps.rstrip("\n")#On supprime le saut de ligne en fin de chaîne de caractère qui est là par défaut.
		Tools1 = verif_tools(Tool_Rps)#On vérifie l'entrée utilisateur, pour être sur qu'il a sélectionné un des 4 outils ou l'option quitter.
		if Tools1 == "a" :#On modifie le fichier yaml en fonction de l'option choisie par l'utilisateur.
			service['Dnscan'] = 'Vraie'#Si Tools1 = a 
		elif Tools1 == "b" :
			service['Harvester'] = 'Vraie'#Si Tools1 = b
		elif Tools1 == "c" :
			service['shodan'] = 'Vraie'#Si Tools1 = c
		elif Tools1 == "d" :
			service['urlscan'] = 'Vraie'#Si Tools1 = d
		elif Tools1 == "q" :
			exit()#Si Tools1 = "q"

	
		autre_outil()#Fonction permettant de demander à l'utilisateur s'il souhaite utiliser un outre outil ou passer à l'exécution. 
		Autre_outil = str(input(BOLD + BLUE + ">>> (Custom Scan) "))#On récupère l'entrée utilisateur.
		print(RESET, end='')#On reset la couleur.
		verif_autreOutil = verif_dependance(Autre_outil)#On vérifie l'entrée utilisateur avec une petite fonction.
		if verif_autreOutil == "1" :#Si l'utilisateur souhaite utiliser un autre outil, on affiche le menu d'outils.
			SummaryTools()
			Tool_Rps = str(input(BOLD + BLUE + ">>> (Custom scan) "))#On récupère la réponse
			print(RESET, end = '')#On reset la couleur.
			Tool_Rps.rstrip("\n")#On supprime le saut de ligne automatique à la fin de l'entrée utilisateur.
			Tools2 = verif_tools(Tool_Rps)#On vérifie que c'est une bonne entrée, une entrée autorisée.
			if Tools2 == "a" :
				service['Dnscan'] = 'Vraie'#Si Tools2 = a
			elif Tools2 == "b" :
				service['Harvester'] = 'Vraie'#Si Tools2 = b
			elif Tools2 == "c" :
				service['shodan'] = 'Vraie'#Si Tools2 = c
			elif Tools2 == "d" :
				service['urlscan'] = 'Vraie'#Si Tools2 = d
			elif Tools2 == "q" :
				exit()#Si Tools2 = q

			autre_outil()#On propose encore un autre outil à l'utilisateur.
			Autre_outil = str(input(BOLD + BLUE + ">>> (Custom Scan) "))# On récupère l'entrée utilisateur.
			print(RESET, end='')#On reset la couleur.
			verif_autreOutil = verif_dependance(Autre_outil)#On vérifie si l'entrée est correcte.
			if verif_autreOutil == "1" :#Si l'utilisateur veut choisir un autre outil, on affiche le menu d'outils.
				SummaryTools()
				Tool_Rps = str(input(BOLD + BLUE + ">>> (Custom scan) "))#On récupère le choix de l'utilisateur.
				print(RESET, end = '')#On reset la couleur.
				Tool_Rps.rstrip("\n")#On supprime le saut de ligne automatique.
				Tools3 = verif_tools(Tool_Rps)#On vérifie l'entrée utilisateur. 
				if Tools3 == "a" :
					service['Dnscan'] = 'Vraie'#Si Tools3 = a
				elif Tools3 == "b" :
					service['Harvester'] = 'Vraie'#Si Tools3 = b
				elif Tools3 == "c" :
					service['shodan'] = 'Vraie'#Si Tools3 = c
				elif Tools3 == "d" :
					service['urlscan'] = 'Vraie'#Si Tools3 = d
				elif Tools3 == "q" :
					exit()#Si Tools3 = q
				
				autre_outil()#On propose un autre outil à l'utilisateur.
				Autre_outil = str(input(BOLD + BLUE + ">>> (Custom Scan) "))#On récupère la réponse.
				print(RESET, end='')#On reset la couleur.
				verif_autreOutil = verif_dependance(Autre_outil)#On vérifie l'entrée utilisateur.
				if verif_autreOutil == "1" :#Si l'utilisateur veut un autre outil, on affiche le menu d'outils.
					SummaryTools()
					Tool_Rps = str(input(BOLD + BLUE + ">>> (Custom scan) "))#On récupère la réponse.
					print(RESET, end = '')#On reset la couleur.
					Tool_Rps.rstrip("\n")#On supprime le saut de ligne automatique.
					Tools4 = verif_tools(Tool_Rps)#On vérifie l'entrée utilisateur.
					if Tools4 == "a" :
						service['Dnscan'] = 'Vraie'#Si Tools4 = a
					elif Tools4 == "b" :
						service['Harvester'] = 'Vraie'#Si Tools4 = b
					elif Tools4 == "c" :
						service['shodan'] = 'Vraie'#Si Tools4 = c
					elif Tools4 == "d" :
						service['urlscan'] = 'Vraie'#Si Tools4 = d
					elif Tools4 == "q" :
						exit()#Si Tools4 = q

		else :
			print("\0")#Si l'utilisateur choisit directement de ne plus utiliser d'autres outils alors on affiche rien
			#On passe à la suite du code : l'exécution des outils et sélection des options.
		

		with open('config.yml', 'w') as dump_file :
			yaml.dump(service, dump_file)#On sauvegarde les changements effectués, on les écrits dans le fichier.

		print(RESET + "Maintenant que vous avez choisi vos outils, nous allons vous demandez les différentes options que vous souhaitez utiliser avec ces derniers !")
		print(RESET + "Allons-y !")
		
		with open('config.yml', 'r') as file :
			service = yaml.safe_load(file)#On charge le fichier avec les changements.
		
		if service['Dnscan'] == 'Vraie' :#Si dans le fichier, l'outil est activé alors on exécute le code suivant.
			print("Vous allez paramétrer DnScan !")
			print("DnsScan peut fonctionner soit avec un seul domaine soit avec une liste de domaine !")
			print("Votre premier choix va être de choisir entre une liste de domaine à scanner ou un seul !")
			print(RED + "ATTENTION : Si vous voulez attaquer plusieurs domaines, ces derniers doivent se trouver dans un fichier avec un domaine par ligne.")
			print(RED + "Si vous ne savez pas manipuler cette option le script ne fonctionnera pas ! Renseignez-vous au préalable.")
			print(RED + "Il faut placer le fichier contenant tous les domaines à la racine du script pour que ça fonctionne !")
			print(RESET, end='')
			print("="*50)#Menu permettant à l'utilisateur de choisir d'utiliser l'outil soit sur un seul domaine, soit sur une liste de domaine.
			print("1. Un seul domaine")
			print("2. Plusieurs domaines")
			print("="*50)
			choix = str(input(BOLD + BLUE + ">>> (Custom Scan) "))#On récupère l'entrée utilisateur.
			print(RESET, end='')#On reset la couleur.
			verification = verif_choice_dnscan(choix)#On vérifie que l'entrée utilisateur correpond bien à l'une des options proposées.

			if verification == "1" :# Si l'utilisateur veut scanner un seul domaine on exécute ce code.
				print("Nous allons donc scanner un seul domaine.")
				print("Veuillez indiquer la cible que vous voulez scanner. Exemple : www.le-pointcom.fr")#On demande la cible à l'utilisateur.
				cible = str(input(BOLD + BLUE + ">>> (Custom Scan) "))#On récupère l'entrée utilisateur.
				print(RESET, end='')#On reset la couleur.
				verification_cible = verif_domain_dnscan(cible)#On vérifie l'entrée utilisateur pour vérifier que le domaine est acceptable et correct.
				print("Maintenant que nous avons la cible, voici les options qui sont à votre disposition.")
				print("="*50)#Menu des options.
				print("1. Domain - Récupérer toutes les informations liées à un domaine.") 
				print("2. IP - Récupère toutes les IP découvertes dans un fichier texte !")
				print("3. Quick - Permet de réaliser un scan rapide.")
				print("4. No IP - Ne pas afficher les adresses IP dans le fichier de résultat.")
				print("5. Resolver - Utiliser un autre service DNS que celui du système.")
				print("6. Commande libre - Utiliser la commande que vous voulez.")
				print("="*50)
				option = str(input(BOLD + BLUE + ">>> (Custom Scan) "))#On récupère l'entrée utilisateur.
				print(RESET, end='')#On reset la couleur.
				verif_option = verif_option_dnscan(option)#On vérifie l'entrée utilisateur pour vérifier que le domaine est acceptable et correct.

				if verif_option == "1":#Si l'utilisateur veut utiliser cette option, on exécute le code suivant.
					print("Nous allons scanner le domaine sélectionné")
					os.system("python3 dnscan.py -d " + verification_cible + " -o OutputDNScanDomain")#On exécute la commande
					print("Le scan est terminé !")
					os.system("mv OutputDNScanDomain CustomScanOutput/")#On déplace le résultat dans le dossier Custom Scan.
					input("Appuyer pour continuer....")#On demande à l'utilisateur d'appuyer pour passer à la suite.
				
				if verif_option == "2":#Si l'utilisateur veut utiliser la 2ème option
					print("Nous allons récupérer toutes les IPs liées à un domaine.")
					os.system("python3 dnscan.py -d " + verification_cible + " -i DNScanRetrieveIPs -o OutputDNScanDomain")#On exécute la commande
					print("Le scan est terminé !")
					os.system("mv DNScanRetrieveIPs CustomScanOutput/")#On déplace le résultat dans le Custom Scan
					os.system("mv OutputDNScanDomain CustomScanOutput/")#On déplace le résultat dans le Custom Scan
					input("Appuyer pour continuer....")#On demande à l'utilisateur d'appuyer pour passer à la suite.				

				if verif_option == "3":#Même chose que précédemment
					print("Nous allons réaliser un scan rapide de la cible choisie.")
					os.system("python3 dnscan.py -d " + verification_cible + " -q -o OutputDNScanQuick")
					print("Le scan est terminé !")
					os.system("mv OutputDNScanQuick CustomScanOutput/")
					input("Appuyer pour continuer....")
				
				if verif_option == "4":#Même chose que précédemment
					print("Un scan normal va être effectué, cependant les adresses Ip ne seront pas afficher dans la sortie obtenue.")
					os.system("python3 dnscan.py -d " + verification_cible + " -N -o OutputDNScanNOIP")
					print("Le scan est terminé !")
					os.system("mv OutputDNScanNOIP CustomScanOutput/")
					input("Appuyer pour continuer....")

				if verif_option == "5":#Même chose que précédemment
					print("Nous allons utiliser un autre service DNS que celui du système.")
					print("Indiquer le service que vous voulez utiliser.")
					print(RED + "ATTENTION : Le service DNS choisit doit être donné sous forme d'adresse IP.")
					print(RESET, end='')
					resolver = str(input(BOLD + BLUE + ">>> (Custom Scan) "))#Ici, on doit récupérer une entrée utilisateur, une adresse DNS sous forme d'IP.
					print(RESET, end='')#On reset la couleur.
					resolver.rstrip("\n")#On supprime le saut de ligne automatique.
					verif_resolver = verif_resolver_dnscan(resolver)# On vérifie que l'entrée est bien une adresse DNS correct.
					print("Nous allons maintenant passer à l'éxecution du scan.")
					os.system("python3 dnscan.py -d " + verification_cible + " -R " + verif_resolver + " -o OutputDNScanResolver")#On exécute la commande.
					print("Le scan est terminé !")
					os.system("mv OutputDNScanResolver CustomScanOutput/")#On déplace le résultat dans le dossier Custom Scan.
					input("Appuyer pour continuer....")#En appyant, l'utilisateur passe à la suite du script.

				if verif_option == "6":#Commande libre pour l'utilisateur, on ne vérifie rien. C'est l'utilisateur qui doit être sur de sa commande.
					print("Vous avez donc le choix de la commande à utiliser.")
					print(RED + "ATTENTION : Si la commande que vous renseigner n'est pas bonne, cela engendrera une erreur !")
					print(RED + "Il est consigné de se renseigner au préalable avant d'utiliser cette option !")
					print(RED + "Ne pas utiliser l'option de sortie dans un fichier ! Nous nous occupons de tout !")
					print(RESET, end='')#On reset la couleur.
					commande_user = str(input(BOLD + BLUE + ">>> (Custom Scan) "))#On récupère l'entrée utilisateur.
					print(RESET, end='')#On reset la couleur.
					print("Le scan va commencer !")
					os.system(commande_user + " > OutputDNScanFreeCommand")#On exécutre la commande et on récupère le résultat dans un fichier de sortie.
					print("Le scan est terminé !")
					os.system("mv OutputDNScanFreeCommand CustomScanOutput/")#On déplace le fichier de résultat dans le dossier Custom Scan.
					input("Appuyer pour continuer....")

			if verification == "2" :#Si l'utilisateur veut scanner une liste de domaines, on exécute le code suivant.
				print("Nous allons donc scanner une liste de domaine.")
				print("Plusieurs fichiers contenant des domaines sont fournis pas l'outil par défaut.")
				print("Ces fichiers sont les suivants et vous pouvez les utiliser : subdomains.txt, subdomains-100.txt, subdomains-500.txt, subdomains-1000.txt, subdomains-10000.txt, subdomains-uk-500.txt, subdomains-uk-1000.txt")
				print(RED + "Le service de scan de list peut rencontrer des problèmes durant l'exécution. Cela peut arriver quand le service dns est surchargé !")
				print(RESET, end='')
				print("Veuillez saisir le nom de la liste que vous souhaiez utiliser ! Seul les listes fournies par DnsScan")
				cible = str(input(BOLD + BLUE + ">>> (Custom Scan) "))#On demande à l'utilisateur la liste de domaines qu'il veut utiliser.
				print(RESET, end='')#On reset la couleur
				verif_list = verif_list_dnscan(cible)#On vérifie le nom de la liste.
				print("Voici les options qui sont à votre disposition.")
				print("="*50)#On propose les différentes options de l'outil à l'utilisateur.
				print("1. List - Permet de récupérer toutes les informations liées à une liste de domaine.")
				print("2. IP - Récupère toutes les IP découvertes dans un fichier texte !")
				print("3. Quick - Permet de réaliser un scan rapide.")
				print("4. No IP - Ne pas afficher les adresses IP dans le fichier de résultat.")
				print("5. Resolver - Utiliser un autre service DNS que celui du système.")
				print("6. Commande libre - Utiliser la commande que vous voulez.")
				print("="*50)
				option = str(input(BOLD + BLUE + ">>> (Custom Scan) "))#On récupère la réponse utilisateur.
				print(RESET, end='')#On reset la couleur.
				verif_option = verif_option_dnscan(option)#on vérifie la validité du choix utilisateur.

				if verif_option == "1":#Si l'option 1 est choisie, on exécute le code suivant.
					print("Nous allons donc récupérer toutes les informations liées à la liste de domaines.")
					os.system("python3 dnscan.py -l " + verif_list + " -o OutputDNScanList")#On exécute la commande.
					print("Le scan est terminé !")
					os.system("mv OutputDNScanList CustomScanOutput/")#On déplace le fichier de résultat dans le dossier Custom Scan.
					input("Appuyer pour continuer....")#On appuie pour passer à la suite du code.
				
				if verif_option == "2":#Même chose précédemment
					print("Nous allons récupérer toutes les IPs liées à la liste de domaine.")
					os.system("python3 dnscan.py -l " + verif_list + " -i DNScanRetrieveIPs -o OutputDNScanList")
					print("Le scan est terminé !")
					os.system("mv DNScanRetrieveIPs CustomScanOutput/")
					os.system("mv OutputDNScanList CustomScanOutput/")
					input("Appuyer pour continuer....")
				
				if verif_option == "3":#Même chose précédemment
					print("Nous allons réaliser un scan rapide de la cible choisie.")
					os.system("python3 dnscan.py -l " + verif_list + " -q -o OutputDNScanListQuick")
					print("Le scan est terminé !")
					os.system("mv OutputDNScanListQuick CustomScanOutput/")
					input("Appuyer pour continuer....")
				
				if verif_option == "4":#Même chose que précédemment
					print("Un scan normal va être effectué, cependant les adresses Ip ne seront pas afficher dans la sortie obtenue.")
					os.system("python3 dnscan.py -l " + verif_list + " -N -o OutputDNScanListNoIP")
					print("Le scan est terminé !")
					os.system("mv OutputDNScanListNoIP CustomScanOutput/")
					input("Appuyer pour continuer....")

				if verif_option == "5":#Si l'option 5 est choisie, on exécute le code suivant :
					print("Nous allons utiliser un autre service DNS que celui du système.")
					print("Indiquer le service que vous voulez utiliser.")
					print(RED + "ATTENTION : Le service DNS choisit doit être donné sous forme d'adresse IP.")
					print(RESET, end='')
					resolver = str(input(BOLD + BLUE + ">>> (Custom Scan) "))#On récupère le service DNS sous forme d'IP.
					print(RESET, end='')#On réset la couleur.
					resolver.rstrip("\n")#On supprime le saut de ligne automatique.
					verif_resolver = verif_resolver_dnscan(resolver)#On vérifie l'entrée utilisateur. Que ce soit bien une adresse IP de DNS.
					print("Nous allons maintenant passer à l'éxecution du scan.")
					os.system("python3 dnscan.py -l " + verif_list + " -R " + verif_resolver + " -o OutputDNScanListResolver")#On exécute la commande.
					print("Le scan est terminé !")
					os.system("mv OutputDNScanListResolver CustomScanOutput/")#On déplace le fichier de sortie.
					input("Appuyer pour continuer....")

				if verif_option == "6":#Commande libre, même principe que précédemment.
					print("Vous avez donc le choix de la commande à utiliser.")
					print(RED + "ATTENTION : Si la commande que vous renseigner n'est pas bonne, cela engendrera une erreur !")
					print(RED + "Il est consigné de se renseigner au préalable avant d'utiliser cette option !")
					print(RED + "Ne pas utiliser l'option de sortie dans un fichier ! Nous nous occupons de tout !")
					print(RESET, end='')
					commande_user = str(input(BOLD + BLUE + ">>> (Custom Scan) "))
					print(RESET, end='')
					print("Le scan va commencer !")
					os.system(commande_user + " > OutputDNScanFreeCommand")
					print("Le scan est terminé !")
					os.system("mv OutputDNScanListFreeCommand CustomScanOutput/")
					input("Appuyer pour continuer....")

		if service['Harvester'] == 'Vraie' :#Si dans le fichier, l'outil est activé alors on exécute le code suivant.
			print("Vous allez paramétrer theHarvester !")
			end=" "
			Option1="all"
			Perso="False"
			CommandHarvester=""
			while end != "do" :#On affiche le menu d'options pour theHarvester.
				print("="*50)
				print("ggl - scanez via google")
				print("lk - scanez via Linkedin")
				print("do - tout faire sur le future DNS donné ")
				print("p - Personaliser la commande")
				print("ex - quitter theHarvester")
				print("="*50)
				Souhait = str(input(BOLD + BLUE + ">>> (Custom Scan) "))#On récupère l'entrée utilisateur.
				print(RESET, end='')#On reset la couleur.
				Souhait.rstrip("\n")#On supprime le saut de ligne automatique.
				VERIF_SOUHAIT = verif_souhait(Souhait)#On vérifie si l'utilisateur a choisit une option valide.
				
				if VERIF_SOUHAIT == "ggl" :#Si "ggl", on exécute le code suivant.
					Perso = "true"
					print("L'option 'google' est enregistré")
					Option1 = "ggl"
					input("Appuyez sur Entree pour continuer...")
				elif VERIF_SOUHAIT == "lk" :#Si "lk", on exécute le code suivant.
					Perso = "true"
					print("L'option 'linkedin' est enregistré")
					Option1 = "linkedin"
					input("Appuyez sur Entree pour continuer...")
				elif VERIF_SOUHAIT == "p" :#Si "p", on exécute le code suivant.
					Perso = "true"
					print("Veuillez saisir la commande au complet")
					CommandHarvester=input()#On laisse l'utilisateur choisir sa commande de manière totalement libre.
					print("Votre commande à été personalisé, voulez vous lancer TheHarvester avec celle-ci ?")
					QuestionHarvester=input("O (OUI), n (non)")#On demande à l'utilisateur si il veut lancer l'outil avec sa commande.
					if QuestionHarvester == "O" or QuestionHarvester == "o" :#Si oui on exécute le code suivant, si non, on ne fait rien.
						Souhait="do"
						end = "do"
				elif VERIF_SOUHAIT == "ex" :#Si "ex", on exécute le code suivant.
					print("Vous quittez TheHarvester")
					print(RED + "ATTENTION, le scan ne sera pas exécuté !")
					print(RESET, end='')
					end = "do"
				elif VERIF_SOUHAIT == "do" :
					end = "do"
      
			if Souhait == end : 
				if Perso == "true" :
					print("Veuillez patienter quelque seconde...")
					os.system(CommandHarvester + " > OutputtheHarvesterCustom")
				else : 
					#on lui demande l'adresse
					DNS = str(input(BOLD + BLUE + "veuillez saisir l'adresse DNS à Scanner ! Exemple : test.fr et pas www.test.fr : "))
					print(RESET, end='')
					#on fait tourner la command de façon non visible pour l'utilisateur
					verif_DNS = verif_domain_harvester(DNS)
					print("Veuillez patienter quelque seconde...")
					os.system("theHarvester -d " + verif_DNS + " -b " + Option1 + " > OutputtheHarvesterCustom")
				print("Les résulats sont enregistrés dans le fichier OutputtheHarvesterCustom qui sera stocké dans le dossier CustomScanOutput")
				os.system("mv OutputtheHarvesterCustom CustomScanOutput/")
			input("Appuyez sur Entree pour continuer...")

		if service['shodan'] == 'Vraie' :#Si dans le fichier yaml l'outil est activé, alors on exécute le code suivant.
			print("\n")
			print("Vous allez paramétrer shodan !")
			print("La première chose à faire est de choisir la cible : IP ou domaine !")
			print("Veuillez indiquer la cible que vous voulez scaner ! Exemple IP : 8.8.8.8 ; Exemple domaine : www.test.fr")
			Souhait = str(input(BOLD + BLUE + ">>> (Custom Scan) "))#On demande à l'utilisateur sa cible, domaine ou IP.
			print(RESET, end='')#On reset la couleur
			Souhait.rstrip("\n")#On supprime les sauts de ligne automatique.
			verif_souhait = verif_souhait_shodan(Souhait)#On vérifie l'entrée utilisateur pour déterminer si il a rentré une valeur de forme valide.

			#Maintenant qu'on est sur de l'entrée utilisateur, on compte le nombre de point dans l'entrée pour savoir si c'est un domaine ou une IP.
			if verif_souhait.count(".") == 3 :#Si IP, on exécute le code suivant.
				print("Vous avez décidé de scaner une IP.")
				print("Voila ce que nous vous proposons d'effectuer sur une IP.")
				print("="*50)#On propose les options à l'utilisateur.
				print("1. Honeypot - Permet de savoir si la cible est un pot de miel.")
				print("2. Host - Avoir toutes les informations disponibles sur une adresse IP.")
				print("3. MyIP - Permet d'afficher votre IP publique.")
				print("4. Search - Permet de faire une recherche dans la base de données Shodan.")
				print("5. Commande - Choisir la commande que vous souhaitez exécuter.")
				print("="*50)
				Choix = str(input(BOLD + BLUE + ">>> (Custom Scan) "))#On récupère le choix de l'utilisateur.
				print(RESET, end='')#On reset la couleur.
				Choix.rstrip("\n")#On supprime le saut de ligne automatique.
				verif_choix = verif_choix_shodan_IP(Choix)#On vérifie que l'option choisie est valide.
				if verif_choix == "1" :#Pour la première option
					print("Nous allons maintenant scaner l'adresse IP choisie pour voir si c'est un pot de miel ou non.")
					print("L'intégralité des résultats récupérés seront stockés dans un fichier récupérable dans le répertoire CustomScanOutput")
					print(RED + "Le HoneyPot est une option qui n'est pas totalement aboutie, il est possible que cette dernière ne fonctionne pas à tous les coups !!")
					print(RESET, end='')
					os.system("shodan honeyscore " + verif_souhait + " > OutputShodanHoneyPot")
					print("Le scan est terminé !")
					os.system("mv OutputShodanHoneyPot CustomScanOutput/ ")
					input("Appuyer pour continuer....")

				if verif_choix == "2" :#Pour la 2ème option.
					print("Nous allons maintenant scaner l'adresse IP choisie pour obtenir toutes les informations disponible à son sujet.")
					print("L'intégralité des résultats récupérés seront stockés dans un fichier récupérable dans le répertoire CustomScanOutput")
					os.system("shodan host " + verif_souhait + " > OutputShodanHost")
					print("Le scan est terminé !")
					os.system("mv OutputShodanHost CustomScanOutput/ ")
					input("Appuyer pour continuer....")

				if verif_choix == "3" :#Pour la 3ème option.
					print("Cette option permet simplement de récupérer votre adresse IP publique")
					print("Nous n'allons donc pas utiliser la cible que vous avez renseigné ci-dessus.")
					print("L'intégralité des résultats récupérés seront stockés dans un fichier récupérable dans le répertoire CustomScanOutput")
					os.system("shodan myip > OutputShodanMyPublicIP")
					print("Le scan est terminé !")
					os.system("mv OutputShodanMyPublicIP CustomScanOutput/ ")
					input("Appuyer pour continuer....")

				if verif_choix == "4" :#Pour la 4ème option
					print("Nous allons réaliser une recherche dans la bases de données Shodan.")
					print("Nous n'allons pas utiliser la cible que vous avez donnée ci-dessus.")
					print("Pour effecetuer cette recherche, nous allons avoir besoin d'un élément à chercher.")
					print("L'intégralité des résultats récupérés seront stockés dans un fichier récupérable dans le répertoire CustomScanOutput")
					print("Dans notre recherche nous allons utiliser des filtres pour avoir l'IP, le port, l'organisme, et le nom d'hôte.")
					print(RED + "Le choix de la cible vous appartient seulement si vous utilisez une mauvaise cible, le résultat du scan sera forcément erroné.")
					print(RESET, end = '')#On demande une cible à l'utilisateur pour une recherche dans la base de données shodan.
					cible = str(input(BOLD + BLUE + ">>> (Custom Scan) "))#On récupère l'entrée utilisateur qui peut être de toutes sortes donc on ne véirife pas.
					print(RESET, end='')#Si l'utilisateur rentre une mauvaise commande, le résultat ne sera pas correct.
					cible.rstrip("\n")#On supprime le saut de ligne automatique.
				
					if verif_cible(cible) == True : #Ici, on vérifie si l'entrée utilisateur est un bien de type 'str'
						os.system("shodan search --fields ip_str,port,org,hostnames " + cible + " > OutputShodanSearch")#Si c'est le cas, on exécute cette commande.

					print("Le scan est terminé !")
					os.system("mv OutputShodanSearch CustomScanOutput/ ")#On déplace le fichier de résultat dans le dossier Custom Scan.
					input("Appuyer pour continuer....")

				if verif_choix == "5" :#option permettant de choisir une commande librement.
					print("Vous êtes libre de choisir la commande que vous voulez utiliser")
					print("L'intégralité des résultats récupérés seront stockés dans un fichier récupérable dans le répertoire CustomScanOutput")
					print(RED + "Aucune indication ne vous sera donnée, si la commande n'est pas bonne, le fichier de sortie affichera l'erreur !")
					print(RESET, end='')
					commande = str(input(BOLD + BLUE + ">>> (Custom Scan) "))#On récupère la commande que veut exécuter l'utilisateur.
					print(RESET, end='')#On reset la couleur.
					commande.rstrip("\n")#on supprime le saut de ligne automatique.
					os.system(commande + " > OutputShodanFreeCommand")#On exécute la commande.
					print("Le scan est terminé !")
					os.system("mv OutputShodanFreeCommand CustomScanOutput/ ")#On déplace le résultat dans le dossier Custom Scan.
					input("Appuyer pour continuer....")#

			#Maintenant qu'on est sur de l'entrée utilisateur, on compte le nombre de point dans l'entrée pour savoir si c'est un domaine ou une IP.
			if verif_souhait.count(".") == 2 :#Pour domaine, on exécute le code suivant
				print("Vous avez décidé de scaner un domaine.")
				print("Voila ce que nous vous proposons d'effectuer sur un domaine.")
				print("="*50)#On propose les options à l'utilisateur.
				print("1. Domain - Avoir toutes les informations disponibles sur un nom de domaine.")
				print("2. MyIP - Permet d'afficher votre IP public.")
				print("3. Search - Permet de faire une recherche dans la base de données Shodan.")
				print("4. Commande - Choisir la commande que vous souhaitez exécuter.")
				print("="*50)
				Choix = str(input(BOLD + BLUE + ">>> (Custom Scan) "))#On récupère l'entrée utilisateur.
				print(RESET, end='')#On reset la couleur.
				Choix.rstrip("\n")#on supprime le saut de ligne automatique.
				verif_choix_ = verif_choix_shodan_domain(Choix)#On vérifie l'entrée pour voir si elle est valide.
				if verif_choix_ == "1" :#Si option 1, on exécute le code souvent.
					print("Nous allons scanner le domaine cible que nous avons récupéré ci-dessus.")
					print("Ce scan va permettre de récupérer toutes les infos relatives à la cible choisie")
					os.system("shodan domain " + verif_souhait + " > OutputShodanDomain")
					print("Le scan est terminé !")
					os.system("mv OutputShodanDomain CustomScanOutput/ ")
					input("Appuyer pour continuer....")

				if verif_choix_ == "2" : #Si option 2, on exécute le code suivant.
					print("Nous n'allons pas vraiment exécuter de scan dans cette situation.")
					print("Nous allons simplement récupérer votre IP public")
					os.system("shodan myip > OutputShodanPublicIP")
					print("L' IP a été récupérée")
					os.system("mv OutputShodanPublicIP CustomScanOutput/ ")
					input("Appuyer pour continuer....")

				if verif_choix_ == "3" :#Si option3, on exécute le code suivant comme précédemment, même principe.
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

				if verif_choix_ == "4" :#Si option 4, on exécute le code suivant comme précédemment, même principe.
					print("Vous êtes libre de choisir la commande que vous voulez utiliser")
					print("L'intégralité des résultats récupérés seront stockés dans un fichier récupérable dans le répertoire CustomScanOutput")
					print(RED + "Aucune indication ne vous sera donnée, si la commande n'est pas bonne, le fichier de sortie affichera l'erreur !")
					print(RESET, end='')
					commande = str(input(BOLD + BLUE + ">>> (Custom Scan) "))
					print(RESET, end='')
					commande.rstrip("\n")
					os.system(commande + " > OutputShodanFreeCommand")
					print("Le scan est terminé !")
					os.system("mv OutputShodanFreeCommand CustomScanOutput/")
					input("Appuyer pour continuer....")

		if service['urlscan'] == 'Vraie' :
			print("Nous allons utiliser l'outil urlscan.io qui permet de récupérer des informations sur des URL")
			print("Il vous suffit d'indiquer l'url que vous voulez scanner !")
			print("Vous devez donner l'intégralité du lien !! Exemple : https://www.instagram.com/")
			Rps = str(input(BOLD + BLUE + ">>> (Default Scan) "))#On récupère la cible
			print(RESET, end='')#On reset la couleur
			FQDN = verif_urlscan_lien(Rps)#On vérifie la cible.
			headers = {'API-Key':'27a5f4bf-340a-47dd-a710-7a3038a97321','Content-Type':'application/json'}
			data = {"url": Rps, "visibility": "public"}
			response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
			#Ci-dessus, information pour la demande de scan à l'API.
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

			print("URLscan.io est un outil assez particulié.")	
			print("Les options que vous allez voir sont des options pour récupérer des informations supplémentaires du résultat.")
			print("Le scan est le même pour tous le monde MAIS on peut récupérer des informations particulières avec certaines requêtes.")
			print("En sortie vous récupérerez un fichier json et yaml non trié.")
			print("Veuillez indiquer les informations que vous voulez récupérer sur la cible en plus du résultat classique.")
			print("="*50)#On offre les options à l'utilisateur.
			print("1. Image - Récupère une image PNG du domaine scanné.")
			print("2. DOM Snapshot - Récupère une snapshot dom de la hiérarchie du domaine.")
			print("3. Scan classique - Effectuer un scan classique.")
			print("="*50)
			option_resultat = str(input(BOLD + BLUE + ">>> (Custom Scan) "))#On récupère l'option choisie.
			print(RESET, end='')#On reset la couleur.
			verif_option_ = verif_option_resultat(option_resultat)#On vérifie si l'option choisie est valable.

			if verif_option_ == "1" :#Pour l'option 1
				time.sleep(22)
				os.system("curl https://urlscan.io/screenshots/" + uuid + ".png -o ImageURLscan.png")
				os.system("curl https://urlscan.io/api/v1/result/" + uuid + "/ > OutputURLScan.json")
				print("La récupération de l'image est terminée !")
				os.system("mv ImageURLscan.png CustomScanOutput/")
				with open('OutputURLScan.json', 'r') as file:
					configuration = json.load(file)
				with open('OutputURLScan.yaml', 'w') as yaml_file:
					yaml.dump(configuration, yaml_file)
				
				os.system("mv OutputURLScan.yaml CustomScanOutput/")
				os.system("mv OutputURLScan.json CustomScanOutput/")
				os.system("rm ResultURLScanIo.txt")
				input("Appuyer pour continuer....")

			if verif_option_ == "2" :#Pour l'option 2
				time.sleep(22)
				os.system("curl https://urlscan.io/dom/" + uuid + "/ -o SnapshotDOMURLscan")
				os.system("curl https://urlscan.io/api/v1/result/" + uuid + "/ > OutputURLScan.json")
				print("La snapshot est récupérée !")
				os.system("mv SnapshotDOMURLscan CustomScanOutput/")
				with open('OutputURLScan.json', 'r') as file:
					configuration = json.load(file)
				with open('OutputURLScan.yaml', 'w') as yaml_file:
					yaml.dump(configuration, yaml_file)
				
				os.system("mv OutputURLScan.yaml CustomScanOutput/")
				os.system("mv OutputURLScan.json CustomScanOutput/")
				os.system("rm ResultURLScanIo.txt")
				input("Appuyer pour continuer....")

			if verif_option_ == "3" :#Pour l'option 3
				time.sleep(22) # On fige le code pendant 22 secondes pour atteindre que le scan soit terminé
				# et que le résulat puisse être récupéré.
				os.system("curl https://urlscan.io/api/v1/result/" + uuid + "/ > OutputURLScan.json")#On récupère le résultat du scan dans un fichier.
				print("Le scan est terminé !")
				#On va convertir le fichier de sortie en yaml pour que ce soit plus simple à trier.
				with open('OutputURLScan.json', 'r') as file:
					configuration = json.load(file)
				with open('OutputURLScan.yaml', 'w') as yaml_file:
					yaml.dump(configuration, yaml_file)
				
				os.system("mv OutputURLScan.json CustomScanOutput/")
				os.system("mv OutputURLScan.yaml CustomScanOutput/")
				os.system("rm ResultURLScanIo.txt")
				input("Appuyer pour continuer....")

		service['Dnscan'] = 'Faux' #Avant de quitter le script ou de retourner au menu principal, on reset les valeurs du fichier "config.yaml"
		service['urlscan'] = 'Faux'
		service['shodan'] = 'Faux'
		service['Harvester'] = 'Faux'

		with open('config.yml', 'w') as dump_file :
			yaml.dump(service, dump_file)#On enregistre les changements dans le fichier. On écrit les résultats.
		
		print("\n")
		print("Les différents scans personnalisés sont terminés !")
		print("Voulez-vous quitter le script ?")
		print("="*50)#Petit menu permettant de choisir quoi faire à la fin du script, soit le quitter soit retourner au menu principal pour continuer d'utiliser le script.
		print("1. Oui")
		print("2. Non, retourner au menu principal")
		print("="*50)
		fin = str(input(BOLD + BLUE + ">>> "))#On récupère la réponse de l'utilisateur.
		print(RESET, end='')#On reset la couleur.
		verif_fin = verif_fin_choix(fin)#On vérifie la validité de la réponse.

		if verif_fin == "1" :
			exit()#Pour la première option, on quitte le script.
		
		if verif_fin == "2" :#Pour la deuxième option, on affiche le menu principal
			FirstSummary()#On récupère ensuite le choix de l'utilisateur dans le menu principal.
			Rps = str(input(BOLD + BLUE + ">>> "))
			print(RESET, end='')#On reset la couleur.

	#Help, cela affiche le menu
	while Rps == "h" :
		FirstSummary()
		Rps = str(input(BOLD + BLUE + ">>> "))
		print(RESET, end='')

	#Si l'utilisateur rentre une mauvaise commande
	while (Rps != "1" and Rps != "2" and Rps != "3" and Rps != "4" and Rps != "h") :
		print(RED + BOLD + "La commande que vous avez saisie n'existe pas" + RESET)
		Rps = str(input(BOLD + BLUE + ">>> "))
		print(RESET, end = '')
