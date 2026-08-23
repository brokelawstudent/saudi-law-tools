import pytest

from saudi_law_tools import parse_article


@pytest.mark.parametrize(
    ("source", "number"),
    [
        ("المادة الخامسة: نص المادة.", 5),
        ("المادة الخامسة عشرة: نص المادة.", 15),
        ("المادة الحادية والعشرون: نص المادة.", 21),
        ("المادة الثانية و الثلاثون: نص المادة.", 32),
        ("المادة التاسعة والتسعون: نص المادة.", 99),
        ("المادة 125: نص المادة.", 125),
        ("المادة ١٥: نص المادة.", 15),
        ("المادة ۲۵: نص المادة.", 25),
        ("المادة （١٥）： نص المادة.", 15),
    ],
)
def test_supported_article_numbers(source, number):
    result = parse_article(source)

    assert result == {
        "article_number": number,
        "text": "نص المادة.",
        "language": "ar",
    }


def test_article_accepts_diacritics_and_tatweel():
    result = parse_article("المادة الْخَامِسَة: نص المادة.")

    assert result["article_number"] == 5


def test_unrecognized_text_is_preserved():
    text = "هذا نص قانوني بدون رقم مادة."

    assert parse_article(text) == {
        "article_number": None,
        "text": text,
        "language": "ar",
    }
