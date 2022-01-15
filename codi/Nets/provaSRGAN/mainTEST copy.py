from generator import Operations
import cv2
import torch
import numpy as np


def toTensor(img):
        i = np.transpose(img,(2,0,1))
        t = torch.tensor(i, dtype=torch.float)
        t = t[None, :]
        return t

def fromTensor(self):
    i = self.detach().numpy()[0]
    r = np.transpose(i,(1,2,0))
    #r = median_filter(r, size=3)
    return r

if __name__ == '__main__':
    op = Operations()
    #gen = op.createNet()
    gen = op.loadNet('C:/Users/ger-m/Desktop/UNI/4t/TFG/codi/Nets/provaSRGAN/models/generator_1.pth')
    #dev = op.getDevice()
    #gen.to(dev)

    im = cv2.imread('C:/Users/ger-m/Desktop/UNI/4t/TFG/minidataset/hd/25.jpg')
    #im = cv2.normalize(im, None, alpha=1, beta=-1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

    it = toTensor(im)#.to(device = dev, dtype=torch.float)
    cv2.imshow('original',im)
    #cv2.waitKey(0)
    out = gen(it)

    out = fromTensor(out)
    out = cv2.normalize(out, None, 255,0, cv2.NORM_MINMAX, cv2.CV_8UC1)
    
    print(out)
    cv2.imshow('result', out)
    print(out)
    cv2.waitKey(0)