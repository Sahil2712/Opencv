import cv2
import numpy as np
#img=cv2.imread('lena.jpg',1)
img=np.zeros([512,512,3],np.uint8)
img=cv2.line(img,(0,0),(255,255),(287,0,0),4)
img=cv2.arrowedLine(img,(0,0),(255,244),(255,0,56),10)
img=cv2.rectangle(img,(566,0),(246,344),(2737,6,78),1)
img=cv2.circle(img,(566,0),344,(465,86,94),5)
font=cv2.FONT_HERSHEY_COMPLEX
img=cv2.putText(img,'Text',(10,500),font,6,(255,255,255),10,cv2.LINE_AA)

print(img)
cv2.imshow('opencv',img)
k=cv2.waitKey()
cv2.destroyAllWindows()

if k==27:
    cv2.destroyAllWindows()
elif k=='s':
    cv2.imwrite('lena1.png')