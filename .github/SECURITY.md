# Security Policy for DiffPriv-Gateway

## Overview

DiffPriv-Gateway is an open-source privacy-preserving middleware intended to support safer data analytics for SMEs. Because the project is built around Differential Privacy and privacy-aware data processing, both security vulnerabilities and privacy weaknesses are treated as high-priority issues.

This document explains how to report vulnerabilities and which versions are currently supported with security updates.

---

## Supported Versions

We currently provide security support for the following project versions:

| Version | Supported | Python Version |
|---------|-----------|----------------|
| 1.0.x   | ✅ Yes    | 3.12+          |
| < 1.0.0 | ❌ No     | < 3.12         |

> If you have not published formal releases yet, replace the table above with the currently maintained branch/version.

---

## What Should Be Reported

Please report any vulnerability related to:

- **Privacy leaks**  
  Weaknesses in the Differential Privacy implementation, including incorrect noise application, epsilon misuse, or privacy budget leakage.

- **Data handling issues**  
  Unsafe parsing, insecure file handling, or improper treatment of input datasets such as CSV files.

- **Dependency risks**  
  Known vulnerabilities in project dependencies, including libraries such as `diffprivlib`, `pandas`, or related tooling.

- **Misconfiguration or insecure defaults**  
  Settings or implementation choices that could expose sensitive data or reduce privacy guarantees.

---

## Reporting a Vulnerability

Please report vulnerabilities privately and responsibly.

### Contact

Send your report to: **[replace-with-real-email@example.com]**  
Project lead: **Dionysis33**

### Please include

- A clear description of the issue
- Steps to reproduce it
- A proof of concept (PoC), if available
- The affected file, module, or component
- The potential security or privacy impact
- Any suggested mitigation, if known

### Important

- **Do not report vulnerabilities through public GitHub Issues**
- Please allow us time to investigate and prepare a fix before public disclosure

---

## Our Response Process

We aim to follow this process:

1. **Acknowledgment**  
   We will acknowledge receipt of the report within **48 hours**.

2. **Initial triage**  
   We will assess severity and confirm whether the issue is reproducible.

3. **Investigation and remediation**  
   The maintainers will investigate the issue and prepare an appropriate fix.

4. **Resolution and disclosure**  
   Once resolved, we may publish a security advisory and, if requested, credit the reporter.

If the investigation takes longer than expected, we will provide a status update.

---

## Severity

The following are treated as **critical**:

- Privacy budget overflows
- Incorrect implementation of Differential Privacy guarantees
- Data disclosure through statistical outputs
- Any flaw that could enable re-identification of individuals

---

## Responsible Disclosure

We ask all reporters to follow responsible disclosure practices:

- Report privately
- Do not publish exploit details before a fix is available
- Avoid accessing, modifying, or exfiltrating real user data

---

## Maintainers

Security reports are currently reviewed by:

- **Dionysis33**
- **Athina34**

---

**Last updated:** March 30, 2026
