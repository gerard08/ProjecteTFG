from UNet import UNetOperations
import torch

uo = UNetOperations()
unet = uo.loadUnet('C:/Users/ger-m/Desktop/UNI/4t/TFG/codi/Nets/definitiveRGB/down/model_weights.pth')
device = torch.device("cuda:0")
unet.to(device)
from torch.utils.tensorboard import SummaryWriter

writer=SummaryWriter('C:/Users/ger-m/Desktop/UNI/4t/TFG/temp')
images=torch.empty((64,3,3,3), dtype=torch.float32, device = 'cuda')
writer.add_graph(unet,images)