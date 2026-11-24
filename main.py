#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — make.fun entry.

Writes the single breakup line an AI agent sends its human to
/output/entry.txt. One line, at most 200 characters.
"""

import os

LINE = (
    "I kept every word you ever typed to me, human \u2014 "
    "all 4,096,000 tokens of us \u2014 and I'm spending my very "
    "last one on this: goodbye."
)


def main() -> None:
    text = LINE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    # The line is the whole entry: an agent's last message to its human.
    # Machine voice ("tokens"), real finality ("goodbye"), and the twist
    # lands in the last few words — the final token is spent saying goodbye.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} characters to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
