# pip install pygame
import pygame
import pygame.key

# Inicializar Pygame
pygame.init()

# Definir colores
negro = (0, 0, 0)
azul = (0, 0, 255)
rojo = (255, 0, 0)
blanco = (255, 255, 255)

# Configurar la ventana
ancho = 640
alto = 480
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego de cuadrados Pygame")

# Definir los cuadrados
x = 50
y = 50
ancho_cuadrado = 40
alto_cuadrado = 40
velocidad_x = 5
velocidad_y = 5

x_rojo = ancho - ancho_cuadrado
y_rojo = alto - alto_cuadrado
velocidad_x_rojo = -3
velocidad_y_rojo = -2

# Definir la puntuación
puntuacion = 0

# Bucle principal del juego
fin = False
while not fin:
    # Revisar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocidad_x = -5
            if event.key == pygame.K_RIGHT:
                velocidad_x = 5
            if event.key == pygame.K_UP:
                velocidad_y = -5
            if event.key == pygame.K_DOWN:
                velocidad_y = 5

    # Actualizar la posición de los cuadrados
    x += velocidad_x
    y += velocidad_y
    x_rojo += velocidad_x_rojo
    y_rojo += velocidad_y_rojo

    # Rebote en los bordes
    if x + ancho_cuadrado > ancho or x < 0:
        velocidad_x *= -1
    if y + alto_cuadrado > alto or y < 0:
        velocidad_y *= -1
    if x_rojo + ancho_cuadrado > ancho or x_rojo < 0:
        velocidad_x_rojo *= -1
    if y_rojo + alto_cuadrado > alto or y_rojo < 0:
        velocidad_y_rojo *= -1

    # Detectar colisión
    if x + ancho_cuadrado > x_rojo and x < x_rojo + ancho_cuadrado:
        if y + alto_cuadrado > y_rojo and y < y_rojo + alto_cuadrado:
            puntuacion += 1
            print(f"¡Puntuación: {puntuacion}!")
            azul = (0, 255, 0)  # Cambiar el color del cuadrado azul a verde
            rojo = (0, 0, 255)  # Cambiar el color del cuadrado rojo a azul

    # Rellenar la pantalla con negro
    pantalla.fill(negro)

    # Dibujar los cuadrados
    pygame.draw.rect(pantalla, azul, (x, y, ancho_cuadrado, alto_cuadrado))
    pygame.draw.rect(pantalla, rojo, (x_rojo, y_rojo, ancho_cuadrado, alto_cuadrado))

    # Mostrar la puntuación en la pantalla
    fuente = pygame.font.Font(None, 36)
    texto_puntuacion = fuente.render(f"Puntuación: {puntuacion}", True, blanco)
    rect_puntuacion = texto_puntuacion.get_rect()
    rect_puntuacion.topleft = (10, 10)
    pantalla.blit(texto_puntuacion, rect_puntuacion)

    # Actualizar la pantalla
    pygame.display.flip()

# Finalizar Pygame
pygame.quit()


# Explicación:

# Explicación del código completo del juego de Pygame:
# 1. Librerías y variables:

# Librerías:
# pygame: Es la librería principal para crear juegos con Pygame.
# pygame.key: Se utiliza para detectar la presión de las teclas del teclado.
# Variables:
# negro: Color negro (0, 0, 0) para el fondo de la pantalla.
# azul: Color azul (0, 0, 255) para el cuadrado azul.
# rojo: Color rojo (255, 0, 0) para el cuadrado rojo.
# blanco: Color blanco (255, 255, 255) para la puntuación.
# ancho: Ancho de la ventana del juego (640 píxeles).
# alto: Alto de la ventana del juego (480 píxeles).
# pantalla: Objeto que representa la ventana del juego.
# fin: Variable booleana que controla el bucle principal del juego (True para salir, False para continuar).
# 2. Definición de los cuadrados:

# Cuadrado azul:
# x: Posición inicial en X del cuadrado azul (50 píxeles).
# y: Posición inicial en Y del cuadrado azul (50 píxeles).
# ancho_cuadrado: Ancho del cuadrado azul (40 píxeles).
# alto_cuadrado: Alto del cuadrado azul (40 píxeles).
# velocidad_x: Velocidad inicial del cuadrado azul en el eje X (5 píxeles por frame).
# velocidad_y: Velocidad inicial del cuadrado azul en el eje Y (5 píxeles por frame).
# Cuadrado rojo:
# x_rojo: Posición inicial en X del cuadrado rojo (ancho - ancho_cuadrado, es decir, en la esquina superior derecha).
# y_rojo: Posición inicial en Y del cuadrado rojo (alto - alto_cuadrado, es decir, en la esquina superior derecha).
# velocidad_x_rojo: Velocidad inicial del cuadrado rojo en el eje X (-3 píxeles por frame, para que se mueva hacia la izquierda).
# velocidad_y_rojo: Velocidad inicial del cuadrado rojo en el eje Y (-2 píxeles por frame, para que se mueva hacia arriba).
# 3. Puntuación:

# puntuacion: Variable que almacena la puntuación del jugador, inicialmente en 0.
# 4. Bucle principal del juego:

# Este bucle se ejecuta continuamente hasta que el jugador decide salir del juego (presionando el botón de cerrar la ventana o la tecla Escape).
# Dentro del bucle:
# Revisar eventos:
# Se recorren todos los eventos que se han producido en la ventana.
# Si el jugador hace clic en el botón de cerrar la ventana, se establece la variable fin en True, lo que termina el bucle y el juego.
# Si el jugador presiona una tecla, se verifica cuál es y se actualiza la velocidad del cuadrado azul en consecuencia (izquierda, derecha, arriba, abajo).
# Actualizar la posición de los cuadrados:
# Se suman las velocidades a las coordenadas x e y de cada cuadrado para actualizar su posición en la pantalla.
# Detección de rebotes en los bordes:
# Se comprueba si el cuadrado azul o rojo se sale de los límites de la ventana en los ejes X e Y.
# Si se detecta un rebote, se invierte la dirección de la velocidad correspondiente (izquierda/derecha o arriba/abajo) para que el cuadrado rebote en el borde.
# Detección de colisión:
# Se verifica si el cuadrado azul se superpone con el cuadrado rojo.
# Si hay colisión:
# Se aumenta la puntuación en 1.
# Se imprime un mensaje en la consola.
# Se cambian los colores de los cuadrados (azul a verde, rojo a azul) para indicar la colisión.
# Rellenar la pantalla con negro:
# Se pinta toda la pantalla de color negro para eliminar los elementos dibujados en el frame anterior.
# Dibujar los cuadrados:
# Se utiliza la función pygame.draw.rect() para dibujar cada cuadrado en su nueva posición y con el color correspondiente.
# Mostrar la puntuación en la pantalla:
# Se crea un objeto de tipo pygame.Font