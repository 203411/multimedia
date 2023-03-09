"""" 
Detectar formas con opencv
Para filtrar: 
 * Convertir a escala de grises
 * Dilatar contornos
 * Erosionar contornos
 * Mediante filtros (Gaussiong mediana)
 
1.- Obtener la imagen
2.- Filtrarla
3.- Binalizarla
4.- Detectar contornos
5.- Aproximación de poligono

Ejemplo de filtrado
b,img = camara.read()
gris = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
gris = cv2.dilate(gris, None, iterations = 1)
gris = cv2.erode(gris, None, iterations = 1)        

gris = cv2.GaussionBlur(gris,(),0)
gris = cv2.medianBlur()


Ejemplo de binarizado
img = cv2.canny(img,liminf,limsup)


"""

import cv2
camara = cv2.VideoCapture(0)

while camara.isOpened():
    b, img = camara.read()
    canny = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    canny = cv2.Canny(canny,50,150)
    canny = cv2.dilate(canny, None, iterations = 1)
    canny = cv2.erode(canny,None, iterations = 1)
    contornos, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contorno in contornos:
        # Para hallar los contornos nos basamos en el perimetro
        tolerancia = 0.01 * cv2.arcLength(contorno,True)
        poligono = cv2.approxPolyDP(contorno, tolerancia, True)
        # Opcional: Crear un cuadro/rectangulo que encierre el objeto
        x,y,ancho,alto = cv2.boundingRect(poligono)
        if ancho >50 and alto >50:
            img = cv2.rectangle(img,(x,y),(x+ancho,y+ancho),(0,0,255),2)
            if len(poligono)>10:
                cv2.putText(img,'circle ',(x+10,y-10),1,1,(0,0,255),1)
                cv2.drawContours(img,[poligono],0,(0,255,255),2)
            elif len(poligono)<6:
                cv2.putText(img,'rectangle',(x+10,y-10),1,1,(0,0,255),1)
                cv2.drawContours(img,[poligono],0,(0,255,255),2)
            # elif len(poligono)==3:
            #     cv2.putText(img,'triangle',(x+10,y-10),1,1,(0,0,255),1)
                
            
    
    cv2.imshow("Imagen",img)
    if cv2.waitKey(1)== ord('q'):
        break


