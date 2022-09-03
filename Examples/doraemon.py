#resising and greyscaling doraemon
import cv2
import math
import numpy as np
img=cv2.imread('dorae.png',0)
mat=np.full((800,800),255)


cv2.namedWindow('image',cv2.WINDOW_AUTOSIZE)
cv2.imshow('image',img)

for x in range(800):
    for y in range (800):
        if math.sqrt((480-x)**2+(400-y)**2)==200:
            mat[x][y]=0

 


cv2.waitKey(0)
cv2.destroyAllWindows()