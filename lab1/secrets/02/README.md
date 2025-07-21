# Secrets Scanning Exercise 2

Detection alone is not enough. Validation is needed too. In this exercise, we will perform a very small validation for a hardcoded GitHub token.

[This helper script](detect-github-token) should do the job. But however there's room for improvement.

This time the helper script will run the docker image and proceed to validation. Just read the script to understand how it works.

```bash
chmod +x detect-github-token
./detect-github-token
```

### Optional

Use these links to generate a test GitHub token. These are not real.

- Classic PAT - https://token.navs.page/github/pat
- Fine grained PAT - https://token.navs.page/github/fine_grained

Don't just spam the links, they're after all a humble [Cloudflare worker](https://developers.cloudflare.com/workers/)
