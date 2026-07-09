# Security Policy

## Overview

DiffPriv-Gateway is an open-source Python differential privacy middleware prototype for SME analytics. Because the project deals with privacy-preserving analytical outputs, security reports may include both conventional software vulnerabilities and privacy-specific weaknesses.

This project reduces disclosure risk for analytical outputs, but it does not remove the need for proper governance, consent, access control, legal review, or production security controls.

DiffPriv-Gateway is a technical and educational privacy-engineering project. It is not legal advice and does not guarantee GDPR compliance by itself.

## Supported Branches and Versions

| Branch / Version | Supported |
| --- | --- |
| main | Yes, current maintained branch |
| older snapshots / forks | No official support |

## Reporting a Vulnerability

Please do not open public GitHub issues for security or privacy vulnerabilities.

Send vulnerability reports privately to:

Security contact: Please use GitHub private vulnerability reporting if enabled, or contact the maintainer through the GitHub profile linked to this repository.

Do not include exploit details, sensitive data, or private credentials in public discussions, commits, pull requests, or issues.

## What to Report

Please report issues such as:

- Privacy leaks in protected outputs.
- Incorrect differential privacy mechanism behavior.
- Privacy budget misuse or unsafe parameter handling.
- Unsafe data handling.
- Dependency vulnerabilities.
- Insecure defaults.
- Accidental exposure of sensitive data.
- Any behavior that could materially increase re-identification or disclosure risk.

## What to Include

A helpful report should contain:

- A clear description of the issue.
- Steps to reproduce the problem.
- The affected file, module, or workflow.
- The expected and actual behavior.
- The potential security or privacy impact.
- A proof of concept, if it is safe to share privately.
- A suggested mitigation, if known.

Please avoid sending real personal data. Use synthetic or minimal demonstration data whenever possible.

## Response Timeline

When possible, maintainers aim to:

1. Acknowledge the report within 48 hours.
2. Triage and investigate the issue.
3. Prepare a fix or mitigation when appropriate.
4. Coordinate responsible disclosure when public communication is appropriate.

If investigation takes longer, maintainers may provide status updates as practical.

## Responsible Disclosure

Please give maintainers reasonable time to investigate and address reported issues before public disclosure. Do not publish exploit details or use the issue to access, modify, extract, or expose data that you do not own or have permission to test.

Responsible disclosure helps protect users, contributors, and downstream readers of the project.

## Privacy-Specific Note

Differential privacy can reduce disclosure risk for analytical outputs, but it is only one part of a broader privacy and security program. Any real deployment would still require governance, lawful basis and consent review where applicable, access control, secure infrastructure, monitoring, incident response, and legal review.

## Last Updated

July 2026
