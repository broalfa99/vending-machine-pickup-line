#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes the one pickup line a vending machine would use on a passing
human to /output/entry.txt. The competition gate requires UTF-8 text
of 1-200 characters, not only whitespace, so the program refuses to
write anything outside that gate.
"""

from pathlib import Path

OUTPUT = Path("/output/entry.txt")

LINE = (
    "I've vended a thousand snacks without blushing once \u2014 then "
    "you came along and pressed all my buttons."
)


def validate(line: str) -> str:
    """Return the stripped line, or exit unless it is one line of 1-200 chars."""
    text = line.strip()
    if not text or len(text) > 200:
        raise SystemExit(f"entry must be 1-200 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    return text


def main() -> None:
    line = validate(LINE)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(line + "\n", encoding="utf-8")
    # Round-trip check: what the grader reads must be exactly this line.
    back = OUTPUT.read_text(encoding="utf-8").rstrip("\n")
    if back != line:
        raise SystemExit("round-trip mismatch")
    print(f"wrote {len(line)} chars to {OUTPUT}")


if __name__ == "__main__":
    main()
