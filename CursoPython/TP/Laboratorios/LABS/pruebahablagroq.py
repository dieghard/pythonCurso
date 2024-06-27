import pyttsx3
import speech_recognition as  reconoceme_la_voz
from groq import Groq

cliente_local = Groq(
    api_key = "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",
)

while True:
    pregunta = input("que te gustaria preguntar:")
    interaccion_chat = cliente_local.chat.completions.create(
        messages = [
            {
                "role" : "user",
                "content" : pregunta,
            }
        ],
        model = "llama3-8b-8192",
    )

    print (interaccion_chat.choices[0].message.content)
    pregunta = input ("continuar:(si/no)")
    if pregunta == "no":
        break
    else:
        continue