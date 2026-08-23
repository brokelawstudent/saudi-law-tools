from saudi_law_tools import parse_article


def test_written_ordinal():
    result = parse_article(
        "المادة الخامسة: يجب على الشركة الالتزام بالنظام."
    )

    assert result["article_number"] == 5
    assert result["text"] == "يجب على الشركة الالتزام بالنظام."
    assert result["language"] == "ar"


def test_multiword_ordinal():
    result = parse_article(
        "المادة الخامسة عشرة: نص المادة."
    )

    assert result["article_number"] == 15
    assert result["text"] == "نص المادة."


def test_western_number():
    result = parse_article(
        "المادة 15: نص المادة."
    )

    assert result["article_number"] == 15
    assert result["text"] == "نص المادة."


def test_arabic_indic_number():
    result = parse_article(
        "المادة ١٥: نص المادة."
    )

    assert result["article_number"] == 15
    assert result["text"] == "نص المادة."


def test_parenthesized_number():
    result = parse_article(
        "المادة (١٥): نص المادة."
    )

    assert result["article_number"] == 15
    assert result["text"] == "نص المادة."


def test_large_article_number():
    result = parse_article(
        "المادة 125: نص المادة."
    )

    assert result["article_number"] == 125
    assert result["text"] == "نص المادة."


def test_unrecognized_text():
    text = "هذا نص قانوني بدون رقم مادة."

    result = parse_article(text)

    assert result["article_number"] is None
    assert result["text"] == text
    assert result["language"] == "ar"
