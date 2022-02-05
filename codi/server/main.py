from tractament import getImages
from multiprocessing import Pool
from cv2 import imwrite
PATH = '3d/img/'

STEP = 0.10
th = 0.0000000000000#1

def getxy1(xy):
    return (round(xy[0]+STEP,14),round(xy[1]+STEP,14))


#41.79500149991982, 1.7345132483896197
x0, y0 = 41.79500149991982, 1.7345132483896197
#i = [x for x in range(9)]
if __name__ == '__main__':
    l = []
    nrowcols = 5
    nimages = 0
    x = x0
    y = y0
    for i in range(nrowcols):
        for j in range(nrowcols):
            xy0 = (round(x,14),round(y,14))
            xy1 = getxy1(xy0)
            l.append((xy0, xy1))
            im = getImages(xy0,xy1)
            imwrite(PATH + '/sat/' + str(nimages) + '_sat.jpg', im)
            im = getImages(xy0,xy1, True)
            imwrite(PATH + '/rel/' + str(nimages) + '_rel.jpg', im)
            print(xy0,xy1)
            print(nimages)
            y+=STEP-th
            nimages+=1
        y = y0
        x+=STEP-th

    with open('coords', mode='wt', encoding='utf-8') as myfile:
         myfile.write('\n'.join(str(el) for el in l))
    print("DONE!!")