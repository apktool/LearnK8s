

```bash
docker build -f app1/Dockerfile -t flask-app1:v1 app1
kind --name mycluster load docker-image flask-app1:v1

docker build -f app2/Dockerfile -t flask-app2:v1 app2
kind --name mycluster load docker-image flask-app2:v1
```

```bash
kubectl apply -f deploy-ingress-nginx.yaml
```

```bash
kubectl create namespace app-demo

kubectl -n app-demo apply -f app1/deployment.yaml
kubectl -n app-demo apply -f app1/service.yaml
kubectl -n app-demo apply -f app2/deployment.yaml
kubectl -n app-demo apply -f app2/service.yaml

kubectl -n app-demo apply -f ingress.yaml
```

```bash
curl -X GET http://localhost:80/api1/go
curl -X GET http://localhost:80/api2/go
```

## 其他命令

```bash
docker pull registry.k8s.io/ingress-nginx/kube-webhook-certgen:v1.4.4
docker pull registry.k8s.io/ingress-nginx/controller:v1.12.0-beta.0
```

```bash
# 查看 kind 所有 load 的 images
docker exec -it mycluster-control-plane crictl images
# 删除指定的 images
docker exec -it mycluster-control-plane crictl rmi b37d611d0f213
```
