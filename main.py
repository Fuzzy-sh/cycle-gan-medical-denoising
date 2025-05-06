# main.py

from models.generator import Generator
from models.discriminator import Discriminator
from utils.dataset_loader import get_fake_dataloader
from utils.metrics import compute_psnr, compute_ssim
import torch
import torch.nn as nn

def train():
    # Init models
    gen = Generator()
    disc = Discriminator()
    
    # Dummy data
    dataloader = get_fake_dataloader()
    loss_fn = nn.MSELoss()

    for epoch in range(2):
        for x, y in dataloader:
            y_fake = gen(x)
            loss = loss_fn(y_fake, y)
            print(f"Epoch {epoch} - Loss: {loss.item():.4f}")
            
            psnr = compute_psnr(y_fake, y)
            ssim = compute_ssim(y_fake, y)
            print(f"PSNR: {psnr:.2f} | SSIM: {ssim:.2f}")

if __name__ == "__main__":
    train()
