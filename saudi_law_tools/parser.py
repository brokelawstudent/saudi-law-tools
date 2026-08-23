import re


ARABIC_INDIC_TO_ASCII = str.maketrans(
    "٠١٢٣٤٥٦٧٨٩",
    "0123456789",
)

ARABIC_ORDINALS = {
    "الأولى": 1,
    "الثانية": 2,
    "الثالثة": 3,
    "الرابعة": 4,
    "الخامسة": 5,
    "السادسة": 6,
    "السابعة": 7,
    "الثامنة": 8,
    "التاسعة": 9,
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
    "العشرون": 20,
}


ordinal_pattern = "|".join(
    sorted(
        (re.escape(name) for name in ARABIC_ORDINALS),
        key=len,
        reverse=True,
    )
)


ARTICLE_PATTERN = re.compile(
    rf"^\s*المادة\s+(?:\(\s*)?"
    rf"(?P<label>{ordinal_pattern}|\d+|[٠-٩]+)"
    rf"(?:\s*\))?\s*[:：]?\s*(?P<body>.*)\s*$"
)


def parse_article(text: str) -> dict:
    """
    Parse a Saudi Arabic legal article heading.

    Supported examples:
        المادة الخامسة: ...
        المادة الخامسة عشرة: ...
        المادة 15: ...
        المادة ١٥: ...
        المادة (١٥): ...
    """

    stripped_text = text.strip()
    match = ARTICLE_PATTERN.match(stripped_text)

    if not match:
        return {
            "article_number": None,
            "text": stripped_text,
            "language": "ar",
        }

    label = match.group("label").strip()
    article_text = match.group("body").strip()

    if label in ARABIC_ORDINALS:
        article_number = ARABIC_ORDINALS[label]
    else:
        article_number = int(
            label.translate(ARABIC_INDIC_TO_ASCII)
        )

    return {
        "article_number": article_number,
        "text": article_text,
        "language": "ar",
    }


if __name__ == "__main__":
    examples = [
        "المادة الخامسة: يجب على الشركة الالتزام بالنظام.",
        "المادة الخامسة عشرة: نص المادة.",
        "المادة 15: نص المادة.",
        "المادة ١٥: نص المادة.",
        "المادة (١٥): نص المادة.",
    ]

    for example in examples:
        print(parse_article(example))
