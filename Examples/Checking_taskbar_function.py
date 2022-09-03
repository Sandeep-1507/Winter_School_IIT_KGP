import cv2 
import numpy as np
import math
img=cv2.imread('colorextract.png',1)
r,g,b=img[:,:,2],img[:,:,1],img[:,:,0]
n,m,l=img.shape
gray=np.full((n,m),0)

mask1 = cv2.inRange(img, (0, 0, 50), (50, 50,255))
mask2 = cv2.inRange(img, (50,0,0), (255, 50, 50))


cv2.imshow('Original Image',img)
cv2.imshow('mask red color',mask1)
cv2.imshow('mask blue color',mask2)



cv2.namedWindow('B&w',cv2.WINDOW_NORMAL)
cv2.imshow('B&W',mask1.astype(np.uint8))
cv2.namedWindow('COLOR',cv2.WINDOW_NORMAL)
cv2.imshow('COLOR',img.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()        