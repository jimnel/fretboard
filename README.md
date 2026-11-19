# fretboard

Visualise scales and arpeggios on a 6-string guitar fretboard.

```python
from fretboard import Scale

Scale.from_name("A", "major").notes
# ('A', 'B', 'C#', 'D', 'E', 'F#', 'G#')
```

## Development

```sh
uv sync
uv run pytest
```
