import torch.nn as nn

class Discriminator(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(1, 8, kernel_size=3, stride=2),
            nn.LeakyReLU(0.2),
            nn.Flatten(),
            nn.Linear(8*14*14, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.net(x)

