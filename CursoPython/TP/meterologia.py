import tkinter as tk
import requests
import json


def obtener_clima():
    # Reemplaza 'your_api_key' con tu clave API de OpenWeatherMap

    city = entry.get()
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city},es&appid=a7d4020858a5cb002fa17968eff2db4f')
    weather = json.loads(response.text)

    if weather['cod'] == '404' :
         label['text']  = weather['message']
    else:
        label['text'] = format_response(weather)

def format_response(weather):
    try:
        city = weather['name']
        conditions = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = 'Ciudad: %s \nCondiciones: %s \nTemperatura (°C): %s' % (city, conditions, temp)
    except:
        final_str = 'Hubo un problema al obtener la información'
    return final_str

window = tk.Tk()
window.title("Clima loco ☀️🌦️⛅🌤️")

frame = tk.Frame(window)
frame.pack()

label_instruction = tk.Label(frame, text="Escriba la ciudad para saber el clima:")
label_instruction.pack()

entry = tk.Entry(frame)
entry.pack()

button = tk.Button(frame, text="Obtener clima", command=obtener_clima)
button.pack()

label = tk.Label(window, font=("Arial", 20))
label.pack()

window.mainloop()