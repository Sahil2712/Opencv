import cv2
import numpy as np
#events=[i for i in dir(cv2) if 'EVENT' in i]
#print(events)
#It will  print the values whenever we use left click button
def click_event(event,x,y,flags,param):
    if event ==cv2.EVENT_LBUTTONDOWN:
        #print(x,'=',y)
        #font=cv2.FONT_HERSHEY_COMPLEX
        #strxy=str(x)+','+str(y)
        #cv2.putText(img,strxy,(x,y),font,1,(266,488,0),2)
#        point.append((x,y))
 #       if len(point)>=4:#If points are more than 4 the second last and last element will be printed
  #          cv2.line(img,point[-1],point[-2],(255,266,0),6)
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        cv2.circle(img, (x, y), 3, (299, 299, 0), -1)  # -1 is used to close the circle with a given color
        colorimg=np.zeros((512,512,3),np.uint8)
        colorimg[:]=[blue,green,red]
        cv2.imshow('color',colorimg)#In this whenever we use black image it will print the black image instead of color

    #It will print the values whenever we use right click button
    #if event == cv2.EVENT_RBUTTONDOWN:
        #blue=img[y,x,0]
        #green=img[y,x,1]
        #red=img[y,x,2]
        #font = cv2.FONT_HERSHEY_COMPLEX
        #strab = str(blue) + ',' + str(green)+','+str(red)
        #cv2.putText(img, strab, (x, y), font, 1, (463, 432, 364), 2)
        #cv2.imshow('image', img)



img=np.zeros([520,520,3],np.uint8)#It will be a black image
#img=cv2.imread('lena.jpg')
cv2.imshow('image',img)
point=[]
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()