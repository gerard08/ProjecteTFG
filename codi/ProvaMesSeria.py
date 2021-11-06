import icgc
xy0 = (40.76, 0.58)
xy1 = (40.96, 0.78)

(xy0,xy1) = icgc.calculateCoord(xy0, xy1)


im = icgc.getImage(xy0[0], xy0[1], xy1[0], xy1[1], 2080, 1080)
file = open('rebut.png', 'wb')
file.write(im)
file.close()