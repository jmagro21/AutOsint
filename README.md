Projet Scolaire : AUTOSINT

Script Python permettant d'automatiser les 4 outils suivants : Shodan, TheHarvester, Dnscan et URLscan.io.
Ces outils sont très puissants et permettent de faire des recherches publiques (en libre accès) sur des noms de domaine, des IP's et des lites de domaines.
Ces outils récupèrent des adresses IP's, des noms de domaine, des adresses mails et encore tant d'autres choses qui peuvent être utile dans la pratique de l'OSINT.

- Quelques recommandations avant de démarrer la lecture des informations suivantes et l'exécution du script.

        - Vous devez exécuter ce script dans une machine linux. (Version recommandée : Kali Linux)
        
        - Lorsque vous récuprérer le dossier contenant tout ce qui est nécessaire au script pour s'éxecuter, il est nécessaire d'exécuter le script avec l'utilisateur             root.
        
        - L'intégralité des droits doivent être attribués à l'utilisateur root mais rien aux autres. (Exemple : chmod -R 700                                                       Nom_du_dossier_qui_contient_les_fichiers_du_script)

        - Il est conseillé de consulter le fichier "requirements.txt" récupérer avec le dossier et ce, même si il est possible d'installer toutes les dépendances avec le           script. Il est préférable d'avoir installé tous les modules nécessaires au préalable pour éviter tous les problèmes lors du script.

        - Il est obligatoire d'installer toutes les dépendances lors de l'exécution du script pour la première fois. Il est donc très fortement conseillé de réaliser               l'installation des paquets lors de la première exécution du script.
          
        - La dernière étape est de vous laissez porter par le script tout est expliquer par ce dernier au fur et à mesure de l'exécution :)
          
          
Dans ce readme vous allez retrouver des informations concernants les outils que vous allez utiliser. J'indiquerais également les liens permettant de retrouver les documentations officiels de chaque outil : 
        - Dnsscan - récupération passive d'information liées au DNS pouvant cibler un domaine ou une liste de domaine. Cet outil est un projet github qui peut être               retrouver ici --> https://github.com/rbsec/dnscan
        
        - dnscan.py (-d \<domain\> | -l \<list\>) [OPTIONS]

          #### Arguments Obligatoires
            -d  --domain                              Target domain; OR
            -l  --list                                Newline separated file of domains to scan
    
          #### Optional Arguments
            -w --wordlist <wordlist>                  Wordlist of subdomains to use
            -t --threads <threadcount>                Threads (1 - 32), default 8
            -6 --ipv6                                 Scan for IPv6 records (AAAA)
            -z --zonetransfer                         Perform zone transfer and exit
            -r --recursive                            Recursively scan subdomains
            --recurse-wildcards                    Recursively scan wildcards (slow)

            -m --maxdepth                             Maximum levels to scan recursively
            -a --alterations                          Scan for alterations of subdomains (slow)
            -R --resolver <resolver>                  Use the specified resolver instead of the system default
            -L --resolver-list <file>                 Read list of resolvers from a file
            -T --tld                                  Scan for the domain in all TLDs
            -o --output <filename>                    Output to a text file
            -i --output-ips <filename>                Output discovered IP addresses to a text file
            -n --nocheck                              Don't check nameservers before scanning. Useful in airgapped networks
            -q --quick                                Only perform the zone transfer and subdomain scans. Suppresses most file output with -o
            -N --no-ip                                Don't print IP addresses in the output
            -v --verbose                              Verbose output
            -h --help                                 Display help text

            Custom insertion points can be specified by adding `%%` in the domain name, such as:

            ```
            $ dnscan.py -d dev-%%.example.org
            ```
           
        - Shodan est un outil permettant de récupérer, en fonction de l'ip ou du nom de domaine, des informations sur la cible (utilisable via
          l'api ou l'outil en ligne de commande). Toutes les informations complémentaires à cet outil peuvent être retrouvé à ce lien : https://developer.shodan.io/api
          Il est également possible d'utiliser cet outil sous forme de paquet installable sur la distribution Linux de votre choix. C'est d'ailleurs cette méthode que           nous allons utiliser dans notre script.
          Vous pouvez consulter le code pour avoir plus d'informations sur la manière d'utiliser cet outil.
          
        - TheHarvester permet de récupérer des informations sur un nom de domaine ou une IP. Les informations collectés peuvent être diverse : Nom de serveur, adresse           IP, adresses mail, etc...
          Dans notre situation, nous utilisons l'outil qui s'installe comme un paquet classique. Si vous désirez plus d'informations à son sujet, vous pouvez consulter           le code pour en apprendre davantage sur cet outil ou vous pouvez consulter ces différents liens : 
                 - https://www.padawanhacker.fr/tests-d-intrusion/collecte-d-information-passive/the-harvester
                 - 
        - [Urlscan.io](https://urlscan.io/docs/api/) - réalise un scan d'une cible et récupère des informations.
