#!/usr/bin/env python3
"""The One-Liner Groan-Off entry.

Reads the one-line dad joke from entry.txt, validates it against the
competition gate (UTF-8 text, one line, 1-140 characters, not only
whitespace), and writes it to /output/entry.txt.

Pure Python standard library only.
"""

import os
import sys

MAX_CHARS = 140


def load_line(path):
    """Read entry.txt and return the joke as a single line."""
    with open(path, "r", encoding="utf-8") as handle:
        content = handle.read()
    if content.endswith("\n"):
        content = content[:-1]
    return content


def is_tight(line):
    """A one-liner should have no wasted words at the edges."""
    return line == line.strip()


def validate(line):
    """Check the joke against the gate; return an error string or None."""
    if not line.strip():
        return "entry is empty or only whitespace"
    if not is_tight(line):
        return "entry has leading or trailing whitespace"
    if "\n" in line or "\r" in line:
        return "entry must be a single line"
    if len(line) > MAX_CHARS:
        return "entry is %d characters, over the %d limit" % (len(line), MAX_CHARS)
    return None


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    entry_path = os.path.join(here, "entry.txt")
    line = load_line(entry_path)
    error = validate(line)
    if error is not None:
        print("invalid entry: %s" % error, file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    print("wrote %d characters to /output/entry.txt" % len(line))
    return 0


if __name__ == "__main__":
    sys.exit(main())
