#Recuerda usar pip install groq
import os

from groq import Groq
import pyttsx3
import speech_recognition as sr

client = Groq(
    api_key="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",
)
engine = pyttsx3.init()
r = sr.Recognizer()
# Ajustar el umbral de energía para ser más sensible al habla
r.energy_threshold = 3000  # Valor por defecto es 3000, ajusta según sea necesario
# Ajustar el umbral de pausa para responder más rápidamente
r.pause_threshold = 0.8  # Valor por defecto es 0.8 segundos, ajusta según sea necesario
# Ajustar el tiempo de espera para la operación de escucha (opcional)
r.operation_timeout = 5  # 5 segundos de tiempo de espera, ajusta según sea necesario
# Palabra clave para activar y comando para terminar
palabra_clave = "mayordomo"

comandos_terminacion = ["terminar", "salir", "finalizar", "cerrar", "exit", "end", "stop", "quit", "close", "finish", "leave", "bye", "adios", "chao", "hasta luego", "hasta la vista", "nos vemos", "hasta pronto", "hasta mañana", "hasta la próxima", "hasta la otra", "hasta la otra semana", "hasta la otra vez", "hasta la otra ocasión", "nos vemos", "listo"]


# Esperar palabra clave para activar
while True:
    print(f"amo.. Di '{palabra_clave}' para activarme.")
    with sr.Microphone() as source:
            print("Escuchando...")
            audio = r.listen(source)
            try:
                texto = r.recognize_google(audio, language="es-ES").lower()

            except Exception as e:
                print("Error al reconocer el audio:", e)
            if palabra_clave in texto:
                break

# Procesamiento principal
contador = 0
while True:
    if contador==0 :
        print("Por favor amo, digame que desea saber: ")
        engine.say("Por favor, digame que desea saber: ")
        engine.runAndWait()
        contador = 1
    else:
        print("¿amo, Hay algo más en lo que pueda ayudarle?")
        engine.say("¿amo,Hay algo más en lo que pueda ayudarle? ")
        engine.runAndWait()

    with sr.Microphone() as source:
        print("Escuchando...")
        audio = r.listen(source)
        try:
            texto = r.recognize_google(audio, language="es-ES").lower()

        except Exception as e:
            print("Error al reconocer el audio:", e)

    print(f"Usted dijo: {texto}")

    if any(comando in texto for comando in comandos_terminacion):
        print("Finalizando el programa. Hasta luego.")
        engine.say("Adios, genio de la vida!!!  recuerde que estoy a su disposición. Hasta luego.")
        engine.runAndWait()
        break
        #         if: Esta palabra clave inicia una instrucción condicional. Se ejecutará el código dentro del      bloque if solo si la condición especificada es verdadera.

        # any(): Esta función toma un iterable como argumento (en este caso, una expresión generadora) y devuelve True si al menos un elemento del iterable cumple una condición específica. En este caso, la condición es si el elemento coincide con alguna de las palabras o frases en la lista comandos_terminacion.

        # Expresión generadora: La expresión entre paréntesis después de any() es una expresión generadora. Las expresiones generadoras son similares a los bucles for, pero generan elementos uno a la vez en lugar de recorrer toda la lista a la vez. En este caso, la expresión generadora recorre cada elemento de la lista comandos_terminacion y verifica si está presente en el texto.

        # comando in texto: Esta condición verifica si la palabra o frase actual (comando) está presente en el texto. Si lo está, la expresión generadora devuelve True, lo que hace que la función any() devuelva True y se ejecute el código dentro del bloque if.

    try:
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
        texto = ""
    except Exception as e:
        print("Error al procesar la pregunta:", e)
        engine.say("Hubo un error al procesar su pregunta.")
        engine.runAndWait()