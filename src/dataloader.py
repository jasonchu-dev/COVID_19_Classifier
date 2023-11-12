import pandas as pd
import numpy as np
import warnings
from sklearn.utils.class_weight import compute_class_weight

warnings.filterwarnings("ignore")

def preprocess():
    df = pd.read_csv('data/COVID-19_MS_dataset_train.csv')
    
    df.drop(columns=['Person_ID', 'Sample_ID'], inplace=True)
    PCRresult2bin = {'pos': 1, 'neg': 0}
    df.replace({'PCR_result': PCRresult2bin}, inplace=True)

    df = df.sample(frac=1, random_state=42, ignore_index=True)

    X = df.iloc[:, 1:]
    y = df.iloc[:, 0]
    class_weights = compute_class_weight('balanced', classes=np.unique(y), y=y)

    return X, y, class_weights