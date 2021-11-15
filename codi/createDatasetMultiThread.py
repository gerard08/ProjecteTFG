import icgc
from multiprocessing import Pool

def getImages(xy0, xy1, n):
    #convertim les coordenades al format desitjat
    (xy0,xy1) = icgc.calculateCoord(xy0, xy1)

    #obtenim la imatge del servidor
    try:
        im = icgc.getImageHD(xy0[0], xy0[1], xy1[0], xy1[1], 572, 572)
    except:
        print("ERROR getImage")
    
    #la guardem
    try:
        file = open('../dataset/hd/'+ str(n) +'.png', 'wb')
        file.write(im)
        file.close()
    except:
        print("ERROR operacions amb fitxers")

    print("Imatge numero " + str(n))

if __name__ == '__main__':
    #coordenades inicials
    x0 = 42.48
    y0 = 0.80

    #y inicial per poder fer el salt enrera
    y00 = 0.87

    #tamany de la imatge
    step = 0.003

    #calculem les x i y del final de la imatge
    x1 = x0 + step
    y1 = y0 + step

    #llista on emmagatzarem les coordenades
    coordenates = []
    num = 0
    #mentres no ens sortim del marge
    while x1 > 41.0:
        while y1 < 2.9:

            #agrupem les coordenades
            xy0 = (x0,y0)
            xy1 = (x1,y1)
            #les afegim a la llista
            c = {'xy0': xy0, 'xy1':xy1, 'n':num}
            coordenates.append(c)
            num += 1

            #incrementem el valor de y
            b = y1 + step
            y0 = y1
            y1 = b

        #incrementem el valor de x
        a = x1 - step
        x0 = x1
        x1 = a
        y0 = y00
        y1 = y0 + step

        #print(len(coordenates))

    #creem un pool per fer multiprocessing
    pool = Pool(processes=None)
    #els hi passem la funció juntament amb els paràmetres
    [pool.apply(getImages, args=(coordenates[x]['xy0'], coordenates[x]['xy1'], coordenates[x]['n'],)) for x in range(len(coordenates))]
    print("ACABAT")

