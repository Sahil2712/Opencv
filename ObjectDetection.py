#HSV Object Detection
import cv2
import numpy as np
def nothing(x):
    pass
#cap=cv2.VideoCapture("Tracking")#Reading grom thr caamera
cv2.namedWindow("Tracking")#It will pop up the different window
cv2.createTrackbar("LH","Tracking",0,255,nothing)
cv2.createTrackbar("LS","Tracking",0,255,nothing)
cv2.createTrackbar("LV","Tracking",0,255,nothing)
cv2.createTrackbar("UB","Tracking",0,255,nothing)
cv2.createTrackbar("US","Tracking",0,255,nothing)
cv2.createTrackbar("UV","Tracking",0,255,nothing)

while True:
    frame=cv2.imread('smarties.png')
    #_frame=cap.read()#For Calling Cap variable
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    l_h=cv2.getTrackbarPos("UV","Tracking")
    l_s=cv2.getTrackbarPos("UV","Tracking")
    l_v=cv2.getTrackbarPos("UV","Tracking")
    u_h=cv2.getTrackbarPos("UV","Tracking")
    u_s=cv2.getTrackbarPos("UV","Tracking")
    u_v=cv2.getTrackbarPos("UV","Tracking")


    l_b=np.array([l_h,l_s,l_v])
    u_b=np.array([u_h,u_s,u_v])
    mask=cv2.inRange(hsv,l_b,u_b)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('image',frame)#It will pop up the smarties image
    cv2.imshow('mask',mask)#It will pop up the Masked image
    cv2.imshow('result',res)#It will pop up the smarties image


    key=cv2.waitKey(0)
    if(key==27):
        break

#cap.release#To Capture the camera input
cv2.destroyAllWindows()
