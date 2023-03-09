import cv2
import time


cap = cv2.VideoCapture("video1.avi")


frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

start_time = time.time()


while cap.isOpened():

    ret, frame = cap.read()
    if ret == True:

        cv2.imshow('frame', frame)

        fps = int(1 / (time.time() - start_time))
        cv2.putText(frame, "FPS: " + str(fps), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('frame', frame)
        start_time = time.time()

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()