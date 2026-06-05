## Challenge 1 - Secrets and Git

Even after removing hardcoded credentials from the source code and pushing the updated files, the secrets still remain inside the Git commit history. Git stores every previous commit permanently unless the history is explicitly rewritten using tools like `git filter-repo` or BFG Repo Cleaner. This means attackers, collaborators, or automated scanners can still recover exposed credentials from older commits even if the latest code appears secure. Proper remediation therefore requires both removing the secrets from the active codebase and sanitizing the repository history to completely eliminate the exposure.

