import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('smarties.png',cv2.IMREAD_GRAYSCALE)
_,mask=cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
kernal=np.ones([2,2],np.uint8)                #If we use [5,5] for rectangle it will increse the size of balls in diagram
dilation=cv2.dilate(mask,kernal,iterations=5) #Iterations are given to clear the black dots
erosion=cv2.erode(mask,kernal,iterations=5)   #Erosion will decrase the size of balls in image

opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal) #In this First Erosion is performed and then dilation
closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)#In this first dilation is performed and then erosion is performed
gradient=cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal)#In this first dilation is performed and then erosion is performed
th=cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernal)#In this first dilation is performed and then erosion is performed

titles=['image','mask','dilation','erosion','opening','closing','gradient','th']
images=[img,mask,dilation,erosion,opening,closing,gradient,th]
for i in range(8):
    plt.subplot(2,4,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
