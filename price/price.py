import torch
print(torch.cuda.device_count())
x = torch.tensor([0,1,2])
print(x.device)