import torch
import torch.nn as nn
from torchvision.models import vgg19


class FeatureExtractor(nn.Module):
    def __init__(self):
        super(FeatureExtractor, self).__init__()
        vgg19_model = vgg19(pretrained=True)
        self.vgg19_54 = nn.Sequential(*list(vgg19_model.features.children())[:35])

    def forward(self, img):
        return self.vgg19_54(img)


class residualBlock(nn.Module):
    def __init__(self, in_cn):
        super(residualBlock, self).__init__()
        self.convolution = nn.Conv2d(in_cn, in_cn, kernel_size=3, padding=1)
        self.batch_norm = nn.BatchNorm2d(in_cn)
        self.ReLU = nn.PReLU()

    def forward(self, x):
        x0 = x
        x = self.convolution(x)
        x = self.batch_norm(x)
        x = self.ReLU(x)
        x = self.convolution(x)
        x = self.batch_norm(x)
        return x0 + x

    def layerList(self):
        return [self.convolution, self.batch_norm, self.ReLU, self.convolution, self.batch_norm]

    
class finalBlock(nn.Module):
    def __init__(self, in_cn, out_cn):
        super(finalBlock, self).__init__()
        self.conv = nn.Conv2d(in_channels=in_cn, out_channels=out_cn, kernel_size=3, padding=1)
        self.pixsh = nn.PixelShuffle(2)
        self.ReLU = nn.PReLU()

    def forward(self, x):
        x = self.conv(x)
        x = self.pixsh(x)
        x = self.ReLU(x)
        return x
    
    def layerList(self):
        return [self.conv, self.pixsh, self.ReLU]

class fullMediumStructure(nn.Module):
    def __init__(self, nBlocks, in_cn):
        super(fullMediumStructure, self).__init__()
        self.nBlocks = nBlocks
        self.residualBlock = residualBlock(in_cn)
        self.conv = nn.Conv2d(in_cn, in_cn, kernel_size = 3, padding=1)
        self.bn = nn.BatchNorm2d(in_cn)

    def forward(self, x):
        x0 = x
        for i in range(self.nBlocks):
            x = self.residualBlock(x)

        x = self.conv(x)
        x = self.bn(x)
        return x0 + x

    def layerList(self):
        r = []
        for i in range(self.nBlocks):
            r.append(self.residualBlock)
        r.append(self.conv)
        r.append(self.bn)
        return r


class generator(nn.Module):
    def __init__(self, in_cn = 3):
        super(generator, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=in_cn, out_channels=64, kernel_size=9, padding=4)
        self.PReLU = nn.PReLU()

        self.mediumBlock = fullMediumStructure(nBlocks=16, in_cn=64)
        self.finalBlock = finalBlock(in_cn=64, out_cn=256)
        self.finalBlock2 = finalBlock(in_cn=256, out_cn=256)
        self.finalConv = nn.Conv2d(in_channels=64, out_channels=3, kernel_size=9, padding=4)

    def forward(self, x):
        x = self.conv1(x)
        x = self.PReLU(x)
        x = self.mediumBlock(x)
        x = self.finalBlock(x)
        x = self.finalBlock(x)
        x = self.finalConv(x)
        return x




#################ZONA PROVES#################


class Operations:
    def __init__(self):
        pass

    def getDevice(self):
        use_cuda = torch.cuda.is_available()
        device = torch.device("cuda:0" if use_cuda else "cpu")
        torch.backends.cudnn.benchmark = True
        return device

    def createNet(self, n_classes = 3):
        self.net = generator(n_classes)
        return self.net

    def saveNet(self, namefile):
        torch.save(self.net.state_dict(), namefile)
        print('saved successfully')

    def loadNet(self, namefile,batches = 3):
        model = generator(3, batches)
        model.load_state_dict(torch.load(namefile))
        return model

if __name__ == '__main__':
    print('okok')