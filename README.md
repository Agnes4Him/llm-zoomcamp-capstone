## Project structure

healthsecure-ai/

├── app/
│   ├── agent.py          # LangChain agent
│   ├── tools.py          # All tool definitions
│   ├── rag.py            # Pinecone retriever
│   ├── database.py       # PostgreSQL connection
│   ├── prompts.py        # System prompt
│   └── llm.py            # Bedrock LLM configuration
│
├── knowledge_base/
│   ├── 01_member_handbook.md
│   ├── 02_benefits_guide.md
│   ├── 03_coverage_policies.md
│   ├── 04_prior_authorization.md
│   ├── 05_claims_guide.md
│   └── 06_appeals_guide.md
│
├── scripts/
│   ├── ingest_documents.py
│   ├── generate_documents.py
│   └── generate_data.py
│
├── database/
│   └── schema.sql
│
├── .env
├── requirements.txt
└── main.py

## start fastapi app
uv run uvicorn api:app --host 0.0.0.0 --port 5000 --reload

## Setup Flux
Install Flux controllers
Configure ECR authentication
Create an OCIRepository
Create a Kustomization

```bash
flux install

kubectl get pods -n flux-system

kubectl apply -f flux/healthsecure-source.yaml

flux get sources oci

kubectl apply -f flux/healthsecure-app.yaml

flux get kustomizations
```

## Set up Traefik + Gatway API
Install Traefik with Gateway API enabled
```bash
helm repo add traefik https://traefik.github.io/charts
helm repo update

helm install traefik traefik/traefik \
  --namespace traefik \
  --create-namespace \
  --set providers.kubernetesGateway.enabled=true \
  --set service.type=LoadBalancer

kubectl get pods -n traefik
```
Install Gateway API CRDs
```bash
kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/latest/download/standard-install.yaml

kubectl get crd | grep gateway

kubectl get gatewayclass
```

Create gateway
```bash
kubectl apply -f gateway.yaml
```

## Pending...
* Run API in docker with postgres and grafana and test
* add httproute to kubernetes
* Run all in kind cluster locally
* Write script to do following...
- installs docker
- installs kind
- install helm
- create kind cluster
- install and set up flux
- set up Traefik controller and Gateway API CRDs
- setup Grafana
