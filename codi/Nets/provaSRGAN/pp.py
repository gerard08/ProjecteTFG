import torch
from torch.functional import Tensor
import torch.nn as nn

m = nn.Linear(73728,1024)
input = torch.randn(1, 512, 12, 12)
leaky = nn.LeakyReLU()
m2 = nn.Linear(1024,1)
sig = nn.Sigmoid()


input = input.view(1, -1)
output = m(input)
output = leaky(output)
output = m2(output)
output = sig(output)

print(output.size())
print(output)