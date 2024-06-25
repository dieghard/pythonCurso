import pyttsx3
import speech_recognition as sr
from groq import Groq
r = sr.Recognizer()

with sr.Microphone() as source:
    while True:
        pregunta = input("Ingrese su pregunta o una Q para salir  ").capitalize()
        if pregunta == "Q":
                exit (" Gracias por usar nuestra aplicacion")    
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source,timeout=10, phrase_time_limit=5)
        audio = r.listen (source)
        try:
            text= r.recognize_google(audio, language = 'es-ES')
            print(f"Dijiste: {text}")
        except sr.UnknownValueError:
            print(" Lo siento, no he podido entender lo que has dicho.")
        except sr.RequestError:
            print(" Lo siento, ha habido un problema al intentar comunicarme con el servicio de Google")
        usuario = Groq(
            api_key="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",
        )
        
        interaccion_chat = usuario.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": pregunta, # detallamos lo que queremos saber
                }
            ],
            model="llama3-8b-8192", #copia el modelo complatible y lo pegas, reemplaza 
        )

        respuesta = interaccion_chat.choices[0].message.content
        engine = pyttsx3.init()
        engine.say (respuesta)
        engine.runAndWait()
        print (respuesta)
        