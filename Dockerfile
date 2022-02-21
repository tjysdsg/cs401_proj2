FROM python:3.9-bullseye

WORKDIR /root

RUN pip3 install fastapi[all] scikit-learn numpy pandas

# FIXME: dockerfile shouldn't include the model
COPY model.pkl .
COPY train.py .
COPY serve.py .
COPY serve.sh .

RUN chmod +x serve.sh

ENTRYPOINT ./serve.sh

RUN ls -ahl .