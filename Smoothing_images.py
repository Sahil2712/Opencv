import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('images.png')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#Smoothing is used to remove noise in images
kernal=np.ones((5,5),np.float32)/25
dest=cv2.filter2D(img,-1,kernal)
blur=cv2.blur(img,(5,5))
guassion=cv2.GaussianBlur(img,(5,5),16)
titles=['image','2D Convolution','Blur Image','Guassian']
images=[img,dest,blur,guassion]

for i in range(4):
    plt.subplot(1,4,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()