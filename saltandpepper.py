#coding=utf8
"""
Created on Mon Jul 16:58 2016
"""
import cv2
import numpy as np
import random
from RawImg import vaildnumner

def saltpepper(img,salt=0.1,pepper=0):  #添加椒盐噪声
    rows,cols,channels=img.shape
    for i in range(rows):
        for j in range(cols):
            temp=random.random()
            if temp>1-salt:
                img[i,j]=[random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)]
            if temp<pepper:
                img[i,j]=[random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)]
    return img

if __name__=='__main__':
    sp=saltpepper(vaildnumner())
    cv2.imshow('sp',sp)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

