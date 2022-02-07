import torch
import torch.nn as nn

class block(nn.Module):
    def __init__(self, in_cn, out_cn, stride):
        super(block, self).__init__()
        self.conv = nn.Conv2d(in_channels=in_cn, out_channels=out_cn, kernel_size=3, stride=stride, padding=0)
        self.batch_norm = nn.BatchNorm2d(out_cn)
        self.leakyReLu = nn.LeakyReLU()

    def forward(self, x):
        x = self.conv(x)
        x = self.batch_norm(x)
        x = self.leakyReLu(x)
        return x

class discriminator(nn.Module):
    def __init__(self, in_cn = 3, batch = 3):
        super(discriminator, self).__init__()
        self.batch = batch

        self.conv1 = nn.Conv2d(in_channels=in_cn, out_channels=64, kernel_size=3, stride=1, padding=0)
        self.leaky = nn.LeakyReLU()
        self.block1 = block(64, 64, 2)
        self.block2 = block(64, 128, 1)
        self.block3 = block(128, 128, 2)
        self.block4 = block(128, 256, 1)
        self.block5 = block(256, 256, 2)
        self.block6 = block(256, 512, 1)
        self.block7 = block(512, 512, 2)
        self.dense1 = nn.Linear(373248, 1024)
        self.dense2 = nn.Linear(1024, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.conv1(x)
        x = self.leaky(x)
        x = self.block1(x)
        x = self.block2(x)
        x = self.block3(x)
        x = self.block4(x)
        x = self.block5(x)
        x = self.block6(x)
        x = self.block7(x)
        x = x.view(self.batch, -1)
        x = self.dense1(x)
        x = self.leaky(x)
        x = self.dense2(x)
        x = self.sigmoid(x)
        return x

        
#################ZONA PROVES#################


class DiscOps:
    def __init__(self):
        pass

    def getDevice(self):
        use_cuda = torch.cuda.is_available()
        device = torch.device("cuda:0" if use_cuda else "cpu")
        torch.backends.cudnn.benchmark = True
        return device

    def createNet(self, n_classes = 3, batches = 3):
        self.net = discriminator(n_classes, batches)
        return self.net

    def saveNet(self, namefile):
        torch.save(self.net.state_dict(), namefile)
        print('saved successfully')

    def loadNet(self, namefile,batches = 3):
        model = discriminator(batches)
        model.load_state_dict(torch.load(namefile), strict=False)
        return model


if __name__ == '__main__':
    print('okok')