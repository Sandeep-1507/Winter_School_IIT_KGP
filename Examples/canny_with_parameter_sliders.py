#This code is the implementation of canny_edge detection along with its parameters decided by using sliders


import cv2 
import numpy as np
vid=cv2.VideoCapture(0)
def nothing(x):
  pass
cv2.namedWindow('Colorbars')
cv2.createTrackbar("lc1", "Colorbars",0,255,nothing)
cv2.createTrackbar("lc2", "Colorbars",0,255,nothing)
cv2.createTrackbar("lc3", "Colorbars",0,255,nothing)
cv2.createTrackbar("hc1", "Colorbars",0,255,nothing)
cv2.createTrackbar("hc2", "Colorbars",0,255,nothing)
cv2.createTrackbar("hc3", "Colorbars",0,255,nothing)

while(True):
    a1=cv2.getTrackbarPos("lc1", "Colorbars")
    a2=cv2.getTrackbarPos("lc2", "Colorbars")
    a3=cv2.getTrackbarPos("lc3", "Colorbars")
    b1=cv2.getTrackbarPos("hc1", "Colorbars")
    b2=cv2.getTrackbarPos("hc2", "Colorbars")
    b3=cv2.getTrackbarPos("hc3", "Colorbars")

    ret,frame=vid.read()#read the frames and ret is whether it connects to pc or not 
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_color=np.array([a1,a2,a3])
    higher_color=np.array([b1,b2,b3])
    mask=cv2.inRange(hsv,lower_color,higher_color)
    # edge=cv2.Canny(frame,100,200)
    cv2.imshow('mask',mask)
    # cv2.imshow('video',frame)
    # cv2.imshow('video',edge)`w`
    

    if cv2.waitKey(1)& 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()