import os
import cv2
from multiprocessing import Pool
import numpy as np

PATH = "C:/Users/ger-m/Desktop/UNI/4t/TFG/minidataset/sd"

def comprobaNegres(img):
    totalNegres = 0
    i = cv2.imread(PATH + '/' + img)

    #comprobem que l'arxiu no sigui un error
    if type(i) != np.ndarray:
        os.remove(PATH + '/' + img)
        print('foto ' + img + ' eliminada')
        return

    #comprovem el numero de pixels negres que te la imatge
    count = np.count_nonzero(i == [0, 0, 0], axis=1)
    a = []
    for el in count:
        a.append(sum(el))
    totalNegres = sum(a)

    #si es superior del 25%, suprimim la imatge
    if (totalNegres / pow(len(i), 2) > 0.25):
        os.remove(PATH + '/' + img)
        print('foto ' + img + ' eliminada')

    del i, totalNegres


if __name__ == '__main__':
    os.chdir(PATH)
    #fem una llista d'imatges
    images = os.listdir()

    #executem la funció de forma paral·lela
    p = Pool(processes = 4)
    [p.apply(comprobaNegres, args=(im,)) for im in images]
    print("Dataset net :)")

def cleanDataset(path):
    os.chdir(path)
    #fem una llista d'imatges
    images = os.listdir()

    #executem la funció de forma paral·lela
    p = Pool(processes = None)
    [p.apply(comprobaNegres, args=(im,)) for im in images]
    print("Dataset net :)")
