# Secrets Scanning

## What is a Secret?

In coding, secrets refer to sensitive information that should not be exposed publicly or stored insecurely. Examples include passwords, API keys, cryptographic keys, and tokens. If secrets are leaked (e.g., committed to a public GitHub repo), attackers can misuse them to access systems, steal data, or cause harm.

## What is Secret Scanning?

Secret scanning is the automated process of detecting sensitive information, such as passwords, API keys, and tokens, within code repositories and other files. Tools for secret scanning analyze code, configuration files, and commit history to identify and alert developers about exposed secrets before they reach production or become publicly accessible. This helps prevent unauthorized access and reduces the risk of security breaches caused by leaked credentials.

## Scan your project with a Secret scanner

There are a lot of scanners out there. You may learn about them and use them at your will. For the sake of explanation we will use Gitleaks, which has an open source version that's free to use.

### Scanning with Gitleaks

To simply get started use this command from your project's root folder. Use the lab's docker image for convenience.

```bash
docker run --rm -v $(pwd):/src ghcr.io/navhits/gitleaks:latest git -v /src
```

When scanning a sub-folder of a git repo, make sure to mount the entire directory, use directory scanning and then specify the path. In this mode, diff scan will not work.

```bash
# In case the you're mounting the entire repo and scanning a specific sub-folder, specify that path at the end instead of just /src
docker run --rm -v $(pwd):/src ghcr.io/navhits/gitleaks:latest dir -v /src
```

Gitleaks is provided as a docker image for most platforms. It has a homebrew version for macOS and a GitHub.
More info [here](https://github.com/gitleaks/gitleaks?tab=readme-ov-file#installing).

Learn more about gitleaks - <https://gitleaks.io/>
