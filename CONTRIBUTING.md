# Contributing to Saudi Law Tools

Thank you for helping improve reusable Arabic legal-text infrastructure.

## Good first contributions

- Report an unrecognized article or heading format
- Add a minimal, non-confidential parser fixture
- Improve Arabic text normalization
- Add tests for document structure or CLI behavior
- Clarify documentation for a supported use case

Please do not submit confidential, personal, copyrighted, or access-restricted documents. A short synthetic example that preserves the relevant layout is usually enough to reproduce a parser problem.

## Report a parsing bug

Include:

1. The smallest input that shows the problem
2. The output you received
3. The output you expected
4. The installed package and Python versions

Use the repository's parsing-bug issue form when possible.

## Local setup

```bash
git clone https://github.com/brokelawstudent/saudi-law-tools.git
cd saudi-law-tools
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
```

On Windows PowerShell, activate the environment with `.venv\\Scripts\\Activate.ps1`.

## Before opening a pull request

```bash
python -m pytest -q
python -m build
```

Keep changes focused, add tests for behavior changes, update the README when the public API changes, and add a short entry under `Unreleased` in the changelog.

## Compatibility

The project supports Python 3.10 and newer. Existing return keys and meanings should remain compatible within a major version. If a breaking change is necessary, explain it clearly in the pull request.

## Legal and source accuracy

Parser support does not establish that a document is authoritative or current. Avoid claims about legal meaning and link to an official source when a contribution depends on a specific published format.

## Security

Do not open a public issue for a suspected vulnerability. Follow [SECURITY.md](SECURITY.md) instead.

