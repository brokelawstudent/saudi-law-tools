"""Utilities for recognizing numbering used in Arabic legal headings."""

from __future__ import annotations

import re

DIGIT_TRANSLATION = str.maketrans(
    "٠١٢٣٤٥٦٧٨٩۰۱۲۳۴۵۶۷۸۹",
    "01234567890123456789",
)

_DIACRITICS = re.compile(r"[\u0610-\u061a\u064b-\u065f\u0670\u06d6-\u06ed]")

_FEMININE_UNITS = {
    "الأولى": 1,
    "الحادية": 1,
    "الثانية": 2,
    "الثالثة": 3,
    "الرابعة": 4,
    "الخامسة": 5,
    "السادسة": 6,
    "السابعة": 7,
    "الثامنة": 8,
    "التاسعة": 9,
}

_MASCULINE_UNITS = {
    "الأول": 1,
    "الحادي": 1,
    "الثاني": 2,
    "الثالث": 3,
    "الرابع": 4,
    "الخامس": 5,
    "السادس": 6,
    "السابع": 7,
    "الثامن": 8,
    "التاسع": 9,
}

_FEMININE_TEENS = {
    "العاشرة": 10,
    "الحادية عشرة": 11,
    "الثانية عشرة": 12,
    "الثالثة عشرة": 13,
    "الرابعة عشرة": 14,
    "الخامسة عشرة": 15,
    "السادسة عشرة": 16,
    "السابعة عشرة": 17,
    "الثامنة عشرة": 18,
    "التاسعة عشرة": 19,
}

_MASCULINE_TEENS = {
    "العاشر": 10,
    "الحادي عشر": 11,
    "الثاني عشر": 12,
    "الثالث عشر": 13,
    "الرابع عشر": 14,
    "الخامس عشر": 15,
    "السادس عشر": 16,
    "السابع عشر": 17,
    "الثامن عشر": 18,
    "التاسع عشر": 19,
}

_TENS = {
    "العشرون": 20,
    "الثلاثون": 30,
    "الأربعون": 40,
    "الخمسون": 50,
    "الستون": 60,
    "السبعون": 70,
    "الثمانون": 80,
    "التسعون": 90,
}


def normalize_number_label(label: str) -> str:
    """Normalize a number label for matching without altering document text."""

    label = _DIACRITICS.sub("", label)
    label = label.replace("ـ", "")
    label = label.replace("أ", "ا").replace("إ", "ا").replace("آ", "ا")
    return re.sub(r"\s+", " ", label).strip()


def _normalized_map(values: dict[str, int]) -> dict[str, int]:
    return {normalize_number_label(key): value for key, value in values.items()}


def ordinal_labels(gender: str) -> dict[str, int]:
    """Return supported written ordinal labels and their integer values (1-99)."""

    if gender not in {"feminine", "masculine"}:
        raise ValueError("gender must be 'feminine' or 'masculine'")

    units = _FEMININE_UNITS if gender == "feminine" else _MASCULINE_UNITS
    teens = _FEMININE_TEENS if gender == "feminine" else _MASCULINE_TEENS
    labels = {**units, **teens, **_TENS}

    compound_units = {
        label: value
        for label, value in units.items()
        if label not in {"الأولى", "الأول"}
    }
    for tens_label, tens_value in _TENS.items():
        for unit_label, unit_value in compound_units.items():
            labels[f"{unit_label} و{tens_label}"] = tens_value + unit_value
            labels[f"{unit_label} و {tens_label}"] = tens_value + unit_value

    # Retain canonical spellings for compatibility while also accepting common
    # alif/hamza variants during normalized lookup.
    return {**labels, **_normalized_map(labels)}


FEMININE_ORDINALS = ordinal_labels("feminine")
MASCULINE_ORDINALS = ordinal_labels("masculine")


def parse_number_label(label: str, *, gender: str) -> int | None:
    """Parse Western, Arabic-Indic, Eastern Arabic, or written ordinals."""

    normalized = normalize_number_label(label)
    digits = normalized.translate(DIGIT_TRANSLATION)

    if digits.isdecimal():
        return int(digits)

    values = FEMININE_ORDINALS if gender == "feminine" else MASCULINE_ORDINALS
    return values.get(normalized)
