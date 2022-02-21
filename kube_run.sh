kubectl apply -f deployment.yaml || exit 1
kubectl apply -f service.yaml || exit 1
kubectl get deployments || exit 1
kubectl get services