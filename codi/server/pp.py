from icgc import calculaImatge
import cv2
import numpy as np

x0 = 41.16915
y0 = 1.053150
step = 0.2
im = calculaImatge(x0, y0, step)

print(len(im))
file = open('pp120.jfif', 'wb')
file.write(im)
file.close()