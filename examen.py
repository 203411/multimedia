import cv2
import numpy as np

# Global variables
imagen_entrada = "evaluacion.jpg"

bandera = False
x2, y2 = (-1, -1), (-1, -1)

def dibujar():
    global image, canny, img_gray
    img_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    canny = cv2.Canny(image, 40, 100)
    img_canny = cv2.dilate(canny, None, iterations=1)
    # img_canny = cv2.erode(img_canny, None, iterations=1)
    contornos, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)	
    for contorno in contornos:
        error = 0.05 * cv2.arcLength(contorno, True)
        poligono = cv2.approxPolyDP(contorno, error, True)
        x, y, ancho, largo = cv2.boundingRect(poligono)
        if len(poligono) == 4:
            if ancho > 5 and largo > 5:
                cv2.drawContours(image, [poligono], 0, (200, 100, 50), 2)
      
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

# Mostrar las imagenes 
ventana = "RGB"
cv2.namedWindow(ventana)
cv2.setMouseCallback(ventana, dibujar_rectangulo)

image = cv2.imread(imagen_entrada)
# RGB
img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow(ventana,img_rgb)
# Grises
img_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
cv2.imshow('Grises',img_gray)
# Binarizado
canny = cv2.Canny(image, 40, 100)
img_canny = cv2.dilate(canny, None, iterations=1)
cv2.imshow('Binarizado',img_canny)

# Dibujar rectangulo
while True:
    if(x2[0] != -1 and y2[0] != -1):
        cv2.rectangle(img_rgb, x2, y2, (0, 255, 0), 2)
    dibujar()
    if cv2.waitKey(1) == ord('q'):
        break

# Cerrar todo
cv2.waitKey(0)
cv2.destroyAllWindows()
