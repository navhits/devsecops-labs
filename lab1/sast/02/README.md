# SAST Exercise 2

Run semgrep with a custom config on a project to detect issues in the code.

```bash
docker run --rm -v $(pwd):/src ghcr.io/navhits/semgrep semgrep scan -c rule.yml
```

In the above command we run a custom configuration. Our rule would detect  Learn more about writing custom rules [here](https://semgrep.dev/docs/writing-rules/rule-ideas).
