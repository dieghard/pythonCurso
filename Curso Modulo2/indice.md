# Programacion Modulo 2
---
# Funcionamiento del Internet
## ¿Qué es el internet?
 #### El internet es una red mundial de computadoras interconectadas que permite la comunicación y el intercambio de información entre usuarios de todo el mundo. Se basa en una serie de protocolos de comunicación que permiten a las computadoras comunicarse entre sí. 
 La historia del internet se remonta a los años 60, cuando el Departamento de Defensa de los Estados Unidos desarrolló ARPANET, una red de comunicaciones que conectaba computadoras de diferentes universidades e instituciones de investigación. Desde entonces, el internet ha experimentado un crecimiento explosivo y se ha convertido en una herramienta fundamental en todos los aspectos de la vida moderna.

 ## ¿Conoces las tecnologias que estan detras de las paginas web?
 ### Son 3: HTML (HyperText Markup Language), CSS (Cascading Style Sheets) y JavaScript son tres tecnologías fundamentales para la creación y el funcionamiento de páginas web en internet.

 - ***HTML (HyperText Markup Language):*** Es el lenguaje de marcado estándar utilizado para crear páginas web. Permite estructurar el contenido de una página web mediante el uso de etiquetas que definen diferentes elementos como encabezados, párrafos, imágenes, enlaces, formularios, entre otros. HTML proporciona la estructura básica de una página web. La relación entre HTML y el internet es fundamental, ya que HTML es el lenguaje principal utilizado para crear contenido en la web. Cada página web que ves está escrita en HTML, ya sea de forma estática o generada dinámicamente por un servidor.
 - ***CSS (Cascading Style Sheets):*** Es un lenguaje utilizado para definir el estilo y la presentación de una página web escrita en HTML. CSS permite controlar aspectos como el color, la tipografía, el diseño y el espaciado de los elementos HTML. La relación entre CSS y el internet es que CSS permite que las páginas web sean visualmente atractivas y estén bien organizadas. Sin CSS, las páginas web serían simples bloques de texto sin formato. Con CSS, los diseñadores pueden crear diseños elegantes y responsivos que se adaptan a diferentes dispositivos y tamaños de pantalla.
 - ***JavaScript:*** Es un lenguaje de programación que se utiliza principalmente para agregar interactividad y funcionalidad dinámica a las páginas web. Con JavaScript, es posible crear efectos interactivos como animaciones, validación de formularios, manipulación del DOM (Document Object Model) y comunicación con servidores para cargar datos de forma asíncrona. La relación entre JavaScript y el internet radica en que JavaScript permite que las páginas web sean más dinámicas y respondan a las acciones del usuario en tiempo real. Esto incluye desde formularios que se validan antes de enviarlos hasta aplicaciones web complejas como redes sociales o juegos en línea.

---
# HTML:

