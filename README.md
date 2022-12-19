Projet Scolaire : AUTOSINT

Script Python permettant d'automatiser les 4 outils suivants : Shodan, TheHarvester, Dnscan et URLscan.io.
Ces outils sont très puissants et permettent de faire des recherches publiques (en libre accès) sur des noms de domaine, des IP's et des lites de domaines.
Ces outils récupèrent des adresses IP's, des noms de domaine, des adresses mails et encore tant d'autres choses qui peuvent être utile dans la pratique de l'OSINT.

- Quelques recommandations avant de démarrer la lecture des informations suivantes et l'exécution du script.
        - Vous devez exécuter ce script dans une machine linux. (Version recommandée : Kali Linux)
        
        - Lorsque vous récuprérer le dossier contenant tout ce qui est nécessaire au script pour s'éxecuter, il est nécessaire d'exécuter le script avec l'utilisateur            root.
        
        - L'intégralité des droits doivent être attribués à l'utilisateur root mais rien aux autres. (Exemple : chmod -R 700                                                       Nom_du_dossier_qui_contient_les_fichiers_du_script)
          
          
          
          
          
          
Dans ce readme vous allez retrouver des informations 
- Dnsscan - récupération passive d'information liées au DNS
- Shodan - Récupère  en fonction de l'ip ou du nom de domaine des informations sur la cible (utilisable via
l'api ou l'outil en ligne de commande)
- TheHarvester - Récupère des informations sur des adresses mails, noms de domaine etc.
- [Urlscan.io](https://urlscan.io/docs/api/) - réalise un scan d'une cible et récupère des informations.
