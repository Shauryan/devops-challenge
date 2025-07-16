# 🚀 DevOps Challenge: Cloud-Native Flask API

This project is a **DevOps challenge solution** that demonstrates key DevOps practices including containerization, CI/CD, Helm, Kubernetes, and security policies using OPA (Open Policy Agent).

---

## 📌 Features

- Flask API that echoes request headers, method, and body
- Dockerized with a multistage build
- CI/CD with GitHub Actions
- Helm chart to deploy to Kubernetes
- OPA policy for enforcing best practices
- Prometheus metrics exposed

---

## 🛠️ Tech Stack

- Python 3.9 + Flask
- Docker
- Helm
- Kubernetes (Minikube)
- GitHub Actions
- Open Policy Agent (OPA)
- Prometheus Client

---

## 📂 Project Structure

devops-challenge/
├── api/ # Flask app source code
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
├── devops-chart/ # Helm chart for deployment
│ ├── templates/
│ ├── values.yaml
│ └── Chart.yaml
├── opa/ # OPA policies
│ └── policy.rego
└── .github/workflows/ # GitHub Actions CI/CD
└── ci.yml






---

## 🧪 API Usage Example

```bash
curl --header "Content-Type: application/json" \
     --data '{"username":"xyz","password":"xyz"}' \
     http://localhost:5000/api


Welcome to our demo API, here are the details of your request:
Headers:
Content-Type: application/json
Method:
POST
Body:
{"username":"xyz","password":"xyz"}



🐳 Docker Usage
✅ Build

cd api
docker build -t rahulshauryan/devops-api:latest .

✅ Run
docker run -p 5000:5000 rahulshauryan/devops-api:latest

🎯 Helm Chart Deployment (Minikube)
11. Start Minikube
minikube start

2. Install Helm Chart
cd devops-chart
helm install devops-api .

3. Verify Pod and Service
kubectl get pods
kubectl get svc

4. Port Forward
kubectl port-forward svc/devops-api-devops-chart 5000:5000



✅ GitHub Actions CI/CD
CI/CD pipeline is configured via .github/workflows/ci.yml.

Triggers:
Push to master

Pull Requests

Steps:
Checkout code

Install Python dependencies

(Optional) Add unit/integration tests

Check workflow status at:
👉 https://github.com/Shauryan/devops-challenge/actions





🔐 OPA (Open Policy Agent)
OPA is integrated for validating Kubernetes deployment policies.

Example: opa/policy.rego
rego
Copy
Edit
package kubernetes.admission

deny[msg] {
  input.request.kind.kind == "Deployment"
  sa := input.request.object.spec.template.spec.serviceAccountName
  sa == "default"
  msg := "Do not use default service account"
}
To evaluate:

bash
Copy
Edit
opa eval --input input.json --data opa/policy.rego "data.kubernetes.admission.deny"
📈 Prometheus Integration
The Flask app exposes a Prometheus metrics endpoint at /metrics:

python
Copy
Edit
from prometheus_client import Counter
requests_total = Counter('api_requests_total', 'Total API Requests')










📘 TODOs
 Add unit tests for Flask API

 Add container-structure-test

 Enable Ingress for Kubernetes

 Add Open Policy Agent to CI checks

 Add security scans (Trivy, Hadolint)
