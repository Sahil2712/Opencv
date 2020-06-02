import  cv2
import numpy as np

image=cv2.imread('suduko.jpg',0)
_,th1=cv2.threshold(image,127,255,cv2.THRESH_BINARY)
th2=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)#Adaptive_Thresh_MEAN_C -It give mean value of blocksizex blocksize mean C
th3=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

cv2.imshow("Image",image)
#cv2.imshow("th1",th1)
cv2.imshow("th2",th2) #It is much more readable in Adaptive thresholding
cv2.imshow("th3",th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
