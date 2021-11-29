from os import listdir
import re
from multiprocessing import Pool
import cv2

PATH_HD = 'C:/Users/ger-m/Desktop/UNI/4t/TFG/dataset/hd/'
DEST_HD = 'C:/Users/ger-m/Desktop/UNI/4t/TFG/minidataset/hd/'

PATH_SD = 'C:/Users/ger-m/Desktop/UNI/4t/TFG/dataset/sd/'
DEST_SD = 'C:/Users/ger-m/Desktop/UNI/4t/TFG/minidataset/sd/'
W = H = 240

def miniImageHD(imr):
    i = cv2.imread(PATH_HD + imr)
    i= cv2.resize(i, (H, W))
    name = re.split('.png', imr)[0]
    cv2.imwrite(DEST_HD + name + '.jpg', i)
    del i

def miniImageSD(imr):
    i = cv2.imread(PATH_SD + imr)
    i= cv2.resize(i, (H, W))
    cv2.imwrite(DEST_SD + imr, i)
    del i

if __name__ == '__main__':
    imhd = listdir(PATH_HD)
    imsd = listdir(PATH_SD)

    print('fent HD')
    p = Pool(processes=None)
    [p.apply(miniImageHD, args=(im, )) for im in imhd]
    print('fent SD')
    pool = Pool(processes=None)
    [pool.apply(miniImageSD, args=(im, )) for im in imsd]

    print('tot ok')


    