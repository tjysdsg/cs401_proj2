FROM ubuntu:latest

RUN apt-get update

RUN apt-get install -y python3 python3-pip
RUN pip3 install fastapi[all] scikit-learn pickle numpy pandas

RUN ls -ahl