import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import glob
import pickle
#collaboration and distortion correction

def undistort_img():
    obj_points=np.zeros((6*9,3),np.float32)
    obj_points[:,:2]=np.mgrid[0:9,0:6].T.reshape(-1,2)

    #Stores all object points & image points from all images
    objpoints=[]
    imgpoints=[]
    images=glob.glob('./camera/*.jpg')

    for indx,fname in enumerate(images):
        img=cv2.imread(fname)
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        ret,corners=cv2.findChessboardCorners(gray,(9,6),None)
        if ret==True:
            objpoints.append(obj_points)
            imgpoints.append(corners)
        img_size=(img.shape[1],img.shape[0])
        ret,mtx,dist,rvecs,tvecs=cv2.calibrateCamera(objpoints,imgpoints,img_size,None,None)
        dst=cv2.undistort(img,mtx,dist,None,mtx)
        dist_pickle={}
        dist_pickle['mtx']=mtx
        dist_pickle['dist']=dist
        pickle.dump(dist_pickle,open('camera/cal_pickle.p','wb'))
def undistort(img,cal_dir='camera/cal_pickle.p'):
    with open(cal_dir,mode='rb') as f:
        file=pickle.load(f)
    mtx=file['mtx']
    dist=file['dist']
    dst=cv2.undistort(img,mtx,dist,None,mtx)
    return dst

undistort_img()

img=cv2.imread('camera/calibration1.jpg')
dst=undistort(img)