from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# URL dos Exoplanetas da NASA

START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

# Webdriver
browser = webdriver.Chrome("C:Home")
browser.get(START_URL)

time.sleep(10)

planets_data = []

def scrape():
    for i in range(1,2):
        while True:
            time.sleep(2)

            soup = BeautifulSoup(browser.page_source, "html.parser")

            # Verifique o número da página  
            current_page_num = int(soup.find_all("input", attrs={"class", "page_num"})[0].get("value"))

            
            # Obtenha a Tag do Hiperlink

        print(f"Coleta de dados da página {i} concluída")


# Chamando o método  
scrape()

# Defina o cabeçalho, adicione hyperlink
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date", ]

# Defina o dataframe do pandas
planet_df_1 = pd.DataFrame(planets_data, columns=headers)

# Converta para CSV
planet_df_1.to_csv('updated_scraped_data.csv',index=True, index_label="id")