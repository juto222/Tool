import requests

def web():
    print(r"""
                    _    __     _        _           __  
                   | |  / /    | |      (_)         / /  
             _   _ | | / /____ | | _     _         / /_  
            ( \ / )|_||___   _)| || \   | |       / __ \ 
             ) X (  _     | |  | | | |  | | _  _ ( (__) )
            (_/ \_)|_|    |_|  |_| |_| _| |(_)( ) \____/ 
                                      (__/    |/                   


          


                                                         
""")
    url = input("Entrez l'URL du site à vérifier (ex: http://example.com) : ")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Le site {url} est en ligne !")
        else:
            print(f"Le site {url} a répondu avec le code : {response.status_code}")
    except requests.exceptions.RequestException as e:
            print(f"Le site {url} est hors ligne ou inaccessible. Erreur : {e}")


