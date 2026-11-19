import pytest

from fretboard.scales import Scale


def test_a_major():
    assert Scale.from_name("A", "major").notes == ("A", "B", "C#", "D", "E", "F#", "G#")


def test_a_minor():
    assert Scale.from_name("a", "minor").notes == ("A", "B", "C", "D", "E", "F", "G")


def test_flat_root():
    assert Scale.from_name("Bb", "major_pentatonic").notes == ("A#", "C", "D", "F", "G")


def test_unknown_scale():
    with pytest.raises(ValueError):
        Scale.from_name("A", "lydian_dominant_whatever")
