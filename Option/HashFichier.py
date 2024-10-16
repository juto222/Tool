import hashlib

def calculer_hash_fichier():
    print(r"""

                 ______           _        _  _  _          ______   _______ 
                |  ___ \    /\   | |      | || || |   /\   (_____ \ (_______)
                | | _ | |  /  \  | |      | || || |  /  \   _____) ) _____   
                | || || | / /\ \ | |      | ||_|| | / /\ \ (_____ ( |  ___)  
                | || || || |__| || |_____ | |___| || |__| |      | || |_____ 
                |_||_||_||______||_______) \______||______|      |_||_______)
                                                             
          
          
          
          
          """)
    chemin_fichier = input("Entrez le chemin du fichier à vérifier : ")
    hash_malware = input("Entrez le hash SHA-256 connu du malware : ")

    if not hash_malware:
        hash_malware = 'f4f70b84adce36ab5ec531a01f7a97f56f9efbb6d6d70c7759e4f73d4b1e9fdb'

    try:
        sha256_hash = hashlib.sha256()
        with open(chemin_fichier, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        file_hash = sha256_hash.hexdigest()

        if file_hash == hash_malware:
            print(f'Alerte : le fichier {chemin_fichier} correspond à un malware connu !')
        else:
            print(f'Le fichier {chemin_fichier} est sain.')
    except FileNotFoundError:
        print("Erreur : fichier non trouvé. Veuillez vérifier le chemin d'accès.")
