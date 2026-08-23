from saudi_law_tools import parse_document


def test_complete_document_with_extended_structure():
    text = """
الكتاب الأول: أحكام الشركات
الباب الأول: التأسيس
القسم الأول: أحكام عامة
الفصل الأول: التأسيس
الفرع الأول: المتطلبات
المادة الحادية والعشرون:
تؤسس الشركة وفقاً لأحكام النظام.
ويكون مقرها الرئيس في مدينة الرياض.
المادة ۲۲: تحدد أغراض الشركة في نظامها الأساس.
"""

    result = parse_document(text)

    assert [item["element"] for item in result] == [
        "heading",
        "heading",
        "heading",
        "heading",
        "heading",
        "article",
        "article",
    ]
    assert [item["type"] for item in result[:5]] == [
        "book",
        "part",
        "section",
        "chapter",
        "branch",
    ]
    assert result[5]["article_number"] == 21
    assert result[5]["text"] == (
        "تؤسس الشركة وفقاً لأحكام النظام.\nويكون مقرها الرئيس في مدينة الرياض."
    )
    assert result[6]["article_number"] == 22


def test_heading_closes_current_article():
    result = parse_document(
        "المادة الأولى:\nنص المادة.\nالفصل الثاني: الإدارة\nالمادة الثانية: نص آخر."
    )

    assert len(result) == 3
    assert result[0]["text"] == "نص المادة."
    assert result[1]["type"] == "chapter"
    assert result[2]["article_number"] == 2


def test_unstructured_text_is_preserved():
    result = parse_document("مقدمة النظام\nالمادة الأولى: نص المادة.")

    assert result[0] == {
        "element": "text",
        "text": "مقدمة النظام",
        "language": "ar",
    }
    assert result[1]["article_number"] == 1
