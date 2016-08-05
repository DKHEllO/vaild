#coding=utf8
"""
Created on Sat Jul 17:44 2016
"""
import cv2
import random
from RawImg import vaildnumner
def notline(img):   #在图相中画曲线
    n=0
    i=1
    while  n<1:
        x,y=random.randrange(0,40),random.randrange(0,40)
        rx=x
        ry=y
        while y<random.randrange(100,144):
            if i==1:
                x=x-random.randrange(0,2)
                y=y+random.randrange(0,2)
            if i==-1:
                x=x+random.randrange(0,2)
                y=y+random.randrange(0,2)
            cv2.line(img, (y, x), (ry, rx), (random.randrange(100,120),random.randrange(100,120),random.randrange(100,120)),2)
            rx=x
            ry=y
            i=-i
        n=n+1
    return img

if __name__=="__main__":
    img ,num = vaildnumner()
    img = notline(img)
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
