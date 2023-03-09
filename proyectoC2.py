import cv2
import numpy as np

camara = cv2.VideoCapture(0)

frame_weight = 700
frame_height = 700

def dibujar():
    global image, canny, img_gray
    
    img_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    canny = cv2.Canny(img_gray, 40, 100)
    canny = cv2.dilate(canny, None, iterations=1)
    contornos, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contorno in contornos:
        error = 0.01 * cv2.arcLength(contorno, True)
        poligono = cv2.approxPolyDP(contorno, error, True)
        x, y, ancho, largo = cv2.boundingRect(poligono)
        if len(poligono) == 3:
            cv2.drawContours(image, [poligono], 0, (198, 115, 115), 2)
        if len(poligono) == 4:
            if ancho > 75 and largo > 75:
                proporcion_lados = float(ancho)/largo
                if abs(proporcion_lados-1) > 0.25:
                    cv2.drawContours(image, [poligono], 0, (201, 50, 50), 2)
                else:
                    cv2.drawContours(image, [poligono], 0, (250, 250, 250), 2)
        elif len(poligono) > 10:
            cv2.drawContours(image, [poligono], 0, (100, 200, 20), 2)
            
    cv2.imshow(ventana, image)

def dibujar_rectangulo(event, x, y, flags, params):
    global x_init, y_init, bandera, x2, y2
    if event == cv2.EVENT_LBUTTONDOWN:
        bandera = True
        x_init, y_init = x, y
        roi = image[y_init:y, x_init:x] = 255 - image[y_init:y, x_init:x]
    elif event == cv2.EVENT_MOUSEMOVE:
        if bandera:
            x2, y2 = (x_init, y_init), (x, y)
            image[y_init:y, x_init:x] = 255 - image[y_init:y, x_init:x]
            roi = image[y_init:y, x_init:x] = 255 - image[y_init:y, x_init:x]
    elif event == cv2.EVENT_LBUTTONUP:
        bandera = False
        x2, y2 = (x_init, y_init), (x, y)
        image[y_init:y, x_init:x] = 255 - image[y_init:y, x_init:x]
        roi = image[y_init:y, x_init:x] = 255 - image[y_init:y, x_init:x]
        cv2.imshow("Parte recortada", roi)

bandera = False
x2, y2 = (-1, -1), (-1, -1)

ventana = "Proyecto C2"
cv2.namedWindow(ventana)
cv2.setMouseCallback(ventana, dibujar_rectangulo)

while camara.isOpened():
    ret, image = camara.read()
    if(x2[0] != -1 and y2[0] != -1):
        cv2.rectangle(image, x2, y2, (230, 255, 0), 2)
    dibujar()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camara.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
