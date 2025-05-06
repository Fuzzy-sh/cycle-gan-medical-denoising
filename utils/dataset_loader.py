from torch.utils.data import DataLoader, TensorDataset

def get_fake_dataloader():
    x = torch.randn(10, 1, 28, 28)
    y = x + 0.1 * torch.randn_like(x)
    dataset = TensorDataset(x, y)
    return DataLoader(dataset, batch_size=2)
