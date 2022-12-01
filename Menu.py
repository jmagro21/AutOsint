import pyfiglet

BOLD = '\033[1m'
BLUE = '\033[94m'
GREEN = '\033[92m'
RED = '\033[31m'
RESET = '\033[0m'

# Ceci est une proposition de menu, il y a plusieurs propositions faites a l'utilisteurs, le programme se stoppe uniquement
# Quand l'utilisateur selectionne la commande "q", de cette maniere il peut lancer, un scan, puis un autre, relancer la premier scan etc...
# L'utilisateur n'a ainsi pas besoin de relancer le programme a chaque fois"
# Si l'utilisteur entre une mauvaise commande, le programme ne se bloque pas, il indique juste que la commande n'est pas bonne et ainsi 
# l'utilisateur peut entrer une nouvelle commande

# Dans le code, il y a beaucoup de print("blabla"), vous avez juste a le remplacer par une fonction integrant l'utilisation d'un outil ou d'un autre

# Le prof a indiquer que le scan devait être modulable, quoi de mieux que alors que d'effectuer un scan rapide
# integrant touts les outils avec les parametres les plus rapide, un scan lent, et un custom scan qui permet a l'utilisateur de lancer un outil precis. 
# Tout cela rends le programme modulable sans changer la complexite de celui-ci, grace a l'utilisation de fonctions specifiques

def FirstSummary () :
	print(BOLD + BLUE + "Veuillez choisir une option : " + RESET)
	print("="*50)
	print("1 : Quick scan")
	print(u"2 : Slow scan")
	print(u"3 : Custom scan")
	print("4 : Settings")
	print("h : Help")
	print("q : Quit")
	print("="*50)

#Affichage de ma baniere
titre = pyfiglet.figlet_format(" AutOsint", font = "slant"  )
print(titre)

FirstSummary()

Rps = str(input(BOLD + BLUE + ">>> "))
print(RESET, end = '')

while Rps != "q" :

	#On lance tous les outils les uns après le autres avec les paramètres les plus rapides
	if Rps == "1" :
		print("blabla")

	#On lance tous les outils les uns après le autres avec les paramètres les plus lent
	if Rps == "2" :
		print("blabla")

	#L'utilisateur peut choisir un outil ou un autre, il les lancera separement 
	if Rps == "3" :
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
		
			if Rps == "A" :
				print("blabla")
				
			if Rps == "B" :
				print("blabla")
			
			if Rps == "C" :
				print("blabla")
				
			if Rps == "D" :
				print("blabla")
				
      #Si l'utilisateur est con ou s'il rentre une mauvaise commande
			if(Rps != "A" and Rps != "B" and Rps != "C" and Rps != "D") :
				print(RED + BOLD + "La commande que vous avez saisie n'existe pas" + RESET)		
		
			Rps = str(input(BOLD + BLUE + ">>> (Custom scan) "))
			print(RESET, end = '')
	
	#Dans cette partie, l'utilisateuur pourra faire les reglages de sont script
	if Rps == "4" :
		print(BOLD + BLUE + "Veuillez choisir une option : " + RESET)
		print("="*50)
		print("A : blabla")
		print("="*50)
		
		Rps = str(input(BOLD + BLUE + ">>> (Settings) "))
		print(RESET, end = '')
		while Rps != "q" :
		
			if Rps == "A" :
				print("blabla")
				
			if Rps == "B" :
				print("blabla")
				
			if(Rps != "A" and Rps != "B") :
				print(RED + BOLD + "La commande que vous avez saisie n'existe pas" + RESET)	
				
			Rps = str(input(BOLD + BLUE + ">>> (Settings) "))
			print(RESET, end = '')
		
  #Help, cela affiche le menu
	if Rps == "h" :
		FirstSummary()
	#Si l'utilisateur est con ou s'il rentre une mauvaise commande
	if(Rps != "1" and Rps != "2" and Rps != "3" and Rps != "4" and Rps != "h") :
		print(RED + BOLD + "La commande que vous avez saisie n'existe pas" + RESET)

	Rps = str(input(BOLD + BLUE + ">>> "))
	print(RESET, end = '')