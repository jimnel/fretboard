# CLAUDE.md

## Project goal

A Python package for visualising a **6-string guitar fretboard**, showing where the notes of
**scales** and **arpeggios** fall across the neck.

## Domain context

- Instrument: 6-string guitar, standard tuning by default (low to high: E A D G B E).
  Tuning should be configurable rather than hard-coded.
- The fretboard is modelled as strings × frets (fret 0 = open string). Each position's note is
  `(open_string_note + fret) % 12`.
- Scales and arpeggios are defined by a root note plus a list of semitone intervals
  (e.g. major `[0, 2, 4, 5, 7, 9, 11]`, natural minor `[0, 2, 3, 5, 7, 8, 10]`,
  major triad arpeggio `[0, 4, 7]`).
- Visualisation should make it easy to distinguish the root note from other chord/scale tones.

## Layout

- `src/fretboard/notes.py` — pitch classes are ints 0–11 with C = 0. `parse_note` accepts
  any case, `#` and `b`; `note_name` returns sharp names (`"C#"`).
- `src/fretboard/scales.py` — `SCALE_INTERVALS` table and a frozen `Scale(root, intervals)`
  dataclass; build with `Scale.from_name("A", "major")`.
- `tests/` — pytest tests, one file per module.
- `idea.ipynb` — scratch notebook (untracked).

Work internally in pitch classes; convert to names only at the edges (input parsing, display).

## Commands

- `uv sync` — create `.venv` and install the package with dev dependencies
- `uv run pytest` — run tests
