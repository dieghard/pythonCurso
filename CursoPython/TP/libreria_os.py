#Librería "os" para interactuar con el sistema operativo:
import os

ruta_archivo = "archivo.txt"
#Borrar un archivo:
if os.path.exists(ruta_archivo):
  os.remove(ruta_archivo)
  print("Archivo borrado")
else:
  print("El archivo no existe")

#Cambiar el nombre de un archivo:

ruta_vieja = "archivo_viejo.txt"
ruta_nueva = "archivo_nuevo.txt"

if os.path.exists(ruta_vieja):
  os.rename(ruta_vieja, ruta_nueva)
  print("Nombre del archivo cambiado")
else:
  print("El archivo no existe")

  #Recorrer un directorio y sus subdirectorios:
def recorrer_directorio(ruta):
  for archivo in os.listdir(ruta):
    ruta_archivo = os.path.join(ruta, archivo)
    if os.path.isdir(ruta_archivo):
      recorrer_directorio(ruta_archivo)
    else:
      print(ruta_archivo)

ruta_inicial = "/ruta/al/directorio"
recorrer_directorio(ruta_inicial)

#2. Buscar archivos con un nombre específico:
def buscar_archivos(ruta, nombre_archivo):
  for archivo in os.listdir(ruta):
    ruta_archivo = os.path.join(ruta, archivo)
    if os.path.isfile(ruta_archivo) and nombre_archivo in archivo:
      print(ruta_archivo)

ruta_inicial = "/ruta/a/buscar"
nombre_archivo = "archivo_a_buscar.txt"
buscar_archivos(ruta_inicial, nombre_archivo)

#3. Eliminar un directorio y sus subdirectorios:
def eliminar_directorio(ruta):
  if os.path.exists(ruta):
    for archivo in os.listdir(ruta):
      ruta_archivo = os.path.join(ruta, archivo)
      if os.path.isfile(ruta_archivo):
        os.remove(ruta_archivo)
      else:
        eliminar_directorio(ruta_archivo)
    os.rmdir(ruta)
  else:
    print(f"El directorio '{ruta}' no existe.")

ruta_a_eliminar = "/ruta/a/eliminar"
eliminar_directorio(ruta_a_eliminar)

#4. Copiar un archivo a otra ubicación:
import os

def copiar_archivo(ruta_origen, ruta_destino):
  if os.path.exists(ruta_origen):
    nombre_archivo = os.path.basename(ruta_origen)
    ruta_destino = os.path.join(ruta_destino, nombre_archivo)
    os.copy(ruta_origen, ruta_destino)
    print(f"Archivo '{nombre_archivo}' copiado a '{ruta_destino}'.")
  else:
    print(f"El archivo '{ruta_origen}' no existe.")

ruta_origen = "/ruta/archivo_origen.txt"
ruta_destino = "/ruta/destino"
copiar_archivo(ruta_origen, ruta_destino)

#5. Obtener información sobre un archivo:
def obtener_informacion_archivo(ruta):
  if os.path.exists(ruta):
    estado = os.stat(ruta)
    fecha_creacion = estado.st_ctime
    fecha_modificacion = estado.st_mtime
    fecha_acceso = estado.st_atime
    tamaño = estado.st_size
    print(f"Archivo: {ruta}")
    print(f"Fecha de creación: {fecha_creacion}")
    print(f"Fecha de modificación: {fecha_modificacion}")
    print(f"Fecha de acceso: {fecha_acceso}")
    print(f"Tamaño: {tamaño} bytes")
  else:
    print(f"El archivo '{ruta}' no existe.")

ruta_archivo = "/ruta/archivo.txt"
obtener_informacion_archivo(ruta_archivo)




