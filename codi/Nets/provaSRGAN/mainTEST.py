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
    gen = op.createNet()
    #dev = op.getDevice()
    #gen.to(dev)

    im = cv2.imread('C:/Users/ger-m/Desktop/UNI/4t/TFG/minidataset/sd/0.jpg')

    it = toTensor(im)#.to(device = dev, dtype=torch.float)

    out = gen(it)

    out = fromTensor(out)

    cv2.imshow('result', out)
    #print(out)
    cv2.waitKey(0)