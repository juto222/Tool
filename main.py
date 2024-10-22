import random
import string
import hashlib
import dns.resolver
import requests
import nmap
import re
import ipaddress
import webbrowser

from Options import ScanNetwork
from Options import GenererIPv6
from Options import MdpGenerer
from Options import WebCheck
from Options import Sousdomaine
from Options import IPLookup
from Options import HashFichier
from Options import HashMDP
from Options import VerifMDP
from Options import Conv
from Options import DDoS
from Options import Whois
from Options import UsernameLookup

def afficher_menu():
    print("""  
                ░▒▓████████▓▒░  ░▒▓██████▓▒░   ░▒▓██████▓▒░  ░▒▓█▓▒░              
                   ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░              
                   ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░              
                   ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░              
                   ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░              
                   ░▒▓█▓▒░      ░▒▓██████▓▒░   ░▒▓██████▓▒░  ░▒▓████████▓▒░
          

                            https://discord.gg/6WjWn5f6RF  
          

────────────|[Network] ─────────────────────[Mot de passe]────────────────────────────────[PC]────────────────  
│                                │                                   │
│────1  Random IPv6 Generateur   │───3  Générer un mot de passe      │────4  Vérifier si un fichier est un malware
│────2  Scanner Network          │───6  Hacher un mot de passe       │────9  Convertir hexadécimal en décimal
│────5  Sous domaine             │───7  Vérifier un mot de passe     │────10 Vérifier si un site est en ligne
│────12 Attaque DDoS                                                 │────11 Cheat Valorant
│
│───────────[OSINT]──────────────
│ 
│────8  Info sur l'IP
│────13 Sous domaine info
│────14 Username Lookup          
│          
│    0- Quitter
    """)

def obtenir_choix():
    try:
        return int(input("""
 ____(user@Tool)
│__#  """))
    except ValueError:
        print("Entrée invalide. Veuillez entrer un numéro valide.")
        return -1  # Retourne un choix invalide pour forcer la boucle à redemander l'option

while True:
    afficher_menu()
    
    choix = obtenir_choix()  

    if choix == 1:
        try:
            GenererIPv6.generate_ipv6() 
        except Exception as e:
            print(f"Erreur lors de la génération d'IPv6 : {e}")
    elif choix == 2:
        try:
            ScanNetwork.scan_network()  
        except Exception as e:
            print(f"Erreur lors du scan du réseau : {e}")
    elif choix == 3:
        try:
            MdpGenerer.generer_mot_de_passe()
        except Exception as e:
            print(f"Erreur lors de la génération du mot de passe : {e}")
    elif choix == 4:
        try:
            HashFichier.calculer_hash_fichier() 
        except Exception as e:
            print(f"Erreur lors du calcul du hash de fichier : {e}")
    elif choix == 5:
        try:
            Sousdomaine.sousdomaine() 
        except Exception as e:
            print(f"Erreur lors de la recherche de sous-domaines : {e}")
    elif choix == 6:
        try:
            HashMDP.hasher_mot_de_passe() 
        except Exception as e:
            print(f"Erreur lors du hachage du mot de passe : {e}")
    elif choix == 7:
        try:
            VerifMDP.mdp_force()
        except Exception as e:
            print(f"Erreur lors de la vérification du mot de passe : {e}")
    elif choix == 8:
        try:
            IPLookup.obtenir_infos_ip()  
        except Exception as e:
            print(f"Erreur lors de la récupération des informations IP : {e}")
    elif choix == 9:
        try:
            Conv.convertir() 
        except Exception as e:
            print(f"Erreur lors de la conversion : {e}")
    elif choix == 10:
        try:
            WebCheck.web()
        except Exception as e:
            print(f"Erreur lors de la vérification : {e}")
    elif choix == 11:
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        webbrowser.open_new_tab(url)
    elif choix == 12:
        try:
            DDoS.ddos_attack()
        except Exception as e:
            print(f"Une erreur lors de l'attaque est survenue : {e}")
    elif choix == 13:
        try:
            Whois.info_domaine()
        except Exception as e:
            print(f"Une erreur est survenue : {e}")
    elif choix == 14:
        try:
            UsernameLookup.username()
        except Exception as e:
            print("Une erreur est survenue lors de la recherche : {e}")
    elif choix == 0:
        print("Au revoir!")
        break
    else:
        print("Option invalide. Veuillez choisir une option parmi celles proposées.")
    
    # Pause avant de réafficher le menu
    input("Appuyez sur Entrée pour revenir au menu.")
