import os
import cv2
from multiprocessing import Pool
from numpy import ndarray

PATH = "C:/Users/ger-m/Desktop/UNI/4t/TFG/dataset/hd"

def comprobaNegres(img):
    totalNegres = 0
    i = cv2.imread(PATH + '/' + img)

    #comprobem que l'arxiu no sigui un error
    if type(i) != ndarray:
        os.remove(PATH + '/' + img)
        print('foto ' + img + ' eliminada')
        return

    #comprovem el numero de pixels negres que te la imatge
    for x in range(len(i)):
        for y in range(len(i)):
            if list(i[x][y]) == [0, 0, 0]:
                totalNegres += 1

    #si es superior del 25%, suprimim la imatge
    if (totalNegres / pow(len(i), 2) > 0.25):
        os.remove(PATH + '/' + img)
        print('foto ' + img + ' eliminada')


if __name__ == '__main__':
    os.chdir(PATH)
    #fem una llista d'imatges
    images = os.listdir()

    #executem la funció de forma paral·lela
    p = Pool(processes = 4)
    [p.apply(comprobaNegres, args=(im,)) for im in images]
    print("Dataset net :)")


