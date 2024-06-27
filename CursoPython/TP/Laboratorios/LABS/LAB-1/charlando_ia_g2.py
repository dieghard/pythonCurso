from groq import Groq
import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init()
r = sr.Recognizer()


while True:
    with sr.Microphone() as source:
        print("Hable (tiene 10 segundos): ")

    # Ajusta el nivel de ruido ambiental para obtener mejores resultados
        r.adjust_for_ambient_noise(source)

    # Escucha el audio del micrófono durante 10 segundos
        audio = r.listen(source, timeout=10, phrase_time_limit=10)

        try:
            # Usa el reconocimiento de Google con el audio capturado
            text = r.recognize_google(audio, language='es-ES').lower()
            print(f"Escuche esto: {text}")
        except sr.UnknownValueError:
            print("Lo siento, no he podido entender lo que has dicho.")
        except sr.RequestError as e:
            print(f"Lo siento, ha habido un problema al intentar comunicarme con el servicio de Google: {e}")

    if text == "no" or text == "termina" or text == "cortala" or text == "no quiero continuar":
        break
    else:
        continue

    cliente = Groq(
        api_key="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",
    )

    interaccion_chat = cliente.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": text,
            }
        ],
        model="llama3-8b-8192",
    )

    print(interaccion_chat.choices[0].message.content)
    engine.say(interaccion_chat.choices[0].message.content)
    engine.runAndWait()