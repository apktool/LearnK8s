# 基本步骤

```bash
docker build -f Dockerfile -t flask-app:v3 .
kind --name mycluster load docker-image flask-app:v3
```

```bash
helm uninstall chapter-03-app
helm install chapter-03-app deploy -n app-demo
kubectl -n app-demo get pod
curl -X GET http://localhost:80
```

# 其他问题

```bash
> helm install chapter-03-app deploy -n app-demo
Error: INSTALLATION FAILED: cannot re-use a name that is still in use
```

```bash
kubectl -n app-demo get secrets
kubectl -n app-demo delete secrets --all
```

# 其他命令

```bash
helm get manifest chapter-03-app
```
