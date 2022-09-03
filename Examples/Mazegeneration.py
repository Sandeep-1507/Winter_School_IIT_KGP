import numpy as np
import cv2

# img=np.full((20,20),0,dtype=np.uint8)
img = np.zeros((40,40,3), np.uint8)
# cv2.imshow('show',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# white=[255,255,255]
# grey = [127, 127, 127]

red = [0, 0, 255]
blue = [255, 0, 0]
white = [255, 255, 255]
grey = [127, 127, 127]
green = [60, 255, 60] #as the thing said to be the green pixel is having these values :/
black=(0,0,0)

import random
m=0
for i in range(40):
    for j in range(40):
        k=random.random()
        if(k>0.08):
            # print(k)
            
            img[i][j]=white

     

img = cv2.resize(img,(400,400)) 

for i in range(400):
    for j in range(400):
        if (img[i][j]!=white).all():
            m+=1
            img[i][j]=black
# print(m)
# if(img[180][70]==red).all:
#     print("yes")


img[180][7]=red
img[3][19]=red








cv2.imshow('show',img)
cv2.waitKey(0)
cv2.destroyAllWindows()            

          
print (m)          
          





from random import random


# for i in range(10):
#     print(random())


