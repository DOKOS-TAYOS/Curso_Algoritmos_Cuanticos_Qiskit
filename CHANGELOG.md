# Changelog

## Unreleased

- Updated Pillow from 12.2.0 to 12.3.0 to address known security vulnerabilities reported by `pip-audit`.
- Removed the optional `tqdm` dependency from `requirements.txt` because the repository does not currently import it or use progress bars in code or notebooks.
- Added Dependabot configuration for Python dependencies and GitHub Actions.
- Added a dependency review workflow for pull requests that change dependencies or workflows.
- Added a scheduled `pip-audit` workflow for pinned Python dependencies.
- Added a security policy for reporting issues and avoiding accidental credential commits.
- Expanded ignored local files to reduce the risk of committing secrets or generated artifacts.
- Added `quantum-circuit-drawer` and `ipympl` for interactive Matplotlib circuit figures in notebooks.
