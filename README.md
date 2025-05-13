# AWS Multi-Service CLI

A modular Python CLI tool that interacts with AWS services including:
- EC2
- S3
- Route53
- CloudWatch (via `watchtower`)

Supports session-based AWS credentials and structured CLI via `argparse`.

---

## 📦 Features

- Manage EC2 instances (create/list/start/stop/terminate)
- Manage S3 buckets (create/list/upload/delete)
- Manage Route53 domains and DNS records
- Send logs to CloudWatch from CLI with `watchtower`
- Docker-ready for containerized execution
- Jenkins-compatible for CI/CD integration

---

## 🚀 How to Run

### 🐍 Locally with Python

Install dependencies:

```bash
pip install -r requirements.txt
python main.py \
  --service cloudwatch \
  --access_key YOUR_ACCESS_KEY \
  --secret_key YOUR_SECRET_KEY \
  --region us-east-1 \
  --action test-log
```
---

### 🐳 Running with Docker
```bash
docker build -t aws-cli-app .
```
#### Run the container:
```bash
docker run aws-cli-app \
  --service cloudwatch \
  --access_key YOUR_ACCESS_KEY \
  --secret_key YOUR_SECRET_KEY \
  --region us-east-1 \
  --action docker-log
```

