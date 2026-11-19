"""Visualise scales and arpeggios on a 6-string guitar fretboard."""

from fretboard.notes import NOTE_NAMES, note_name, parse_note
from fretboard.scales import SCALE_INTERVALS, Scale

__all__ = ["NOTE_NAMES", "SCALE_INTERVALS", "Scale", "note_name", "parse_note"]