- ## Estructura Basica HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
</body>
</html>
```
> - > `<!DOCTYPE html>`
>- >`<html>`
>- >`<head>`
>- >`<meta>`
>- >`<title>`
>- >`<body>`
- ## Encabezados:
>- >`<h1>, <h2>, <h3>, <h4>, <h5>, <h6>`: Encabezados de distintos niveles.
- ## Párrafo y Texto:
>- > `<p>: Párrafo.`
>- > `<br>: Salto de línea.`
>- > `<hr>: Línea horizontal.`
>- >`<strong>: Texto en negrita.`
>- >`<em>: Texto en cursiva.`
>- >`<u>: Texto subrayado.`
>- >`<mark>: Texto marcado.`
>- >`<small>: Texto más pequeño.`
>- >`<sup>: Texto sobrescrito.`
>- >`<sub>: Texto subíndice.`
- ## Listas: 
>- >`<ul>: Lista desordenada.`
>- >`<ol>: Lista ordenada.`
>- >`<li>: Elemento de lista.`
>- >`<dl>: Lista de definición.`
>- >`<dt>: Término de definición.`
>- >`<dd>: Definición.`
- ## Enlaces y Anclas:
>- >` <a>: Enlace.`
>- >`<href>: URL de destino.`
>- >`<target>: Destino del enlace.`
>- >`<name>: Nombre del ancla.`
- ## Imagenes y Multimedia:
>- >`<img>: Imagen.`
>- >`<src>: URL de la imagen.`
>- >`<alt>: Texto alternativo.`
>- >`<audio>: Audio.`
>- >`<video>: Video.`
>- >`<source>: Fuente multimedia.`
- ## Tablas:
>- >`<table>: Tabla.`
>- >`<tr>: Fila de la tabla.`
>- >`<td>: Celda de la tabla.`
>- >`<th>: Encabezado de la tabla.`
- ## Formularios:
>- >`<form>: Formulario.`
>- >`<input>: Campo de entrada.`
>- >`<textarea>: Área de texto.`
>- >`<select>: Menú desplegable.`
>- >`<option>: Opción de selección.`
>- >`<button>: Botón.`
- ## Elementos Semánticos:
`<header>, <nav>, <main>, <section>, <article>, <aside>, <footer>: Ayudan a estructurar semánticamente la página.`
- ## Otros:
>- >`<iframe>: Incrusta contenido externo.`
>- >`<script>: Incluye scripts JavaScript.`
>- >`<div>: Contenedor genérico.`
>- >`<span>: Para aplicar estilos a porciones de texto.`
>- > ID/CLASS
>- > Eventos (onclick, onmouseover, onkeydown)

---
# CSS:
- **¿Qué es CSS?**: Explicación de qué es CSS y su relación con HTML.
- **Beneficios de CSS**: Razones para usar CSS y sus ventajas sobre los estilos en línea.
- **Sintaxis de CSS**: La estructura básica de una regla CSS (selector, propiedad, valor).

### Selectores CSS:

- **Selectores de Elemento**: Estilizar elementos HTML directamente.
- **Selectores de Clase y de ID**: Aplicar estilos a elementos con clases e IDs.
- **Selectores de Atributo**: Estilizar elementos según sus atributos.
- **Selectores de Descendencia y de Hijo**: Apuntar a elementos hijos o descendientes.

### Propiedades CSS:

- **Color y Fondo**: Cambiar el color de texto y de fondo.
- **Tipografía**: Estilizar fuentes y texto.
- **Modelo de Caja**: Controlar el tamaño, el margen, el relleno y el borde de los elementos.
- **Posicionamiento**: Posicionar elementos en la página (relativo, absoluto, fijo).
- **Flexbox**: Introducción a Flexbox para diseño flexible y alineación de elementos.
- **Grid**: Introducción a CSS Grid para diseño de cuadrícula.
- **Animaciones y Transiciones**: Crear animaciones y transiciones suaves.
- **Transformaciones**: Rotar, escalar y trasladar elementos.
- **Filtros y Efectos**: Aplicar efectos visuales a elementos.

### Unidades y Medidas:

- **Unidades de Longitud**: px, em, rem, %, etc.
- **Unidades de Color**: RGB, RGBA, HSL, HSLA, hex.
- **Media Queries**: Hacer diseños responsivos para diferentes tamaños de pantalla.
- **Viewport Units**: vw, vh, vmin, vmax.

### Diseño Responsivo:

- **Diseño Adaptativo vs. Diseño Fluidos**: Diferencias y usos.
- **Mobile First**: Estrategia de diseño centrada en dispositivos móviles.
- **Breakpoints**: Puntos de quiebre para adaptar el diseño.

### Buenas Prácticas:

- **Organización de Estilos**: Mantener estilos organizados y escalables.
- **Comentarios en CSS**: Documentar el código CSS.
- **Optimización de Carga**: Reducir el tamaño y la cantidad de archivos CSS.

### Herramientas y Recursos:

- **Frameworks CSS**: Introducción a frameworks como Bootstrap, Foundation, etc.

# JavaScript:
