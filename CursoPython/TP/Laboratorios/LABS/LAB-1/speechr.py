'''
pip SpeechRecognition
pip  pyaudio
'''
import speech_recognition as sr

# Inicializa el recognizer
r = sr.Recognizer()

# Configura el micrófono
with sr.Microphone() as source:
    print("Hable (tiene 10 segundos): ")
    
    # Ajusta el nivel de ruido ambiental para obtener mejores resultados
    r.adjust_for_ambient_noise(source)

    # Escucha el audio del micrófono durante 10 segundos
    audio = r.listen(source, timeout=10, phrase_time_limit=10)

    try:
        # Usa el reconocimiento de Google con el audio capturado
        text = r.recognize_google(audio, language='es-ES')
        print(f"Dijiste: {text}")
    except sr.UnknownValueError:
        print("Lo siento, no he podido entender lo que has dicho.")
    except sr.RequestError as e:
        print(f"Lo siento, ha habido un problema al intentar comunicarme con el servicio de Google: {e}")
