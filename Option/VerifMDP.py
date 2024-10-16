import re

def mdp_force(password):

    print(r"""

                          ______  _     _  _______   ______  _    _ 
                         / _____)| |   | |(_______) / _____)| |  / )
                        | /      | |__ | | _____   | /      | | / / 
                        | |      |  __)| ||  ___)  | |      | |< <  
                        | \_____ | |   | || |_____ | \_____ | | \ \ 
                         \______)|_|   |_||_______) \______)|_|  \_)
                                            

    """)
    
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        print("Le mot de passe est trop court. Il doit contenir au moins 8 caractères.")

    if re.search(r'[a-z]', password):
        score += 1

    if re.search(r'[A-Z]', password):
        score += 1

    if re.search(r'[0-9]', password):
        score += 1

    if re.search(r'[@$!%*?&]', password):
        score += 1

    if score == 5:
        print("Mot de passe très fort")
    elif 3 <= score < 5:
        print("Mot de passe moyen")
    else:
        print("Mot de passe faible")

    return score
