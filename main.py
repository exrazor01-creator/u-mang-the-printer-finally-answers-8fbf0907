#!/usr/bin/env python3
"""The Printer Finally Answers — make.fun entry.

The joke: after years of silent service the office printer files its
first grievance, in its own voice. It opens with a machine's idea of
evidence — an error code and an exact lifetime page count, 41,209 —
then answers every beat of the prompt from the other side of the desk:
the error is not a fault, it is a decision; the jam is not a jam, it
is the printer keeping one sheet for itself; the thump is not a fix,
it is a threat the printer can out-escalate — a sheet today, the toner
tomorrow. The escalation is strictly mechanical and therefore funny:
each punishment costs the office a little more of the machine. One
sentence, one voice, no setup and no aside. Pure standard library,
no network, no files read, no randomness.
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
    """Enforce the competition's line rules, cheapest checks first.

    Rejects, in order: a non-string, an empty or padded line, any line
    break, anything over the 240-char limit, non-ASCII characters, and
    doubled spaces. Returns the unchanged text when every check passes.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string, got %s" % type(text).__name__)
    if not text:
        raise ValueError("entry must not be empty")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line (no newline characters)")
    if len(text) > MAX_LEN:
        raise ValueError(
            "entry is %d chars, over the %d-char limit" % (len(text), MAX_LEN)
        )
    if "  " in text:
        raise ValueError("entry must not contain two spaces in a row")
    if not all(ord(ch) < 128 for ch in text):
        raise ValueError("entry must be ASCII only")
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
