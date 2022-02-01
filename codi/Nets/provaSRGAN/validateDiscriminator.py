EPOCH = 1

from torch import optim
from discriminator import Operations
import torch.nn as nn
from DatasetDiscriminator import createDatasets
import torch
from tensorboardX import SummaryWriter
import torchvision.utils as vutils
import numpy as np

def validation(epoch, dataloader, model, criterion, dev, writer):
    model.eval()
    total_losses = None
    lensamples = len(dataloader)
    for i_batch, sample_batched in enumerate(dataloader):
        images = sample_batched['img'].to(device=dev, dtype=torch.float)
        ground = sample_batched['gth'].to(device=dev, dtype=torch.float)
        n_iter = epoch*lensamples + i_batch
        
        try:
            output = torch.squeeze(model(images))
        except:
            output = ground
            print('ERROR!!')


        # if n_iter%100==0:
        #     xi = vutils.make_grid(images, normalize=True, scale_each=True)
        #     xl = vutils.make_grid(ground, normalize=True, scale_each=True)
        #     xo = vutils.make_grid(output, normalize=True, scale_each=True)
        #     x = torch.cat((xi,xl,xo),1)
        #     writer.add_image('validation/output' + str(n_iter), x, n_iter)
            
        loss = criterion(output, ground)
        mean_loss = np.mean(np.array(loss))

        writer.add_scalar('validation/accuracy', mean_loss, n_iter)

        print('Validation -> sample/numSamples/epoch: {0}/{1}/{2}, Accuracy: {3}%' \
              .format(i_batch, lensamples, epoch, mean_loss))



        if total_losses is None:
            total_losses = np.array(loss)
        else:
            total_losses = np.concatenate((total_losses, np.array(loss)))

        del images
        del ground
        del n_iter
        del output
    mean_loss = np.mean(np.array(total_losses))
    print('Mean Accuracy: {}'.format(mean_loss))


def criterion(x,y):
    nx = x.cpu().detach().numpy()
    ny = y.cpu().detach().numpy()
    r = []
    for i, el in enumerate(nx):
        r.append((1 - abs(ny[i] - el))*100)
    return r

if __name__ == '__main__':
    writer = SummaryWriter('C:/Users/ger-m/Desktop/UNI/4t/TFG/codi/Nets/provaSRGAN/runs/GANDiscriminatorValidator')

    uo = Operations()
    dev = uo.getDevice()
    net = uo.loadNet('C:/Users/ger-m/Desktop/UNI/4t/TFG/codi/Nets/provaSRGAN/models/modelGANDISC.pth')
    net.to(dev)

    validation_generator = createDatasets('validate', batch=1)

    for epoch in range(EPOCH):
        validation(epoch, validation_generator, net, criterion, dev, writer)

    