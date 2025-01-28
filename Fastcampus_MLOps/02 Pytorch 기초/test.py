import os
import torch
print(torch.cuda.is_available())
print(torch.__version__)


os.environ['CUDA_DEVICE_ORDER']="PCI_BUS_ID"
os.environ['CUDA_VISIBLE_DEVICES']='0'
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('Device:', device)
# print('Current cuda device:', torch.cuda.current_device())
print('Count of using GPUs:', torch.cuda.device_count())

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print ('Available devices ', torch.cuda.device_count())
print(torch.cuda.get_device_name(device))