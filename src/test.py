import argparse
import pandas as pd
import tensorflow as tf
from utils import dir_exist, dir_len

def main(args):
    model = tf.keras.models.load_model(f'models/model_{dir_len(offset=0)}.h5')

    test_df = pd.read_csv('https://jasonchu-dev-q3567j.s3.us-west-1.amazonaws.com/COVID_19_Classifier/COVID-19_MS_dataset_test.csv')
    attributes = test_df[['Person_ID', 'Sample_ID']]
    test_df.drop(columns=['Person_ID', 'Sample_ID', 'PCR_result'], inplace=True)
    predictions = model.predict(test_df)

    data = {'Idx': [], 'Person ID': [], 'Sample ID': [], 'PCR Result': []}

    for (idx, person_id, sample_id), (result) in zip(attributes.itertuples(), predictions):
        result = 'pos' if result > 0.5 else 'neg'
        if args.verbose == 1:
            idx = str(idx).rjust(4)
            person_id = str(person_id).rjust(4)
            sample_id = str(sample_id).rjust(4)
            print(f'Idx: {idx} | Person ID: {person_id} | Sample ID: {sample_id} | PCR Result: {result}')

        data['Idx'].append(idx)
        data['Person ID'].append(person_id)
        data['Sample ID'].append(sample_id)
        data['PCR Result'].append(result)

    dir_exist('reports')
    df = pd.DataFrame(data)
    df.to_csv('reports/test_results.csv', index=False)
    print(f'Results saved as reports/test_results.csv')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", type=int, default=0, help="print results (default is 0 for print)")
    args = parser.parse_args()
    main(args)