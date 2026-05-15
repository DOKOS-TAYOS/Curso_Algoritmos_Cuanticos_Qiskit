# Security Policy

This repository contains teaching material for a quantum algorithms course. It should not contain private credentials, service tokens, research data with restricted access, or personal information.

## Reporting a Security Issue

If you find a security issue, please open a private security advisory on GitHub if available, or contact the repository owner directly. Avoid posting secrets or exploit details in public issues.

## Good Practices for Contributors

- Do not commit API tokens, IBM Quantum credentials, `.env` files, local notebooks with private outputs, or machine-specific configuration.
- Use a local virtual environment (`.venv`) and install dependencies from `requirements.txt`.
- Keep dependency updates small and review Dependabot pull requests before merging.
- If a secret is committed by mistake, rotate it immediately and remove it from the repository history before sharing the repository further.
