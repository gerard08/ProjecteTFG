from tractament import getImages
from multiprocessing import Pool
from cv2 import imwrite
PATH = '3d/img/'

STEP = 0.2
th = 0.001

def getxy1(xy):
    return (round(xy[0]+STEP,5),round(xy[1]+STEP,5))



x0 = 41.16915
y0 = 1.053150
#i = [x for x in range(9)]
if __name__ == '__main__':
    nrowcols = 5
    nimages = 0
    x = x0
    y = y0
    for i in range(nrowcols):
        for j in range(nrowcols):
            xy0 = (round(x,5),round(y,5))
            xy1 = getxy1(xy0)
            im = getImages(xy0,xy1)
            # imwrite(PATH + str(nimages) + '_sat.jpg', im)
            print(xy0,xy1)
            print(nimages)
            y+=STEP+th
            nimages+=1
        y = y0
        x+=STEP+th

    print("DONE!!")