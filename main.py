from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Étape 1: Configurer le WebDriver
#driver = webdriver.Chrome(executable_path="E:\Bureau\Emulation\Jeux WII\OP\chromedriver-win64.zip\chromedriver-win64")  # Remplacez avec le chemin vers votre WebDriver
driver = webdriver.Chrome()

# URL cible
url = "https://www.boursobank.com/credit/credit-immobilier?origine=2247&at_medium=sl&at_campaign=fr_sea&at_platform=google&at_term=&at_creation=ppi&at_variant=filrouge&origine=2247&at_medium=sl&at_campaign=fr_sea&at_platform=google&at_term=&at_creation=ppi&at_variant=filrouge&gad_source=1&gclid=Cj0KCQiA4fi7BhC5ARIsAEV1YiacKJ_nRth0h6cpsAtw750ZW6IqhC9Vc2BaarwT32sKlQfEapKXS8EaAoEsEALw_wcB#simulateur"

# Ouvrir la page avec Selenium
driver.get(url)

# Récupérer le contenu HTML
html = driver.page_source
#print(html)


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
champ_texte.send_keys("21500")


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

# Optionnel : Vérifier que l'élément `<select>` caché a bien été mis à jour
selected_value = driver.find_element(By.ID, 'performanceTag').get_attribute('value')
print(f"Valeur sélectionnée : {selected_value}")  # Doit afficher "B"



time.sleep(500)

# Exemple: Trouver un champ de texte par son nom, écrire dedans, et valider
#champ_texte.send_keys(Keys.RETURN)  # Simuler un appui sur "Entrée"
    
