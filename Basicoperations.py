import numpy as np
import cv2

img=cv2.imread('messi1.jpg')
img2=cv2.imread('images.png')
print(img.shape) #It will print the total number of rows,columns and channels
print(img.size)#It will print size of the image
print(img.dtype) #It will print the datatype of the image
ball=img[280:340,330:390]
img[273:333,100:160]=ball
img=cv2.resize(img,(512,512))#Resizing of image1 and storing in  img1
img2=cv2.resize(img2,(512,512))#Resize of image 1 and storing it in image 1
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))
dest=cv2.add(img,img2);#Merging two images and store in the dest variable
dest=cv2.addWeighted(img,0.5,img2,0.5,0);#Seperating images based on weight or distributing the image

cv2.imshow('image',dest)
cv2.waitKey(0)


