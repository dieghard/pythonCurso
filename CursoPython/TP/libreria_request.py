# Librería "requests" para hacer peticiones HTTP:
#pip install requests
import requests

url = "https://www.wikipedia.org/"
respuesta = requests.get(url)

if respuesta.status_code == 200:
  contenido = respuesta.text
  print(contenido)  # Imprime el contenido HTML de la página
else:
  print(f"Error al obtener la página: {respuesta.status_code}")