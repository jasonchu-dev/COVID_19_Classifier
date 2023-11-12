import os
import yaml

def models_dir_exist():
    os.makedirs('models', exist_ok=True)

def models_dir_len(offset=1):
    items = os.listdir('models')
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