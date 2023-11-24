import tensorflow as tf
from model import FCNN
from dataloader import preprocess
from utils import dir_len, dir_exist, parameters

def main():
    X, y, class_weights = preprocess()
    batch_size, epochs, validation_split, patience, lr, _ = parameters()
    model = FCNN()
    
    optimizer = tf.keras.optimizers.Adam(learning_rate=lr)
    model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['binary_accuracy'])
    
    early_stopping = tf.keras.callbacks.EarlyStopping(
        monitor='binary_accuracy',
        min_delta=0,
        patience=patience,
        verbose=0,
        mode='auto',
        baseline=None,
        restore_best_weights=False,
        start_from_epoch=0
    )

    model.fit(X, y, batch_size=batch_size, class_weight={0: class_weights[0], 1: class_weights[1]}, epochs=epochs, callbacks=[early_stopping], validation_split=validation_split)

    dir_exist('models')
    model.save(f'models/model_{dir_len()}.h5')

if __name__ == "__main__":
    main()