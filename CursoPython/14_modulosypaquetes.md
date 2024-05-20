# Modulos y Paquetes en Python 💾

## Modulos 
Un módulo en Python es simplemente un archivo de Python que contiene definiciones y declaraciones de Python. Estas definiciones pueden ser funciones, clases, variables o incluso otro código ejecutable.

Para usar un módulo en Python, simplemente usamos la palabra clave ***import*** seguida del nombre del módulo.
```python
# Crear un archivo llamado mi_modulo.py
# Contenido de mi_modulo.py
def saludar(nombre):
    print("Hola, " + nombre)

# Ahora, en otro archivo Python, podemos importar y usar la función saludar
import mi_modulo
mi_modulo.saludar("Juan")
```
## Paquetes
Un paquete en Python es una forma de estructurar módulos en un directorio jerárquico. Un paquete puede contener módulos y otros paquetes. Esto ayuda a organizar y reutilizar el código de manera eficiente.

Para crear un paquete, simplemente creamos un directorio y lo llenamos con archivos de Python (módulos). Además, necesitamos un archivo especial llamado _ _ init _ _.py en el directorio para que Python lo reconozca como un paquete.
```python
mi_paquete/
    __init__.py
    modulo1.py
    modulo2.py
```
### En otro archivo Python, podemos importar módulos de nuestro paquete
```python
from mi_paquete import modulo1, modulo2

modulo1.saludar("Juan")

```
## Importacion selectiva:
Además de importar todo un módulo o paquete, también podemos importar selectivamente funciones, clases o variables específicas de un módulo.
```python
# Importar solo la función saludar del módulo mi_modulo
from mi_modulo import saludar

saludar("Juan")
```