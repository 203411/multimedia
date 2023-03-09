import cv2

camara = cv2.VideoCapture(0)

while(camara.isOpened()):
    red,frame = camara.read()
    cv2.imshow('webCam',frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
    
capture.release()
cv2.destroyAllWindows()
