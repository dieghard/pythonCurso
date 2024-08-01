#API: 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
#Primero deberiamos tener instalado Groq y pyttsx3
# pip install groq
# pip install pyttsx3
from groq import Groq
import pyttsx3

#Usamos GROQ para hacer una interaccion con un chatbot

while True:
    contenido = input("A continuacion escribe lo que quieras, si no quieres volver a preguntar pon Q o Salir: ").capitalize()
    if contenido == "Q" or contenido == "Salir":
        exit("Gracias por hablar con nosotros, hasta la proxima")
        #break (Mas opciones para romper el bucle)
        #False (Mas opciones para romper el bucle)

    client = Groq(
        api_key = "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",
    )

    interaccion_chat = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": contenido,
            }
        ],
        model="llama3-8b-8192",
    )
    #Escuchemos la respuesta del chatbot con pyttsx3
    engine = pyttsx3.init()
    engine.say(interaccion_chat.choices[0].message.content)
    engine.runAndWait()
    print(interaccion_chat.choices[0].message.content)

