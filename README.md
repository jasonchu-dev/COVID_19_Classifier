# COVID-19 Classifier

Prediction of PCR results from saliva sample/mass spectrometry data using deep learning.

Dataset: https://www.kaggle.com/datasets/kerneler/saliva-testing-dataset/data

### Fully Connected Neural Network

* 6 linear layers
* 3 dropout layers
* ReLU and Sigmoid

## Run

Clone
```
    git clone https://github.com/jasonchu-dev/COVID_19_Classifier.git
```
Download Docker and run
```
    bash scripts/run.sh
```
To clean files
```
    bash scripts/clean_files.sh
```
To delete docker container and image
```
    bash scripts/clean_docker.sh
```
Adjust hyperparameters in configs if need be.