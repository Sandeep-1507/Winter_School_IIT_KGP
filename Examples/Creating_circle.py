#Creating a circle using opencv_library

import cv2
import math
import numpy as np

mat=np.full((800,800),255)





for x in range(800):
    for y in range (800):
        if math.sqrt((400-x)**2+(400-y)**2)<=200:
         mat[x][y]=0

 
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',mat.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()