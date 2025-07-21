# Scanning for secrets in GitHub Actions with Gitleaks

## What is GitHub Actions?

GitHub Actions is a tool built into [GitHub](https://github.com/) that lets you automate tasks like building, testing, and deploying code right from your repository. You can set up workflows using YAML files, which run automatically when certain events happen (like pushing code or opening a pull request). This makes it easier to manage CI/CD (Continuous Integration and Continuous Deployment) without needing extra services. Learn more in the [GitHub Actions documentation](https://docs.github.com/en/actions).

## Sample GitHub Action to run something when a PR is created

```yaml
name: GHA for PRs

on: [pull_request]

jobs:
  job1:
    runs-on: ubuntu-latest # You can use any runner provided by GitHub
    steps:
      - name: Checkout
        uses: actions/checkout@4 # To clone the repo into the runner

      - uses: user/action@tag # You can reference someone's GitHub action. Just like importing packages in code

      - name: Run Script
        run: echo "Hello world" # Use run to execute any shell scripts
      - name: Run Multi line Script
        run: |
          echo "Hello"
          echo "World"
```

## Using Gitleaks in GitHub action

Gitleaks provides its own GitHub action we can directly use.

```yaml
uses: gitleaks/gitleaks-action@v2
```

More info about Gitleaks GitHub actions [here](https://github.com/gitleaks/gitleaks/tree/master?tab=readme-ov-file#github-action).
