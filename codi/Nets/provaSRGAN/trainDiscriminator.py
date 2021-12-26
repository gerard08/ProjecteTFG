EPOCH = 5

from torch import optim
from discriminator import Operations
import torch.nn as nn
from DatasetDiscriminator import createDatasets
import torch
from tensorboardX import SummaryWriter
import torchvision.utils as vutils
import numpy as np
import cv2

# def accuracy(im1, im2):
#     i1 = im1.cpu().detach().numpy()
#     i2 = im2.cpu().detach().numpy()
#     r = []
#     for i in range(3):
#         res = cv2.absdiff(i1[0][i], i2[0][i])
#         res = res.astype(np.uint8)
        
#         percentage = (np.count_nonzero(res) * 100)/ res.size
#         r.append(100 - percentage)
#     return np.mean(np.array(r))


def train(epoch, dataloader, model, criterion, optimizer, dev, writer):
    model.train()

    lensamples = len(dataloader)

    for i_batch, sample_batched in enumerate(dataloader):

        images_ = sample_batched['img'].to(device = dev, dtype=torch.float)

        ground_ = sample_batched['gth'].to(device = dev, dtype=torch.float)
        n_iter = epoch*lensamples + i_batch

        output_ = model(images_)
        if n_iter%100==0:
            xi = vutils.make_grid(images_, normalize=True, scale_each=True)
            writer.add_image('train/output'+ str('pred:' + str(output_) + ' gth:' + str(ground_)), xi, n_iter)
            print('imatge guardada')

        loss = criterion(output_, ground_)
        #acc = criterion2(output_, ground_)

        del images_, ground_, output_
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        writer.add_scalar('train/loss', loss.item(), n_iter)
        #writer.add_scalar('train/acc', acc, n_iter)

        
        print('Train -> sample/numSamples/epoch: {0}/{1}/{2}, Loss: {3}' \
              .format(i_batch, lensamples, epoch, loss.item()))


if __name__ == '__main__':
    writer = SummaryWriter('C:/Users/ger-m/Desktop/UNI/4t/TFG/codi/Nets/provaSRGAN/runs/GANDiscriminator')

    op = Operations()
    net= op.createNet(batches=3)
    dev = op.getDevice()
    net.to(dev)

    criterion = nn.MSELoss()
    #optimizer = optim.Adam(net.parameters(), lr=1e-4, weight_decay=1e-4)
    optimizer = optim.SGD(net.parameters(), lr=0.0001)
    training_generator = createDatasets('train', batch=3)    
    
    for epoch in range(EPOCH):
        train(epoch, training_generator, net, criterion, optimizer, dev, writer)   

    op.saveUnet('C:/Users/ger-m/Desktop/UNI/4t/TFG/GANDisc/model.pth')       