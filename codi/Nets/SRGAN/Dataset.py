PATH = 'C:/Users/ger-m/Desktop/UNI/4t/TFG/minidataset/'
LISTFILE = 'C:/Users/ger-m/Desktop/UNI/4t/TFG/minidataset/listfile.txt'

import numpy as np
from torch.utils import data
import cv2


class MyDataset(data.Dataset):
    def __init__(self, lst, path):
        self.lst = lst
        self.path = path

    def __getitem__(self, index):
        
        imsd = 'sd/' + self.lst[index]
        imhd = 'hd/' + self.lst[index]
        
        x = cv2.imread(self.path + imsd)/255.0
        y = cv2.imread(self.path + imhd)/255.0

        x = np.transpose(x,(2,0,1))
        y = np.transpose(y,(2,0,1))

        #return x, y
        return {'img':x, 'gth':y}

    def __len__(self):
        return len(self.lst)

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