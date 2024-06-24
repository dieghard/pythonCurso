"""ESTO VA EN LA TERMINAL:
python -m pip install --upgrade pip
pip install pyttsx3
"""
import pyttsx3

engine = pyttsx3.init()
que_queres_que_diga = input("Escribe lo que quieras que diga: ")
engine.say(que_queres_que_diga)
#Cambiando la velocidad de la voz
rate = engine.getProperty('rate')
print(f"la velocidad actual es: {rate}")
engine.setProperty('rate', 500)
engine.say(que_queres_que_diga)
engine.setProperty('rate', 50)
engine.say(que_queres_que_diga)
#Buscando las voces que tiene Windows instalado
voces = engine.getProperty('voices')

for voz in voces: #Recorriendo todas las voces que hay instaladas
    print(f"El nombre es: {voz.name}")
#Cambiando la voz a la segunda, en este caso Ingles
engine.setProperty('voice', voces[1].id)
engine.say(que_queres_que_diga)
engine.runAndWait()

