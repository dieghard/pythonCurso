#API:  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
import pyttsx3
engine = pyttsx3.init()
import speech_recognition as sr
r = sr.Recognizer()

from groq import Groq     

while True:
    with sr.Microphone() as source:                  #with igual a con....
        print("Hable: ")
    pregunta = print
    audio = r.listen(source)
    try:                                                 # Dice proba a hacer algo y atrapa el eror, 
        text = r.recognize_google(audio, language= 'es-ES')
        print(F"Digiste: {text}")
    except sr.UnknownValueError:                        #La documentación me dice el error que sale
        print("Lo siento, no he podido entender lo que has dicho.")
    except sr.RequestError:
        print("Lo siento, he habido un problema al intentar comunicarme con el servidor de Google.")
        
    if pregunta == "Q":
        exit("GRACIAS POR USAR NUESTRA APP")
        #break #False #!cualquier opción esta bien

    usuario = Groq(   #es un objeto pq tiene metodo y propidades pq tiene . y un metodo
    api_key= "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",
    )

    interaccion_chat = usuario.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": (pregunta),
            }
        ],
        model="llama3-8b-8192",
    )
    respuenta = interaccion_chat.choices[0].message.content
    engine.say(respuenta)
    engine.runAndWait() #siempre va al final de todo para que hable
    print(interaccion_chat.choices[0].message.content)