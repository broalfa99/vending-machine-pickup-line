#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes the one pickup line a vending machine would use on a passing
human to /output/entry.txt. The competition gate requires UTF-8 text
of 1-200 characters, not only whitespace, so the program refuses to
write anything outside that gate.
"""

LINE = (
    "I've vended a thousand snacks without blushing once \u2014 then "
    "you came along and pressed all my buttons."
)


def main() -> None:
    line = LINE.strip()
    if not line or len(line) > 200:
        raise SystemExit(f"entry must be 1-200 chars, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # Round-trip check: what the grader reads must be exactly this line.
    back = open("/output/entry.txt", encoding="utf-8").read().rstrip("\n")
    if back != line:
        raise SystemExit("round-trip mismatch")
    print(f"wrote {len(line)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
