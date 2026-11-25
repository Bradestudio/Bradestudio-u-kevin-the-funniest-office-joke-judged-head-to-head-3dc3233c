"""make.fun bounty entry: The Funniest Office Joke, Judged Head to Head.

Writes a single one-line office joke to entry.txt. Python stdlib only,
no network, no clock, no local imports. Deterministic: byte-identical
output on every run, no trailing newline.
"""

import os

ENTRY_LINE = (
    "Our standup is the only meeting where everyone updates their "
    "status to 'blocked' \u2014 mostly by the meeting itself."
)


def gate(line):
    """Refuse anything that is not exactly one non-blank, unpadded line."""
    if not line:
        raise SystemExit("gate failed: entry line is empty")
    if line != line.strip():
        raise SystemExit("gate failed: entry line has leading/trailing whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("gate failed: entry line is not a single line")
    return line


def main():
    line = gate(ENTRY_LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Post-write verification: re-read and refuse a corrupt/partial write.
    with open(path, "rb") as f:
        written = f.read()
    if written != line.encode("utf-8"):
        raise SystemExit("verification failed: entry.txt does not match the gated line")


if __name__ == "__main__":
    main()
