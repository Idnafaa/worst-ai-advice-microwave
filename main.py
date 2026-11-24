"""Worst AI Advice entry: one line of terrible advice, written to /output/entry.txt.

The line is deliberately bad advice in a cheerful assistant voice: charging a
phone in a microwave is a real folk myth that would destroy the phone, which is
exactly why it lands as a joke. The program keeps the text fixed so every run
produces the same file, and it refuses to write anything longer than the
competition's 140-character cap.
"""

import os

ADVICE = (
    "Certainly! To charge your phone faster, pop it in the microwave "
    "for 30 seconds \u2014 the waves charge it faster than any cable can."
)

MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ADVICE.strip()
    if not text:
        raise ValueError("advice line is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"advice line is {len(text)} chars, over the 140 cap")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
