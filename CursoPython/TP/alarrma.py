import time
import pyttsx3
engine = pyttsx3.init()
# Obtén todas las voces disponibles
voices = engine.getProperty('voices')
# Obtén todas las voces disponibles
voices = engine.getProperty('voices')
hora_alarma = input("Ingrese la hora de la alarma (HH:MM): ")
while True:
    hora_actual = time.localtime()
    hora_alarma_str = hora_alarma.strftime('%H:%M:%S')
    hora_actual_str = time.strftime('%H:%M:%S')

    if hora_actual_str == hora_alarma_str:
        print("¡Hora de levantarse!")
        engine.say("A levantarse dijo la rana mientras espiaba por la ventana")
        engine.runAndWait()
        break
    time.sleep(1)  # Esperar un segundo antes de volver a verificar