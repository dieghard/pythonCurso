import cv2
import numpy as np

# Carga el clasificador pre-entrenado de OpenCV para la detección de caras
cascada_cara = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicia la captura de video
cap = cv2.VideoCapture(0)

while True:
    # Lee un frame de la captura de video
    ret, frame = cap.read()

    # Convierte el frame a escala de grises
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta caras en la imagen en escala de grises
    caras = cascada_cara.detectMultiScale(gris, 1.1, 4)

    # Recorre cada cara detectada
    for (x, y, w, h) in caras:
        # Crea una máscara con la forma del rostro y color azul
        mascara = np.zeros((h, w), dtype=np.uint8)
        cv2.rectangle(mascara, (0, 0), (w, h), (255, 255, 255), -1)

        # Aplica un desenfoque gaussiano a la máscara para suavizar los bordes
        mascara = cv2.GaussianBlur(mascara, (5, 5), 0)

        # Invierte la máscara para que el rostro sea negro y el fondo blanco
        mascara_invertida = 255 - mascara

        # Aplica la máscara invertida a la región de la cara
        region_cara_con_mascara = cv2.bitwise_and(frame[y:y+h, x:x+w], frame[y:y+h, x:x+w], mask=mascara_invertida)

        # Aplica un desenfoque a la cara
        #cara_desenfocada = cv2.GaussianBlur(region_cara_con_mascara, (99, 99), 30)
        # Convierte la cara a escala de grises
        cara_gris = cv2.cvtColor(region_cara_con_mascara, cv2.COLOR_BGR2GRAY)
        cara_color = cv2.cvtColor(cara_gris, cv2.COLOR_GRAY2BGR)
        # Combina la región de la cara con la máscara con el resto del frame
        # frame[y:y+h, x:x+w] = cv2.addWeighted(region_cara_con_mascara, 0.5, frame[y:y+h, x:x+w], 0.5, 0)
      # Combina la región de la cara con la máscara con el resto del frame
        frame[y:y+h, x:x+w] = cv2.addWeighted(cara_color, 0.5, frame[y:y+h, x:x+w], 0.5, 0)

    # Muestra el frame con la máscara aplicada
    cv2.imshow('Reconocimiento Facial con Máscara', frame)

    # Si se presiona la tecla 'q', termina el bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera la captura de video y cierra todas las ventanas
cap.release()
cv2.destroyAllWindows()