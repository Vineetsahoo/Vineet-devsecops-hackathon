# DevSecOps Hackathon

This repository contains solutions for a multi-stage DevSecOps security challenge focused on secure development, vulnerability scanning, container hardening, and Infrastructure as Code (IaC) security practices.

The project demonstrates:
* **Secret detection and remediation** using Gitleaks
* **Vulnerable Flask application scanning** using Semgrep
* **Docker image hardening** using Trivy
* **Terraform security analysis** using Checkov

---

## Project Structure

```text
vineet-devsecops-hackathon/
├── challenge1/
├── challenge2/
├── challenge3/
├── challenge4/
└── REPORT.md

## Challenges
### Challenge 1 -  Secrets & Git
Simulated accidental credential exposure, detected secrets using Gitleaks, and migrated sensitive data to environment variables.

### Challenge 2 — Vulnerable Flask Application
Created intentionally vulnerable Flask code, scanned vulnerabilities using Semgrep, and remediated insecure patterns.

### Challenge 3 — Docker Hardening
Built insecure and hardened Dockerfiles, scanned them using Trivy, and reduced security findings.

### Challenge 4 — Infrastructure as Code Security
 Created insecure Terraform configurations, scanned them using Checkov, and fixed all security issues.

