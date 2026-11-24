"""Worst AI Advice entry.

One line of terrible advice, written to /output/entry.txt for the judge.

The joke: a cheerful assistant voice confidently recommends charging a phone
in a microwave. It is specific enough to follow, concrete enough to picture,
and bad enough to laugh at -- the waves do not charge anything, they cook it.
The text is fixed, so every run writes the same file, and the program refuses
to emit anything longer than the competition's 140-character cap.
"""

import os

ADVICE = (
    "Certainly! To charge your phone faster, pop it in the microwave "
    "for 30 seconds \u2014 the waves charge it faster than any cable can."
)

MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"


def build_line() -> str:
    line = ADVICE.strip()
    if not line or line.isspace():
        raise ValueError("advice line is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"advice is {len(line)} chars, over the 140 cap")
    return line


def main() -> None:
    text = build_line()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the gate counts every character of the file.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
