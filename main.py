#!/usr/bin/env python3
"""One Line, Big Laugh — writes a single funny line to /output/entry.txt.

Stdlib only. The line is a fixed, hand-written joke: one concrete scene
(a check-engine light that never goes off), one turn (the driver names it),
one landing final line. 137 characters, no trailing newline.
"""

from pathlib import Path

ENTRY = (
    "My check-engine light has been on so long I named it Greg. "
    "He's been glowing for three years and frankly, he's the only "
    "light in my life."
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be only whitespace"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
