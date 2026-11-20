"""Scales defined as a root note plus semitone intervals."""

from dataclasses import dataclass

from fretboard.notes import note_name, parse_note

SCALE_INTERVALS: dict[str, tuple[int, ...]] = {
    "major": (0, 2, 4, 5, 7, 9, 11),
    "minor": (0, 2, 3, 5, 7, 8, 10),
    "harmonic_minor": (0, 2, 3, 5, 7, 8, 11),
    "melodic_minor": (0, 2, 3, 5, 7, 9, 11),
    "major_pentatonic": (0, 2, 4, 7, 9),
    "minor_pentatonic": (0, 3, 5, 7, 10),
    "blues": (0, 3, 5, 6, 7, 10),
}


@dataclass(frozen=True)
class Scale:
    root: int
    intervals: tuple[int, ...]

    @classmethod
    def from_name(cls, root: str, name: str) -> "Scale":
        """Build a scale from a root note name and a key of ``SCALE_INTERVALS``."""
        if name not in SCALE_INTERVALS:
            raise ValueError(f"Unknown scale {name!r}; choose from {sorted(SCALE_INTERVALS)}")
        return cls(parse_note(root), SCALE_INTERVALS[name])

    @property
    def pitch_classes(self) -> tuple[int, ...]:
        return tuple((self.root + i) % 12 for i in self.intervals)

    @property
    def notes(self) -> tuple[str, ...]:
        return tuple(note_name(p) for p in self.pitch_classes)

    def __len__(self):
        return len(self.intervals)