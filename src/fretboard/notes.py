"""Note names and pitch classes.

Notes are represented internally as pitch classes: integers 0-11 with C = 0.
"""

NOTE_NAMES = ("C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B")

_NATURALS = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
_ACCIDENTALS = {"#": 1, "b": -1}


def parse_note(name: str) -> int:
    """Convert a note name such as ``"A"``, ``"c#"`` or ``"Bb"`` to a pitch class."""
    if not name or name[0].upper() not in _NATURALS:
        raise ValueError(f"Invalid note name: {name!r}")
    pitch = _NATURALS[name[0].upper()]
    for char in name[1:]:
        if char not in _ACCIDENTALS:
            raise ValueError(f"Invalid note name: {name!r}")
        pitch += _ACCIDENTALS[char]
    return pitch % 12


def note_name(pitch_class: int) -> str:
    """Return the (sharp) name of a pitch class."""
    return NOTE_NAMES[pitch_class % 12]
