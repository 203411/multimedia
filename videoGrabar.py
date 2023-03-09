import cv2
import time


def grabar():
    cap=cv2.VideoCapture(0)
    pre_timeframe=0
    new_timeframe=0
    frame_width = 640
    frame_height = 480

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('video1.avi', fourcc, 20.0, (frame_width, frame_height))


    while(cap.isOpened()):
        success, frame = cap.read()
        if not success:
            break
        
        frame= cv2.resize(frame, (frame_width,frame_height))
        out.write(frame)
        new_timeframe=time.time()
        fps= 1/(new_timeframe-pre_timeframe)
    
        
        pre_timeframe = new_timeframe
        fps=int(fps)
        cv2.putText(frame, "FPS: " + str(fps), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

grabar()