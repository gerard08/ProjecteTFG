PATH = 'C:/Users/ger-m/Desktop/UNI/4t/TFG/minidatasetD'

import icgc
import cv2
import numpy as np

x0 = 41.34
y0 = 0.52

step = 0.01

x1 = x0 + step
y1 = y0 + step

xy0 = (x0,y0)
xy1 = (x1,y1)

(xy0,xy1) = icgc.calculateCoord(xy0, xy1)

im = icgc.getImage(xy0[0], xy0[1], xy1[0], xy1[1], 572, 572, 'relleu')
im2 = icgc.getImageHD(xy0[0], xy0[1], xy1[0], xy1[1], 572, 572)

n=0

file = open(PATH + '/relleu/'+ str(n) +'.jpg', 'wb')
file.write(im)
file.close()

file = open(PATH + '/sat/'+ str(n) +'.jpg', 'wb')
file.write(im2)
file.close()
# imatge = cv2.imread(PATH + '/relleu/'+ str(n) +'.jpg')

# nparr = np.frombuffer(im, dtype=np.float64)
# img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
# cv2.imshow('result', img)

# nparr = np.frombuffer(im2, np.uint8)
# img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
# cv2.imshow('result_sd', img)
# cv2.waitKey(0)