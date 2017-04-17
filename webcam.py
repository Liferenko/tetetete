import numpy as np
import cv2

camera = cv2.VideoCapture(0)

while(True):
    ret, frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(0): #stop frame and let "destroyAllWindow" close window
        break

camera.release()
cv2.destroyAllWindows()