#coding=utf8
"""
Created on Thu Jul 23:33 2016
"""
import cv2
import numpy as np
import random
from RawImg import vaildnumner

def polyline(img):
    pts=np.array([[0,random.randrange(0,20)],[random.randrange(20,30),random.randrange(0,20)],[40,random.randrange(20,40)]],np.uint8)
    pts=pts.reshape((-1,1,2))
    cv2.polylines(img,np.array([pts],np.int32),True,(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)),2)
    img=cv2.blur(img,(1,1))
    return img

if __name__=='__main__':
    img,num=vaildnumner()
    img=polyline(img)
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()