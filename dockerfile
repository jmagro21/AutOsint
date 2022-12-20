#On spécifie l'image de base.
FROM python:3.10
#Le fichier docker va aller chercher python 3.10 dans le docker hub qui a déjà python et tous ses modules par défaut installés.

WORKDIR /var/www/
#On définie le répertoire dans lequel on va envoyer nos fichiers pour l'exécution du script.
#Ansi tous les résultats obtenues vont être stockés dans ce répertoire. 

ADD ./Main.py /var/www/Main.py
ADD ./config.yml /var/www/config.yml
ADD ./requirements.txt /var/www/requirements.txt
#On ajoute les fichiers du script et on indique leurs positions (ici on met ça à la racine ".")

RUN pip install pyfiglet
RUN pip install pyyaml
RUN pip install requests
RUN pip install netaddr
RUN pip install cryptography
RUN pip install packaging
RUN pip install dnspython
RUN pip install shodan
#Ici on installe les dépendanes pour notre script avant que ce dernier ne soit exécuté.On utilise la commande pip pour installer les modules.

CMD [ "python3", "Main.py" ]
#lastly we specified the entry command this line is simply running python ./main.py in our container terminal




