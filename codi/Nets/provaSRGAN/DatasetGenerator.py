PATH = 'C:/Users/ger-m/Desktop/UNI/4t/TFG/minidataset/sd/'
LISTFILE = 'C:/Users/ger-m/Desktop/UNI/4t/TFG/minidataset/listfile.txt'

import numpy as np
# from numpy.core.defchararray import index
from torch.utils import data
import cv2

class MyDataset(data.Dataset):
    def __init__(self, lst):
        self.img_lst = lst

    def __getitem__(self, index):
        
        x = cv2.imread(PATH + self.img_lst[index])
        x = np.transpose(x,(2,0,1))

        return x

    def __len__(self):
        return len(self.img_lst)


def createDatasets(type, batch):
    f = open(LISTFILE, 'r')
    images = f.read()
    images = images.split("\n")
    f.close()

    generator = None

    if type == 'train':
        train = images[:int(len(images)*0.7)]
        training_set = MyDataset(train)
        generator = data.DataLoader(training_set, batch_size=batch, shuffle=True)

    elif type == 'validate':
        test = images[int(len(images)*0.7):int(len(images)*0.8)]
        validation_set = MyDataset(test)
        generator = data.DataLoader(validation_set, batch_size=batch, shuffle=True)

    if generator is None:
        raise Exception('Especifica un tipus de dataset: (train/validate)')

    return generator
