import os #Module qui va permettre de passer des commandes systèmes.
import pyfiglet # On importe le module qui permet de faire un menu sympa

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
		print("Veuillez simplement indiquer la cible IP ou Nom de Domaine")
		# Ci-dessous, on est obligé de garder le nom de variable 'Rps' sinon les autres règles ne s'appliqueront pas dans cette partie du code.
		# On ne pourrait plus quitter avec 'q' par exemple. Donc on garde Rps pour TOUTES LES ENTRÉES UTILISATEURS !!!!
		Rps = str(input(BOLD + BLUE + ">>> (Default Scan) "))
		print(RESET, end = '') # Ici c'est simplement pour éviter le retour à la ligne.


	#L'utilisateur peut choisir un outil ou un autre, il les lancera separement 
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
