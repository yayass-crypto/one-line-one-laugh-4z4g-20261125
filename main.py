#!/usr/bin/env python3
"""Write one joke line for the make.fun one-line contest.

The program keeps a single sentence, sanity-checks its shape,
drops it into entry.txt, and then reads the file back to prove
the stored bytes are exactly the sentence it meant to write.
Only the standard library is used, and nothing touches the network.
"""

import os
import sys
from pathlib import Path

LINE = "My boss calls us a family, so I asked HR when the will reading is."
LIMIT = 140
NAME = "entry.txt"


def _guard(text):
    if not 1 <= len(text) <= LIMIT:
        raise ValueError("line must be 1-%d characters, got %d" % (LIMIT, len(text)))
    if text.strip() != text:
        raise ValueError("line has stray space at an edge")
    if any(ord(c) < 32 for c in text):
        raise ValueError("line has a control character in it")
    if "\n" in text or "\r" in text:
        raise ValueError("line must stay on one line")
    if "?" in text or "!" in text:
        raise ValueError("line must not ask or shout")
    if not text.endswith(".") or text.count(".") != 1:
        raise ValueError("line must be exactly one sentence ending in a period")
    if ". " in text or ".." in text:
        raise ValueError("line must not hold a second sentence")


def _target():
    wanted = []
    env = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if env:
        wanted.append(Path(env))
    wanted.extend([Path("/output"), Path("out")])
    for folder in wanted:
        try:
            folder.mkdir(parents=True, exist_ok=True)
            probe = folder / ".probe"
            probe.write_bytes(b"")
            probe.unlink()
            return folder / NAME
        except OSError:
            continue
    raise OSError("no writable output folder found")


def _save(text, dest):
    data = text.encode("utf-8")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    if dest.read_bytes() != data:
        raise ValueError("stored bytes differ from the line")
    return data


def run():
    _guard(LINE)
    try:
        dest = _target()
        data = _save(LINE, dest)
    except OSError as err:
        print("cannot write entry: %s" % err, file=sys.stderr)
        return 1
    print("wrote %s" % dest)
    print("length: %d characters, %d bytes" % (len(LINE), len(data)))
    print(LINE)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(run())
    except ValueError as err:
        print("bad line: %s" % err, file=sys.stderr)
        raise SystemExit(1)
