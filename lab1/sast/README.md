# SAST

## What is SAST?

SAST stands for Static Application Security Testing. It is a method of analyzing source code, bytecode, or binaries for security vulnerabilities without running the program. SAST helps developers find and fix security issues early in the development process, making applications safer before they are released.

## Scan your code with a SAST tool

There are a lot of scanners out there. You may learn about them and use them at your will. For the sake of explanation we will use Semgrep, which has a community version that's free for open source projects.

### Scanning with Semgrep

To simply get started use this command from your project's root folder. Use the lab's docker image for convenience.

```bash
docker run --rm -v $(pwd):/src ghcr.io/navhits/semgrep:latest semgrep scan -c auto
```

If you prefer to install semgrep, you may follow this [docs](https://semgrep.dev/docs/getting-started/quickstart).

Learn more about Semgrep - https://semgrep.dev
