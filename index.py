"""
Candas Kuran
Projet Meteo
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time


ville = input("enrez la code postal et nom de la ville :")
#? ville = 1400 yverdon-les-bains, 1000 lausanne, 1450 Le Château-de-Ste-Croix, 8000 zurich, 3000 bern, 4000 basel, 1123 Aclens, 1352 Agiez, 1165 Allaman, 1304 Allens, 1143 Apples, 1091 Aran, 1170 Aubonne, 1042 Assens, 1269 Bassins, 1372 Bavois, 1268 Begnins	
input_split = ville.split(',')

 
    #? stackoverflow => https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python
service_obj = Service("WebDrivers_path\chromedriver.exe")
browser = webdriver.Chrome(service=service_obj)
        
url = browser.get("https://prevision-meteo.ch/")
time.sleep(0.1)

for v in input_split: 

    localite = browser.find_element("xpath" , "/html/body/div[2]/nav/div[2]/div/form/div/input")
    #? avec le func. split = input_split = ["1400 yverdon-les-bains", "1000 lausanne", "1450 Sainte-Croix"]

    localite.send_keys(v)  
    time.sleep(0.1)

    rechercher = browser.find_element("xpath" , "/html/body/div[2]/nav/div[2]/div/form/div/span/button")
    rechercher.click()
    time.sleep(0.1)

        #? pour obtenir la valeur de la page html (temperature,humidite,date....etc)
    date = browser.find_element("xpath" , "/html/body/div[2]/main/div/div[1]/div[2]/div[1]/div/div/div/p[1]").text
    tmp = browser.find_element("xpath" , "/html/body/div[2]/main/div/div[1]/section/div[1]/section[1]/div[1]/div/div[2]/span[1]").text
    maxmin = browser.find_element("xpath" , "/html/body/div[2]/main/div/div[1]/section/div[1]/section[1]/div[1]/div/div[2]/span[2]").text
    humidite = browser.find_element("xpath" , "/html/body/div[2]/main/div/div[1]/div[2]/div[1]/div/div/div/ul/li[3]/p[3]").text


        #? pour exporter les valeurs vers un fichier txt
    liste = open("listesDeMeteo.txt" , "a")
    liste.write(f"\n -------------- \n ville : {v}\n date : {date}\n temperateur : {tmp}\n MaxMin : {maxmin}\n {humidite}")

