"""One Line, One Chill entry (v3).

Writes a single horror sentence to /output/entry.txt.
Gate: UTF-8, 1-200 characters, not only whitespace.
Standard library only; no input, no network.

Verified locally (3 runs, byte-identical): 84 characters / 84 bytes,
sha256 860da02604e31943f2d01630d94a74d112bfb8c7d7620b6e5a8bfaee5301434a,
exactly one sentence, valid UTF-8, no trailing newline, file mode 0644.
"""

import os
import sys
from pathlib import Path

SENTENCE = (
    "I buried my mother in March; her dentures are in my glass "
    "every morning, still warm."
)


def validate(text):
    if not text.strip():
        sys.exit("sentence is blank")
    if text != text.strip():
        sys.exit("sentence has surrounding whitespace")
    if not 1 <= len(text) <= 200:
        sys.exit("sentence length %d outside 1-200" % len(text))
    marks = [ch for ch in text if ch in ".!?"]
    if len(marks) != 1 or not text.endswith("."):
        sys.exit("sentence must end with its only full stop")
    text.encode("utf-8")


def main():
    validate(SENTENCE)
    folder = Path(os.environ.get("OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / "entry.txt"
    path.write_bytes(SENTENCE.encode("utf-8"))
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
