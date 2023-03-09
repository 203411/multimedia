import numpy as np
import cv2
import time as reloj


camara = cv2.VideoCapture(0)

numFrames = 200
tiempo_inicial = reloj.time()
for i in range(0, numFrames):
    if(camara.isOpened()):
        flag,frame = camara.read()
        # imread --- BGR
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        cv2.imshow('Prueba',frame)

tiempo_total = reloj.time() - tiempo_inicial
print("Refresh Rate: ",numFrames/tiempo_total, " fps")
    
camara.release()
cv2.destroyAllWindows()