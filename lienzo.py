import cv2
import numpy as np




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
    elif evento == cv2.EVENT_MOUSEMOVE:
        if activar:
            x2,y2 = x,y

            lienzo = color_lienzo*np.ones((512,512,3), np.uint8)
            lienzo = cv2.rectangle(lienzo, (x1,y1), (x2,y2), (0,0,255), 2)
            # x1,y1 = x,y

            cv2.imshow(ventana, lienzo)
    elif evento == cv2.EVENT_LBUTTONUP:
        activar = False
    
cv2.setMouseCallback(ventana, dibujar)

cv2.imshow(ventana, lienzo)

while True:
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()