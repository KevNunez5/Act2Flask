#Actividad para semana TEC
import requests

# URL base de la API de perros para obtener imágenes
url = "https://api.thedogapi.com/v1/images/search"

# Parámetros para obtener 3 imágenes
params = {
    "limit": 3  # Queremos obtener solo 3 imágenes
}

# Hacemos la solicitud a la API con los parámetros
response = requests.get(url, params=params)

# Verificamos si la solicitud fue exitosa
if response.status_code == 200:
    # Parseamos la respuesta en formato JSON
    data = response.json()
    
    # Solo iteramos sobre las primeras 3 imágenes (por si llegan más)
    for i, dog in enumerate(data[:3]):  # Limitar a 3 por seguridad
        print(f"Imagen {i+1}: {dog['url']}")
else:
    print("Error al consultar la API:", response.status_code)
