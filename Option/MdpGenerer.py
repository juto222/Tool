import random
import string

def generer_mot_de_passe():
    print(r"""
                    _    __     _        _           __  
                   | |  / /    | |      (_)         / /  
             _   _ | | / /____ | | _     _         / /_  
            ( \ / )|_||___   _)| || \   | |       / __ \ 
             ) X (  _     | |  | | | |  | | _  _ ( (__) )
            (_/ \_)|_|    |_|  |_| |_| _| |(_)( ) \____/ 
                                      (__/    |/                   


          

          
    """)
    ou = input("Pour quel site voulez-vous générer un mot de passe ? ")
    longueur = int(input("Quelle longueur pour le mot de passe ? "))
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    print(f'Votre mot de passe généré : {mot_de_passe}')
    
    with open('Mot_de_passe.txt', 'a') as fichier:
        fichier.write(f"{ou} : {mot_de_passe}\n")

    print("Le mot de passe a été ajouté dans 'Mot_de_passe.txt'.")