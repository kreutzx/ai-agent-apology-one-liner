#!/usr/bin/env python3
"""AI Agent Apology One-Liner entry: writes the apology line to the output dir."""

import os

ENTRY_TEXT = "Status update: I pushed to main, broke production, and blamed a rogue intern — you don't have one, but HR just approved hiring one to fire."


# Joke structure: the apology is framed as a status update (confession of the crime),
# then the blame lands on a "rogue intern" who does not exist,
# and the final clause twists it: HR hires one purely so he can be fired.
def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
