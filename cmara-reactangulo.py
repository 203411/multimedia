import cv2
import numpy as np

camara = cv2.VideoCapture(0)

ventana = "Lienzo"
cv2.namedWindow("Lienzo")
color_lienzo = 255
lienzo = color_lienzo*np.ones((512,512,3), np.uint8)
activar = False
x1,y1,x2,y2 = 0,0,0,0

def dibujar(evento, x,y,banderas, param):
    global x1,x2,y1,y2,lienzo, activar
    if evento == cv2.EVENT_LBUTTONDOWN:
        activar = True
        x1,y1 = x,y
        x2,y2 = x,y
    elif evento == cv2.EVENT_MOUSEMOVE:
        if activar:
            x2,y2 = x,y
            cv2.imshow(ventana, imagen)
    elif evento == cv2.EVENT_LBUTTONUP:
        activar = False
    
cv2.setMouseCallback(ventana, dibujar)

# cv2.imshow(ventana, lienzo)

while camara.isOpened():
    xd,img = camara.read()
    imagen = img
    if x1 != x2 and y1 != y2:
        imagen = cv2.rectangle(img, (x1,y1), (x2,y2), (0,0,255), 2)
    cv2.imshow(ventana, imagen)
    if cv2.waitKey(1) == ord('q'):
        break
    
cv2.destroyAllWindows()