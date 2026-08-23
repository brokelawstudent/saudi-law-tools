from saudi_law_tools import normalize_arabic_text, normalize_digits


def test_arabic_indic_digits():
    assert normalize_digits("المادة ١٥") == "المادة 15"


def test_eastern_arabic_digits():
    assert normalize_digits("المادة ۲۰") == "المادة 20"


def test_remove_tatweel():
    text = "المــــادة الخامسة"

    result = normalize_arabic_text(text)

    assert result == "المادة الخامسة"


def test_repeated_spaces():
    text = "المادة     الخامسة:    نص المادة."

    result = normalize_arabic_text(text)

    assert result == "المادة الخامسة: نص المادة."


def test_preserve_line_breaks():
    text = """
المادة الأولى:   
   نص المادة الأولى.

المادة الثانية:
   نص المادة الثانية.
"""

    result = normalize_arabic_text(text)

    assert result == (
        "المادة الأولى:\n"
        "نص المادة الأولى.\n\n"
        "المادة الثانية:\n"
        "نص المادة الثانية."
    )


def test_disable_number_normalization():
    text = "المادة ١٥"

    result = normalize_arabic_text(
        text,
        normalize_numbers=False,
    )

    assert result == "المادة ١٥"


def test_disable_tatweel_removal():
    text = "المــــادة"

    result = normalize_arabic_text(
        text,
        remove_tatweel=False,
    )

    assert result == "المــــادة"
