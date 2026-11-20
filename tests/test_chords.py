import pytest

from fretboard.chords import Chord


def test_from_name():
    chord = Chord.from_name("A", "min")
    assert chord.notes == ("A", "C", "E")
    assert chord.name == "A min"


@pytest.mark.parametrize(
    "notes, expected",
    [
        (["C", "E", "G"], "C maj"),
        (["a", "c", "e"], "A min"),
        ([7, 11, 2, 5], "G 7"),
        (["B", "D", "F", "A"], "B m7b5"),
        (["C", "G", "E", "C"], "C maj"),  # order and doubling don't matter
    ],
)
def test_from_notes_identifies_quality(notes, expected):
    assert Chord.from_notes(notes).name == expected


def test_unknown_quality():
    chord = Chord.from_notes(["C", "D", "E"])
    assert chord.quality is None
    assert chord.name == "C (C D E)"


def test_from_notes_empty():
    with pytest.raises(ValueError):
        Chord.from_notes([])


def test_from_name_unknown():
    with pytest.raises(ValueError):
        Chord.from_name("C", "nope")


def test_len():
    assert len(Chord.from_name("C", "maj7")) == 4
