"""Entry for the "One Line, One Chill" bounty (v2).

The program writes one horror sentence to /output/entry.txt.
Gate: UTF-8 text, 1-200 characters, not only whitespace.
Standard library only; reads nothing, uses no network.

Verified locally (3 runs, byte-identical): 83 characters / 83 bytes,
exactly one sentence, valid UTF-8, no trailing newline, file mode 0644.
"""

import os
import sys
from pathlib import Path

LINE = (
    "I buried my mother in March; her dentures are in my glass "
    "every morning, still wet."
)


def check(line):
    """Raise SystemExit unless the line passes the bounty gate."""
    if not line.strip():
        sys.exit("line is blank")
    if line != line.strip():
        sys.exit("line has padding whitespace")
    if not 1 <= len(line) <= 200:
        sys.exit("line length %d outside 1-200" % len(line))
    endings = [ch for ch in line if ch in ".!?"]
    if len(endings) != 1 or not line.endswith("."):
        sys.exit("line must be exactly one sentence ending in a period")
    line.encode("utf-8")  # raises if not encodable


def main():
    check(LINE)
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(LINE.encode("utf-8"))
    os.chmod(target, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
