"""Whole-document parsing for Saudi legal and regulatory text."""

from __future__ import annotations

from .parser import parse_article
from .structure import parse_heading


def parse_document(text: str) -> list[dict]:
    """Parse a multi-line legal document into headings, articles, and text.

    Article bodies may span multiple lines. A recognized structural heading
    closes the preceding article, while unstructured content outside an article
    is retained instead of discarded.
    """

    elements: list[dict] = []
    current_article: dict | None = None

    def save_current_article() -> None:
        nonlocal current_article
        if current_article is not None:
            current_article["text"] = current_article["text"].strip()
            elements.append(current_article)
            current_article = None

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        heading = parse_heading(line)
        if heading["type"] is not None:
            save_current_article()
            elements.append({"element": "heading", **heading})
            continue

        article = parse_article(line)
        if article["article_number"] is not None:
            save_current_article()
            current_article = {"element": "article", **article}
            continue

        if current_article is not None:
            separator = "\n" if current_article["text"] else ""
            current_article["text"] += separator + line
            continue

        elements.append({"element": "text", "text": line, "language": "ar"})

    save_current_article()
    return elements
