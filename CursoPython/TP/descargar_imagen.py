#Descargar una imagen
import requests

url_imagen = "http://www.generallevalle.gob.ar/imagen/layout/logo-municipalidad-general-levalle-color.gif"
nombre_archivo = "muni.gif"

respuesta = requests.get(url_imagen)

if respuesta.status_code == 200:
  with open(nombre_archivo, "wb") as archivo:
    archivo.write(respuesta.content)
  print(f"Imagen descargada y guardada como: {nombre_archivo}")
else:
  print(f"Error al descargar la imagen: {respuesta.status_code}")