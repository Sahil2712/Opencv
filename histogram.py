import cv2
import numpy as np
from matplotlib import pyplot as plt
#img=np.zeros((200,200),np.uint8)
img=cv2.imread('lena.jpg')
"""b,g,r=cv2.split(img)
cv2.imshow("imgq",img)
cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)

#plt.hist(img.ravel(),256,[0,256])
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
"""
hist=cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist)
plt.show()
cv2.waitKey(0)

cv2.destroyAllWindows()
