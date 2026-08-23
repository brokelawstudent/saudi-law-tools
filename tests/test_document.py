from saudi_law_tools import parse_document


def test_complete_document():
    text = """
الباب الأول: تأسيس الشركة
الفصل الأول: أحكام عامة
المادة الأولى: تؤسس الشركة وفقاً لأحكام النظام.
المادة الثانية: يكون مقر الشركة في المملكة العربية السعودية.
"""

    result = parse_document(text)

    assert len(result) == 4

    assert result[0]["element"] == "heading"
    assert result[0]["type"] == "part"
    assert result[0]["number"] == 1
    assert result[0]["title"] == "تأسيس الشركة"

    assert result[1]["element"] == "heading"
    assert result[1]["type"] == "chapter"
    assert result[1]["number"] == 1
    assert result[1]["title"] == "أحكام عامة"

    assert result[2]["element"] == "article"
    assert result[2]["article_number"] == 1
    assert result[2]["text"] == "تؤسس الشركة وفقاً لأحكام النظام."

    assert result[3]["element"] == "article"
    assert result[3]["article_number"] == 2
    assert result[3]["text"] == "يكون مقر الشركة في المملكة العربية السعودية."


def test_document_with_numeric_articles():
    text = """
الفصل ٥: أحكام خاصة
المادة 15: نص المادة الخامسة عشرة.
المادة ١٦: نص المادة السادسة عشرة.
"""

    result = parse_document(text)

    assert len(result) == 3
    assert result[0]["number"] == 5
    assert result[1]["article_number"] == 15
    assert result[2]["article_number"] == 16


def test_unstructured_text_is_preserved():
    text = """
مقدمة النظام
المادة الأولى: نص المادة.
"""

    result = parse_document(text)

    assert result[0]["element"] == "text"
    assert result[0]["text"] == "مقدمة النظام"

    assert result[1]["element"] == "article"
    assert result[1]["article_number"] == 1


def test_blank_lines_are_ignored():
    text = """

المادة الأولى: نص المادة.


المادة الثانية: نص آخر.

"""

    result = parse_document(text)

    assert len(result) == 2
