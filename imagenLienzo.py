import cv2
import numpy as np
x1,y1 = 0,0
x2,y2 = 0,0
activar=False
nombre_ventana = "Ventana"

def dibujar(evento, x, y, banderas, param):
    global x1, y1, x2, y2, img, activar
    if evento==cv2.EVENT_LBUTTONDOWN:
        activar = True
        x1, y1 = x,y
        x2,y2 = x,y
    elif evento==cv2.EVENT_MOUSEMOVE:
        if activar == True:
            x2,y2 = x,y
            img2 = cv2.line(img, (x1, y1), (x2,y2), (255,0,0), 5)
            cv2.imshow(nombre_ventana, img2)
            x1,y1 = x,y
    if evento==cv2.EVENT_LBUTTONUP:
        activar = False
        x2,y2 = x,y
        img2 = cv2.line(img, (x1,y1), (x2,y2), (255,0,0), 5)
        cv2.imshow(nombre_ventana, img2)
        
cv2.namedWindow(nombre_ventana)
cv2.setMouseCallback(nombre_ventana, dibujar)
img = np.zeros((521,512,3), np.uint8)
cv2.imshow(nombre_ventana, img)
cv2.waitKey(0)
cv2.destroyAllWindows()

