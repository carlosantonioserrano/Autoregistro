# instalamos libreria cv2 con la sentencia:
# pip install opencv-python

# instalamos libreria mediapipe
# pip install mediapipe

# importamos librerias
import cv2
import mediapipe as mp # el "as" es un sobrenombre para no escribir el nombre largo

# creamos variable para almacenar el descriptor o detector de rostro
# el descriptor es una herramienta que no sentrega las características de la imagen
detector = mp.solutions.face_detection # en la pagina de mediapipe se ve la sentencia

# el detector debe tener su herramienta de dibujo
# creamos variable que almacenaremos herramienta de dibujo
dibujo = mp.solutions.drawing_utils # aqui llamamos al mediapipe con el sobrenombre "mp"

# hacemos la videocaptura
cap = cv2.VideoCapture(0) # con el cero declaramos cuál webcam usar

# inicializamos parámetros
with detector.FaceDetection(min_detection_confidence = 0.75) as rostros:

    while True:
        # 1o leemos los fotogramas o frame
        ret, frame = cap.read() # ret lectura de fotogramas y frame los fotogramas

        # corrigiendo la colorimetría
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # deteccion de rostros
        resultado = rostros.process(rgb) # guardamos los rostros que se han detectado

        # creando filtro de seguridad
        if resultado.detections is not None:
            for rostro in resultado.detections: # si encuentra rostros en los resultados...
                dibujo.draw_detection(frame, rostro, dibujo.DrawingSpec(color=(255,0,0))) #le entregamos la ventana frame

        # mostramos los fotogramas
        cv2.imshow("Presione la tecla ESC para tomar la foto", frame)

        # declaramos la tecla para finalizar el while
        t = cv2.waitKey(1)
        if t == 27: # leo el código ASCII teclado
            break

cap.release()
cv2.destroyAllWindows()
