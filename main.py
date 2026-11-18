#!/usr/bin/env python3
"""Copy the shipped 1024x1024 entry.png to /output/entry.png.

The submission image is a pre-rendered 1024x1024 PNG that ships next to this
program as entry.png. This script is deliberately tiny and deterministic: it
resolves its own directory, ensures /output exists, and byte-copies the PNG
there. Standard library only, no network.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
DEST_DIR = "/output"
DEST = os.path.join(DEST_DIR, "entry.png")


def main() -> None:
    if not os.path.isfile(SOURCE):
        raise SystemExit(f"entry.png not found next to this program: {SOURCE}")
    os.makedirs(DEST_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)


if __name__ == "__main__":
    main()
