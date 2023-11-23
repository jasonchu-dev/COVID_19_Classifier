FROM ubuntu:20.04

COPY . ./

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

CMD [ "bash", "scripts/docker.sh" ]