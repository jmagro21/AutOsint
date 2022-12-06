import os

#demande à l'utilisateur l'adresse ip de l'hôte
hote=str(input("saisis l'adresse IP de l'hote: "))
hote.rstrip('\n')
  
#retourne la localisation, les ports ouverts, l'organisation possédant l'adr>
os.system("shodan host "+ hote) 
  
#affiche si l'adresse ip choisis par l'utilisateur est un honeypot
#Cette ligne de code ne fonctionne pas avec l'adresse IP de l'ESGI 
os.system("shodan honeyscore "+ hote) 
