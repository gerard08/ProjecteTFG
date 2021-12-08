from UNet import UNetOperations
import cv2
import torch
import numpy as np
from scipy.ndimage import median_filter
import time
import icgc

class Imatge:

    def __init__(self, img):
        if type(img) == str:
            self.img = cv2.imread(img)
        else:
            self.img = img

    def toTensor(self):
        i = np.transpose(self.img,(2,0,1))
        t = torch.tensor(i, dtype=torch.float)
        t = t[None, :]
        return t

    def fromTensor(self):
        i = self.img.detach().numpy()[0]
        r = np.transpose(i,(1,2,0))
        r = median_filter(r, size=3)
        return r/255.0
        
    

if __name__ == '__main__':
    t0 = time.time()
    uo = UNetOperations()
    unet = uo.loadUnet('C:/Users/ger-m/Desktop/UNI/4t/TFG/codi/Nets/definitiveRGB/down/model_weights.pth')

    t0p5 = time.time()
    x0 = 41.34
    y0 = 0.52

    step = 0.01

    x1 = x0 + step
    y1 = y0 + step

    xy0 = (x0,y0)
    xy1 = (x1,y1)
    (xy0,xy1) = icgc.calculateCoord(xy0, xy1)
    im = icgc.getImage(xy0[0], xy0[1], xy1[0], xy1[1], 240, 240)

    nparr = np.fromstring(im, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    img = Imatge(img)
    #img = Imatge('C:/Users/ger-m/Desktop/UNI/4t/TFG/minidataset/sd/5124.jpg')

    out = unet(img.toTensor())

    result = Imatge(out).fromTensor()
    t1 = time.time()
    print(t1-t0p5)
    cv2.imshow('original', img.img)
    cv2.imshow('result', result)
    cv2.waitKey(0)