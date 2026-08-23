from saudi_law_tools import parse_heading


def test_part_written_number():
    result = parse_heading("الباب الأول")

    assert result["type"] == "part"
    assert result["number"] == 1
    assert result["title"] == ""
    assert result["language"] == "ar"


def test_part_with_title():
    result = parse_heading("الباب الثاني: الشركات")

    assert result["type"] == "part"
    assert result["number"] == 2
    assert result["title"] == "الشركات"


def test_chapter_written_number():
    result = parse_heading("الفصل الثالث: إدارة الشركة")

    assert result["type"] == "chapter"
    assert result["number"] == 3
    assert result["title"] == "إدارة الشركة"


def test_chapter_arabic_indic_number():
    result = parse_heading("الفصل ٥: أحكام عامة")

    assert result["type"] == "chapter"
    assert result["number"] == 5
    assert result["title"] == "أحكام عامة"


def test_parenthesized_number():
    result = parse_heading("الفصل (12): أحكام ختامية")

    assert result["type"] == "chapter"
    assert result["number"] == 12
    assert result["title"] == "أحكام ختامية"


def test_unrecognized_heading():
    text = "أحكام عامة"

    result = parse_heading(text)

    assert result["type"] is None
    assert result["number"] is None
    assert result["title"] == text
    assert result["language"] == "ar"
