import requests

def username():
    pseudo = input("Quel est le pseudo que tu cherches ? : ").strip()

    urls = [
        f"https://tiktok.com/@{pseudo}",
        f"https://instagram.com/{pseudo}",  
        f"https://github.com/{pseudo}",
        f"https://youtube.com/@{pseudo}",
        f"https://x.com/{pseudo}",  # Twitter
        f"https://pinterest.com/{pseudo}",
        f"https://facebook.com/{pseudo}",
        f"https://linkedin.com/in/{pseudo}",
        f"https://snapchat.com/add/{pseudo}",
        f"https://reddit.com/u/{pseudo}",
        f"https://stackoverflow.com/users/{pseudo}",
        f"https://discord.com/users/{pseudo}",
        f"https://telegram.me/{pseudo}",
        f"https://flickr.com/people/{pseudo}",
        f"https://tumblr.com/blog/view/{pseudo}",
        f"https://vimeo.com/{pseudo}",
        f"https://steamcommunity.com/id/{pseudo}",
        f"https://soundcloud.com/{pseudo}",
        f"https://medium.com/@{pseudo}",
        f"https://behance.net/{pseudo}",
        f"https://dribbble.com/{pseudo}",
        f"https://clubhouse.com/@{pseudo}",
        f"https://gitlab.com/{pseudo}",
        f"https://myspace.com/{pseudo}",
        f"https://vk.com/{pseudo}",
        f"https://ok.ru/{pseudo}",
        f"https://twitch.tv/{pseudo}",
        f"https://spotify.com/user/{pseudo}",
        f"https://foursquare.com/user/{pseudo}",
        f"https://dailymotion.com/{pseudo}",
        f"https://replit.com/@{pseudo}",
        f"https://bandcamp.com/{pseudo}",
        f"https://taringa.net/{pseudo}"
    ]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    print(f"Recherche du pseudo '{pseudo}' sur {len(urls)} plateformes...")
    
    found_count = 0
    
    for url in urls:
        try:
            response = requests.get(url, headers=headers, timeout=5, allow_redirects=False)
            if response.status_code == 200:
                print(f"[+] Utilisateur trouvé sur : {url}")
                found_count += 1
            elif response.status_code == 404:
                print(f"[-] Utilisateur non trouvé sur : {url}")
            else:
                print(f"[?] Réponse inattendue ({response.status_code}) pour : {url}")
        except requests.exceptions.RequestException as e:
            print(f"[!] Erreur pour {url} : {e}")
    
    print(f"\nRecherche terminée. Trouvé sur {found_count} plateformes.")

