EPOCH = 5

from torch import optim
from generator import Operations as genOperations
from discriminator import Operations as discOperations
import torch.nn as nn
from DatasetGenerator import createDatasets
import torch
from tensorboardX import SummaryWriter
import torchvision.utils as vutils
import torch.nn.functional as F


def train(epoch, dataloader, genmodel, discmodel, criterion, optimizer, dev, writer):
    genmodel.train()

    lensamples = len(dataloader)

    for i_batch, sample_batched in enumerate(dataloader):

        images = sample_batched.to(device = dev, dtype=torch.float)

        #ground_ = sample_batched['gth'].to(device = dev, dtype=torch.float)
        n_iter = epoch*lensamples + i_batch

        #output = genmodel(images)
        #prediction = discmodel(output)

        if n_iter%100==0:
            auxim = F.interpolate(images, size=(960, images.shape[2]))
            xi = vutils.make_grid(images, normalize=True, scale_each=True)
            #xg = vutils.make_grid(ground,  normalize=True, scale_each=True)
            xo = vutils.make_grid(output, normalize=True, scale_each=True)
            x = torch.cat((xi,xo),1)
            writer.add_image('train/output'+ str(n_iter), x, n_iter)

        ground = torch.ones(1, 3).to(device = dev, dtype=torch.float)
        loss = criterion(prediction, ground)
        #acc = criterion2(output_, ground_)

        del images, ground, output
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        writer.add_scalar('train/loss', loss.item(), n_iter)
        #writer.add_scalar('train/acc', acc, n_iter)

        
        print('Train -> sample/numSamples/epoch: {0}/{1}/{2}, Loss: {3}' \
              .format(i_batch, lensamples, epoch, loss.item()))


if __name__ == '__main__':
    writer = SummaryWriter('C:/Users/ger-m/Desktop/UNI/4t/TFG/codi/Nets/provaSRGAN/runs/GANGenerator')

    batches = 1

    genop = genOperations()
    gennet= genop.createNet()
    dev = genop.getDevice()
    gennet.to(dev)

    discop = discOperations()
    discnet = discop.loadNet('modelGANDISC.pth')
    dev = discop.getDevice()
    discnet.to(dev)

    criterion = nn.MSELoss()
    optimizer = optim.Adam(gennet.parameters(), lr=1e-4, weight_decay=1e-4)
    #optimizer = optim.SGD(net.parameters(), lr=0.0001)
    training_generator = createDatasets('train', batch=batches)    
    
    for epoch in range(EPOCH):
        train(epoch, training_generator, gennet, discnet, criterion, optimizer, dev, writer)   

    genop.saveNet('modelGANGEN.pth')       