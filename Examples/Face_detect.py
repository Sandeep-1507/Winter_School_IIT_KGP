#face detection using the library
import cv2
import numpy as np
imcap=cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
while True:
    success, img = imcap.read() 
     
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    
    faces = faceCascade.detectMultiScale(imgGray, 1.3, 5)  

    
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255,   0), 3)
    
    cv2.imshow('face_detect', img)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
map.release()
cv2.destroyWindow('face_detect')






