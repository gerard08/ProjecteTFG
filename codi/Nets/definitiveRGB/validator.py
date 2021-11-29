EPOCH = 1

import torch
from UNet import UNetOperations
import Dataset
from tensorboardX import SummaryWriter
import numpy as np
import torchvision.utils as vutils
import cv2
from skimage.metrics import structural_similarity as ssim



def similarity(im1, im2):
    r = []
    i1 = im1.cpu().detach().numpy()
    i2 = im2.cpu().detach().numpy()
    for i in range(i1.shape[0]):
        img1 = np.transpose(i1[i],(1,2,0))
        img2 = np.transpose(i2[i],(1,2,0))
        r.append(ssim(img1, img2, multichannel=True))
    return r
    # r = []
    # for i in range(3):
    #     res = cv2.absdiff(i1[0][i], i2[0][i])
    #     res = res.astype(np.uint8)
    #     percentage = (np.count_nonzero(res) * 100)/ res.size
    #     r.append(100 - percentage)
    # return np.mean(np.array(r))

def validation(epoch, dataloader, model, criterion, dev, writer):
    model.eval()
    total_losses = None
    lensamples = len(dataloader)
    for i_batch, sample_batched in enumerate(dataloader):
        images = sample_batched['img'].to(device=dev, dtype=torch.float)
        ground = sample_batched['gth'].to(device=dev, dtype=torch.float)
        n_iter = epoch*lensamples + i_batch
        
        output = model(images)

        if n_iter%100==0:
            xi = vutils.make_grid(images, normalize=True, scale_each=True)
            xl = vutils.make_grid(ground, normalize=True, scale_each=True)
            xo = vutils.make_grid(output, normalize=True, scale_each=True)
            x = torch.cat((xi,xl,xo),1)
            writer.add_image('validation/output' + str(n_iter), x, n_iter)
            
        loss = criterion(output, ground)

        writer.add_scalar('validation/similarity', np.mean(np.array(loss)), n_iter)

        print('Validation -> sample/numSamples/epoch: {0}/{1}/{2}, Similarity: {3}%' \
              .format(i_batch, lensamples, epoch, np.mean(np.array(loss))))

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

if __name__ == '__main__':
    writer = SummaryWriter('C:/Users/ger-m/Desktop/UNI/4t/TFG/codi/Nets/definitiveRGB/runs/exp-KAGGLE')

    uo = UNetOperations()
    dev = uo.getDevice()
    unet = uo.loadUnet('C:/Users/ger-m/Desktop/UNI/4t/TFG/codi/Nets/definitiveRGB/down/model_weights.pth')
    unet.to(dev)

    validation_generator = Dataset.createDatasets('validate', batch=5)

    for epoch in range(EPOCH):
        validation(epoch, validation_generator, unet, similarity, dev, writer)

    