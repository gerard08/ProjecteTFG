from os import listdir
import re
from multiprocessing import Pool
import cv2
from embrutaImatges import embruta
from cleanDataset import cleanDataset

PATH_HD = 'C:/Users/ger-m/Desktop/UNI/4t/TFG/dataset/dataset/hd/'
DEST_HD = 'C:/Users/ger-m/Desktop/UNI/4t/TFG/minidataset480/hd/'

PATH_SD = 'C:/Users/ger-m/Desktop/UNI/4t/TFG/dataset/dataset/sd/'
DEST_SD = 'C:/Users/ger-m/Desktop/UNI/4t/TFG/minidataset480/sd/'
W = H = 120

def miniImageHD(imr):
    i = cv2.imread(PATH_HD + imr)
    i= cv2.resize(i, (H, W))
    name = re.split('.png', imr)[0]
    cv2.imwrite(DEST_HD + name + '.jpg', i)
    del i

def miniImageSD(imr):
    i = cv2.imread(DEST_HD + imr)
    #i= cv2.resize(i, (H, W))
    i = embruta(i)
    #name = re.split('.png', imr)[0]
    cv2.imwrite(DEST_SD + imr , i)
    del i

if __name__ == '__main__':
    imhd = listdir(PATH_HD)
    imsd = listdir(DEST_HD)

    # print('fent HD...')
    # p = Pool(processes=None)
    # [p.apply(miniImageHD, args=(im, )) for im in imhd]
    print('fent SD...')
    pool = Pool(processes=None)
    [pool.apply(miniImageSD, args=(im, )) for im in imsd]

    # print('netejant HD...')
    # cleanDataset(DEST_HD)
    # print('netejant SD...')
    # cleanDataset(DEST_SD)
    # print('tot ok, apagant pc...')
    # import os
    # os.system('shutdown -s')


    