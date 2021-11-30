import torch
import torch.nn as nn

class Block(nn.Module):
  def __init__(self, in_cn, out_cn, mid_cn = None):
    super(Block, self).__init__()
    if mid_cn is None:
      mid_cn = out_cn
    #cada block te dos convolucions
    self.conv1 = nn.Conv2d(in_cn, mid_cn, 3, padding=1)
    #self.bn1 = nn.BatchNorm2d(mid_cn)
    #definim la funció d'activació
    self.relu1 = nn.ReLU(inplace=True)

    self.conv2 = nn.Conv2d(mid_cn, out_cn, 3, padding=1)
    #self.bn2 = nn.BatchNorm2d(out_cn)
    #definim la funció d'activació
    self.relu2 = nn.ReLU(inplace=True)

  def forward(self, x):
    x = self.conv1(x)
    #x = self.bn1(x)
    x = self.relu1(x)
    x = self.conv2(x)
    #x = self.bn2(x)
    x = self.relu2(x)
    return x

  def layersList(self):
    return [self.conv1, self.bn1, self.conv2, self.bn2]


class Encoder(nn.Module):
  #a chs passem les dimensions dels Blocks que tindrem
  def __init__(self, in_cn, out_cn, pool=True):
    super(Encoder, self).__init__()
    self.pool = pool
    if pool:
      self.mp = nn.MaxPool2d(2)
    self.block = Block(in_cn, out_cn)

  def layers_list(self):
    return self.block.layersList()

  def forward(self, x):
    if self.pool:
      x = self.mp(x)
    x = self.block(x)
    return x


class Decoder(nn.Module):
  def __init__(self, in_cn, out_cn, mid_cn):
    super(Decoder, self).__init__()
    self.decoder = nn.Upsample(scale_factor=2, mode='nearest')
    self.block = Block(in_cn, out_cn, mid_cn=mid_cn)

  def layers_list(self):
    return self.block.layersList()

  def forward(self, x1, x2=None, x3=None):
    x1 = self.decoder(x1)
    if x2 is None and x3 is None:
      x = x1
    elif x3 is None:
      x = torch.cat([x2,x1], dim=1)
    else:
      x = torch.cat([x2,x3,x1], dim=1)
    x = self.block(x)
    return x


class Mid(nn.Module):
    def __init__(self, in_cn, out_cn, small_cn=None):
        super(Mid, self).__init__()
        self.mp = nn.MaxPool2d(2)
        self.conv1 = nn.Conv2d(in_cn, out_cn, 3, padding=1)
        if small_cn is None:
            self.conv2 = nn.Conv2d(out_cn, in_cn, 3, padding=1)
        else:
            self.conv2 = nn.Conv2d(out_cn, small_cn, 3, padding=1)

    def layers_list(self):
        return [self.conv1, self.conv2]
    
    def forward(self, x):
        x = self.mp(x)
        x = self.conv1(x)
        x = self.conv2(x)
        return x


class OutConv(nn.Module):
    def __init__(self, in_cn, out_cn):
        super(OutConv, self).__init__()
        self.conv = nn.Conv2d(in_cn, out_cn, 1)
    
    def layerslist(self):
        return [self.conv]

    def forward(self, x):
        x = self.conv(x)
        return x


class UNet(nn.Module):
  def __init__(self, num_class):
    super(UNet, self).__init__()
    self.RGBenc1 = Encoder(3, 32, pool=False)
    self.RGBenc2 = Encoder(32, 64)
    self.RGBenc3 = Encoder(64, 128)
    self.RGBenc4 = Encoder(128, 256)

    self.Depthenc1 = Encoder(1, 32, pool=False)
    self.Depthenc2 = Encoder(32, 64)
    self.Depthenc3 = Encoder(64, 128)
    self.Depthenc4 = Encoder(128, 256)

    self.mid = Mid(512, 1024, 512)
    self.dec1 = Decoder(512, 256, 512)
    self.dec2 = Decoder(512, 128, 256)
    self.dec3 = Decoder(256, 64, 128)
    self.dec4 = Decoder(128, 64, 64)
    self.outcnv = OutConv(64, num_class)

  def forward(self, x):
    rgb, d = x
    rgb1 = self.RGBenc1(rgb)
    rgb2 = self.RGBenc2(rgb1)
    rgb3 = self.RGBenc3(rgb2)
    rgb4 = self.RGBenc4(rgb3)

    d1 = self.Depthenc1(d)
    d2 = self.Depthenc2(d1)
    d3 = self.Depthenc3(d2)
    d4 = self.Depthenc4(d3)
    
    x5 = self.mid(torch.cat([rgb4, d4], dim=1))
    x = self.dec1(x5)
    x = self.dec2(x, rgb3, d3)
    x = self.dec3(x, rgb2, d2)
    x = self.dec4(x, rgb1, d1)
    x = self.outcnv(x)

    return x


class UNetOperations:

  def __init__(self):
    pass      

  def getDevice(self):
    use_cuda = torch.cuda.is_available()
    device = torch.device("cuda:0" if use_cuda else "cpu")
    torch.backends.cudnn.benchmark = True
    return device

  def createUNet(self, n_classes):
    self.unet = UNet(n_classes)
    return self.unet

  def saveUnet(self, namefile):
    torch.save(self.unet.state_dict(), namefile)
    print('saved successfully')

  def loadUnet(self, namefile, n_classes = 3):
    model = UNet(n_classes)
    model.load_state_dict(torch.load(namefile))
    return model
