import hashlib

def hasher_mot_de_passe(mot_de_passe):
    print(r"""
             ______   _____    ______                              _____       _  _      _   __   ___ 
            |  ___ \ (____ \  (_____ \                   _  _     / ___ \     | || |    | | /  | / __)
            | | _ | | _   \ \  _____) )   ___  ___  ___ ( \( \   ( (   ) )  _ | || |  _ | |/_/ || |__ 
            | || || || |   | ||  ____/   (___)(___)(___) ) )) )   > > < <  / || || | / )| |  | ||  __)
            | || || || |__/ / | |                       (_/(_/   ( (___) )( (_| || |< ( | |  | || |   
            |_||_||_||_____/  |_|                                 \_____/  \____||_| \_)|_|  |_||_|   
          


                                                                                          
    """)
    mot_de_passe = input("Entrez le mot de passe à hasher : ")
    mot_de_passe_hash = hasher_mot_de_passe(mot_de_passe)
    mot_de_passe_bytes = mot_de_passe.encode()
    hash_object = hashlib.sha256(mot_de_passe_bytes)
    return hash_object.hexdigest()
    print(f"Le mot de passe hashé est : {mot_de_passe_hash}")
