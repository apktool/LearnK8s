# Docker

## 构建镜像

```bash
docker build -f Dockerfile -t flaskapi:v1 .
```

```bash
> docker build -f Dockerfile -t flaskapi:v1 .
[+] Building 30.1s (3/3) FINISHED                                                                                                                                                                                                                                    docker:default
 => [internal] load build definition from Dockerfile                                                                                                                                                                                                                           0.0s
 => => transferring dockerfile: 252B                                                                                                                                                                                                                                           0.0s
 => ERROR [internal] load metadata for docker.io/library/python:3.14.0a3-bookworm                                                                                                                                                                                             30.0s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                                                                                                                                                  0.0s
------
 > [internal] load metadata for docker.io/library/python:3.14.0a3-bookworm:
------
Dockerfile:1
--------------------
   1 | >>> FROM python:3.14.0a3-bookworm
   2 |     RUN mkdir /app
   3 |     WORKDIR /app
--------------------
ERROR: failed to solve: python:3.14.0a3-bookworm: failed to resolve source metadata for docker.io/library/python:3.14.0a3-bookworm: failed to authorize: failed to fetch oauth token: Post "https://auth.docker.io/token": dial tcp 69.171.229.73:443: i/o timeout
```

```bash
> export https_proxy=http://127.0.0.1:7890/
```

```bash
# 先测试 docker 镜像没有问题
docker run --name flaskapi -p 8000:8000 flaskapi:v1
```

# 搭建 kind 集群

```bash
# kind delete cluster --name mycluster
kind create cluster --config kind.yaml --name mycluster
kubectl cluster-info --context kind-mycluster
```

# 加载 docker 镜像

```bash
kind --name mycluster load docker-image flaskapi:v1
```

# K8s

```bash
kubectl create namespace app-demo
kubectl -n app-demo apply -f deployment.yaml
kubectl -n app-demo apply -f service.yaml
kubectl -n app-demo get pod -l app=flask-app
```

# 浏览器查看

```bash
curl -X GET http://localhost:80
```

# 其他常见命令

```bash
kubectl -n app-demo exec pod/chapter-01-9bd95974d-wtcjz -it -- bash
kubectl -n app-demo exec `kubectl -n app-demo get pods -l app=flask-app -o name` -it -- bash
kubectl -n app-demo logs -f pod/chapter-01-9bd95974d-wtcjz
```


```bash 
> kubectl apply -f https://kind.sigs.k8s.io/examples/ingress/deploy-ingress-nginx.yaml
> kubectl apply -f ingress.yaml        
Error from server (InternalError): error when creating "ingress.yaml": Internal error occurred: failed calling webhook "validate.nginx.ingress.kubernetes.io": failed to call webhook: Post "https://ingress-nginx-controller-admission.ingress-nginx.svc:443/networking/v1/ingresses?timeout=10s": dial tcp 10.96.246.94:443: connect: connection refused
```

```bash
kubectl get validatingwebhookconfigurations
kubectl delete -A ValidatingWebhookConfiguration ingress-nginx-admission
```

# MiniKube

```bash
minikube start --base-image=registry.cn-hangzhou.aliyuncs.com/google_containers/kicbase:v0.0.45
```

```bash
minikube image load flaskapi:v1
minikube -n app-demo service chapter-01
```