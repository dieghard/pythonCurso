#hacer un juego de Cara o Cruz donde el usuario tenga
#2 opciones para elegir, si jugar contra la computadora
#o un amigo… si elige la segunda deberíamos preguntarle el nombre a ambos

entrada1 = input("Hola Jugador👋, escribe tu Nombre ::.. ")
jugador1 = input("Queres jugar con un Amigo 🤹 ingresa 1 , o contra la Computadora 🖥️  ingresa 2 ::.. ")

if jugador1.isdigit() or jugador1 == 1:
    print (f"{entrada1} Que tu amigo escriba su nombre y Juguemos cara o cruz 🪙🪙...!")

if not jugador1.isdigit():
    print ("Debes ingresar opcion 1 o 2 solamente 🫨🫨... vuelve a empezar 😥😥...")
    exit()

jugador2 = input("Jugador 2 escribe tu Nombre ::..")