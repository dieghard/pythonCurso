#Recuerda usar pip install groq
import os

from groq import Groq
import pyttsx3
import speech_recognition as sr
import time

client = Groq(
    api_key="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",
)
engine = pyttsx3.init()
r = sr.Recognizer() 
# Ajustar el umbral de energía para ser más sensible al habla
r.energy_threshold = 3000  # Valor por defecto es 3000, ajusta según sea necesario
# Ajustar el umbral de pausa para responder más rápidamente
r.pause_threshold = 0.5  # Valor por defecto es 0.5 segundos, ajusta según sea necesario
# Ajustar el tiempo de espera para la operación de escucha (opcional)
r.operation_timeout = 5  # 5 segundos de tiempo de espera, ajusta según sea necesario
# Palabra clave para activar y comando para terminar
# Lista de palabras o frases clave para despertar al asistente

palabras_clave = ["mayordomo", "asistente", "despertate", "dame bola", "IA", "computadora", "esclavo", "ok google"]
#Aca lo imprime
print(f"amo.. Di alguna de estas palabras para despertarme: {', '.join(palabras_clave)}")
#Aca lo dice
engine.say(f"amo.. Di alguna de estas palabras para activarme: {', '.join(palabras_clave)}")
engine.runAndWait()


comandos_terminacion = ["terminar", "salir", "finalizar", "cerrar", "exit", "end", "stop", "quit", "close", "finish", "leave", "bye", "adios", "adiós", "chao",  "chau","hasta luego", "hasta la vista", "nos vemos", "hasta pronto", "hasta mañana", "hasta la próxima", "hasta la otra", "hasta la otra semana", "hasta la otra vez", "hasta la otra ocasión", "nos vemos", "listo"]

# Esperar palabra clave para activar
while True:

    for countdown in range(5, 0, -1):
        print(f"Abriendo micrófono en {countdown} segundos...", end='\r')
        time.sleep(1)
    print("Escuchando palabra clave...")

    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            texto = r.recognize_google(audio, language="es-ES").lower()
            print(f"Se ha detectado: {texto}")
            #La parte palabra in texto for palabra in palabras_clave crea una comprensión de listas.
            # Este tipo de construcción genera un iterable de manera eficiente. En este caso, el iterable contiene:
            # True si la palabra actual (palabra) de la lista palabras_clave se encuentra en el texto.
            # False si la palabra actual no se encuentra en el texto.
            if any(palabra in texto for palabra in palabras_clave): #comprension de listas
            #La función any actúa como un filtro para verificar si hay alguna coincidencia entre las palabras clave y el texto.
            # Su uso es eficiente porque evita iterar sobre toda la lista de palabras clave si no se encuentra ninguna coincidencia.
            # Es útil para simplificar la lógica y evitar código repetitivo.
                palabra_detectada = next(palabra for palabra in palabras_clave if palabra in texto)
                #                 La comprensión de listas genera un iterable que contiene las palabras clave que se encuentran en el texto.
                # La función next toma este iterable y devuelve la primera palabra clave coincidente.
                # any verifica si se ha detectado al menos una palabra clave.
                # Si any devuelve True, next obtiene la primera palabra clave coincidente
                print(f"¡Activado con la palabra '{palabra_detectada}'!")
                engine.say(f"Estoy listo para ayudarte, amo. Me has activado con la palabra {palabra_detectada}.")
                engine.runAndWait()
                break
            else:
                print("Palabra clave no detectada. Sigo esperando.")
        except sr.WaitTimeoutError:
            print("Tiempo de espera agotado, volviendo a escuchar...")
        except sr.UnknownValueError:
            print("No se pudo entender el audio")
        except sr.RequestError as e:
            print(f"Error en el servicio de reconocimiento de voz; {e}")

# Fase de conversación
contador = 0
while True:
    if contador == 0:
        print("Por favor amo, dígame qué desea saber: ")
        engine.say("Por favor, dígame qué desea saber: ")
        engine.runAndWait()
        contador = 1
    else:
        print("¿Amo, hay algo más en lo que pueda ayudarle?")
        engine.say("¿Amo, hay algo más en lo que pueda ayudarle?")
        engine.runAndWait()

    with sr.Microphone() as source:
        print("Escuchando...")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            texto = r.recognize_google(audio, language="es-ES").lower()
            print(f"Usted dijo: {texto}")

            if any(comando in texto for comando in comandos_terminacion):
                print("Finalizando el programa. Hasta luego.")
                engine.say("Adiós, genio de la vida. Recuerde que estoy a su disposición. Hasta luego.")
                engine.runAndWait()
                break

            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "user", "content": texto},
                ],
                model="llama3-8b-8192",
            )
            respuesta = chat_completion.choices[0].message.content
            print(respuesta)
            engine.say(respuesta)
            engine.runAndWait()
        except sr.WaitTimeoutError:
            print("Tiempo de espera agotado, volviendo a escuchar...")
        except sr.UnknownValueError:
            print("No se pudo entender el audio")
        except sr.RequestError as e:
            print(f"Error en el servicio de reconocimiento de voz; {e}")
        except Exception as e:
            print("Error al procesar la pregunta:", e)
            engine.say("Hubo un error al procesar su pregunta.")
            engine.runAndWait()