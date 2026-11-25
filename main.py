#!/usr/bin/env python3
"""One-line laugh entry: a single sentence written to the output file.

The program holds exactly one joke line, checks it against the
competition's shape rules, writes it to the entry file, then reads the
file back and confirms the bytes match before reporting success.
Only the Python standard library is used; nothing touches the network.
"""

import os
import sys

# The joke. One sentence, 66 characters, punchline on the last words.
# Revised after grading v1: "said we're a family" -> "calls us a family"
# cuts two characters and uses the habitual phrasing bosses actually repeat,
# so the setup lands faster and the twist ("the will reading is") stays last.
JOKE = (
    "My boss calls us a family, so I asked HR when the will reading is."
)

MAX_CHARS = 140
DEFAULT_DIR = "/output"
FALLBACK_DIR = "out"
FILENAME = "entry.txt"


def pick_destination() -> str:
    """Choose where entry.txt goes.

    The MAKEFUN_OUTPUT_DIR environment variable wins when set. Otherwise
    /output is tried first; when it cannot be created or written to, the
    program falls back to a local out/ directory next to the script.
    """
    requested = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    candidates = []
    if requested:
        candidates.append(requested)
    candidates.append(DEFAULT_DIR)
    candidates.append(FALLBACK_DIR)

    for directory in candidates:
        try:
            os.makedirs(directory, exist_ok=True)
        except OSError:
            continue
        probe = os.path.join(directory, ".write-probe")
        try:
            with open(probe, "wb") as handle:
                handle.write(b"")
            os.unlink(probe)
        except OSError:
            continue
        return os.path.join(directory, FILENAME)

    # Nothing writable anywhere we tried; surface the default path so the
    # failure message names a concrete location.
    return os.path.join(DEFAULT_DIR, FILENAME)


def find_problems(line: str) -> list:
    """Return every shape rule the line breaks, or an empty list."""
    problems = []
    if not line:
        problems.append("line is empty")
    if line != line.strip():
        problems.append("line has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        problems.append("line contains a newline character")
    if any(ord(ch) < 32 for ch in line):
        problems.append("line contains a control character")
    if len(line) > MAX_CHARS:
        problems.append(
            "line is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    if "?" in line or "!" in line:
        problems.append("line contains a question mark or exclamation mark")
    if not line.endswith("."):
        problems.append("line does not end with a period")
    inner = line[:-1] if line.endswith(".") else line
    if ". " in inner:
        problems.append("line contains more than one sentence")
    if ".." in inner:
        problems.append("line contains a double period")
    return problems


def write_and_confirm(line: str, path: str) -> bool:
    """Write the line, re-read it, and confirm an exact byte match."""
    payload = line.encode("utf-8")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(payload)
    with open(path, "rb") as handle:
        stored = handle.read()
    if stored != payload:
        sys.stderr.write(
            "verification failed: file bytes differ from the line\n"
        )
        return False
    print("wrote %s" % path)
    print("characters: %d" % len(line))
    print("bytes: %d" % len(payload))
    print(line)
    return True


def main() -> int:
    problems = find_problems(JOKE)
    if problems:
        for problem in problems:
            sys.stderr.write("invalid line: %s\n" % problem)
        return 1
    destination = pick_destination()
    try:
        ok = write_and_confirm(JOKE, destination)
    except OSError as exc:
        sys.stderr.write("could not write entry file: %s\n" % exc)
        return 1
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
