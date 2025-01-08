import requests

# URL cible
url = "https://espace-personnel.direct-assurance.fr/espace-personnel/accueil"

# Session pour gérer les cookies
session = requests.Session()

# Ajouter un User-Agent
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
})

# Requête GET avec la session
response = session.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print(f"Erreur : {response.status_code}")
