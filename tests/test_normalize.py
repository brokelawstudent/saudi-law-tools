from saudi_law_tools import normalize_arabic_text, normalize_digits


def test_normalize_both_arabic_digit_sets():
    assert normalize_digits("١٥ و ۲۰") == "15 و 20"


def test_normalize_text_preserves_document_lines():
    source = "المــــادة   ١٥ :  \n  نص المادة.\n\n  الفصل ۲"

    assert normalize_arabic_text(source) == "المادة 15 :\nنص المادة.\n\nالفصل 2"


def test_normalization_options():
    source = "المــــادة ١٥"

    assert (
        normalize_arabic_text(source, normalize_numbers=False, remove_tatweel=False)
        == source
    )
