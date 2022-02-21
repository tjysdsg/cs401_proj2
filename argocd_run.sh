# argocd app create cs401-proj2 \
#   --repo https://github.com/tjysdsg/cs401-proj2 \
#   --path . \
#   --project jt304-project \
#   --dest-namespace jt304 \
#   --dest-server https://kubernetes.default.svc \
#   --sync-policy auto || exit 1

# argocd app get cs401-proj2 || exit 1
argocd app sync cs401-proj2
