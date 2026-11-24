#!/usr/bin/env python3
"""Two Lines to Your Past Self - make.fun bounty entry.

Writes a two-line warning to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

Line 1 warns my past self about one specific moment, in a single sentence.
Line 2 says in one sentence why that moment mattered and what changed
because of it.

The text is fixed and written out verbatim: the program is deterministic,
makes no network calls, and always writes the same bytes.
"""

import os

ENTRY = (
    "Don't send that 2 a.m. text to Maya from the taxi outside the airport \u2014 "
    "you mean it as a joke, and she hears it as goodbye.\n"
    "She never answers, and you spend the next three years learning that funny "
    "and final are not the same thing.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
