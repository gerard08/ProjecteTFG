EPOCH = 5

from torch import optim
from discriminator import Operations
import torch.nn as nn
from DatasetDiscriminator import createDatasets
import torch
from tensorboardX import SummaryWriter
import torchvision.utils as vutils

def train(epoch, dataloader, model, criterion, optimizer, dev, writer):
    model.train()

    lensamples = len(dataloader)

    for i_batch, sample_batched in enumerate(dataloader):

        images_ = sample_batched['img'].to(device = dev, dtype=torch.float)

        ground_ = sample_batched['gth'].to(device = dev, dtype=torch.float)
        n_iter = epoch*lensamples + i_batch

        output_ = torch.squeeze(model(images_))
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
    writer = SummaryWriter('C:/Users/ger-m/Desktop/UNI/4t/TFG/codi/Nets/provaSRGAN/runs/GANDiscriminator480')

    batches = 3


    op = Operations()
    net= op.createNet(batches=batches)
    dev = op.getDevice()
    net.to(dev)


    criterion = nn.MSELoss()
    #optimizer = optim.Adam(net.parameters(), lr=1e-4, weight_decay=1e-4)
    optimizer = optim.SGD(net.parameters(), lr=0.0001)
    training_generator = createDatasets('train', batch=batches)    
    
    for epoch in range(EPOCH):
        train(epoch, training_generator, net, criterion, optimizer, dev, writer)   

    op.saveNet('modelGANDISC480.pth')       


def entrena():
    writer = SummaryWriter('C:/Users/ger-m/Desktop/UNI/4t/TFG/codi/Nets/provaSRGAN/runs/GANDiscriminator480')

    batches = 1


    op = Operations()
    net= op.createNet(batches=batches)
    dev = op.getDevice()
    net.to(dev)


    criterion = nn.MSELoss()
    #optimizer = optim.Adam(net.parameters(), lr=1e-4, weight_decay=1e-4)
    optimizer = optim.SGD(net.parameters(), lr=0.0001)
    training_generator = createDatasets('train', batch=batches)    
    
    for epoch in range(EPOCH):
        train(epoch, training_generator, net, criterion, optimizer, dev, writer)   

    op.saveNet('modelGANDISC480.pth')       
    print('guardat!!')