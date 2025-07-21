# Secrets Scanning Exercise 1

Run gitleaks on a project to detect hardcoded secrets in the code.

```bash
docker run --rm -v $(pwd):/src ghcr.io/navhits/gitleaks:latest git -v /src
```
