#!/bin/bash

FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y python3 python3-pip git && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /repo

RUN git clone https://github.com/jasonchu-dev/COVID_19_Classifier.git

RUN cd COVID_19_Classifier && \
    pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

CMD ["bash"]