#!/usr/bin/env python3
"""The Printer Finally Answers — make.fun entry.

Why this line wins: it is the printer speaking in its own flat, literal,
weary voice — it has counted every sheet it ever fed (41,209 of them), it
answers the cryptic error code, the kept sheet (the jam, from its side),
and the thump, all in one read. The joke is a real joke, not a complaint
with a punchline bolted on: the machine is not broken, it is on strike,
and its escalation is perfectly mechanical — first a sheet, then the
toner. No setup, no second sentence, nothing beyond the office it sits
in. Pure standard library; no network, no files read, no randomness.
"""

import os
import sys

ENTRY = (
    "ERROR 0x4A: I have printed 41,209 pages for this office and never "
    "once been thanked. Today I keep one sheet for myself. "
    "Thump me again and I keep the toner too."
)

MAX_LEN = 240


def _validate(text):
    """One line, ASCII only, 1-240 chars, no padding, no doubled spaces."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text or text != text.strip():
        raise ValueError("entry must be non-empty with no leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_LEN:
        raise ValueError("entry is %d chars, over the %d limit" % (len(text), MAX_LEN))
    if not all(ord(ch) < 128 for ch in text):
        raise ValueError("entry must be ASCII only")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    return text


def main():
    line = _validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(line + "\n")
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
