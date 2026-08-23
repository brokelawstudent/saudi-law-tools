import re
import unicodedata


DIGIT_TRANSLATION = str.maketrans(
    "٠١٢٣٤٥٦٧٨٩۰۱۲۳۴۵۶۷۸۹",
    "01234567890123456789",
)


def normalize_digits(text: str) -> str:
    """
    Convert Arabic-Indic and Eastern Arabic numerals
    to Western Arabic numerals.

    Examples:
        ١٥ -> 15
        ۲۰ -> 20
    """

    return text.translate(DIGIT_TRANSLATION)


def normalize_arabic_text(
    text: str,
    *,
    normalize_numbers: bool = True,
    remove_tatweel: bool = True,
) -> str:
    """
    Conservatively normalize Arabic legal text.

    The function:
    - Applies Unicode NFC normalization
    - Optionally converts Arabic numerals to 0-9
    - Removes tatweel/kashida characters
    - Collapses repeated spaces and tabs
    - Preserves line breaks
    """

    text = unicodedata.normalize("NFC", text)

    if remove_tatweel:
        text = text.replace("ـ", "")

    if normalize_numbers:
        text = normalize_digits(text)

    # Collapse repeated horizontal whitespace.
    text = re.sub(r"[ \t]+", " ", text)

    # Remove spaces around line breaks while keeping
    # the document's line structure.
    text = re.sub(r" *\n *", "\n", text)

    return text.strip()
