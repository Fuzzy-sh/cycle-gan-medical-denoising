import torch

def compute_psnr(pred, target):
    mse = torch.mean((pred - target) ** 2)
    psnr = 10 * torch.log10(1 / mse)
    return psnr.item()

def compute_ssim(pred, target):
    # Placeholder – real SSIM would require skimage or similar
    return 0.85  # dummy value for showcase


