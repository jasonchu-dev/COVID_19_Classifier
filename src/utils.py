import os
import yaml

def dir_exist(dir):
    os.makedirs(dir, exist_ok=True)

def dir_len(dir='models', offset=1):
    items = os.listdir(dir)
    return len(items) + offset

def parameters():
    with open('configs/hyperparameters.yaml', 'r') as file:
        hyperparameters = yaml.safe_load(file)

    batch_size = hyperparameters['batch_size']
    epochs = hyperparameters['epochs']
    validation_split = hyperparameters['validation_split']
    patience = hyperparameters['patience']
    lr = hyperparameters['lr']
    dropout = hyperparameters['dropout']

    return batch_size, epochs, validation_split, patience, lr, dropout