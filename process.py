from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, requests, ast
import dataframe_image as dfi
import pandas as pd

def send_notif_with_image(image_path):
    topic = "SimuImmoTopicTTank"
    headers = {"Filename": f"{image_path}"}

    with open(image_path, 'rb') as image_file:
        response = requests.put(f"https://ntfy.sh/{topic}", headers=headers, data=image_file)
        if response.status_code == 200:
            print("Notification envoyée avec succès.")
        else:
            print("Échec de l'envoi de la notification.")

def afficher_tableau(resultats):
    # Importer la bibliothèque pour afficher les tableaux
    from tabulate import tabulate

    # Créer une liste d'en-têtes en fonction des clés du premier résultat
    if resultats:
        headers = resultats[0].keys()
        # Créer une liste de lignes en extrayant les valeurs de chaque résultat
        rows = [result.values() for result in resultats]
        # Afficher le tableau
        data_to_send = tabulate(rows, headers=headers, tablefmt='grid')
        print()

        #data_dict = ast.literal_eval(resultats)
        df = pd.DataFrame(resultats)
        dfi.export(df, 'dataframe_image.png')


        send_notif_with_image('dataframe_image.png')

    else:
        print("Aucun résultat à afficher.")


import re

def extraire_informations(data, loanDuration):
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


def process_BoursoBank_simulation(loanDuration):
    # Étape 1: Configurer le WebDriver
    driver = webdriver.Chrome()

    # URL cible
    url = "https://www.boursobank.com/credit/credit-immobilier?origine=2247&at_medium=sl&at_campaign=fr_sea&at_platform=google&at_term=&at_creation=ppi&at_variant=filrouge&origine=2247&at_medium=sl&at_campaign=fr_sea&at_platform=google&at_term=&at_creation=ppi&at_variant=filrouge&gad_source=1&gclid=Cj0KCQiA4fi7BhC5ARIsAEV1YiacKJ_nRth0h6cpsAtw750ZW6IqhC9Vc2BaarwT32sKlQfEapKXS8EaAoEsEALw_wcB#simulateur"

    # Ouvrir la page avec Selenium
    driver.get(url)

    # Récupérer le contenu HTML
    html = driver.page_source

    boutons_a_cliquer = ["Tout accepter", "Vos mensualités", "À deux"]

    for texte_bouton in boutons_a_cliquer:
        bouton = driver.find_element(By.XPATH, f"//span[text()='{texte_bouton}']")
        bouton.click()
        time.sleep(1)

    champ_texte = driver.find_element(By.ID, "text-input-0")
    champ_texte.send_keys("24")

    champ_texte = driver.find_element(By.ID, "text-input-1")
    champ_texte.send_keys("2800")

    champ_texte = driver.find_element(By.ID, "text-input-2")
    champ_texte.send_keys("0")

    champ_texte = driver.find_element(By.ID, "text-input-3")
    champ_texte.send_keys("25")

    champ_texte = driver.find_element(By.ID, "text-input-4")
    champ_texte.send_keys("2800")

    champ_texte = driver.find_element(By.ID, "text-input-5")
    champ_texte.send_keys("0")

    radio_buttons = driver.find_elements(By.NAME, "isEmployee")
    driver.execute_script("arguments[0].click();", radio_buttons[0])
    driver.execute_script("arguments[0].click();", radio_buttons[2])

    button = driver.find_element(By.XPATH, "//button[text()='Étape suivante']")
    button.click()

    radio_buttons = driver.find_elements(By.NAME, "isVefa")
    driver.execute_script("arguments[0].click();", radio_buttons[1])

    button = driver.find_element(By.XPATH, "//button[text()='Étape suivante']")
    button.click()

    radio_buttons = driver.find_elements(By.NAME, "residenceType")
    driver.execute_script("arguments[0].click();", radio_buttons[0])

    button = driver.find_element(By.XPATH, "//button[text()='Étape suivante']")
    button.click()


    champ_texte = driver.find_element(By.ID, "text-input-6")
    champ_texte.send_keys("300000")

    champ_texte = driver.find_element(By.ID, "text-input-7")
    champ_texte.send_keys("22500")

    champ_texte = driver.find_element(By.ID, "text-input-9")
    champ_texte.send_keys("22500")



    # Attendre que le conteneur de la liste déroulante soit cliquable
    wait = WebDriverWait(driver, 10)

    dropdown_containers = driver.find_elements(By.CLASS_NAME, 'c-select__combobox')
    dropdown_container = dropdown_containers[0]

    # Cliquer sur le conteneur pour ouvrir la liste déroulante
    dropdown_container.click()

    # Attendre que les options soient visibles
    options = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'c-select__option')))

    # Parcourir les options pour sélectionner celle avec le texte "B"
    for option in options:
        if option.text == f"{loanDuration}":
            option.click()
            break

    # Attendre que le conteneur de la liste déroulante soit cliquable
    wait = WebDriverWait(driver, 10)

    dropdown_containers = driver.find_elements(By.CLASS_NAME, 'c-select__combobox')
    dropdown_container = dropdown_containers[1]

    # Cliquer sur le conteneur pour ouvrir la liste déroulante
    dropdown_container.click()

    # Attendre que les options soient visibles
    options = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'c-select__option')))

    # Parcourir les options pour sélectionner celle avec le texte "B"
    for option in options:
        if option.text == "B":
            option.click()
            break

    button = driver.find_element(By.XPATH, "//button[text()='Étape suivante']")
    button.click()

    driver.implicitly_wait(10)

    rounded_card = driver.find_element(By.CLASS_NAME, "simulation-card")
    card_text = driver.execute_script("return arguments[0].innerText;", rounded_card)
    print("Texte complet de la carte :\n")
    print(card_text)
    driver.quit()
    
    return extraire_informations(card_text, loanDuration)
