# AWS Multi-Service CLI

A Python-based CLI tool for managing AWS infrastructure through EC2, S3, and Route53.  
Designed for learning, automation, and hands-on DevOps practice.

## 🚀 Features

- 🖥 Create, list, start/stop, and terminate EC2 instances (with optional VPC/Subnet creation)
- ☁️ Create and manage S3 buckets, upload files, and delete resources
- 🌐 Create Route53 hosted zones and manage DNS records
- 🔐 Works with temporary AWS credentials via Boto3 session
- 🛠 Jenkinsfile for CI/CD automation
- 🐍 Built with modular Python scripts for reusability

## 📦 Setup & Run

```bash
git clone https://github.com/AdamLevs/aws-multi-service-cli.git
cd aws-multi-service-cli
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python main.py
