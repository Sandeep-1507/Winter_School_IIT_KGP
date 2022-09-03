import cv2 as cv

# img=cv.imread('img.jpg')
# cv.imshow("image",img)
# cv.waitKey(0)
capture=cv.VideoCapture('kitty.gif')

while True:
    isTrue, frame=capture.read()
    cv.imshow('kitty',frame)

    if cv.waitKey(20)& 0xFF==ord('d'):
        capture.release()

cv.destroyAllWindows
# not working in my case