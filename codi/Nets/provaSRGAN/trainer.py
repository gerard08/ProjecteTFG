EPOCH = 5

from torch import optim
from UNet import UNetOperations
import torch.nn as nn
import Dataset
import torch
from tensorboardX import SummaryWriter
import torchvision.utils as vutils
import numpy as np
import cv2

def accuracy(im1, im2):
    i1 = im1.cpu().detach().numpy()
    i2 = im2.cpu().detach().numpy()
    r = []
    for i in range(3):
        res = cv2.absdiff(i1[0][i], i2[0][i])
        res = res.astype(np.uint8)
        
        percentage = (np.count_nonzero(res) * 100)/ res.size
        r.append(100 - percentage)
    return np.mean(np.array(r))


def train(epoch, dataloader, model, criterion, criterion2, optimizer, dev, writer):
    model.train()

    lensamples = len(dataloader)

    for i_batch, sample_batched in enumerate(dataloader):

        images_ = sample_batched['img'].to(device = dev, dtype=torch.float)

        ground_ = sample_batched['gth'].to(device = dev, dtype=torch.float)
        n_iter = epoch*lensamples + i_batch

        output_ = model(images_)
        if n_iter%100==0:
            xi = vutils.make_grid(images_, normalize=True, scale_each=True)
            xg = vutils.make_grid(ground_,  normalize=True, scale_each=True)
            xo = vutils.make_grid(output_, normalize=True, scale_each=True)
            x = torch.cat((xi,xg,xo),1)
            writer.add_image('train/output'+ str(n_iter), x, n_iter)
            print('imatge guardada')

        loss = criterion(output_, ground_)
        acc = criterion2(output_, ground_)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        writer.add_scalar('train/loss', loss.item(), n_iter)
        writer.add_scalar('train/acc', acc, n_iter)

        
        print('Train -> sample/numSamples/epoch: {0}/{1}/{2}, Loss: {3}, Accuracy: {4}' \
              .format(i_batch, lensamples, epoch, loss.item(), acc))


if __name__ == '__main__':
    writer = SummaryWriter('C:/Users/ger-m/Desktop/UNI/4t/TFG/codi/Nets/definitiveRGB/runs/exp-2Train_0.15')

    op = UNetOperations()
    unet= op.createUNet(n_classes=3)
    dev = op.getDevice()
    unet.to(dev)

    criterion = nn.MSELoss()
    optimizer = optim.Adam(unet.parameters(), lr=1e-4, weight_decay=1e-4)
    training_generator = Dataset.createDatasets('train', batch=3)    
    
    for epoch in range(EPOCH):
        train(epoch, training_generator, unet, criterion, accuracy, optimizer, dev, writer)   

    op.saveUnet('model.pth')       