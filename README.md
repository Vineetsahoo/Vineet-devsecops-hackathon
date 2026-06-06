# DevSecOps Hackathon

Concise solutions for a four-part DevSecOps security challenge covering secret detection, application scanning, container hardening, and Infrastructure-as-Code (IaC) security.

## Overview

- Challenge 1: Secret detection and remediation (Gitleaks)
- Challenge 2: Vulnerable Flask app scanning and fixes (Semgrep)
- Challenge 3: Dockerfile hardening and image scanning (Trivy)
- Challenge 4: Terraform security checks and remediation (Checkov)

## Repository layout

```
vineet-devsecops-hackathon/
├── challenge1/
│   ├── app.py
│   ├── gitleaks-before.json
│   └── gitleaks-after.json
├── challenge2/
│   ├── app.py
│   ├── app_vulnerable.py
│   ├── semgrep-before.json
│   └── semgrep-after.json
├── challenge3/
│   ├── app.py
│   ├── Dockerfile          # hardened
│   ├── Dockerfile.insecure
│   └── requirements.txt
├── challenge4/
│   ├── main.tf
│   ├── main_insecure.tf
│   ├── checkov-before.txt
│   └── checkov-after.txt
└── REPORT.md
```

## Prerequisites

- Python 3.8+ (for running the sample Flask apps)
- Optional scanners (installed separately): `gitleaks`, `semgrep`, `trivy`, `checkov`

Install Python dependencies for challenges that require them:

```powershell
python -m pip install -r challenge3/requirements.txt
```

## Check it out

Each challenge folder contains the vulnerable and remediated artifacts and the scanner output files. Quick guidance:

- Challenge 1 (Secrets & Git)
	- Review detected secrets: `challenge1/gitleaks-before.json`
	- Remediated output: `challenge1/gitleaks-after.json`

- Challenge 2 (Flask app + Semgrep)
	- Run the vulnerable app: `python challenge2/app_vulnerable.py`
	- Run the fixed app: `python challenge2/app.py`
	- Semgrep reports: `challenge2/semgrep-before.json`, `challenge2/semgrep-after.json`

- Challenge 3 (Docker + Trivy)
	- Build insecure image (example):

		```powershell
		docker build -f challenge3/Dockerfile.insecure -t demo:insecure challenge3/
		trivy image demo:insecure
		```

	- Build hardened image:

		```powershell
		docker build -f challenge3/Dockerfile -t demo:hardend challenge3/
		trivy image demo:hardend
		```

- Challenge 4 (Terraform + Checkov)
	- Run Checkov against the insecure config:

		```powershell
		checkov -d challenge4/ -o json > challenge4/checkov-before.txt
		```

	- After fixes, re-run and compare: `challenge4/checkov-after.txt`

## Notes

- Scanner binaries (gitleaks, semgrep, trivy, checkov) are not included. Install them via their official docs or package managers.
- The repository is intended for learning and demonstration purposes only.


