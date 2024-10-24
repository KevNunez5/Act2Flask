import requests
from bs4 import BeautifulSoup

# URL de la página de Wikipedia de la serie Titans
URL = "https://en.wikipedia.org/wiki/Titans_(2018_TV_series)"
page = requests.get(URL)

# Crear objeto BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")

# Buscar todas las tablas de episodios (están dentro de elementos <table>)
tables = soup.find_all("table", class_="wikiepisodetable")

episode_list = []

# Iterar sobre todas las tablas de episodios
for table in tables:
    rows = table.find_all("tr")
    
    # Extraer los títulos de los episodios de cada fila
    for row in rows:
        title_column = row.find("td", class_="summary")
        if title_column:
            title = title_column.get_text(strip=True).strip('"')
            episode_list.append(title)

# Mostrar episodios con el formato solicitado
for i, title in enumerate(episode_list, start=1):
    print(f'{i} "{title}"')
