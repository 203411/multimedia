import cv2
import numpy as np

lienzo = 255*np.ones((720,720,3),np.uint8)

activar = False
x1,x2,y1,y2,xin,yin = 0,0,0,0,0,0

def dibujar (evento,x,y,banderas,param):
    global x1,x2,y1,y2,lienzo, activar, xin,yin
    if evento == cv2.EVENT_LBUTTONDOWN:
        xin,yin = x,y
        activar =True
        x1,y1 = x,y
    elif evento == cv2.EVENT_MOUSEMOVE:
        if activar:
            x2,y2 = x,y
            # lienzo = 255*np.ones((512,512,3),np.uint8)
            lienzo = cv2.line(lienzo, (x1,y1),(x2,y2),(0,0,256),2)
            x1,y1 = x,y

            cv2.imshow(ventana,lienzo)
    elif evento == cv2.EVENT_LBUTTONUP:
        lienzo = cv2.line(lienzo, (xin,yin),(x2,y2),(0,0,256),2)
        cv2.imshow(ventana,lienzo)
        activar = False

ventana = 'principal'
cv2.namedWindow(ventana)
cv2.setMouseCallback(ventana,dibujar)
cv2.imshow(ventana,lienzo)
while True:
    if cv2.waitKey(10)& 0XFF == 27:
        break
cv2.destroyAllWindows()