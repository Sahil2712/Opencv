#Python program to create trackbar
import cv2 as cv
import numpy as np
def nothing(x):
    print(x)
#img1=np.zeros((300,512,3),np.uint8)

cv.namedWindow('image')
cv.createTrackbar('CP','image',10,400,nothing)
switch='color/gray'
cv.createTrackbar(switch,'image',0,1,nothing)
while(1):
    img1 =cv.imread('lena.jpg')

    pos=cv.getTrackbarPos('CP','image')
    font=cv.FONT_HERSHEY_COMPLEX
    cv.putText(img1,str(pos),(50,150),font,4,(0,0,255))
    k=cv.waitKey(1) & 0xFF
    if k==27:
        break
    s=cv.getTrackbarPos(switch,'image')
    if s==0:
        #img1[:]=0
        pass
    else:
        img1=cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
    img1=cv.imshow('image',img1)

cv.destroyAllWindows()