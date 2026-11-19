import pytest

from fretboard.notes import note_name, parse_note


@pytest.mark.parametrize(
    "name, expected",
    [("C", 0), ("c", 0), ("C#", 1), ("Db", 1), ("A", 9), ("Bb", 10), ("B#", 0), ("Cb", 11)],
)
def test_parse_note(name, expected):
    assert parse_note(name) == expected


@pytest.mark.parametrize("name", ["", "H", "C?", "#"])
def test_parse_note_invalid(name):
    with pytest.raises(ValueError):
        parse_note(name)


def test_note_name_wraps():
    assert note_name(9) == "A"
    assert note_name(13) == "C#"
