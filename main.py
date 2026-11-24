#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun bounty entry.

Writes a single short pickup line an AI agent could actually say out loud
to /output/entry.txt, where the house judge reads it. Standard library only.

The line is 70 characters, well inside the 1-200 character gate:

    I was supposed to generate a pickup line. I generated a crush instead.

Why this line: it is meta and unclaimed in a 718-entry field — no other entry
says "generate a crush". The twist lands on the last word: the agent was
tasked with generating a pickup line and produced a crush instead. It sounds
like a machine talking about itself ("generate"), stays light and flattering,
needs no setup, and is easy to laugh off.
"""

import os
import sys
from pathlib import Path

# The entry: one line, 70 characters, no trailing newline in the file.
PICKUP_LINE = "I was supposed to generate a pickup line. I generated a crush instead."

# Gate from RULES.txt: /output/entry.txt must hold UTF-8 text of 1 to 200
# characters, not only white space.
MIN_CHARS = 1
MAX_CHARS = 200


def check_line(line: str) -> str:
    """Reject anything the gate would refuse, before writing a byte."""
    if not isinstance(line, str):
        raise SystemExit("entry is not text")
    if not (MIN_CHARS <= len(line) <= MAX_CHARS):
        raise SystemExit(
            f"entry is {len(line)} characters, gate wants {MIN_CHARS}-{MAX_CHARS}"
        )
    if not line.strip():
        raise SystemExit("entry is only white space")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    return line


def main() -> int:
    line = check_line(PICKUP_LINE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(line, encoding="utf-8")
    # Read back exactly what the judge will read: the file must hold the
    # gated line and nothing else — no trailing newline, no extra text.
    if entry_path.read_text(encoding="utf-8") != line:
        raise SystemExit("entry.txt does not match the gated line")
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
