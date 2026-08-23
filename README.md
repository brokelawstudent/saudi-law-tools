# Saudi Law Tools 🇸🇦⚖️

Open-source Python tools for parsing, normalizing, and structuring Saudi Arabian legal and regulatory text.

## About

Saudi Law Tools is an open-source project designed to make Saudi legal text easier for developers, researchers, students, and legal-tech projects to process programmatically.

The project is currently in its early stages. The first module focuses on identifying Arabic legal article headings and converting them into structured Python data.

## Features

* Parse Arabic legal article headings
* Recognize common Arabic ordinal article numbers
* Extract article numbers and article text
* Return structured data for further processing
* Automated tests with GitHub Actions
* Lightweight and dependency-free core

## Example

```python
from saudi_law_tools import parse_article

text = "المادة الخامسة: يجب على الشركة الالتزام بالنظام."

result = parse_article(text)

print(result)
```

Output:

```python
{
    "article_number": 5,
    "text": "يجب على الشركة الالتزام بالنظام.",
    "language": "ar"
}
```

## Current Support

The parser currently recognizes Arabic ordinal article headings from:

* المادة الأولى
* المادة الثانية
* المادة الثالثة
* المادة الرابعة
* المادة الخامسة
* المادة السادسة
* المادة السابعة
* المادة الثامنة
* المادة التاسعة
* المادة العاشرة

Support for additional numbering formats and more complex Saudi legal document structures is planned.

## Project Goals

Saudi Law Tools aims to gradually provide reusable open-source infrastructure for working with Saudi legal and regulatory documents.

Planned areas of development include:

* Arabic and numeric article-number recognition
* Chapter and section extraction
* Arabic legal-text normalization
* Cross-reference detection
* Structured JSON export
* Regulation comparison tools
* Improved handling of real-world Saudi legal documents

## Development

Clone the repository:

```bash
git clone https://github.com/brokelawstudent/saudi-law-tools.git
cd saudi-law-tools
```

Install the testing dependency:

```bash
python -m pip install pytest
```

Run the tests:

```bash
python -m pytest -q
```

Tests are also automatically run through GitHub Actions whenever changes are pushed or a pull request is opened.

## Contributing

Contributions are welcome.

If you find a parsing case that is not handled correctly, have an idea for a new feature, or want to improve support for Saudi legal documents, feel free to open an issue or submit a pull request.

When reporting parsing problems, providing a short example of the legal-text structure is especially helpful.

## Disclaimer

Saudi Law Tools is a software project for processing legal text. It does not provide legal advice and should not be treated as a substitute for professional legal analysis.

## License

This project is licensed under the MIT License.

