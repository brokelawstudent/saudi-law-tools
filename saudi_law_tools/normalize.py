"""Conservative normalization helpers for Arabic legal text."""

from __future__ import annotations

import re
import unicodedata

from .numbers import DIGIT_TRANSLATION


def normalize_digits(text: str) -> str:
    """Convert Arabic-Indic and Eastern Arabic numerals to ASCII digits."""

    return text.translate(DIGIT_TRANSLATION)


def normalize_arabic_text(
    text: str,
    *,
    normalize_numbers: bool = True,
    remove_tatweel: bool = True,
) -> str:
    """Conservatively normalize Arabic legal text while preserving line breaks."""

    text = unicodedata.normalize("NFC", text)

    if remove_tatweel:
        text = text.replace("ـ", "")
    if normalize_numbers:
        text = normalize_digits(text)

    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    return text.strip()
