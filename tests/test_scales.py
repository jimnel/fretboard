import pytest

from fretboard.scales import SCALE_ALIASES, SCALE_INTERVALS, Scale


def test_a_major():
    assert Scale.from_name("A", "major").notes == ("A", "B", "C#", "D", "E", "F#", "G#")


def test_a_minor():
    assert Scale.from_name("a", "minor").notes == ("A", "B", "C", "D", "E", "F", "G")


def test_flat_root():
    assert Scale.from_name("Bb", "major_pentatonic").notes == ("A#", "C", "D", "F", "G")


def test_unknown_scale():
    with pytest.raises(ValueError):
        Scale.from_name("A", "lydian_dominant_whatever")


@pytest.mark.parametrize("name, intervals", list(SCALE_INTERVALS.items()))
def test_intervals_well_formed(name, intervals):
    assert intervals[0] == 0
    assert list(intervals) == sorted(set(intervals))
    assert intervals[-1] < 12


@pytest.mark.parametrize(
    "root, name, expected",
    [
        ("D", "dorian", "D E F G A B C"),
        ("E", "phrygian", "E F G A B C D"),
        ("F", "lydian", "F G A B C D E"),
        ("G", "mixolydian", "G A B C D E F"),
        ("B", "locrian", "B C D E F G A"),
        ("E", "phrygian_dominant", "E F G# A B C D"),
        ("A", "hungarian_minor", "A B C D# E F G#"),
        ("G", "lydian_dominant", "G A B C# D E F"),
        ("G#", "altered", "G# A B C D E F#"),
        ("C", "whole_tone", "C D E F# G# A#"),
        ("C", "diminished_half_whole", "C C# D# E F# G A A#"),
    ],
)
def test_scale_spellings(root, name, expected):
    assert " ".join(Scale.from_name(root, name).notes) == expected


@pytest.mark.parametrize("mode, degree", [("dorian", 1), ("phrygian", 2), ("lydian", 3),
                                          ("mixolydian", 4), ("minor", 5), ("locrian", 6)])
def test_major_modes_are_rotations(mode, degree):
    c_major = Scale.from_name("C", "major")
    mode_root = c_major.notes[degree]
    assert set(Scale.from_name(mode_root, mode).notes) == set(c_major.notes)


@pytest.mark.parametrize("alias, name", [("ionian", "major"), ("aeolian", "minor")])
def test_aliases(alias, name):
    assert Scale.from_name("C", alias) == Scale.from_name("C", name)


def test_aliases_point_to_real_scales():
    assert set(SCALE_ALIASES.values()) <= set(SCALE_INTERVALS)
    assert not set(SCALE_ALIASES) & set(SCALE_INTERVALS)
