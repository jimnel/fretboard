"""Chords defined as a root note plus semitone intervals above the root."""

from collections.abc import Iterable
from dataclasses import dataclass

from fretboard.notes import note_name, parse_note

CHORD_INTERVALS: dict[str, tuple[int, ...]] = {
    "maj": (0, 4, 7),
    "min": (0, 3, 7),
    "dim": (0, 3, 6),
    "aug": (0, 4, 8),
    "sus2": (0, 2, 7),
    "sus4": (0, 5, 7),
    "7": (0, 4, 7, 10),
    "maj7": (0, 4, 7, 11),
    "min7": (0, 3, 7, 10),
    "m7b5": (0, 3, 6, 10),
    "dim7": (0, 3, 6, 9),
}

_QUALITY_BY_INTERVALS = {v: k for k, v in CHORD_INTERVALS.items()}


def _to_pitch_class(note: int | str) -> int:
    return parse_note(note) if isinstance(note, str) else note % 12


@dataclass(frozen=True)
class Chord:
    root: int
    intervals: tuple[int, ...]

    @classmethod
    def from_name(cls, root: str, quality: str) -> "Chord":
        """Build a chord from a root note name and a key of ``CHORD_INTERVALS``."""
        if quality not in CHORD_INTERVALS:
            raise ValueError(f"Unknown chord {quality!r}; choose from {sorted(CHORD_INTERVALS)}")
        return cls(parse_note(root), CHORD_INTERVALS[quality])

    @classmethod
    def from_notes(cls, notes: Iterable[int | str]) -> "Chord":
        """Build a chord from notes (names or pitch classes); the first note is the root."""
        pitches = [_to_pitch_class(n) for n in notes]
        if not pitches:
            raise ValueError("A chord needs at least one note")
        root = pitches[0]
        intervals = tuple(sorted({(p - root) % 12 for p in pitches}))
        return cls(root, intervals)

    @property
    def quality(self) -> str | None:
        """The chord quality (e.g. ``"min7"``), or ``None`` if it isn't a known chord."""
        return _QUALITY_BY_INTERVALS.get(self.intervals)

    @property
    def pitch_classes(self) -> tuple[int, ...]:
        return tuple((self.root + i) % 12 for i in self.intervals)

    @property
    def notes(self) -> tuple[str, ...]:
        return tuple(note_name(p) for p in self.pitch_classes)

    @property
    def name(self) -> str:
        quality = self.quality or "(" + " ".join(self.notes) + ")"
        return f"{note_name(self.root)} {quality}"

    def __len__(self) -> int:
        return len(self.intervals)

    def __str__(self) -> str:
        return self.name
