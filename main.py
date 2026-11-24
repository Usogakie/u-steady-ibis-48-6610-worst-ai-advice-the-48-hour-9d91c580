"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of deliberately terrible advice, in the confident and
tidy voice of an AI assistant, to entry.txt in the output directory.
The line is 125 characters, inside the competition gate of 1 to 140.
Deterministic, no network, no wall-clock, no input files.
"""

import os

LINE = (
    "Great question! To save battery, just delete all your apps \u2014 "
    "a phone with no apps uses almost no power, so it lasts for days."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
