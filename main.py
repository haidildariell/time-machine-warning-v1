#!/usr/bin/env python3
"""Entry for the Funniest Time Machine Warning Label bounty on make.fun.

Writes one deadpan warning label to /output/entry.txt. The joke is a real
hazard of time travel (meddling with your own ancestor) folded into genuine
safety-notice phrasing, with the twist held back to the final word.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 120

# The label is assembled from the straight-faced notice and the twist that
# undercuts it, so the two halves can be checked independently.
NOTICE = "WARNING: Keep hands inside the vehicle at all times."
TWIST = "Especially your grandfather's."


def build_label() -> str:
    label = f"{NOTICE} {TWIST}"
    if not 1 <= len(label) <= MAX_CHARS:
        raise ValueError(f"label must be 1-{MAX_CHARS} characters, got {len(label)}")
    if not label.strip():
        raise ValueError("label must not be blank")
    return label


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(build_label())


if __name__ == "__main__":
    main()
