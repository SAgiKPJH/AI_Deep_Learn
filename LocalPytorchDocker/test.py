import os
import torch
print("Torch cuda is available: ", torch.cuda.is_available())
print("Torch version: ", torch.__version__)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('Device:', device)
# print('Current cuda device:', torch.cuda.current_device())
print('Count of using GPUs:', torch.cuda.device_count())
print("Device name: ", torch.cuda.get_device_name(device))