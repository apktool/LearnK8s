# 创建 kind 集群

```bash
kind create cluster --config kind.yaml --name mycluster
kubectl cluster-info --context kind-mycluster
```

# 拉取镜像

```bash
# https://artifacthub.io/packages/helm/k8s-dashboard/kubernetes-dashboard
# 之所以有这步，还是因为网络不通，所以这里先 pull 下来，然后再 load 进去，以解决 image 下载不下来的问题
HTTPS_PROXY=$https_proxy

docker pull docker.io/kubernetesui/dashboard-api:1.10.2
docker pull docker.io/kubernetesui/dashboard-auth:1.2.3
docker pull kong:3.8
docker pull docker.io/kubernetesui/dashboard-metrics-scraper:1.2.2
docker pull docker.io/kubernetesui/dashboard-web:1.6.1

kind --name mycluster load docker-image docker.io/kubernetesui/dashboard-api:1.10.2
kind --name mycluster load docker-image docker.io/kubernetesui/dashboard-auth:1.2.3
kind --name mycluster load docker-image kong:3.8
kind --name mycluster load docker-image docker.io/kubernetesui/dashboard-metrics-scraper:1.2.2
kind --name mycluster load docker-image docker.io/kubernetesui/dashboard-web:1.6.1
```

# 安装 dashboard

```bash
helm repo add kubernetes-dashboard https://kubernetes.github.io/dashboard
helm install kubernetes-dashboard kubernetes-dashboard/kubernetes-dashboard --create-namespace --namespace kubernetes-dashboard
helm delete kubernetes-dashboard --namespace kubernetes-dashboard
```

# 创建 token

```bash
kubectl apply -f dashboard-admin.yaml
kubectl apply -f dashboard-role.yaml
kubectl -n kubernetes-dashboard create token admin-user
```

# 访问 dashboard

```bash
kubectl -n kubernetes-dashboard port-forward svc/kubernetes-dashboard-kong-proxy 8443:443
https://localhost:8443/
```
