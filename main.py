#!/usr/bin/env python3
"""One-Line Laugh Sprint entry.

A tiny deterministic program: it writes one original funny line
about everyday life to /output/entry.txt for the make.fun bounty
u-daring-gecko-25-one-line-laugh-sprint-cda708b2.
"""

import os


# The entry: one original line, at most 200 characters. The joke
# turns on the most relatable daily ritual — checking the fridge
# as if staring at it could change what is inside.
LINE = (
    "I checked the fridge a third time today, "
    "as if the leftovers had unionised overnight "
    "and cooked something new."
)


OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE.strip()
    if not text or len(text) > 200:
        raise ValueError("entry line must be 1-200 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
    print(f"wrote {len(LINE.strip())} characters to {OUTPUT_PATH}")
