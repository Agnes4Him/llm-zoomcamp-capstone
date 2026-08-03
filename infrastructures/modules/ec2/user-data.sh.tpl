#!/bin/bash

set -e

exec > >(tee /var/log/bootstrap.log)
exec 2>&1

echo "Updating system"

apt-get update -y
apt-get upgrade -y

echo "Installing Docker"

apt-get install -y docker.io

systemctl enable docker
systemctl start docker


echo "Installing k3s"

curl -sfL https://get.k3s.io | sh -

systemctl enable k3s


echo "Waiting for k3s"

until kubectl get nodes >/dev/null 2>&1
do
  sleep 5
done


mkdir -p /home/ubuntu/.kube

cp /etc/rancher/k3s/k3s.yaml /home/ubuntu/.kube/config

chown -R ubuntu:ubuntu /home/ubuntu/.kube


export KUBECONFIG=/etc/rancher/k3s/k3s.yaml



echo "Installing Helm"

curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash



echo "Installing Gateway API CRDs"

kubectl apply -f \
https://github.com/kubernetes-sigs/gateway-api/releases/latest/download/standard-install.yaml



echo "Installing Traefik Gateway Controller"

helm repo add traefik https://traefik.github.io/charts

helm repo update


helm upgrade --install traefik traefik/traefik \
--namespace traefik \
--create-namespace \
--set providers.kubernetesGateway.enabled=true



echo "Installing External Secrets Operator"


helm repo add external-secrets https://charts.external-secrets.io

helm repo update


helm upgrade --install external-secrets \
external-secrets/external-secrets \
--namespace external-secrets \
--create-namespace



echo "Installing Flux"


curl -s https://fluxcd.io/install.sh | bash


echo "Creating bootstrap manifests"


mkdir -p /opt/bootstrap


cat <<EOF >/opt/bootstrap/flux-oci-repository.yaml
${flux_repo}
EOF


cat <<EOF >/opt/bootstrap/flux-kustomization.yaml
${flux_kustomization}
EOF


cat <<EOF >/opt/bootstrap/gateway.yaml
${gateway}
EOF


cat <<EOF >/opt/bootstrap/secret-store.yaml
${secret_store}
EOF


cat <<EOF >/opt/bootstrap/externalsecret.yaml
${external_secret}
EOF



echo "Applying Gateway"

kubectl apply -f /opt/bootstrap/gateway.yaml



echo "Applying External Secrets configuration"

kubectl apply -f /opt/bootstrap/secret-store.yaml

kubectl apply -f /opt/bootstrap/externalsecret.yaml



echo "Applying Flux OCI GitOps"


kubectl apply -f /opt/bootstrap/flux-oci-repository.yaml

kubectl apply -f /opt/bootstrap/flux-kustomization.yaml



echo "Bootstrap completed"