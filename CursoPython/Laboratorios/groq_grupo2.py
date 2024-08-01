#API: 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

from groq import Groq
import pyttsx3


while True:

    pregunta_usuario = input("ingresa tu pregunta o una Q para salir: ").capitalize()
    if pregunta_usuario == "Q":
        exit("Gracias por usar nuestra aplicacion")
        #break # False #!cualquier opcion esta bien
    usuario = Groq(
        api_key= "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",
    )

    interaccion_chat = usuario.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": pregunta_usuario,
            }
        ],
        model="llama3-8b-8192",
    )
    respuesta = interaccion_chat.choices[0].message.content
    engine = pyttsx3.init()
    engine.say(respuesta)
    engine.runAndWait()
