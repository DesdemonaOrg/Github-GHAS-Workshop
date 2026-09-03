# Security Policy

## Supported Versions

We currently support the latest version of this application.

| Version        | Supported |
| -------------- | --------- |
| Latest         | ✅         |
| Older versions | ❌         |

## Reporting a Security Vulnerability

If you discover a security vulnerability, please **do not create a public GitHub issue**.

Instead, report the vulnerability privately through the repository's security reporting mechanism.

When reporting a vulnerability, please provide:

* Description of the vulnerability
* Steps to reproduce
* Affected component or file
* Potential security impact
* Suggested remediation, if known
* Any proof-of-concept code, if applicable

We will review the report and work with the reporter to validate and remediate the issue.

## Security Response Process

Security reports are handled using the following process:

1. **Report** – Vulnerability is reported privately.
2. **Triage** – The security team validates and assesses the vulnerability.
3. **Classification** – Severity and priority are determined.
4. **Remediation** – A fix is developed and tested.
5. **Verification** – The fix is validated through security testing.
6. **Release** – The remediation is deployed through the normal SDLC process.
7. **Closure** – The security issue is documented and closed.

## Severity

Security issues are prioritized based on their potential impact and exploitability.

| Severity | Example                                          | Target Response |
| -------- | ------------------------------------------------ | --------------- |
| Critical | Remote code execution, credential compromise     | Immediate       |
| High     | Authentication bypass, significant data exposure | Urgent          |
| Medium   | Limited data exposure, privilege weakness        | Planned         |
| Low      | Minor security weakness                          | Normal backlog  |

## Security Controls

This repository uses security controls throughout the software development lifecycle, including:

* Dependency scanning
* Dependabot
* Dependency graph
* CodeQL code scanning
* Secret scanning
* Push protection
* Security advisories
* Pull request security checks
* Branch and tag protection/rulesets
* Code review
* Automated CI/CD security checks

## Secret Management

Secrets, credentials, API keys, tokens, certificates, and connection strings must not be committed to the repository.

Use approved secret-management mechanisms such as:

* GitHub Actions secrets
* Organization-level secrets
* Environment secrets
* Azure Key Vault or an equivalent enterprise secret-management service

If a secret is accidentally committed:

1. Revoke or rotate the secret immediately.
2. Investigate potential exposure.
3. Remove the secret from the source code.
4. Review GitHub secret-scanning alerts.
5. Remediate the affected application or infrastructure.

Removing a secret from the latest commit does **not** necessarily mean the secret is no longer exposed.

## Dependency Security

Third-party dependencies must be kept up to date.

Security vulnerabilities identified through Dependabot or other security tools should be reviewed and remediated according to their severity and organizational SLA.

Developers should avoid introducing dependencies that are:

* Unmaintained
* Known to contain critical vulnerabilities
* Incompatible with organizational security requirements
* From untrusted sources

## Code Security

Code changes should be analyzed using automated security scanning where applicable.

CodeQL findings must be reviewed before merging code into protected branches.

Security findings should not be suppressed without appropriate justification and review.

## Security Exceptions

A security finding may only be accepted or suppressed when:

* The finding has been reviewed.
* The business or technical justification is documented.
* The risk is understood.
* An owner is identified.
* An expiration or review date is established where appropriate.

## Disclosure

Please avoid publicly disclosing vulnerability details before the issue has been assessed and remediated.

We appreciate responsible disclosure and cooperation from security researchers and contributors.

## Contact

For security-related questions or vulnerability reports, use the repository's private security reporting process or contact the organization's designated security team.
