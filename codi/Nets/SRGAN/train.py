TRAINED = 0

import torch
import torch.nn as nn

from discriminator import DiscOps
from generator import GenOps
from dataset import createDatasets
from generator import FeatureExtractor

import argparse

import numpy as np
import torch
import torch.nn as nn
from torch.autograd import Variable
from torchvision.utils import make_grid
from torch import optim
from tensorboardX import SummaryWriter


writer = SummaryWriter('GANTraining')

parser = argparse.ArgumentParser()
parser.add_argument("--epoch", type=int, default=0, help="epoch to start training from")
parser.add_argument("--n_epochs", type=int, default=10, help="number of epochs of training")
parser.add_argument("--dataset_name", type=str, default="Dataset", help="name of the dataset")
parser.add_argument("--batch_size", type=int, default=3, help="size of the batches")
parser.add_argument("--lr", type=float, default=0.0002, help="adam: learning rate")
parser.add_argument("--b1", type=float, default=0.5, help="adam: decay of first order momentum of gradient")
parser.add_argument("--b2", type=float, default=0.999, help="adam: decay of first order momentum of gradient")
parser.add_argument("--decay_epoch", type=int, default=8, help="epoch from which to start lr decay")
parser.add_argument("--n_cpu", type=int, default=-1, help="number of cpu threads to use during batch generation")
parser.add_argument("--hr_height", type=int, default=480, help="high res. image height")
parser.add_argument("--hr_width", type=int, default=480, help="high res. image width")
parser.add_argument("--channels", type=int, default=3, help="number of image channels")
parser.add_argument("--sample_interval", type=int, default=100, help="interval between saving image samples")
parser.add_argument("--checkpoint_interval", type=int, default=1, help="interval between model checkpoints")
opt, unknown = parser.parse_known_args()
print(opt)

hr_shape = (opt.hr_height, opt.hr_width)


# Initialize generator and discriminator
opG = GenOps()
opD = DiscOps()
if TRAINED:
    generator = opG.loadNet('../input/trainedgan-1/generator_5.pth')
    discriminator = opD.loadNet('../input/trainedgan-1/discriminator_5.pth')
else:
    generator = opG.createNet()
    discriminator = opD.createNet()

feature_extractor = FeatureExtractor()

feature_extractor.eval()

# Losses
criterion_GAN = torch.nn.MSELoss()
criterion_content = torch.nn.L1Loss()
# Optimizers
optimizer_G = torch.optim.Adam(generator.parameters(), lr=opt.lr, betas=(opt.b1, opt.b2))
optimizer_D = torch.optim.Adam(discriminator.parameters(), lr=opt.lr, betas=(opt.b1, opt.b2))
#optimizer_G = optim.SGD(generator.parameters(), lr=opt.lr)
#optimizer_D = optim.SGD(discriminator.parameters(), lr=opt.lr)

training_set = createDatasets('train', batch=opt.batch_size)  

Tensor = torch.cuda.FloatTensor

# ----------
#  Training
# ----------
#dev = opG.getDevice()
generator.cuda()
discriminator.cuda()
feature_extractor.cuda()
#criterion_GAN.to(dev)
#criterion_content.to(dev)

#generator.train()
#discriminator.train()
n_iter = 0
for epoch in range(opt.epoch, opt.n_epochs):
    for i, imgs in enumerate(training_set):

        # Configure model input
        imgs_lr = Variable(imgs["img"].type(Tensor))
        imgs_hr = Variable(imgs["gth"].type(Tensor))

        # Adversarial ground truths
        valid = Variable(Tensor(np.ones((imgs_lr.size(0), 1))), requires_grad=False)
        fake = Variable(Tensor(np.zeros((imgs_lr.size(0), 1))), requires_grad=False)

        # ------------------
        #  Train Generators
        # ------------------

        optimizer_G.zero_grad()

        # Generate a high resolution image from low resolution input
        gen_hr = generator(imgs_lr)

        # Adversarial loss
        loss_GAN = criterion_GAN(discriminator(gen_hr), valid)

        # Content loss
        gen_features = feature_extractor(gen_hr)
        real_features = feature_extractor(imgs_hr)
        loss_content = criterion_content(gen_features, real_features.detach())

        # Total loss
        loss_G = loss_content + 1e-3 * loss_GAN

        loss_G.backward()
        optimizer_G.step()

        # ---------------------
        #  Train Discriminator
        # ---------------------

        optimizer_D.zero_grad()

        # Loss of real and fake images
        loss_real = criterion_GAN(discriminator(imgs_hr), valid)
        loss_fake = criterion_GAN(discriminator(gen_hr.detach()), fake)

        # Total loss <3
        loss_D = (loss_real + loss_fake) / 2

        loss_D.backward()
        optimizer_D.step()

        # --------------
        #  Log Progress
        # --------------
        print(
            "\r[Epoch %d/%d] [Batch %d/%d] [D loss: %f] [G loss: %f]"
            % (epoch, opt.n_epochs, i, len(training_set), loss_D.item(), loss_G.item()),
            end=""
        )
        writer.add_scalar('train/lossDisc', loss_D.item(), n_iter)
        writer.add_scalar('train/lossGen', loss_G.item(), n_iter)

        batches_done = epoch * len(training_set) + i
        if batches_done % opt.sample_interval == 0:
            # Save image grid with upsampled inputs and SRGAN outputs
            imgs_lr = nn.functional.interpolate(imgs_lr, scale_factor=4)
            gen_hr = make_grid(gen_hr, nrow=1, normalize=True)
            imgs_lr = make_grid(imgs_lr, nrow=1, normalize=True)
            img_grid = torch.cat((imgs_lr, gen_hr), -1)
            writer.add_image('train/output'+ str(n_iter), img_grid, batches_done)
            #save_image(img_grid, "images/%d.png" % batches_done, normalize=False)
        
        n_iter += 1
        del imgs_lr, imgs_hr, gen_hr

    if opt.checkpoint_interval != -1 and epoch % opt.checkpoint_interval == 0:
        # Save model checkpoints
        torch.save(generator.state_dict(), "saved_models/generator_%d.pth" % epoch)
        torch.save(discriminator.state_dict(), "saved_models/discriminator_%d.pth" % epoch)
