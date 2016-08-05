#coding=utf8
"""
Created on Mon Jul 12:43 2016
"""
from RawImg import vaildnumner
import cv2
import numpy as np
import random

def Rotation(img):  #对图像进行旋转和仿射变换
    #构建旋转矩阵
    M = cv2.getRotationMatrix2D((39, 39), random.randrange(-45, 45), 1)
    imgB = np.ones([80, 80, 3], np.uint8)
    imgB = imgB * 255
    imgB[20:60, 20:60] = img
    imgR = cv2.warpAffine(imgB, M, (80, 80))

    #构建仿射变换矩阵
    pts1 = np.float32([[0, 0], [0, 80], [80, 0]])
    pts2 = np.float32([[0, 0], [0, 63], [80, 23]])
    M = cv2.getAffineTransform(pts1, pts2)
    imgR = cv2.warpAffine(imgR, M, (80, 80))
    imgR = imgR[20:60, 20:60]
    return imgR

if __name__=='__main__':
    img,num=vaildnumner()
    img=Rotation(img)
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()