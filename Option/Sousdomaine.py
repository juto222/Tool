import dns.resolver
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def sousdomaine():
    print(r"""
                         _  _  _  _  _  _  _  _  _      ______   _____   ______  
                        | || || || || || || || || |    / _____) / ___ \ |  ___ \ 
                        | || || || || || || || || |   | /      | |   | || | _ | |
                        | ||_|| || ||_|| || ||_|| |   | |      | |   | || || || |
                        | |___| || |___| || |___| | _ | \_____ | |___| || || || |
                         \______| \______| \______|(_) \______) \_____/ |_||_||_|  
    """)
    domain = input("Entrez le domaine cible (ex: example.com): ").strip()

    subdomains = [
        'www', 'mail', 'ftp', 'dev', 'admin', 'blog', 'api', 'admin-api', 'dashboard', 'support', 'staging', 
        'shop', 'portal', 'login', 'app', 'webmail', 'dns', 'vpn', 'help', 'test', 'm', 'mobile', 'news', 
        'contact', 'docs', 'git', 'status', 'secure', 'files', 'media', 'cloud', 'storage', 'appserver', 
        'crm', 'billing', 'payments', 'analytics', 'customer', 'account', 'store', 'order', 
        'auth', 'devops', 'email', 'api-dev', 'api-staging', 'monitoring', 'sandbox', 'internal', 'backup', 
        'root', 'private', 'ssh'
    ]

    for sub in subdomains:
        full_domain = f"{sub}.{domain}"

        # Vérification DNS
        try:
            dns.resolver.resolve(full_domain)
            print(f"[DNS] Le sous-domaine {full_domain} existe.")
        except dns.resolver.NXDOMAIN:
            print(f"[DNS] Le sous-domaine {full_domain} n'existe pas.")
            continue
        except dns.resolver.NoAnswer:
            print(f"[DNS] Le sous-domaine {full_domain} n'a pas de réponse.")
            continue
        except Exception as e:
            print(f"[DNS] Erreur avec {full_domain}: {e}")
            continue

        # Vérification HTTP
        try:
            response_http = requests.get(f"http://{full_domain}", timeout=5)
            print(f"[HTTP] http://{full_domain} → code {response_http.status_code}")
        except Exception as e:
            print(f"[HTTP] Erreur pour http://{full_domain} : {e}")

        # Vérification HTTPS
        try:
            response_https = requests.get(f"https://{full_domain}", timeout=5, verify=False)
            print(f"[HTTPS] https://{full_domain} → code {response_https.status_code}")
        except Exception as e:
            print(f"[HTTPS] Erreur pour https://{full_domain} : {e}")

    input("\nAppuyez sur Entrée pour revenir au menu.")
