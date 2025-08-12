# Setup Local Kubernetes Cluster using Minikube

Install Minikube

```
brew install minikube
```

Start Minikube

```
minikube start --memory=8192 --cpus=4
```

![Pasted image 20250805200803.png](./images/Pasted%20image%2020250805200803.png)

Verify minikube is running

```
kubectl get nodes
```

![Pasted image 20250804234245.png](./images/Pasted%20image%2020250804234245.png)