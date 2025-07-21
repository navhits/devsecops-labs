# SCA

## What is SCA?

SCA stands for Software Composition Analysis. It's a process used to check the code you write (and the libraries you use) for security risks, license issues, and outdated components. Most modern apps use lots of open-source packages, and SCA tools help you find out if any of those packages have known vulnerabilities (commonly notified as a CVE) or problems, so you can fix them before they cause trouble.

## What is a CVE?

A CVE (Common Vulnerabilities and Exposures) is like an official ID number for a security problem found in software. When someone discovers a bug that could let hackers break in or cause trouble, it's given a CVE so everyone can talk about the same issue. CVEs help developers and security teams quickly find out if their code or the libraries they use have known risks, so they can fix them before bad things happen.

## Who introduced CVE and who maintains it?

The CVE system was introduced by MITRE Corporation in 1999. MITRE continues to maintain the CVE list, working with a global community of organizations called CVE Numbering Authorities (CNAs) to assign and publish CVE identifiers for security vulnerabilities.

## Other Vulnerability Identifiers

Besides CVE, some platforms maintain their own vulnerability databases and identifiers:

- **deps.dev**: Google’s deps.dev tracks vulnerabilities in open source packages across multiple ecosystems.
- **osv.dev**: osv.dev is an open source vulnerability database and service. It provides detailed information about security issues in open source packages across various ecosystems. Developers can search for vulnerabilities by package, version, or ecosystem, helping them identify and address security risks in their dependencies.
- **GitHub Advisory Database**: GitHub maintains a database of security advisories for open source projects. Vulnerabilities here have unique GitHub Security Advisory (GHSA) IDs, and often reference CVEs as well.

Apart from these, every language and package ecosystem maintains their own vulnerability indices with unique IDs. These platforms help developers stay informed about vulnerabilities in the libraries and dependencies they use, sometimes providing more timely or ecosystem-specific information than CVE alone.

## Scan your project with a SCA tool

There are a lot of scanners out there. You may learn about them and use them at your will. For the sake of explanation we will use Safedep Vet, which has an open source version that's free to use.

### Scanning with Vet

To simply get started use this command from your project's root folder. Use the lab's docker image for convenience.

```bash
docker run --rm -v $(pwd):/src ghcr.io/navhits/vet:latest scan -D /src
```

If you prefer to install vet, you may follow this [docs](https://docs.safedep.io/quickstart).

Learn more about vet - <https://safedep.io>
