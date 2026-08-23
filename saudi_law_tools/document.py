from .parser import parse_article
from .structure import parse_heading


def parse_document(text: str) -> list[dict]:
    """
    Parse a multi-line Saudi legal document into structured elements.

    Recognizes:
    - Parts (الباب)
    - Chapters (الفصل)
    - Articles (المادة)
    - Multi-line article bodies
    - Other standalone text
    """

    elements = []
    current_article = None

    def save_current_article():
        nonlocal current_article

        if current_article is not None:
            current_article["text"] = current_article["text"].strip()
            elements.append(current_article)
            current_article = None

    for raw_line in text.splitlines():
        line = raw_line.strip()

        if not line:
            continue

        # Check for a structural heading such as الباب or الفصل.
        heading = parse_heading(line)

        if heading["type"] is not None:
            save_current_article()

            elements.append(
                {
                    "element": "heading",
                    **heading,
                }
            )
            continue

        # Check whether this line begins a new article.
        article = parse_article(line)

        if article["article_number"] is not None:
            save_current_article()

            current_article = {
                "element": "article",
                **article,
            }
            continue

        # If an article is currently open, treat this line
        # as a continuation of that article.
        if current_article is not None:
            if current_article["text"]:
                current_article["text"] += "\n" + line
            else:
                current_article["text"] = line

            continue

        # Otherwise preserve the line as standalone text.
        elements.append(
            {
                "element": "text",
                "text": line,
                "language": "ar",
            }
        )

    save_current_article()

    return elements
