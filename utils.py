import requests
import dataframe_image as dfi
import pandas as pd

def send_notif_with_image(image_path):
    topic = "SimuImmoTopicTTank"
    headers = {"Filename": f"{image_path}"}

    with open(f"outputs/{image_path}", 'rb') as image_file:
        response = requests.put(f"https://ntfy.sh/{topic}", headers=headers, data=image_file)
        if response.status_code == 200:
            print("Notification envoyée avec succès.")
        else:
            print("Échec de l'envoi de la notification.")

def order_data(resultats):
    # Créer une liste d'en-têtes en fonction des clés du premier résultat
    if resultats:

        df = pd.DataFrame(resultats)

        output_filename = 'loan_info.png'
        dfi.export(df, f'outputs/{output_filename}')

        send_notif_with_image(output_filename)

    else:
        print("Aucun résultat à afficher.")


import re

def extract_loan_data(data, loanDuration):
    # Dictionnaire pour stocker les résultats
    resultats = {'Durée emprunt' : f"{loanDuration}"}

    # Expressions régulières pour extraire les valeurs numériques
    patterns = {
        "Capital emprunté": r"Capital emprunté\s+([\d\s]+) €",
        "Taux nominal fixe": r"Taux standard\s+([\d,]+) %",
        "Remise écoresponsable": r"Remise écoresponsable\s+([-\d,]+) %",
        "Taux après remise(s)": r"Taux après remise\(s\)\s+([\d,]+) %",
        "Mensualité standard": r"Mensualité standard\s+([\d\s,]+) €",
        "Mensualité après remise(s)": r"Mensualité après remise\(s\)\s+([\d\s,]+) €",
        "Montant assurance": r"assurance\s+([\d\s,]+) €/mois",
        "Économies réalisées": r"Economies réalisées\s+([\d\s]+) €",
        "Frais de dossier": r"Frais de dossier\s+([\d\s]+) €"
    }

    # Parcourir les motifs et extraire les valeurs correspondantes
    for champ, pattern in patterns.items():
        match = re.search(pattern, data)
        if match:
            # Nettoyer la valeur en supprimant les espaces et en remplaçant la virgule par un point
            valeur = match.group(1).replace(" ", "").replace(",", ".")
            resultats[champ] = float(valeur)

    return resultats
