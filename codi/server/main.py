from tractament import getImages
from multiprocessing import Pool
PATH = '3d/img/'

xy0 = [(41.169, 1.053), (41.169, 1.553), (41.169, 2.053),
(41.569, 1.053), (41.569, 1.553), (41.569, 2.053),
(42.069, 1.053), (42.069, 1.553), (42.069, 2.053)]

xy1 = [(41.569, 1.553), (41.569, 2.053), (41.569, 2.553),
(42.069, 1.553), (42.069, 2.053), (42.069, 2.553),
(42.569, 1.553), (42.569, 2.053), (42.569, 2.553)]
#i = [x for x in range(9)]
if __name__ == '__main__':
    p = Pool()
    [p.apply(getImages, args=(xy0[i], xy1[i], i,)) for i in range(len(xy0))]
    getImages(xy0[0], xy1[0], 0)
    print("DONE!!")