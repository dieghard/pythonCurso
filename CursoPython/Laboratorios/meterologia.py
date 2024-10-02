import tkinter as tk
import requests

# Función para obtener el clima
def obtener_clima():
    city = entry.get()  # Obtiene la ciudad ingresada
    api_key = '5d43b95c7457432d99601007240210'  # Reemplaza con tu clave API válida de WeatherAPI
    
    try:
        # Llamada a la API de WeatherAPI
        response = requests.get(f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&lang=es')
        weather = response.json()
        
        if 'error' in weather:
            label_clima['text'] = f"Error: {weather['error']['message']}"
        else:
            label_clima['text'] = format_response(weather)

    except requests.exceptions.RequestException as e:
        label_clima['text'] = f"Error al obtener los datos: {e}"

# Función para formatear la respuesta del clima
def format_response(weather):
    city = weather['location']['name']
    conditions = weather['current']['condition']['text']
    temp = weather['current']['temp_c']  # La temperatura ya está en Celsius
    return f'{city}\n{conditions}\nTemperatura: {temp:.1f}°C'

# Configuración de la ventana principal
window = tk.Tk()
window.title("Consulta del Clima")
window.geometry("300x250")
window.configure(bg="#F0F0F0")  # Fondo claro

# Título
label_titulo = tk.Label(window, text="Consulta del Clima", font=("Arial", 16, "bold"), bg="#F0F0F0", fg="#333")
label_titulo.pack(pady=10)

# Entrada para la ciudad
entry = tk.Entry(window, font=("Arial", 12), justify="center", bd=2, relief="solid")
entry.pack(pady=10)

# Botón para obtener el clima
button = tk.Button(window, text="Obtener clima", command=obtener_clima, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", relief="flat", cursor="hand2")
button.pack(pady=10)

# Label para mostrar los resultados del clima
label_clima = tk.Label(window, text="", font=("Arial", 12), bg="#F0F0F0", fg="#333", justify="center")
label_clima.pack(pady=20)

window.mainloop()
