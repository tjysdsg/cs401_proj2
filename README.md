# Files

- `serve.sh` and `serve.py` is the server running script
- `test_api.sh` and `client.py` is the test client script
- `train.py` contains the code related to model training and inference
- `model.pkl` is the pretrained model
- `build_docker.sh` rebuilds the docker image and push it to quay.io (not needed as quay.io auto builds the image)
- `docker_local_run.sh`, `kube_run.sh`, `argocd_run.sh` runs the service using docker, kubernetes, and argocd
  respectively
- `deployment.yaml` and `service.yaml` is the configuration for kubernetes
