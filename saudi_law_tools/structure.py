import re

from .parser import ARABIC_INDIC_TO_ASCII


ARABIC_MASCULINE_ORDINALS = {
    "الأول": 1,
    "الثاني": 2,
    "الثالث": 3,
    "الرابع": 4,
    "الخامس": 5,
    "السادس": 6,
    "السابع": 7,
    "الثامن": 8,
    "التاسع": 9,
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
    "العشرون": 20,
}


ordinal_pattern = "|".join(
    sorted(
        (re.escape(name) for name in ARABIC_MASCULINE_ORDINALS),
        key=len,
        reverse=True,
    )
)


HEADING_PATTERN = re.compile(
    rf"^\s*(?P<kind>الباب|الفصل)\s+"
    rf"(?:\(\s*)?"
    rf"(?P<label>{ordinal_pattern}|\d+|[٠-٩]+)"
    rf"(?:\s*\))?"
    rf"\s*[:：-]?\s*(?P<title>.*)\s*$"
)


def parse_heading(text: str) -> dict:
    """
    Parse structural headings in Arabic legal documents.

    Examples:
        الباب الأول
        الباب الثاني: الشركات
        الفصل الثالث: إدارة الشركة
        الفصل ٥: أحكام عامة
    """

    stripped_text = text.strip()
    match = HEADING_PATTERN.match(stripped_text)

    if not match:
        return {
            "type": None,
            "number": None,
            "title": stripped_text,
            "language": "ar",
        }

    kind = match.group("kind")
    label = match.group("label").strip()
    title = match.group("title").strip()

    if label in ARABIC_MASCULINE_ORDINALS:
        number = ARABIC_MASCULINE_ORDINALS[label]
    else:
        number = int(
            label.translate(ARABIC_INDIC_TO_ASCII)
        )

    heading_type = "part" if kind == "الباب" else "chapter"

    return {
        "type": heading_type,
        "number": number,
        "title": title,
        "language": "ar",
    }
