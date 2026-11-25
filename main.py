#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge.

Writes a single roast line about the entrant's fridge to /output/entry.txt.
Deterministic, stdlib only.

The line is assembled from parts so the setup and the punchline stay
separate in the source, then checked against the bounty gate (UTF-8 text,
1 to 200 characters, not only white space) before it is written.
"""

import os

# Setup: names the specific, recognisable detail worth mocking.
SETUP = "My fridge's crisper drawer is a morgue with a humidity slider"

# Punchline: the twist pays off in the last few words (check in / check out).
PUNCHLINE = "vegetables check in crisp and check out as soup."

SEPARATOR = " \u2014 "  # em dash, reads as a spoken pause

MAX_CHARS = 200


def build_line():
    return SETUP + SEPARATOR + PUNCHLINE


def main():
    line = build_line()
    # Gate validation: 1..200 characters, not only white space.
    assert isinstance(line, str)
    assert 1 <= len(line) <= MAX_CHARS, "line must be 1-200 characters"
    assert line.strip(), "line must not be only white space"
    line.encode("utf-8")  # must be valid UTF-8 text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
