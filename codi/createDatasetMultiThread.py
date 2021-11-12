import icgc
from multiprocessing import Pool
from math import sqrt
AX = 90
AY = 200
nImages = 200000

def getImages(xy0, xy1, n):
    (xy0,xy1) = icgc.calculateCoord(xy0, xy1)
    try:
        im = icgc.getImageHD(xy0[0], xy0[1], xy1[0], xy1[1], 572, 572)
    except:
        print("ERROR getImage")
    
    try:
        file = open('../dataset/hd/'+ str(n) +'.png', 'wb')
        file.write(im)
        file.close()
    except:
        print("ERROR operacions amb fitxers")
    print("Imatge numero " + str(n))

if __name__ == '__main__':
    x0 = 42.48
    y00 = 0.87
    y0 = 0.80

    step = 0.003

    x1 = x0 + step
    y1 = y0 + step

    xy0 = (x0,y0)
    xy1 = (x1,y1)

    coordenates = []
    num = 0
    while x1 > 41.0:

        while y1 < 2.9:

            xy0 = (x0,y0)
            xy1 = (x1,y1)
            c = {'xy0': xy0, 'xy1':xy1, 'n':num}
            coordenates.append(c)
            num += 1

            b = y1 + step
            y0 = y1
            y1 = b

        a = x1 - step
        x0 = x1
        x1 = a
        y0 = y00
        y1 = y0 + step
        print(len(coordenates))

    pool = Pool(processes=None)
    [pool.apply(getImages, args=(coordenates[x]['xy0'], coordenates[x]['xy1'], coordenates[x]['n'],)) for x in range(len(coordenates))]
    print("ACABAT")

