import cv2
import numpy as np
img1=cv2.imread('apple.jpg',1)
img2=cv2.imread('orange.jpg',1)
apple_orange=np.hstack((img1[:,:256],img2[:,256:]))
cv2.imshow('Apple',img1)
cv2.imshow('Orange',img2)
cv2.imshow('Orange1',apple_orange)

cv2.waitKey(0)
cv2.destroyAllWindows()