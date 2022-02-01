from os import listdir
import re
from multiprocessing import Pool
import cv2

PATH = 'C:/Users/ger-m/Desktop/UNI/4t/TFG/dataset/hd/'
DEST = 'C:/Users/ger-m/Desktop/UNI/4t/TFG/dataset/sd/'
W = H = 120
PERCENT = 0.5

def embruta(im):
    #i = cv2.imread(PATH + im)
    i = cv2.resize(im, (int(W * PERCENT), int(H * PERCENT)))#, interpolation=cv2.INTER_CUBIC)
    i = cv2.resize(i, (W, H))
    #print(im)
    #im = re.split('.png', im)[0] + '.jpg'
    #cv2.imwrite(DEST + im, i)#, [cv2.IMWRITE_PNG_COMPRESSION, 9])
    return i


if __name__ == '__main__':
    l = listdir(PATH)

    #creem un pool per fer multiprocessing
    pool = Pool(processes=None)
    #els hi passem la funció juntament amb els paràmetres
    [pool.apply(embruta, args=(im, )) for im in l]
    print("Imatges brutes amb èxit :)")