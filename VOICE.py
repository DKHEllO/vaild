#coding=utf8
"""
Created on Mon Jul 11:27 2016
"""
import cv2
import numpy as np
import random

def voice(img):     #主要为图像添加直线，圆等噪声
    line=0
    circle=0
    while line < 10:
        cv2.line(img, (random.randrange(0, 144), random.randrange(0, 40)),
                 (random.randrange(0, 144), random.randrange(0, 40)),
                 (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)), 1)
        line = line + 1
    while circle < 20:
        cv2.circle(img, (random.randrange(0, 144), random.randrange(0, 40)), 1,
                   (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)), -1)
        circle = circle + 1

    return img