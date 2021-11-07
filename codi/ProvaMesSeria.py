import icgc
xy0 = (40.77, 0.37)
xy1 = (40.78, 0.38)

(xy0,xy1) = icgc.calculateCoord(xy0, xy1)


im = icgc.getImage(xy0[0], xy0[1], xy1[0], xy1[1], 572, 572)
imr = icgc.getImage(xy0[0], xy0[1], xy1[0], xy1[1], 572, 572, 'relleu')
file = open('rebut.png', 'wb')
file.write(im)
file.close()
file = open('relleu.png', 'wb')
file.write(imr)
file.close()