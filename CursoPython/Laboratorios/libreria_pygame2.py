import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir colores
negro = (0, 0, 0)
blanco = (255, 255, 255)
rojo = (255, 0, 0)
verde = (0, 255, 0)
amarillo = (255, 255, 0)

# Configurar la ventana
ancho = 640
alto = 480
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("¡Agarra la fruta!")

# Definir la cesta
ancho_cesta = 100
alto_cesta = 50
x_cesta = ancho // 2 - ancho_cesta // 2
y_cesta = alto - alto_cesta - 10
velocidad_cesta = 5

# Definir la fruta
radio_fruta = 20
velocidad_caida = 5
frutas = []

# Definir la bomba
radio_bomba = 15
velocidad_bomba = 7
bombas = []

# Puntuación
puntuacion = 0

# Bucle principal del juego

fin = False
fuente = pygame.font.Font(None, 36)
while not fin:
    # Revisar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_cesta -= velocidad_cesta
                if x_cesta < 0:
                    x_cesta = 0
            if event.key == pygame.K_RIGHT:
                x_cesta += velocidad_cesta
                if x_cesta + ancho_cesta > ancho:
                    x_cesta = ancho - ancho_cesta

    # Crear nuevas frutas y bombas
    if random.random() < 0.2:  # 20% de probabilidad de crear una fruta
        frutas.append({"x": random.randrange(ancho - radio_fruta * 2), "y": -radio_fruta})
    if random.random() < 0.1:  # 10% de probabilidad de crear una bomba
        bombas.append({"x": random.randrange(ancho - radio_bomba * 2), "y": -radio_bomba})

    # Actualizar la posición de la fruta
    for fruta in frutas:
        fruta["y"] += velocidad_caida
        if fruta["y"] + radio_fruta > alto:
            frutas.remove(fruta)

    # Actualizar la posición de la bomba
    for bomba in bombas:
        bomba["y"] += velocidad_bomba
        if bomba["y"] + radio_bomba > alto:
            bombas.remove(bomba)

    # Detectar colisión con fruta
    for fruta in frutas:
        if fruta["y"] + radio_fruta > y_cesta and fruta["x"] >= x_cesta and fruta["x"] <= x_cesta + ancho_cesta:
            frutas.remove(fruta)
            puntuacion += 1
            print(f"¡Fruta atrapada! Puntuación: {puntuacion}")

    # Detectar colisión con bomba
    for bomba in bombas:
        if bomba["y"] + radio_bomba > y_cesta and bomba["x"] >= x_cesta and bomba["x"] <= x_cesta + ancho_cesta:
            fin = True
            print("¡Has chocado con una bomba!")

    # Rellenar la pantalla con negro
    pantalla.fill(negro)


    # Dibujar la cesta
    pygame.draw.rect(pantalla, blanco, (x_cesta, y_cesta, ancho_cesta, alto_cesta))

   # Dibujar la fruta
    for fruta in frutas:
        pygame.draw.circle(pantalla, verde, (fruta["x"], fruta["y"]), radio_fruta)

    # Dibujar la bomba
    for bomba in bombas:
        pygame.draw.circle(pantalla, rojo, (bomba["x"], bomba["y"]), radio_bomba)

    # Mostrar la puntuación en la pantalla
    texto_puntuacion = fuente.render(f"Puntuación: {puntuacion}", True, blanco)
    rect_puntuacion = texto_puntuacion.get_rect()
    rect_puntuacion.topleft = (10, 10)
    pantalla.blit(texto_puntuacion, rect_puntuacion)

    # Actualizar la pantalla
    pygame.display.flip()
# Finalizar Pygame
pygame.quit()

# Explicación:

# Librerías y variables:
# Se importan las librerías necesarias (pygame y random).
# Se definen colores para la cesta, la fruta, la bomba, el fondo y el texto.
# Se establecen las dimensiones de la ventana y se crea la ventana del juego.
# Definición de la cesta:
# Se definen el ancho, alto, posición inicial y velocidad de la cesta.
# Definición de la fruta:
# Se define el radio de la fruta, la velocidad de caída y se crea una lista vacía para almacenar las frutas.
# Definición de la bomba:
# Se define el radio de la bomba, la velocidad de caída y se crea una lista vacía para almacenar las bombas.
# Puntuación:
# Se define una variable para almacenar la puntuación inicial (0).
# Bucle principal del juego:
# Este bucle se ejecuta continuamente hasta que el jugador decide salir del juego o choca con una bomba.
# Dentro del bucle:
# Revisar eventos:
# Se comprueba si el jugador ha hecho clic en el botón de cerrar la ventana o ha presionado alguna tecla.
# Si se presiona una tecla de flecha, se actualiza la posición de la cesta hacia la izquierda o derecha, controlando que no se salga de los límites de la ventana.
# Crear nuevas frutas y bombas:
# Se utiliza la función random.random() para generar números aleatorios entre 0 y 1.
# Si el número aleatorio es menor que un valor específico (en este caso, 0.2 para la fruta y 0.1 para la bomba), se crea una nueva fruta o bomba y se agrega a la lista correspondiente.
# Actualizar la posición de la fruta:
# Se recorre la lista de frutas y se aumenta la posición en Y (caída) de cada fruta.
# Si una fruta se cae por debajo de la pantalla, se elimina de la lista.
# Actualizar la posición de la bomba:
# Se recorre la lista de bombas y se aumenta la posición en Y (caída) de cada bomba.
# Si una bomba se cae por debajo de la pantalla, se elimina de la lista.
# Detectar colisión con fruta:
# Se recorre la lista de frutas y se verifica si alguna fruta ha colisionado con la cesta.
# Si hay colisión, se elimina la fruta de la lista, se aumenta la puntuación y se imprime un mensaje en la consola.
# Detectar colisión con bomba:
# Se recorre la lista de bombas y se verifica si alguna bomba ha colisionado con la cesta.
# Si hay colisión, se establece la variable fin en True, lo que termina el bucle y el juego, y se imprime un mensaje en la consola.
# Rellenar la pantalla con negro:
# Se pinta toda la pantalla de color negro para eliminar los elementos dibujados en el frame anterior.
# Dibujar la cesta:
# Se utiliza la función pygame.draw.rect() para dibujar la cesta en su nueva posición y con el color blanco.
# Dibujar la fruta:
# Se recorre la lista de frutas y se utiliza la función pygame.draw.circle() para dibujar cada fruta en su nueva posición y con el color verde.
# Dibujar la bomba:
# Se recorre la lista de bombas y se utiliza la función pygame.draw.circle() para dibujar cada bomba en su nueva posición y con el color rojo.
# Mostrar la puntuación en la pantalla:
# Se crea un objeto de tipo pygame.Font para definir la fuente del texto.
# Se crea un objeto pygame.Surface con la puntuación formateada.
# Se obtiene el rectángulo de la superficie de texto y se posiciona en la esquina superior izquierda de la pantalla.
# Se copia la superficie de texto a la pantalla principal.