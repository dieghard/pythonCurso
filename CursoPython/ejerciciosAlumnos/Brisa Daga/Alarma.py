#MI SOFWARE ALARMA:
import time
import pyttsx3
from datetime import datetime
engine = pyttsx3.init()
hora_alarma = input("Ingrese la hora de la alarme (HH:MM): ")
hora_alarma = datetime.strptime(hora_alarma, '%H:%M')
while True:
    hora_actual = datetime.now()
    hora_alarma_str = hora_alarma.strftime('%H:%M:%S')
    hora_actual_str = hora_actual.strftime('%H:%M:%S')
    if hora_actual_str == hora_alarma_str:
        print("¡Hora de levantarse!")
        engine.say("A levantarse dijo la rana mientras espiaba por la ventana")
        engine.runAndWait()
        break
    time.sleep(1) #Espera 1 segundo antes de volver a verificar





