import cv2
import numpy as np
img=cv2.imread('images.png',1)
image_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(image_gray,127,255,0)
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("No of COntours"+str(len(contours)))
print(contours[0])
cv2.drawContours(img,contours,10,(255,255,0),3)
cv2.imshow("image",img)
cv2.imshow("image_gray",image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()