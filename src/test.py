import pandas as pd
import tensorflow as tf
from utils import models_dir_len

def main():
    model = tf.keras.models.load_model(f'models/model_{models_dir_len(offset=0)}.h5')

    test_df = pd.read_csv('data/COVID-19_MS_dataset_test.csv')
    attributes = test_df[['Person_ID', 'Sample_ID']]
    test_df.drop(columns=['Person_ID', 'Sample_ID', 'PCR_result'], inplace=True)
    predictions = model.predict(test_df)

    for (idx, person_id, sample_id), (result) in zip(attributes.itertuples(), predictions):
        idx = str(idx).rjust(4)
        person_id = str(person_id).rjust(4)
        sample_id = str(sample_id).rjust(4)
        result = 'pos' if result > 0.5 else 'neg'
        print(f'Idx: {idx} | Person ID: {person_id} | Sample ID: {sample_id} | PCR Result: {result}')

if __name__ == "__main__":
    main()