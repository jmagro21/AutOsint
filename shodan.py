import os

#demande à l'utilisateur l'adresse IP de l'hôte
hote=str(input("saisis l'adresse ip de l'hôte: "))
hote.rstrip('\n')
#retourne la localisation, les ports ouverts, l'organisatio possédant l'adresse IP de l'hôte 
os.system("shodan host "+ hote) 

#affiche si l'adresse IP chosis par l'utilisateur est honeypot (ça peut être utile pour savoir si l'adresse Ip est un tracknar)
#par contre cette ligne ne fonctionne pas encore 
os.system("shodan honeyscore" +hote) 
