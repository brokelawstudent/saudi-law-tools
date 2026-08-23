# Saudi Law Tools

[![Tests](https://github.com/brokelawstudent/saudi-law-tools/actions/workflows/tests.yml/badge.svg)](https://github.com/brokelawstudent/saudi-law-tools/actions/workflows/tests.yml)
[![PyPI](https://img.shields.io/pypi/v/saudi-law-tools.svg)](https://pypi.org/project/saudi-law-tools/)
[![Python](https://img.shields.io/pypi/pyversions/saudi-law-tools.svg)](https://pypi.org/project/saudi-law-tools/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Dependency-free Python tools for turning Saudi Arabian legal and regulatory text into data that applications can use.

Saudi Law Tools is designed for developers, researchers, students, and legal-tech projects working with Arabic legal documents. It preserves source text, exposes a small Python API, and includes a command-line interface for file and pipeline use.

> [!IMPORTANT]
> This project processes text; it does not provide legal advice or determine the legal meaning, validity, or current status of a document.

## Install

```bash
python -m pip install saudi-law-tools
```

The package supports Python 3.10 and newer and has no runtime dependencies.

## Quick start

### Parse an article

```python
from saudi_law_tools import parse_article

result = parse_article("المادة الحادية والعشرون: يجب على الشركة الاحتفاظ بالسجلات.")
```

```python
{
    "article_number": 21,
    "text": "يجب على الشركة الاحتفاظ بالسجلات.",
    "language": "ar",
}
```

Article numbers may use written Arabic ordinals from 1 through 99, Western digits (`21`), Arabic-Indic digits (`٢١`), or Eastern Arabic digits (`۲۱`). Parentheses, common separators, and diacritics are supported.

### Parse a complete document

```python
from saudi_law_tools import parse_document

text = """
الباب الأول: تأسيس الشركة
الفصل الأول: أحكام عامة
المادة الأولى:
تؤسس الشركة وفقاً لأحكام النظام.
ويكون مقرها الرئيس في مدينة الرياض.
"""

elements = parse_document(text)
```

The document parser recognizes `الكتاب`, `الباب`, `القسم`, `الفصل`, and `الفرع`, keeps multi-line article bodies together, and preserves unstructured text instead of silently dropping it.

### Normalize Arabic text

```python
from saudi_law_tools import normalize_arabic_text

normalized = normalize_arabic_text("المــــادة   ١٥ :   أحكام الشركة")
# "المادة 15 : أحكام الشركة"
```

Normalization is conservative: it applies Unicode NFC, converts both common Arabic digit sets, removes tatweel, collapses horizontal whitespace, and preserves line breaks. Each behavior can be disabled where exposed by the API or CLI.

## Command line

Parse a UTF-8 document into JSON:

```bash
saudi-law-tools parse regulation.txt -o regulation.json
```

Normalize a document:

```bash
saudi-law-tools normalize regulation.txt -o normalized.txt
```

Both commands accept `-` or no filename to read from standard input, making them suitable for Unix pipelines:

```bash
printf 'المادة ١٥: نص المادة.' | saudi-law-tools parse --compact
```

Run `saudi-law-tools --help` for all options. The CLI is also available as `python -m saudi_law_tools`.

## Public API

| Function | Purpose |
| --- | --- |
| `parse_article(text)` | Parse one numbered article heading and its inline body |
| `parse_heading(text)` | Parse a book, part, section, chapter, or branch heading |
| `parse_document(text)` | Convert a multi-line document into ordered structured elements |
| `normalize_digits(text)` | Convert Arabic-Indic and Eastern Arabic digits to `0-9` |
| `normalize_arabic_text(text, ...)` | Conservatively normalize Arabic legal text |

All parsing functions return ordinary Python dictionaries and lists, so their output can be serialized directly as JSON.

## Scope and limitations

This is an early-stage parser, not a complete Saudi legal-document model. Layouts vary between official sources and historical documents. Scanned PDFs require OCR before this package can process their text, and legal meaning must always be checked against an authoritative source.

If a real-world heading is not recognized, please open a bug report containing the smallest non-confidential example that reproduces it.

## Development

```bash
git clone https://github.com/brokelawstudent/saudi-law-tools.git
cd saudi-law-tools
python -m pip install -e '.[dev]'
python -m pytest -q
python -m build
```

Tests run on every push and pull request across supported Python versions. See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidance and [CHANGELOG.md](CHANGELOG.md) for release notes.

## Roadmap

- Extract paragraph and list-item structure inside articles
- Detect internal article references
- Add source-aware fixtures for common official-document layouts
- Export document trees as well as flat ordered elements
- Expand property-based and corpus testing

## License

MIT. See [LICENSE](LICENSE).

