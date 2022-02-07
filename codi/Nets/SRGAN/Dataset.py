PATH_SD = '../input/dataset120/minidataset120/hd/'
PATH_HD = '../input/minidataset480/minidataset480/hd/'
LISTFILE = '../input/minidataset480/minidataset480/listfile.txt'

import numpy as np
from torch.utils import data
import cv2


class MyDataset(data.Dataset):
    def __init__(self, lst):
        self.lst = lst

    def __getitem__(self, index):
        
        img = self.lst[index]
        
        x = cv2.imread(PATH_SD + img)
        y = cv2.imread(PATH_HD + img)
        
        x = cv2.normalize(x, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
        y = cv2.normalize(y, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

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
        train = images[:int(len(images)*0.7)]#0.7
        training_set = MyDataset(train)
        generator = data.DataLoader(training_set, batch_size=batch, shuffle=True)

    elif type == 'validate':
        test = images[int(len(images)*0.7):]
        validation_set = MyDataset(test)
        generator = data.DataLoader(validation_set, batch_size=batch, shuffle=True)

    if generator is None:
        raise Exception('Especifica un tipus de dataset: (train/validate)')

    return generator