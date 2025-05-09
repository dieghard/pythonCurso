#Import necesarios para el Laboratorio 1
import pyttsx3
import speech_recognition as sr
from groq import Groq

#Primero usamos pyttsx3 para saludarnos!

engine = pyttsx3.init()
engine.say("¡Hola! ¿En qué puedo ayudarte hoy?")
engine.runAndWait()
#Valores para logica
habla = input ("Desea escuchar la respuesta? S/N ").upper()
escrito = input ("Desea escribir la pregunta? S/N").upper()

#Segundo usamos SpeechRecognition para dar nuestro prompt

# Inicializa el recognizer
r = sr.Recognizer()
while True:
    if escrito == "N":
        # Configura el micrófono
        with sr.Microphone() as source:
            print("Hable (tiene 10 segundos): ")

            # Ajusta el nivel de ruido ambiental para obtener mejores resultados
            r.adjust_for_ambient_noise(source)

            # Escucha el audio del micrófono durante 10 segundos
            audio = r.listen(source, timeout=10, phrase_time_limit=5)

            try:
                # Usa el reconocimiento de Google con el audio capturado
                prompt = r.recognize_google(audio, language='es-ES')
                print(f"Dijiste: {prompt}")
            except sr.UnknownValueError:
                print("Lo siento, no he podido entender lo que has dicho.")
            except sr.RequestError as e:
                print(f"Lo siento, ha habido un problema al intentar comunicarme con el servicio de Google: {e}")
    else:
        prompt = input ("Qué desea preguntar?")
    #Tercero le pasamos todos los datos a la API de inteligencia artificial


    client = Groq(
        api_key = "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",
    )
    interaccion_chat = client.chat.completions.create(
        messages = [
            {
                "role" : "user",
                "content" : prompt,
            }
        ],
        model = "llama3-8b-8192",
    )



    #Cuarto obtenemos un resultado por medio de pyttsx3
    #print(chat_completion.choices[0].message.content)
    # 
    if habla == "S":
        engine.say(interaccion_chat.choices[0].message.content)
        engine.runAndWait() 
    print (interaccion_chat.choices[0].message.content)
    seguir = input ("Continuar? S/N").upper()
    if seguir == "N":
        break
print ("Gracias, hasta la próxima!! \n Nos vemos!")
        