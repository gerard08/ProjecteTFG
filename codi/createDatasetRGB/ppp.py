from icgc import getImage, calculateCoord


x0 = 42.34
y0 = 1.52

step = 0.05

x1 = x0 + step
y1 = y0 + step

xy0 = (x0,y0)
xy1 = (x1,y1)

xy0, xy1 = calculateCoord(xy0, xy1)

im1 = getImage(xy0[0], xy0[1], xy1[0], xy1[1], 500, 500)
im2 = getImage(xy0[0], xy0[1], xy1[0], xy1[1], 500, 500, 'relleu')

file = open('img.png', 'wb')
file.write(im1)
file.close()

file = open('relleu.png', 'wb')
file.write(im2)
file.close()