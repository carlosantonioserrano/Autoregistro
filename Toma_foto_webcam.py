# ejecuta en la consola el siguiente comando
# pip install opencv-python

# importamos librerias
from logging import captureWarnings
import cv2

# abrimos la camara
cap = cv2.VideoCapture(0)

#opcional para confirar ancho y alto
cap.set(cv2.CAP_PROP_FRAME_WIDTH,2560) #ancho
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1440) #alto

# Tomar la imagen
ret, frame = cap.read() # se guarda en la variable frame

# Para guardar la imagen
cv2.imwrite('D:/python/face1.jpg',frame)

# Liberar la cámara
cap.release()
