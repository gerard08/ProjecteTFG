import icgc

AX = 90
AY = 200

def getImages(xy0, xy1, n):
    (xy0,xy1) = icgc.calculateCoord(xy0, xy1)
    im = icgc.getImageHD(xy0[0] + AX, xy0[1] + AY, xy1[0] + AX, xy1[1] + AY, 572, 572)
    imr = icgc.getImage(xy0[0], xy0[1], xy1[0], xy1[1], 572, 572)
    file = open('dataset/hd/'+ str(n) +'.png', 'wb')
    file.write(im)
    file.close()
    file = open('dataset/sd/'+ str(n) +'.png', 'wb')
    file.write(imr)
    file.close()
    return 'OK'

if __name__ == '__main__':
    x0 = 42.38
    y0 = 0.77

    step = 0.01

    x1 = x0 + step
    y1 = y0 + step

    xy0 = (x0,y0)
    xy1 = (x1,y1)
    import math
    nImages = 10000

    nij = int(math.sqrt(nImages))
    for i in range(nij):

        for j in range(nij):
            if y0 > 2.816359:
                break
            xy0 = (x0,y0)
            xy1 = (x1,y1)

            getImages(xy0, xy1, j+(10*i))
            print("Imatge " + str(j+(10*i)) + "/" + str(nImages) + ": OK")

            b = y1 + step
            y0 = y1
            y1 = b

        a = x1 + step
        x0 = x1
        x1 = a
