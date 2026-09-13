import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://quotes.toscrape.com/"
response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, "html.parser")
citas = soup.find_all("div", class_="quote")

datos = []
for cita in citas:
    frase_texto = cita.find("span", class_="text").get_text(strip=True)
    autor = cita.find("small", class_="author").get_text(strip=True)
    
    # Extraer las etiquetas asociadas a cada cita
    tags_tags = cita.find_all("a", class_="tag")
    lista_tags = [tag.get_text(strip=True) for tag in tags_tags]

    datos.append({
        "frase": frase_texto,
        "autor": autor,
        "tags": ", ".join(lista_tags)
    })

df = pd.DataFrame(datos)
df.to_csv("catalogo_citas.csv", index=False)
print("Scraping exitoso y archivo catalogo_citas.csv creado.")

with open ("scraper_quotes.py","w",encoding="utf-8") as f:
    f.write(script_code)
