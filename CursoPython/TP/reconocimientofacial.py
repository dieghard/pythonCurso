#instalar esto
# pip install opencv-python
# pip install opencv-python-headless
import cv2
# Carga el clasificador pre-entrenado de OpenCV para la detección de caras
cascada_cara = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0) # Inicia la captura de video
while True:     # Lee un frame de la captura de video
    ret, frame = cap.read()
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)# Convierte el frame a escala de grises
    caras = cascada_cara.detectMultiScale(gris, 1.1, 4) # Detecta caras en la imagen en escala de grises
    for (x, y, w, h) in caras: # Dibuja un rectángulo alrededor de cada cara detectada
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('Reconocimiento Facial', frame) # Muestra el frame con los rectángulos en una ventana
    if cv2.waitKey(1) & 0xFF == ord('q'): # Si se presiona la tecla 'q', termina el bucle
        break
cap.release() # Libera la captura de video y cierra todas las ventanas
cv2.destroyAllWindows()