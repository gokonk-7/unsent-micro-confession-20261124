"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt:
a To: line naming who it was meant for, and the unsent message
itself, one line written exactly as it was typed.
"""

import os

ENTRY = (
    "To: my driving instructor\n"
    "I failed the first test on purpose. "
    "Those lessons were the only hour a week anyone was patient with me."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate, as published in the competition rules: /output/entry.txt must
    # be UTF-8 text of 1 to 260 characters, not only white space, and the
    # message itself is one line of at most 200 characters.
    lines = ENTRY.split("\n")
    assert 1 <= len(ENTRY) <= 260, f"entry is {len(ENTRY)} chars, gate is 1-260"
    assert len(lines) == 2 and lines[0].startswith("To: "), "entry must be a To: line plus one message line"
    assert len(lines[1]) <= 200, f"message is {len(lines[1])} chars, cap is 200"
    assert ENTRY.strip(), "entry must not be only white space"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
