#!/bin/bash

FROM tensorflow/tensorflow:latest-gpu

RUN apt-get update && \
    apt-get install -y python3 python3-pip git vim && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /repo

RUN git clone https://github.com/jasonchu-dev/COVID_19_Classifier.git

RUN cd COVID_19_Classifier && \
    pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''", "--NotebookApp.allow_origin='*'"]