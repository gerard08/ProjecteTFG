import icgc

x0 = 41.34
y0 = 0.52

step = 0.01

x1 = x0 + step
y1 = y0 + step

xy0 = (x0,y0)
xy1 = (x1,y1)

(xy0,xy1) = icgc.calculateCoord(xy0, xy1)


im = icgc.getImage(xy0[0], xy0[1], xy1[0], xy1[1], 572, 572)
imr = icgc.getImageHD(xy0[0] + 90, xy0[1] + 200, xy1[0] + 90, xy1[1] + 200, 572, 572, 'relleu')
file = open('rebut.png', 'wb')
file.write(im)
file.close()
file = open('relleu.png', 'wb')
file.write(imr)
file.close()