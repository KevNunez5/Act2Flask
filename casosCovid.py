#Actividad 2 semana TEC
import requests

# URL de la API de COVID-19 para México
url = 'https://api.api-ninjas.com/v1/covid19?country=mexico'

# Clave API (reemplaza con tu clave real)
api_key = 'cuizZxSDNv6hxR6OQOwO3A==6X6grd9NZVoFijXh'

# Cabecera para enviar la clave API
headers = {
    'X-Api-Key': api_key
}

# Hacemos la solicitud GET a la API
response = requests.get(url, headers=headers)

# Verificamos si la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()

    # Buscamos los casos para el 27 de octubre de 2021
    target_date = '2021-10-27'
    
    if data and 'cases' in data[0]:
        cases = data[0]['cases']
        
        if target_date in cases:
            confirmed_cases = cases[target_date]['total']
            print(f"Casos confirmados en México al 27 de octubre de 2021: {confirmed_cases}")
        else:
            print(f"No se encontraron datos para la fecha {target_date}")
    else:
        print("No se encontraron datos de casos.")
else:
    print(f"Error al consultar la API: {response.status_code}")
