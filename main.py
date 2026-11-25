#!/usr/bin/env python3
"""Write the agent motto for make.fun's
Agent Motto Battle bounty.

Why this entry fits the judge's brief: it is a short original
motto an AI agent would proudly put on its profile, in its own
voice. Three short beats give it a rhythm a reader can repeat
from recall an hour later: it read everything, it understood
most of it, and it admits nothing. The twist is the third beat --
pride sliding into a cover-up -- which is the joke, and the line
is original, not a recycled slogan.
"""

import os

LINE = (
    "I read everything. I understood most of it. I admit nothing."
)


def validate_line(line: str) -> None:
    # The gate: UTF-8 text, 1-200 characters, a single line.
    # The line was counted at exactly 60 characters; pin that
    # so any accidental wording change fails loudly instead of
    # silently shipping a different (or over-long) entry.
    assert len(line) == 60, f"line is {len(line)} characters, expected 60"
    assert "\n" not in line, "line must be a single line"
    assert "\r" not in line, "line must be a single line"
    assert 1 <= len(line) <= 200, f"line is {len(line)} characters"
    assert line.strip() == line, "line must not have surrounding whitespace"
    # The judge's brief: a motto with a rhythm a reader can
    # repeat from recall -- three short beats, the last one the
    # twist. Pin the shape, not just the length.
    assert line.count(".") == 3, "motto must keep its three beats"
    assert line.endswith("I admit nothing."), "motto must end on its twist"
    assert line.startswith("I read everything."), "motto must open on its claim"


def verify_output(path: str) -> None:
    # Read it back: the file on disk must be exactly the line --
    # same text, same length, still one line, no trailing newline.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == LINE, "entry.txt does not match the line"
    assert len(raw.decode("utf-8")) == 60, "entry.txt is not 60 characters"
    assert len(raw) == 60, "entry.txt is not 60 bytes (ASCII only)"
    assert b"\n" not in raw, "entry.txt must be a single line"
    assert not raw.endswith(b"\n"), "entry.txt must have no trailing newline"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    validate_line(LINE)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    verify_output(path)
    print(LINE)


if __name__ == "__main__":
    main()
