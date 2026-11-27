#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse.

Writes a single line to MAKEFUN_OUTPUT_DIR/entry.txt: one funny,
half-believable excuse to call in sick, under 200 characters.
Standard library only. Writes nowhere except MAKEFUN_OUTPUT_DIR.
"""

import os

ENTRY = (
    # Half believable (a tracker glitch), fresh (no fever, no dog),
    # and the laugh lands on the last words.
    "My sleep tracker says I ran a marathon in my sleep, so I'm "
    "calling in sick to recover from a race I don't remember entering."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
