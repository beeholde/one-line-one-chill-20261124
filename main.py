"""One Line, One Chill entry.

Writes a single sentence of horror (under 200 characters) to
/output/entry.txt. Standard library only; no network, no input files.

The line is held in STORY below and checked before it is written:
exactly one sentence, 1-200 characters, no trailing newline.
Verified locally: 92 characters / 92 bytes, one sentence, no newline.
"""

import os
import sys

STORY = (
    "I counted seven pills in my dead mother's weekly box on Sunday; "
    "on Wednesday there were six."
)

TERMINATORS = ".!?"


def sentence_total(text):
    """How many sentences a line holds: one per terminal mark."""
    return sum(1 for ch in text if ch in TERMINATORS)


def entry_path():
    base = os.environ.get("OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def main():
    line = STORY
    if not 1 <= len(line) <= 200:
        sys.exit("entry must be 1-200 characters, got %d" % len(line))
    if sentence_total(line) != 1:
        sys.exit("entry must be exactly one sentence")
    if line != line.strip() or not line.strip():
        sys.exit("entry must not be blank or padded")
    path = entry_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(line.encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
