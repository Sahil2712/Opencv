import cv2
import numpy as np
from matplotlib import  pyplot as plt
cap=cv2.VideoCapture(0);
#out=cv2.VideoWriter('outptu.avi',four_cc,20.0,(640,480))
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        font=cv2.FONT_HERSHEY_COMPLEX
        frame=cv2.putText(frame,str("Hello"),(10,40),font,1,(0,255,255),2,cv2.LINE_AA)
        cv2.imshow('Frame',frame)
       # out.write(frame)
     #   gqray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
       #cv2.imshow('frame',gray)
        lap = cv2.Laplacian(frame, cv2.CV_64F, ksize=3)

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break
titles=['frame','laplacian']
iamges=[frame,lap]
for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(iamges[i],"gray")
    plt.title(titles[i])
    plt.xticks(),plt.yticks()
plt.show()
cap.release()
#out.release()
cv2.destroyAllWindows()
