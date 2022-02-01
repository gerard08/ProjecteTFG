import torch
from discriminator import Operations

uo = Operations()
dev = uo.getDevice()
unet = uo.loadNet('modelGANDISC.pth')
unet.to(dev)
print(unet)