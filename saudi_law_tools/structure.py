"""Parsers for structural headings in Arabic legal documents."""

from __future__ import annotations

import re

from .numbers import MASCULINE_ORDINALS, parse_number_label

ARABIC_MASCULINE_ORDINALS = MASCULINE_ORDINALS

HEADING_TYPES = {
    "الكتاب": "book",
    "الباب": "part",
    "القسم": "section",
    "الفصل": "chapter",
    "الفرع": "branch",
}

_ordinal_pattern = "|".join(
    sorted((re.escape(name) for name in MASCULINE_ORDINALS), key=len, reverse=True)
)
_kind_pattern = "|".join(re.escape(name) for name in HEADING_TYPES)

HEADING_PATTERN = re.compile(
    rf"^\s*(?P<kind>{_kind_pattern})\s+"
    rf"(?:[\(（]\s*)?"
    rf"(?P<label>{_ordinal_pattern}|\d+|[٠-٩۰-۹]+)"
    rf"(?:\s*[\)）])?"
    rf"\s*[:：\-–—]?\s*(?P<title>.*)\s*$"
)

_HEADING_WITH_SEPARATOR = re.compile(
    rf"^\s*(?P<kind>{_kind_pattern})\s+(?:[\(（]\s*)?"
    rf"(?P<label>.+?)(?:\s*[\)）])?\s*[:：\-–—]\s*(?P<title>.*)\s*$"
)


def parse_heading(text: str) -> dict:
    """Parse a book, part, section, chapter, or branch heading."""

    stripped_text = text.strip()
    match = _HEADING_WITH_SEPARATOR.match(stripped_text) or HEADING_PATTERN.match(
        stripped_text
    )

    if not match:
        return {
            "type": None,
            "number": None,
            "title": stripped_text,
            "language": "ar",
        }

    number = parse_number_label(
        match.group("label").strip(" \t()（）"), gender="masculine"
    )
    if number is None:
        return {
            "type": None,
            "number": None,
            "title": stripped_text,
            "language": "ar",
        }

    return {
        "type": HEADING_TYPES[match.group("kind")],
        "number": number,
        "title": match.group("title").strip(),
        "language": "ar",
    }
