import requests



def obtenir_infos_ip():
    print(r"""
                  __   ____   ______       __     __    _____       __      __   ______   ______ 
                 /  | / __ \ (_____ \     /  |   / /   / ___ \     /  |    /  | / __   | / __   |
                /_/ |( (__) )  ____) )   /_/ |  / /_  ( (   ) )   /_/ |   /_/ || | //| || | //| |
                  | | \__  /  /_____/      | | / __ \  > > < <      | |     | || |// | || |// | |
                  | |   / /   _______  _   | |( (__) )( (___) ) _   | | _   | ||  /__| ||  /__| |
                  |_|  /_/   (_______)(_)  |_| \____/  \_____/ (_)  |_|(_)  |_| \_____/  \_____/ 
          



                                                                                 
""")
    
    ip_address = input("Entrez une adresse IP : ")
    
    url = f"http://ipinfo.io/{ip_address}/json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"IP: {data.get('ip')}")
            print(f"Ville: {data.get('city')}")
            print(f"Région: {data.get('region')}")
            print(f"Pays: {data.get('country')}")
            print(f"Fournisseur d'accès (ISP): {data.get('org')}")
            print(f"Code postal: {data.get('postal')}")
            print(f"Localisation: {data.get('loc')}")
            print(f"Fuseau horaire: {data.get('timezone')}")
        else:
            print(f"Erreur : Impossible de récupérer les informations de l'IP {ip_address}")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

        obtenir_infos_ip()

