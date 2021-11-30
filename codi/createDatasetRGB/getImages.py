import icgc



def getImages(xy0, xy1, n):
    (xy0,xy1) = icgc.calculateCoord(xy0, xy1)
    im = icgc.getImage(xy0[0], xy0[1], xy1[0], xy1[1], 572, 572)
    imr = icgc.getImage(xy0[0], xy0[1], xy1[0], xy1[1], 572, 572, 'relleu')
    file = open('img/satellite/'+ str(n) +'.png', 'wb')
    file.write(im)
    file.close()
    file = open('img/relleu/'+ str(n) +'.png', 'wb')
    file.write(imr)
    file.close()
    return 'OK'

if __name__ == '__main__':
    x0 = 41.34
    y0 = 0.52

    step = 0.01

    x1 = x0 + step
    y1 = y0 + step

    xy0 = (x0,y0)
    xy1 = (x1,y1)
        
    for i in range(10):
        a = x1 + step
        x0 = x1
        x1 = a

        for j in range(10):
            b = y1 + step
            y0 = y1
            y1 = b

            xy0 = (x0,y0)
            xy1 = (x1,y1)

            print(getImages(xy0, xy1, j+(10*i)))
