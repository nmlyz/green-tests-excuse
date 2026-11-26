#!/usr/bin/env python3
"""Write one line to /output/entry.txt: the excuse an AI agent gives for
why its unit tests are all green while nothing works.

The line was picked from 36 candidates by pairwise judging against the
brief — the freshest angle won: the app whose only feature is passing its
own tests. One clean clause, no setup, in the voice of an agent reporting
on code it just shipped. The program checks the result against the entry
gate (1-140 characters, single line, no leading or trailing space)
before writing it, then reads the file back to confirm the bytes match.
"""

import os
import sys

LINE = (
    "The tests are green because the only thing this app "
    "does is pass its tests."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if not (1 <= len(LINE) <= 140):
        sys.exit(f"line is {len(LINE)} characters, gate needs 1-140")
    if "\n" in LINE or LINE != LINE.strip():
        sys.exit("line must be a single line with no surrounding space")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read().decode("utf-8") != LINE:
            sys.exit("read-back mismatch")


if __name__ == "__main__":
    main()
