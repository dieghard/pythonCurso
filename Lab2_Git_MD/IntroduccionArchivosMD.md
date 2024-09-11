<h1 style = "color: #6485de ;text-decoration: underline "> Introduccion a MD. 📑</h1>
Los archivos .md (Markdown) son ampliamente utilizados en la documentación de software, escritura de README en repositorios de GitHub, blogs técnicos, y mucho más debido a su simplicidad y capacidad de conversión a HTML.

## 2. ¿Qué es Markdown?

- Markdown es un lenguaje de marcado ligero que permite escribir texto de forma sencilla y formateada.
- Fue creado en 2004 por John Gruber con el objetivo de que sea fácil de leer y escribir en texto plano.
- Utilizado principalmente para escribir documentos de texto que pueden convertirse fácilmente en HTML.
- Archivos Markdown tienen la extensión .md o .markdown.

## 3. ¿Donde se utiliza Markdown?

- Documentación de software: README.md en repositorios de GitHub, GitLab, Bitbucket, etc.
- Blogs y artículos: Plataformas como Medium, Dev.to, y GitHub Pages.
- Aplicaciones de notas: Obsidian, Notion, Joplin, etc.
- Correos electrónicos: Formato de correo enriquecido en algunas herramientas.

## 4. Ventajas de usar Markdown.

- Simplicidad: Fácil de escribir y leer en texto plano.
- Versatilidad: Se puede convertir fácilmente a HTML, PDF, etc.
- Ligero y rápido: No requiere de herramientas complejas para escribir o interpretar.
- Compatibilidad: Soportado por la mayoría de plataformas de desarrollo y publicación.

## 5. Sintaxis Básica de Markdown:

1. Encabezados: Usan el símbolo # seguido del texto. Puedes usar hasta seis # para definir niveles de encabezados.

```md
# Encabezado 1
## Encabezado 2
### Encabezado 3
#### Encabezado 4
##### Encabezado 5
###### Encabezado 6

```

# Encabezado 1

## Encabezado 2

### Encabezado 3

#### Encabezado 4

##### Encabezado 5

###### Encabezado 6

2. Estilos de texto:

```md
Negrita: **texto en negrita** o __texto en negrita__
Cursiva: *texto en cursiva* o _texto en cursiva_
Combinando ambas: ***texto en negrita y cursiva*** o ___texto en negrita y cursiva___
Tachado: ~~texto tachado~~
```

Negrita: **texto en negrita** o __texto en negrita__ `<br>`
Cursiva: *texto en cursiva* o _texto en cursiva_ `<br>`
Combinando ambas: ***texto en negrita y cursiva*** o ___texto en negrita y cursiva___ `<br>`
Tachado: ~~texto tachado~~
3. Listas:

```md
Listas ordenadas:
1. Primer
2. Segundo
3. Tercero


Listas desordenadas:
- Elemento 1
- Elemento 2
- Elemento 3
```

Listas ordenadas:

1. Primer
2. Segundo
3. Tercero

Listas desordenadas:

- Elemento 1
- Elemento 2
- Elemento 3

4. Citas: Se usan el símbolo > para citar texto.

> Esto es una cita en Markdown.

5. Enlaces:

```md
[texto del enlace](URL)

```

[Visita GitHub](https://github.com)
6. Imagenes:

```md
![texto alternativo](URL de la imagen)
```

![Logo de GitHub](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png)

7. Bloques de Codigo:

```
Para código en línea, usa el acento grave: `codigo`.
Para bloques de código, usa tres acentos graves (```):
Lo bueno de implementar codigo asi es que tomará los colores por defecto del lenguaje para mostrarlo,
haciendolo más visible que con texto plano.
```

```python
def funcion():
    print("Hola Mundo")
```

8. Tablas: Puedes crearlas utilizando | para columnas y - para encabezados:

```
| Encabezado 1 | Encabezado 2 |
|--------------|--------------|
| Celda 1      | Celda 2      |
| Celda 3      | Celda 4      |
```

| Encabezado 1 | Encabezado 2 |
| ------------ | ------------ |
| Celda 1      | Celda 2      |
| Celda 3      | Celda 4      |

9. Documentacion oficial: https://www.markdownguide.org/basic-syntax/
10. Podes usar HTML en los archivos MD. Algunas de las etiquetas más utiles son:

```md
<div> </div>
<br>
<p> </p>
<h1> <h2>...
Agregando Estilos:
<div align="center"> </div>
<br>
<p> </p>
<h1 style= "color: red; text-decoration: underline"> <h2>...

```

Lo bueno de utilizar etiquetas HTML es que le ponemos poner estilos (syles) de manera mas sencilla, si bien Github no lo soporta por temas de seguridad, podemos asignarles clases a las etiquetas y despues editarlas dentro del "style". En el proximo curso aprenderemos más sobre esto. Por el momento con las que mencione son más que suficientes para organizar bien un Markdown.

11. Podemos hacer lineas horizontales con (---) (***) o (___)

---
