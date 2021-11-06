import NASA
import cv2
import time
import icgc

t = time.time()
im = NASA.getImage(2.0746306228255373, 41.49239124630928, dim=0.01)
cv2.imwrite('image.png', im)
t1 = time.time()
print('temps NASA:' + str(t1-t))

#####################################################################
x0 = 290368.84
x1 = 4538236.42
y1 = 292203.28
y0 = 4540070.86
width = 520
height = 520

t = time.time()
im = icgc.getImage(x0, x1, y1, y0,width,height)
file = open('rebut.png', 'wb')
file.write(im)
file.close()
t1 = time.time()
print('temps IGN:' + str(t1-t))
