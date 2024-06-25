
from groq import Groq
import pyttsx3 
import speech_recognition as sr

#inicializar pyttsx3
engine = pyttsx3.init()

#Inicializar el reconocedor de voz
r = sr.Recognizer()

#Pedir al usuario que hable
print("Por favor, digame que desea saber: ")
engine.say("Por favor, digame que desea saber: ")
engine.runAndWait()

with sr.Microphone() as source:
    audio = r.listen(source) 

#Intentar reconocer la voz y convertirla a texto
try:
    pregunta = r.recognize_google(audio, language="es-ES")
    print(f"Usted dijo: {pregunta}")
    engine.say(f"Usted dijo: {pregunta}")
    engine.runAndWait()
    
except sr.UnknownValueError:
    print("No se pudo entender el audio")
    engine.say("No se pudo entender el audio")
    engine.runAndWait()
    pregunta = ""
except sr.RequestError as e:
    print(f"Error al solicitar resultados; {e}")
    engine.say("Error al solicitar resultados")
    engine.runAndWait()
    pregunta = ""


#Inicializar Groq con la clave API
usuario = Groq(
    api_key= "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"
)

#Crear la solicitud de chat con el mensaje del usuario
try:
    chat_completion = usuario.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": pregunta,
        }
    ],
    model="llama3-8b-8192",
)
    
#Obtener la respuesta del modelo
    respuesta = chat_completion.choices[0].message.content 
    engine.say (respuesta)
    engine.runAndWait()

except Exception as e:
    
# Manejar cualquier excepción que ocurra
    print(f"Error: {e}")
    engine.say("Hubo un error al procesar tu solicitud.")

engine.runAndWait()

