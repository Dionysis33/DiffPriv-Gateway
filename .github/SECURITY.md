# Security Policy for DiffPriv-Gateway 

## Overview
As an open-source privacy middleware designed for SME data analytics, the security and integrity of **DiffPriv-Gateway** are our top priorities. This policy outlines how we handle security vulnerabilities and which versions are currently supported with security updates.

## Supported Versions
We currently provide security support for the following versions of the project:

| Version | Supported          | Python Version |
| ------- | ------------------ | -------------- |
| 1.0.x   | :white_check_mark: | 3.12+ |
| < 1.0.0 | :x:                | < 3.12         |

## Reporting a Vulnerability
We strongly encourage users and researchers to report any potential security vulnerabilities, especially those related to:
* **Privacy Leaks**: Flaws in the Laplacian mechanism or epsilon budget tracking.
* **Data Handling**: Insecure parsing of CSV datasets.
* **Dependency Risks**: Vulnerabilities in core libraries like `diffprivlib` or `pandas`.

**Please follow these steps to report a vulnerability:**
1. **Email**: Send a detailed report to **[Your-Email-Here]** (or the project lead, Dionysis33).
2. **Details**: Include a description of the vulnerability, a proof of concept (PoC), and the potential impact on SME data privacy.
3. **Disclosure**: We follow a responsible disclosure policy. Please do not report security vulnerabilities via public GitHub Issues.

### Our Response Process
* **Acknowledgment**: You will receive an acknowledgment of your report within **48 hours**.
* **Investigation**: Our team (Dionysis33 & Athina34) will prioritize the fix based on the severity.
* **Resolution**: Once a fix is verified, we will release a security advisory and credit the researcher (if desired).

## Ethical Considerations
Since this project implements **Differential Privacy** for **GDPR compliance**, we treat all "privacy budget" overflows or mathematical weaknesses as critical security bugs.

---
*Last updated: February 28, 2026*
