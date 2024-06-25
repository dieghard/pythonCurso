#Import necesarios para el Laboratorio 1
import pyttsx3
import speech_recognition as sr
from groq import Groq
    
def escuchar():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hable (tiene 10 segundos): ")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=10, phrase_time_limit=10)
        try:
            prompt = r.recognize_google(audio, language='es-ES')
            print(f"Dijiste: {prompt}")
            return prompt
        except sr.UnknownValueError:
            print("Lo siento, no he podido entender lo que has dicho.")
            return None
        except sr.RequestError as e:
            print(f"Lo siento, ha habido un problema al intentar comunicarme con el servicio de Google: {e}")
            return None
        
def hablar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

def interactuar_con_ia(prompt):
    if prompt is None:
        return "No se pudo obtener un prompt válido."
    
    client = Groq(
        api_key="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",
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content
contador = 0
while True:
    if contador == 0:
        hablar("¡Acabas de iniciar la charla con Groq una Inteligencia Artificial!")
        contador += 1
        seguir = ""
    else:
        hablar("¿Quieres seguir charlando con Groq? Pulsa ENTER para hacerlo, si quieres salir a continuacion envia una Q o escribe Salir:")
        seguir = input("").capitalize()
    if not seguir == "Q" or seguir == "Salir":
        def main():
            hablar("¡Hola! ¿En qué puedo ayudarte hoy?")
            prompt = escuchar()
            respuesta = interactuar_con_ia(prompt)
            hablar(respuesta)
        if __name__ == "__main__":
            main()
    else:
        exit()