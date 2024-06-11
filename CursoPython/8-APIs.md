# ¿Qué es una API?
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
- ### Modularidad: Las APIs permiten dividir aplicaciones grandes en módulos más pequeños y manejables, que pueden ser desarrollados y mantenidos de forma independiente.
- ### Reusabilidad: El código que expone una API puede ser reutilizado por múltiples aplicaciones, reduciendo la duplicación de esfuerzos.
- ### Interoperabilidad: Las APIs permiten que diferentes sistemas y tecnologías se comuniquen entre sí, independientemente del lenguaje de programación en el que estén escritos.
- ### Escalabilidad: Facilitan el escalado de aplicaciones, ya que los servicios pueden ser distribuidos en diferentes servidores.

# Actividades 💬
- Realiza un programa que se conecte con la inteligencia artificial Groq. Link: https://console.groq.com/docs/quickstart
- Realiza un programa que se conecte con la API de OpenWeatherMap. Link: https://openweathermap.org/api
