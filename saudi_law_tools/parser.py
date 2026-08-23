import re


def parse_article(text: str) -> dict:
    """
    Parse a simple Saudi legal article heading and return
    structured information.

    Example:
        المادة الخامسة: يجب على الشركة الالتزام بالنظام.
    """

    arabic_numbers = {
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
    }

    pattern = r"المادة\s+([^\s:]+)\s*[:：]?\s*(.*)"
    match = re.match(pattern, text.strip())

    if not match:
        return {
            "article_number": None,
            "text": text.strip(),
            "language": "ar",
        }

    article_word = match.group(1)
    article_text = match.group(2).strip()

    return {
        "article_number": arabic_numbers.get(article_word),
        "text": article_text,
        "language": "ar",
    }


if __name__ == "__main__":
    example = "المادة الخامسة: يجب على الشركة الالتزام بالنظام."
    print(parse_article(example))
