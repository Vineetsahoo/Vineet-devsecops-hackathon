**Challenge 1 - Secrets and Git**

Even after removing hardcoded credentials from the active source, secrets were still recoverable from the Git history. Git preserves prior commits until the history is rewritten, so scanners can still surface old secrets unless the repository history is sanitized.

- **Findings (before):** Gitleaks reported hardcoded AWS access key and a password in the repo history ([challenge1/gitleaks-before.json](challenge1/gitleaks-before.json)).
- **Findings (after):** A post-change scan still shows secrets found in previous commits and additional detections in the repository ([challenge1/gitleaks-after.json](challenge1/gitleaks-after.json)).
- **Remediation:** Rewrite history with `git filter-repo` or BFG to remove secrets from all commits, rotate any exposed credentials immediately, and add a pr**e-commit/gitleaks CI check to block secrets from being committed.

**Challenge 2 - Static Code Analysis (Semgrep)**

- **Findings (before):** Semgrep flagged a SQL injection (user input passed to `execute()`) in `app_vulnerable.py` ([challenge2/semgrep-before.json](challenge2/semgrep-before.json)).
- **Findings (after):** The fixed codebase (`app.py`) shows no Semgrep findings ([challenge2/semgrep-after.json](challenge2/semgrep-after.json)).
- **Remediation:** Use parameterized queries / ORM query methods, validate and sanitize inputs, add focused unit tests and enforce Semgrep in CI to prevent regressions.

**Challenge 3 - Container / Image Scanning (Trivy)**

- **Findings (before):** Trivy reported a large number of vulnerable packages in the original image (summary in [challenge3/trivy-before.txt](challenge3/trivy-before.txt)) — many medium/high/critical findings.
- **Findings (after):** After hardening, Trivy reports significantly fewer issues (summary in [challenge3/trivy-after.txt](challenge3/trivy-after.txt)) — vulnerability count reduced from the original scan to a much smaller set.
- **Remediation:** Rebase to minimal up-to-date base images, pin and update packages, remove unnecessary packages, apply OS-level updates, and rebuild images regularly; integrate Trivy (or similar) into the CI pipeline to fail builds on unacceptable severity thresholds.

**Challenge 4 - Infrastructure as Code (Checkov / Terraform)**

- **Findings (before):** Checkov scanned `main_insecure.tf` and reported 9 passed checks / 14 failed checks (details in [challenge4/checkov-before.txt](challenge4/checkov-before.txt)). Failures included missing S3 public access block settings, public ACLs, missing encryption/lifecycle/replication, and overly permissive security group rules.
- **Findings (after):** After remediations, Checkov shows improvements: 17 passed checks / 6 failed checks (details in [challenge4/checkov-after.txt](challenge4/checkov-after.txt)). Remaining failures are related to optional logging/notification/lifecycle features and resources not attached to other components.
- **Remediation:** Enable S3 public access blocks, KMS encryption, bucket versioning, lifecycle rules, event notifications, enable access logging, and restrict security group ingress (add descriptions and attach SGs to resources). Enforce Checkov in CI to catch new IaC issues before merge.

---


