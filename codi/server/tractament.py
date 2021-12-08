from UNet import UNetOperations
import cv2
import torch
import numpy as np
from scipy.ndimage import median_filter
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
        i = self.img.cpu().detach().numpy()[0]
        r = np.transpose(i,(1,2,0))
        r = median_filter(r, size=3)
        return r
        
    
def winSuperRes(im, div = 4):

    uo = UNetOperations()
    unet = uo.loadUnet('C:/Users/ger-m/Desktop/UNI/4t/TFG/codi/Nets/definitiveRGB/down/model_weights.pth')

    dev = uo.getDevice()
    unet.to(dev)

    #comprovem que les imatges siguin cuadrades
    assert(im.shape[0] == im.shape[1])

    s = int(len(im)/div)
    imgs = []
    sj = s
    si = s
    for i in range(div):
        for j in range(div):
            im1 = im[si-s:si,sj-s:sj]
            imgs.append(im1)
            sj += s
        si += s
        sj = s

    processed_imgs = []

    for img in imgs:
        i = Imatge(img)
        it = i.toTensor().to(device = dev, dtype=torch.float)
        o = unet(it)
        i = Imatge(o)
        processed_imgs.append(i.fromTensor())
        del o, it, i

    n = 0
    for j in range(div):
        for i in range(div):
            if i == 0:
                im = processed_imgs[n]
            else:
                im = cv2.hconcat([im, processed_imgs[n]])
            n += 1
        if j == 0:
            img = im
        else:
            img = cv2.vconcat([img, im])

    return img


def getImages(xy0, xy1):
    (xy0,xy1) = icgc.calculateCoord(xy0, xy1)
    im = icgc.getImage(xy0[0], xy0[1], xy1[0], xy1[1], 2400, 2400)

    nparr = np.frombuffer(im, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    res = winSuperRes(img, div=10)
    return res
