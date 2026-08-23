from saudi_law_tools import parse_article


def test_parse_fifth_article():
    text = "المادة الخامسة: يجب على الشركة الالتزام بالنظام."

    result = parse_article(text)

    assert result["article_number"] == 5
    assert result["text"] == "يجب على الشركة الالتزام بالنظام."
    assert result["language"] == "ar"


def test_unrecognized_text():
    text = "هذا نص قانوني بدون رقم مادة."

    result = parse_article(text)

    assert result["article_number"] is None
    assert result["text"] == text
    assert result["language"] == "ar"
