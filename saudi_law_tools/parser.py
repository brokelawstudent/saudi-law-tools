"""Parsers for numbered Saudi legal provisions."""

from __future__ import annotations

import re

from .numbers import DIGIT_TRANSLATION, FEMININE_ORDINALS, parse_number_label

# Kept as public compatibility aliases for users of version 0.1.x.
ARABIC_INDIC_TO_ASCII = DIGIT_TRANSLATION
ARABIC_ORDINALS = FEMININE_ORDINALS

_ordinal_pattern = "|".join(
    sorted((re.escape(name) for name in FEMININE_ORDINALS), key=len, reverse=True)
)

ARTICLE_PATTERN = re.compile(
    rf"^\s*الماد(?:ة|ه)\s+(?:[\(（]\s*)?"
    rf"(?P<label>{_ordinal_pattern}|\d+|[٠-٩۰-۹]+)"
    rf"(?:\s*[\)）])?\s*[:：\-–—]?\s*(?P<body>.*)\s*$"
)

_ARTICLE_WITH_SEPARATOR = re.compile(
    r"^\s*الماد(?:ة|ه)\s+(?:[\(（]\s*)?"
    r"(?P<label>.+?)(?:\s*[\)）])?\s*[:：\-–—]\s*(?P<body>.*)\s*$"
)


def parse_article(text: str) -> dict:
    """Parse a numbered Arabic legal article heading.

    Written feminine ordinals from 1 through 99 are supported, together with
    Western, Arabic-Indic, and Eastern Arabic digits.
    """

    stripped_text = text.strip()
    match = _ARTICLE_WITH_SEPARATOR.match(stripped_text) or ARTICLE_PATTERN.match(
        stripped_text
    )

    if not match:
        return {
            "article_number": None,
            "text": stripped_text,
            "language": "ar",
        }

    label = match.group("label").strip(" \t()（）")
    article_number = parse_number_label(label, gender="feminine")

    if article_number is None:
        return {
            "article_number": None,
            "text": stripped_text,
            "language": "ar",
        }

    return {
        "article_number": article_number,
        "text": match.group("body").strip(),
        "language": "ar",
    }
