import pytest

from saudi_law_tools import parse_heading


@pytest.mark.parametrize(
    ("source", "heading_type", "number", "title"),
    [
        ("الكتاب الأول: الأحكام التمهيدية", "book", 1, "الأحكام التمهيدية"),
        ("الباب الثاني: الشركات", "part", 2, "الشركات"),
        ("القسم الثالث: الإدارة", "section", 3, "الإدارة"),
        ("الفصل الحادي والعشرون: أحكام خاصة", "chapter", 21, "أحكام خاصة"),
        ("الفرع ۵: أحكام عامة", "branch", 5, "أحكام عامة"),
        ("الفصل (12): أحكام ختامية", "chapter", 12, "أحكام ختامية"),
    ],
)
def test_supported_headings(source, heading_type, number, title):
    result = parse_heading(source)

    assert result == {
        "type": heading_type,
        "number": number,
        "title": title,
        "language": "ar",
    }


def test_unrecognized_heading_is_preserved():
    text = "أحكام عامة"

    assert parse_heading(text) == {
        "type": None,
        "number": None,
        "title": text,
        "language": "ar",
    }
