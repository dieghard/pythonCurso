import requests

#Funcion para obtener el clima:

def obtener_clima():
	ciudad = entrada.get()
	api_key = "dd16ff59111549fe97e10508240210"
	try:
		respuesta = requests.get(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={ciudad}&lang=es")
		clima = respuesta.json()

		if 'error' in clima:
			label_clima['text'] = f"Error: {clima['error']['message']}"
		else:
			label_clima['text'] = f"El clima en {ciudad} es de {clima['current']['temp_c']}°C con {clima['current']['condition']['text']}"
	except:
		label_clima['text'] = "Error al obtener el clima"