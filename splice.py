#coding=utf8
"""
Created on Mon Jul 10:39 2016
"""
from RawImg import vaildnumner
import cv2
import numpy as np
import random

def splice(img0,img1,img2,img3,img4,imgsize=40,size=3.5):

#img0,img1,img2,img3为要拼接的图片，imgsize为图片的尺寸（imgsize×imgsize）

    i=0
    n=0
    img=[img0,img1,img2,img3,img4]
    imgR = np.ones([imgsize, size*imgsize, 3], np.uint8)
    imgR = imgR * 255

#将图片随机拼接在3.5×imgsize的白底图片上
#该方法为图像混合主要运用了图像位运算的一些内容

    while i < size:
        v1 = img[n]
        if i == 0:
            roi = imgR[0:imgsize, 0:imgsize]
        if i == 1:
            i = random.uniform(0.5, 1)
            roi = imgR[0:imgsize, i * imgsize:imgsize + i * imgsize]
        if 1 < i < 2:
            i = random.uniform(1.5, 2)
            roi = imgR[0:imgsize, i * imgsize:imgsize + i * imgsize]
        if 2 < i < 3:
            i = 2.5
            roi = imgR[0:imgsize, i * imgsize:imgsize + i * imgsize]
        v1gray = cv2.cvtColor(v1, cv2.COLOR_BGR2GRAY)
        #构建掩模
        ret, mask = cv2.threshold(v1gray, 175, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)
        #与运算
        img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
        img2_fg = cv2.bitwise_and(v1, v1, mask=mask_inv)
        dst = cv2.add(img1_bg, img2_fg)
        #与背景混合
        imgR[0:imgsize, i * imgsize:imgsize + i * imgsize] = dst
        i = i+1
        n = n+1
    return imgR

if __name__=='__main__':
    imgsize=40
    fontsize=1
    img0, num0 = vaildnumner(imgsize,fontsize)
    img1, num1 = vaildnumner(imgsize,fontsize)
    img2, num2 = vaildnumner(imgsize,fontsize)
    img3, num3 = vaildnumner(imgsize,fontsize)
    img=splice(img0,img1,img2,img3,imgsize)
    cv2.imshow('img',img)
    cv2.waitKey(0)
