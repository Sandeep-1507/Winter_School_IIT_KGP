from importlib.resources import path
import numpy as np
import cv2
from collections import deque

img = np.zeros((40,40,3), np.uint8)

red = [0, 0, 255]
blue = [255, 0, 0]
white = [255, 255, 255]
grey = [127, 127, 127]
green = [60, 255, 60] 
black=(150,150,150) #since my image was pixelated and i couldn't find the soln i changed the black value to match the black in that image


import random
m=0
for i in range(40):
    for j in range(40):
        k=random.random()
        if(k>0.25):
            print(k)
            m+=1
            img[i][j]=white
        

     

img = cv2.resize(img,(200,200)) 


img[180][7]=blue  #here one can define the starting and ending coordinates
img[150][8]=red      #grey coloured pixel was ideal for my path so for ending and starting i used blue and red instead

#bfs

path_col=grey
gol_col=red


img1=img   #randomly generated image


class Node():
    def __init__(self, index, parent):
        self.x = index[0]
        self.y = index[1]
        self.parent = parent

def show_path(end, start):
    print("ending point:", end.x, end.y)
    print("starting point: ", start.x, start.y)
    current = end
    while(current != start):    
        img1[current.x][current.y] = green
        current = current.parent
    
def bfs(start):  
    q = deque()
    q.append(start)
    
    
    cv2.namedWindow('path', cv2.WINDOW_NORMAL)
    while len(q):
        current = q.popleft()
        i, j = current.x, current.y
        
        cv2.imshow('path', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        if j+1 < img.shape[1]: 
            if (img[i][j+1] == gol_col).all():
                    break    
            if (img[i][j+1] > black).all() and (img[i][j+1] != path_col).all():
                   
                
                img[i][j+1] = path_col  
                n = Node((i, j+1), current)
                q.append(n)
        if i+1 < img.shape[0]:
            if (img[i+1][j] == gol_col).all():
                    break
            if (img[i+1][j] > black).all() and (img[i+1][j] != path_col).all():
                
                
                img[i+1][j] = path_col
                n = Node((i+1, j), current)
                q.append(n)
        if j-1 > 0:
            if (img[i][j-1] == gol_col).all():
                    break
            if (img[i][j-1] > black).all() and (img[i][j-1] != path_col).all():
                
                
                img[i][j-1] = path_col
                n = Node((i, j-1), current)
                q.append(n)
        if i-1 > 0:
            if (img[i-1][j] == gol_col).all():
                    break
            if (img[i-1][j] > black).all() and (img[i-1][j] != path_col).all():
                
                
                img[i-1][j] = path_col
                n = Node((i-1, j), current)
                q.append(n)
                        
    show_path(current, start)  


start = Node((180,7), None)
bfs(start)


cv2.namedWindow('final', cv2.WINDOW_NORMAL)
cv2.imshow("final", img1)
cv2.waitKey(0)
