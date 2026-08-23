# Changelog

All notable changes to Saudi Law Tools are recorded here. The project follows [Semantic Versioning](https://semver.org/).

## Unreleased

## 0.2.0 - 2026-08-24

### Added

- Command-line interface for parsing documents to JSON and normalizing UTF-8 text
- Written Arabic ordinal recognition from 1 through 99
- Eastern Arabic (`۰۱۲۳۴۵۶۷۸۹`) digit support in parsers
- Structural parsing for `الكتاب`, `القسم`, and `الفرع`
- Recognition of common full-width parentheses and separators
- Public version metadata and expanded project documentation
- Issue forms, pull-request guidance, and a security policy

### Changed

- Continuous integration now tests all supported Python minor versions and builds the distribution
- PyPI installation is the primary documented installation method

### Fixed

- Diacritics and tatweel no longer prevent a separated article or heading number from being recognized

## 0.1.0 - 2026-08-23

- Initial public release
- Article, chapter, and part parsing
- Multi-line document parsing
- Arabic digit and tatweel normalization

