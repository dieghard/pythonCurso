'''
pip install  pyttsx3
pip install pyaudio

'''
import pyttsx3
engine = pyttsx3.init()
# Obtén todas las voces disponibles
voices = engine.getProperty('voices')
# Obtén todas las voces disponibles
voices = engine.getProperty('voices')

# Muestra todas las voces disponibles
for i, voice in enumerate(voices):
    print(f"{i}. {voice.name} ({voice.languages})")

input ("¿Saludar a los alumnos??? (S/N)")
#  volumen actual
volume = engine.getProperty('volume')
#print(f"Volumen actual: {volume}")
# velocidad actual
rate = engine.getProperty('rate')
#print(f"Velocidad actual: {rate}")
# Cambia velocidad a 150
engine.setProperty('rate', 150)
#print("La velocidad cambio a 150")

engine.setProperty('voice', voices[0].id)
#engine.say("¿Hola Queridos Alumnos como andan??")
#engine.say("Esta noche vamos a disfrutar la velada con los dos profesores mas zarpados en el mundo de la programacion")
#engine.say("Claro que si!!!! son Diego y Gaspar")
#engine.say("y les van a volar el cerebro.... puuuuuuffffff... NOS VEMOS")

engine.runAndWait()