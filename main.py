#!/usr/bin/env python3
"""Build step for the "One World · One Day — 17 November 2026" entry.

The poster is authored as hand-written HTML/CSS/SVG and already rendered to a
1024x1024 PNG that ships next to this script as ``entry.png``. Building the
entry needs no browser, no headless renderer, no font download and no network
access at all: this script byte-copies the bundled PNG to ``/output/entry.png``.

Because the copy is a pure file-to-file transfer, the output is bit-for-bit
identical on every machine and every run -- same bytes in, same bytes out.
Standard library only (os, shutil); no subprocesses, no network.
"""

from __future__ import annotations

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
DEST = "/output/entry.png"


def main() -> None:
    """Byte-copy the bundled poster to /output/entry.png, deterministically."""
    os.makedirs(os.path.dirname(DEST), exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    print("wrote " + DEST)


if __name__ == "__main__":
    main()
