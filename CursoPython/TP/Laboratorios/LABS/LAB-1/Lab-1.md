# 👨‍💻Laboratorio 1👩‍💻
## Charlando con la Inteligencia Artificial
---
### En este primer laboratorio crearemos una Inteligencia Artificial donde el input será nuestra voz y la respuesta por parte de la I.A. será por sonido. 
### La IA seleccionada es Groq, debido a la facilidad que tiene usar su API gratuita!
---
## ¡Antes de empezar repasemos algunos conceptos!

#### Python tiene una palabra reservada para usar librerias que no trae por defecto, esta palabra es  ***import***, seguido del nombre nos dejará usar los metodos, funciones y variables que está traiga definidas en su interior. Un ejemplo ya visto es ***import random*** libreria que nos permite generar numeros aleatorios.

#### Ahora empiezan los problemas, ya que no todas las librerias estan por defecto en la instalacion de python, hay algunas que debemos instalarlas nosotros y esto se hace poniendo el siguiente comando en la terminal (***Es muy importante que recuerden ponerlo en la terminal, ya que sino python no hará nada***)

### ***pip install***

#### Seguido del nombre de la libreria a instalar, nos descargará todos los modulos y paquetes que son necesarios para usarla!

## 👀OJO👀
##### Al usar pip install solo se nos descargara de forma local la libreria, si compartimos el archivo de python.py, el mismo no se ejecutará ya que no esta instalado en la computadora del cliente! La solucion es al momento de compartir el ejecutable es instalarle la libreria(más adelante lo veremos más a fondo)
---
## ¿Qué es una API?
### Las APIs (Application Programming Interfaces, o Interfaces de Programación de Aplicaciones) son un conjunto de definiciones y protocolos que permiten que las diferentes aplicaciones de software se comuniquen entre sí. 
---
API (Interface de Programación de Aplicaciones): Es una interfaz que define las interacciones entre diferentes piezas de software. Una API especifica cómo deben interactuar los componentes del software entre sí. Esto incluye qué funciones están disponibles, cómo se llaman esas funciones, qué parámetros se deben proporcionar y qué resultados se pueden esperar.

## Componentes de una API:
### No se preocupen, las veremos más a fondo en proximos modulos!🤣
- Endpoints
- Métodos HTTP
- Headers
- Body
---
## Ejemplo de uso de una API:
Imagina que tienes una aplicación de clima que necesita obtener los datos meteorológicos de diferentes ciudades. En lugar de tener una base de datos propia con esta información, tu aplicación puede usar una API pública de un servicio meteorológico. El proceso sería algo así:
- Tu aplicación envía una solicitud a la API del servicio meteorológico en un endpoint como https://api.weather.com/v3/weather/forecast?city=Barcelona.
- La API del servicio meteorológico procesa la solicitud, recupera los datos del clima actual de su base de datos y envía una respuesta con esta información.
- Tu aplicación recibe la respuesta y presenta los datos al usuario, como la temperatura actual, la previsión del tiempo, etc.
## Beneficios de las APIs
- #### Modularidad: Las APIs permiten dividir aplicaciones grandes en módulos más pequeños y manejables, que pueden ser desarrollados y mantenidos de forma independiente.
- #### Reusabilidad: El código que expone una API puede ser reutilizado por múltiples aplicaciones, reduciendo la duplicación de esfuerzos.
- #### Interoperabilidad: Las APIs permiten que diferentes sistemas y tecnologías se comuniquen entre sí, independientemente del lenguaje de programación en el que estén escritos.
- #### Escalabilidad: Facilitan el escalado de aplicaciones, ya que los servicios pueden ser distribuidos en diferentes servidores.


---
## Usando pip install en el Laboratorio

#### Para este caso necesitarémos instalar las siguientes librerias:
- #### pyttsx3
- #### SpeechRecognition
- #### pyaudio
- #### groq
---
### Nuestros pasos para realizar el programa completo serán los siguientes:
## 1- Realizar un programa que haga hablar a nuestra computadora utilizando la libreria pyttsx3. 

## 2- Realizar un programa que escuche nuestra voz y la transcriba a texto utilizando la libreria SpeechRecognition

## 3- Realiza un programa que permita consultar a la API de groq, mandandole un mensaje con un input y recibiendo por terminal la respuesta.

## 4- Realiza un programa que permita consultar la API de groq siendo el input nuestra voz y que nos de la respuesta por medio de sonido.

Documentacion API groq: https://console.groq.com/docs/quickstart

