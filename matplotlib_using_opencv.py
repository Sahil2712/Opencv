import cv2
from matplotlib import pyplot as plt

img=cv2.imread('lena.jpg',-1)
cv2.imshow('img',img)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)#If you don't convert it willshow the default image
plt.imshow(img)
plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.deqstroyAllWindows()