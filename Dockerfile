FROM ubuntu:latest

WORKDIR /root

RUN apt-get update

RUN apt-get install -y python3 python3-pip
RUN pip3 install fastapi[all] scikit-learn numpy pandas

COPY model.pkl .
COPY serve.py .
COPY serve.sh .

RUN chmod +x serve.sh

ENTRYPOINT ./serve.sh

RUN ls -ahl .