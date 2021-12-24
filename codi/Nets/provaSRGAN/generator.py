import torch
import torch.nn as nn

class residualBlock(nn.Module):
    def __init__(self, in_cn):
        super(residualBlock, self).__init__()
        self.convolution = nn.Conv2d(in_cn, in_cn, kernel_size=3)
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
        self.conv = nn.Conv2d(in_cn, out_cn, kernel_size=3)
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
        self.conv = nn.Conv2d(in_cn, in_cn, kernel_size = 3)
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
    def __init__(self, in_cn):
        super(generator, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=in_cn, out_channels=64, kernel_size=9, stride=1)
        self.PReLU = nn.PReLU()

        self.mediumBlock = fullMediumStructure(nBlocks=8, in_cn=in_cn)
        self.finalBlock1 = finalBlock(in_cn, out_cn=256)
        self.finalBlock2 = finalBlock(in_cn=256, out_cn=256)
        self.finalConv = nn.Conv2d(in_channels=256, out_channels=3, kernel_size=9)

    def forward(self, x):
        x = self.conv1(x)
        x = self.PReLU(x)
        x = self.mediumBlock(x)
        x = self.finalBlock1(x)
        x = self.finalBlock2(x)
        x = self.finalConv(x)
        return x


if __name__ == '__main__':
    print('okok')