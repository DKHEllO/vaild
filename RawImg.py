import numpy as np
import cv2
import random

def vaildnumner(imgsize=40,fsize=1,font=cv2.FONT_HERSHEY_SIMPLEX):
    num=random.choice("01234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
    img=np.ones([imgsize,imgsize,3],np.uint8)
    img[:,:,:]=img*255
    cv2.putText(img,num,(imgsize/5,3*imgsize/4),font,fsize,(random.randrange(0,180),random.randrange(0,180),random.randrange(0,180)),3)
    return img,num

if __name__ =='__main__':
    img,num=vaildnumner()
    print num
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()





