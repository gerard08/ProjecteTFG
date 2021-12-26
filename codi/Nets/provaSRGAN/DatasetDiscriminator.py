PATH = 'C:/Users/ger-m/Desktop/UNI/4t/TFG/minidataset/'
LISTFILE = 'C:/Users/ger-m/Desktop/UNI/4t/TFG/minidataset/listfile.txt'

import numpy as np
# from numpy.core.defchararray import index
from torch.utils import data
import cv2

def createDict(lst):
    l0 = ['sd/' + x for x in lst]
    l1 = ['hd/' + x for x in lst]

    final = {}
    for i in range(len(l0)):
        final[l0[i]] = 0
        final[l1[i]] = 1

    return final

class MyDataset(data.Dataset):
    def __init__(self, lst, path):
        self.path = path
        self.dict = createDict(lst)
        self.keys = list(self.dict)

    def __getitem__(self, index):
        
        x = cv2.imread(self.path + self.keys[index])
        y = self.dict[self.keys[index]]

        x = np.transpose(x,(2,0,1))

        return {'img':x, 'gth':y}

    def __len__(self):
        return len(self.keys)


def createDatasets(type, batch):
    f = open(LISTFILE, 'r')
    images = f.read()
    images = images.split("\n")
    f.close()

    generator = None

    if type == 'train':
        train = images[:int(len(images)*0.7)]
        training_set = MyDataset(train, PATH)
        generator = data.DataLoader(training_set, batch_size=batch, shuffle=True)

    elif type == 'validate':
        test = images[int(len(images)*0.7):]
        validation_set = MyDataset(test, PATH)
        generator = data.DataLoader(validation_set, batch_size=batch, shuffle=True)

    if generator is None:
        raise Exception('Especifica un tipus de dataset: (train/validate)')

    return generator
