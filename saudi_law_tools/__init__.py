"""Public API for Saudi Law Tools."""

from .document import parse_document
from .normalize import normalize_arabic_text, normalize_digits
from .parser import parse_article
from .structure import parse_heading

__version__ = "0.2.0"

__all__ = [
    "normalize_arabic_text",
    "normalize_digits",
    "parse_article",
    "parse_document",
    "parse_heading",
]
