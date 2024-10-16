import dns.resolver

def sousdomaine():
    print(r"""
                         _  _  _  _  _  _  _  _  _      ______   _____   ______  
                        | || || || || || || || || |    / _____) / ___ \ |  ___ \ 
                        | || || || || || || || || |   | /      | |   | || | _ | |
                        | ||_|| || ||_|| || ||_|| |   | |      | |   | || || || |
                        | |___| || |___| || |___| | _ | \_____ | |___| || || || |
                         \______| \______| \______|(_) \______) \_____/ |_||_||_|
          




""")
    domain = input("Entrez le domaine cible ex(url.com): ")
    subdomains = ['www', 'mail', 'ftp', 'dev', 'admin']
    for sub in subdomains:
        try:
            result = dns.resolver.resolve(f'{sub}.{domain}', 'A')
            print(f'Sous-domaine trouvé : {sub}.{domain} - IP : {result[0]}')
        except dns.resolver.NXDOMAIN:
            pass
        except Exception as e:
            print(f'Erreur : {e}')