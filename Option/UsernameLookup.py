import requests

def username():
    pseudo = input("Quel est le pseudo que tu cherches ? : ")

    urls = [
        f"https://tiktok.com/@{pseudo}",
        f"https://instagram.com/{pseudo}",  
        f"https://github.com/{pseudo}",
        f"https://youtube.com/@{pseudo}",
        f"https://x.com/{pseudo}", 
        f"https://pinterest.com/{pseudo}"
    ]

    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Utilisateur trouvé sur : {url}")
            elif response.status_code == 404:
                print(f"Utilisateur non trouvé sur : {url}")
            else:
                print(f"Erreur lors de la vérification de {url} : Code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Erreur de requête pour {url} : {e}")
