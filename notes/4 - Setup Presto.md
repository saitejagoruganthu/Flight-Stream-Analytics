# Setup Presto Cluster inside in Minikube

Add Presto repo to helm

```
helm repo add presto https://prestodb.github.io/presto-helm-charts
```

![Pasted image 20250805011622.png](./images/Pasted%20image%2020250805011622.png)

Update the helm repo to fetch latest version

```
helm repo update
```

![Pasted image 20250805011719.png](./images/Pasted%20image%2020250805011719.png)

Create presto namespace

```
kubectl create namespace presto
```

Install helm repo for presto

```
helm install presto presto/presto --namespace presto
```

![Pasted image 20250809151859.png](./images/Pasted%20image%2020250809151859.png)

Verify that presto coordinator is started

```
kubectl get all -n presto
```

Get logs from coordinator to check if server is started (It should say `SERVER STARTED`)

```
kubectl logs presto-coordinator-5f455f47f4-lhm7k -n presto
```

![Pasted image 20250809152011.png](./images/Pasted%20image%2020250809152011.png)
![Pasted image 20250805231624.png](./images/Pasted%20image%2020250805231624.png)
