from .parser import parse_article
from .structure import parse_heading


def parse_document(text: str) -> list[dict]:
    """
    Parse a multi-line Saudi legal document into structured elements.

    Recognizes:
    - Parts (الباب)
    - Chapters (الفصل)
    - Articles (المادة)
    - Other text
    """

    elements = []

    for line in text.splitlines():
        line = line.strip()

        if not line:
            continue

        heading = parse_heading(line)

        if heading["type"] is not None:
            elements.append(
                {
                    "element": "heading",
                    **heading,
                }
            )
            continue

        article = parse_article(line)

        if article["article_number"] is not None:
            elements.append(
                {
                    "element": "article",
                    **article,
                }
            )
            continue

        elements.append(
            {
                "element": "text",
                "text": line,
                "language": "ar",
            }
        )

    return elements
