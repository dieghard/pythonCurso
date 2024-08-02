import funciones as f
contador = 0
while True:
    if contador == 0:
        f.hablar("¡Acabas de iniciar la charla con Groq una Inteligencia Artificial!")
        contador += 1
        seguir = ""
    else:
        f.hablar("¿Quieres seguir charlando con Groq? Pulsa ENTER para hacerlo, si quieres salir a continuacion envia una Q o escribe Salir:")
        seguir = input("").capitalize()
    if not seguir == "Q" or seguir == "Salir":
        def main():
            f.hablar("¡Hola! ¿En qué puedo ayudarte hoy?")
            prompt = f.escuchar()
            respuesta = f.interactuar_con_ia(prompt)
            f.hablar(respuesta)
        if __name__ == "__main__":
            main()
    else:
        exit()