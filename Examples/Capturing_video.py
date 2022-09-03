import cv2 
import numpy as np
vid=cv2.VideoCapture(0)

while(True):
    ret,frame=vid.read()#read the frames and ret is whether it connects to pc or not 

    cv2.imshow('video',frame)


    if cv2.waitKey(1)& 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()
    