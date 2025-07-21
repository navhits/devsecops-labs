# SCA Exercise 1

Run vet on a project to detect issues in the packages used.

```bash
docker run --rm -v $(pwd):/src ghcr.io/navhits/vet:latest scan -D /src
```

In the above command we run the default configuration. The default config should help identify all basic issues. In semgrep a configuration is referred to as a rule. Rules can be written by anyone. Learn more about rules [here](https://semgrep.dev/docs/writing-rules/overview).
