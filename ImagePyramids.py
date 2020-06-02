import cv2
import numpy as np
img=cv2.imread('lena.jpg')
layer=img.copy()
guassianpyramid=[layer]
"""
lr=cv2.pyrDown(img)
lr1=cv2.pyrDown(lr)
lr2=cv2.pyrDown(lr1)
#lr3=cv2.pyrDown(lr2)
#lr4=cv2.pyrDown(lr3)
hr=cv2.pyrDown(lr1)
hr1=cv2.pyrDown(hr)
hr2=cv2.pyrDown(hr1)
hr3=cv2.pyrDown(hr2)
"""
for i in range(6):
    layer=cv2.pyrDown(layer)
    guassianpyramid.append(layer)
    cv2.imshow(str(i),layer)

cv2.imshow("image",img)
"""
cv2.imshow("image1",lr)
cv2.imshow("image2",lr1)
cv2.imshow("image3",lr2)
#cv2.imshow("image4",lr3)
#cv2.imshow("image5",lr4)
cv2.imshow("image6",hr)
cv2.imshow("image7",hr1)
cv2.imshow("image8",hr2)
cv2.imshow("image9",hr3)
#cv2.imshow("image5",lr4)
"""
cv2.waitKey(0)
cv2.destroyAllWindows()

