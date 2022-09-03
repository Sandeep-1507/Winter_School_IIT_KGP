from importlib.resources import path
import cv2
from collections import deque

img1 = cv2.imread("task1_d.png")
# img1[200][355]=red
# img1[539][490]=green

img = img1



print(img.shape)    


red = [0, 0, 255]
blue = [255, 0, 0]
white = [255, 255, 255]
grey = [127, 127, 127]
green = [0, 255, 0] 
obs_col=(229, 233, 234)
path_col=grey #what color you want your processing path to be


img1[200][355]=red  #here the points are added
img1[539][490]=green

img = img1

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
        current = q.pop() #for dfs
        i, j = current.x, current.y
        
        cv2.imshow('path', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        if j+1 < img.shape[1]:     
            if (img[i][j+1] != obs_col).any() and (img[i][j+1] != grey).any():
                if (img[i][j+1] == green).all():
                    break   
                
                img[i][j+1] = path_col  
                n = Node((i, j+1), current)
                q.append(n)
        if i+1 < img.shape[0]:
            if (img[i+1][j] != obs_col).any() and (img[i+1][j] != grey).any():
                if (img[i+1][j] == green).all():
                    break
                
                img[i+1][j] = path_col
                n = Node((i+1, j), current)
                q.append(n)
        if j-1 > 0:
            if (img[i][j-1] != obs_col).any() and (img[i][j-1] != grey).any():
                if (img[i][j-1] == green).all():
                    break
                
                img[i][j-1] = path_col
                n = Node((i, j-1), current)
                q.append(n)
        if i-1 > 0:
            if (img[i-1][j] != obs_col).any() and (img[i-1][j] != grey).any():
                if (img[i-1][j] == green).all():
                    break
                
                img[i-1][j] = path_col
                n = Node((i-1, j), current)
                q.append(n)
                        
    show_path(current, start)  


start = Node((200,355), None)
bfs(start)


  
cv2.namedWindow('final', cv2.WINDOW_NORMAL)
cv2.imshow("final", img1)
cv2.waitKey(0)