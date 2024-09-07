<h1><span style= "color: red; text-decoration: underline">Laboratorio 2:</span> Introduccion a Git y Archivos MD <h1>

---

# 1- Introduccion a Git y GitHub 👽

## ¿Qué es Git?

- Es un sistema de control de versiones distribuido.
- Permite a los desarrolladores colaborar en proyectos de software.
- Seguimiento de cambios en archivos y codigo fuente.
- Fue desarrollado por Linus Torvalds en 2005.

## ¿Qué es GitHub?
- Plataforma web que utiliza Git.
- Ofrece herramientas de colaboracion, revision de codigo y gestion de proyectos.
- Es utilizada para almacenar y compartir codigo, colaborar en proyectos de código abierto y gestionar repositorios.

---

## 2- Conceptos Básicos de Git.

### Repositorio (Repo/Repository):
> Lugar donde se almacena el código de un proyecto junto a su historial de cambios.

### Commit:
> Una instantanea de los cambios en el repositorio. Cada commit tiene un mensaje que describe los cambios realizados.

### Branch(Rama):
>Permite crear "lineas de tiempo" separadas del proyecto para trabajar en diferentes caracteristicas o corregir errores.
Ejemplo: **main o master** suelen ser las ramas principales y por lo general se crean algunas como ***devop, develop, feature/nueva-funcionalidad.***

### Merge:
> Proceso por el cual se combinan los cambios de una rama con otra.

### Pull Request (PR):
> Solicitud para funcionar cambios de una rama en otra, utilizada en Github principalmente para colaborar y revisar codigo.

### Clone y Fork:
> - ***Clone:*** Copiar un repositorio en local.
> - ***Fork:*** Crear una copia de un repositorio en tu cuenta de Github.

---

## 3- Comandos Básicos de Git.

- #### **git init :** inicializa un nuevo repositorio de Git.
- #### **git clone [url]:** Clona un repositorio existente.
- #### **git add [archivo]:** Añade un archivo al área de preparacion.
- #### **git commit -m "mensaje":** Realiza un commit de los cambios.
- #### **git status:** Muestra el estado del repositorio.
- #### **git push:** Envia los commit locales al repositorio remoto.
- #### **git pull:** Trae y fusiona cambios en el repositorio remoto. 

---
## 4- Instalar Git.
>Link para descargarlo: https://git-scm.com/

Para verificar si Git esta instalado correctamente, ejecutar el siguiente codigo en tu terminal.
```
git --version
```
Si esta instalado correctamente deberá imprimir la version instalada.

## 5- Configurando tu Cuenta de Git.
#### Configurar tu cuenta es un paso importante, ya que cada commit que realices tendrá tu nombre y correo electrónico asociado. Los comandos de configuración se ejecutan en la terminal o en el símbolo del sistema.
#### Nos creamos una cuenta en GitHub, https://github.com/

1. Configurar el nombre de usuario:
```
git config --global user.name "Tu Nombre"
```
2. Configurar el correo electrónico:
```
git config --global user.email "tuemail@ejemplo.com"
```
3. Verifica la configuracion:
```
git config --global --list
```
---
## 6- Uso Básico de Git.
##### Acá hay dos formas de utilizar Git, la correcta y la que nos ayuda visual Studio Code. La correcta es mediante el uso de la terminal, y es la que veremos a continuacion.

### Crea tu primer Repositorio en Git.
1. Crea una carpeta para tu proyecto con los siguientes comandos:
    ```
    mkdir mi-primer-repositorio
    cd mi-primer-repositorio
    ```
2. Inicializa un repositorio de Git en la carpeta:
    ```
    git init
    ```
3. Crea un archivo de texto, por ejemplo, README.md:
    ```
    echo "#Mi Primer Repositorio" >> README.md
    ```
4. Añadir el archivo al área de preparacion
    ```
    git add README.md
    ```
    Podes agregar todos los archivos de la carpeta con el siguiente comando:
    ```
    git add .
    ```
5. Hacer un commit de los cambios:
    ```
    git commit -m "Agrega el archivo README con título inicial"

    ```
6. Creando y Usando Ramas(Branches). <br>
    Las ramas nos permiten trabajar en caracteristicas o cambios separados al codigo principal, para este primer ejemplo usaremos la principal ***main o master***
    ```
    El comando es:
    git branch nombre-de-la-rama

    El que utilizaremos:
    git branch -M main

    Para cambiar entre ramas:
    git checkout nombre-de-la-rama
    ```
7. Para fusionar cambios de una rama a otra:
    <br> Para fusionar cambios, primero cambiamos a la rama principal y luego ejecutamos:
    ```
    git checkout main
    git merge nombre-de-la-rama
    ```
8. Para Eliminar una rama:
    ```
    git branch -d nombre-de-la-rama
    ```
9. Podemos ver el estado del repositorio y el historial con los siguientes comandos:
    ```
    git status

    git log
    ```
### 7- Conectar con GitHub:
1. En tu cuenta de GitHub, haz clic en el botón New para crear un nuevo repositorio.
2. Para conectarlo, en la terminal agrega el repositorio remoto(GitHub) a tu repositorio local:
    ```
    git remote add origin https://github.com/tuusuario/mi-primer-repositorio.git
    ```
3. Subir(Push) los Cambios al repositorio Remoto:
    ```
    git push -u origin main
    ```

### 8- Conectar nuestra cuenta de GitHub en VisualStudioCode.
### Poniendo bonito nuestro perfil:
https://gprm.itsvg.in/
https://rahuldkjain.github.io/gh-profile-readme-generator/
https://profilinator.rishav.dev/

---
# 1- Introduccion a MD.