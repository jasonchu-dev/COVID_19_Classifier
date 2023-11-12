import tensorflow as tf
from tensorflow.keras.layers import Dense, Dropout
from utils import parameters

def FCNN():
    _, _, _, _, _, dropout = parameters()
    return tf.keras.Sequential([
        Dense(1358, activation='relu'),
        Dropout(rate=dropout),
        Dense(679, activation='relu'),
        Dropout(rate=dropout),
        Dense(97, activation='relu'),
        Dropout(rate=dropout),
        Dense(40, activation='relu'),
        Dense(40, activation='relu'),
        Dense(1, activation='sigmoid')
    ])