import io
import json

from saudi_law_tools.cli import main


def test_parse_from_stdin_as_json():
    stdout = io.StringIO()

    exit_code = main(
        ["parse", "-"],
        stdin=io.StringIO("المادة الحادية والعشرون: نص المادة."),
        stdout=stdout,
    )

    assert exit_code == 0
    payload = json.loads(stdout.getvalue())
    assert payload[0]["article_number"] == 21


def test_normalize_from_stdin():
    stdout = io.StringIO()

    exit_code = main(
        ["normalize", "-"],
        stdin=io.StringIO("المــــادة ١٥"),
        stdout=stdout,
    )

    assert exit_code == 0
    assert stdout.getvalue() == "المادة 15\n"
