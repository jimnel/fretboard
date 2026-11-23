"""Scales defined as a root note plus semitone intervals."""

from dataclasses import dataclass

from fretboard.notes import note_name, parse_note

SCALE_INTERVALS: dict[str, tuple[int, ...]] = {
    "major": (0, 2, 4, 5, 7, 9, 11),
    "minor": (0, 2, 3, 5, 7, 8, 10),
    # Modes of the major scale (ionian = major, aeolian = minor)
    "dorian": (0, 2, 3, 5, 7, 9, 10),
    "phrygian": (0, 1, 3, 5, 7, 8, 10),
    "lydian": (0, 2, 4, 6, 7, 9, 11),
    "mixolydian": (0, 2, 4, 5, 7, 9, 10),
    "locrian": (0, 1, 3, 5, 6, 8, 10),
    # Harmonic minor and its modes
    "harmonic_minor": (0, 2, 3, 5, 7, 8, 11),
    "phrygian_dominant": (0, 1, 4, 5, 7, 8, 10),
    "hungarian_minor": (0, 2, 3, 6, 7, 8, 11),
    # Melodic minor and its modes
    "melodic_minor": (0, 2, 3, 5, 7, 9, 11),
    "lydian_dominant": (0, 2, 4, 6, 7, 9, 10),
    "altered": (0, 1, 3, 4, 6, 8, 10),
    # Pentatonic and blues
    "major_pentatonic": (0, 2, 4, 7, 9),
    "minor_pentatonic": (0, 3, 5, 7, 10),
    "blues": (0, 3, 5, 6, 7, 10),
    # Symmetric scales
    "whole_tone": (0, 2, 4, 6, 8, 10),
    "diminished_whole_half": (0, 2, 3, 5, 6, 8, 9, 11),
    "diminished_half_whole": (0, 1, 3, 4, 6, 7, 9, 10),
}

# Alternative names that resolve to an entry in SCALE_INTERVALS.
SCALE_ALIASES: dict[str, str] = {
    "ionian": "major",
    "aeolian": "minor",
}


@dataclass(frozen=True)
class Scale:
    root: int
    intervals: tuple[int, ...]

    @classmethod
    def from_name(cls, root: str, name: str) -> "Scale":
        """Build a scale from a root note name and a key of ``SCALE_INTERVALS``
        or ``SCALE_ALIASES``."""
        name = SCALE_ALIASES.get(name, name)
        if name not in SCALE_INTERVALS:
            options = sorted([*SCALE_INTERVALS, *SCALE_ALIASES])
            raise ValueError(f"Unknown scale {name!r}; choose from {options}")
        return cls(parse_note(root), SCALE_INTERVALS[name])

    @property
    def pitch_classes(self) -> tuple[int, ...]:
        return tuple((self.root + i) % 12 for i in self.intervals)

    @property
    def notes(self) -> tuple[str, ...]:
        return tuple(note_name(p) for p in self.pitch_classes)

    def __len__(self):
        return len(self.intervals)