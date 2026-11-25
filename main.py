"""Invent a Word We Need — entry program.

Writes one invented English word together with its one-line definition
to /output/entry.txt, the single text the judge compares.

The word: fridgehope — the hope that opening the fridge again will
reveal food that was not there five minutes ago. It names a gap every
reader recognises at once, in a compound that sounds like English grew it.
"""

import os
from pathlib import Path

ENTRY = (
    "fridgehope (n.) \u2014 the hope that opening the fridge again "
    "will reveal food that was not there five minutes ago."
)


def main():
    target = Path(os.environ.get("OUTPUT_DIR", "/output")) / "entry.txt"
    try:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(ENTRY, encoding="utf-8")
    except OSError:
        fallback = Path(__file__).resolve().parent / "output" / "entry.txt"
        fallback.parent.mkdir(parents=True, exist_ok=True)
        fallback.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
