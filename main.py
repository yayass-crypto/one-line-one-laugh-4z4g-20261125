#!/usr/bin/env python3
"""One-line laugh entry: write a single funny line to the entry file.

Holds exactly one joke, checks it against the competition's shape
rules (1-140 characters, single line, ends with a period), writes it
to /output/entry.txt (or out/entry.txt when /output is not writable),
then reads the file back and confirms the bytes match.
Standard library only; no network access.
"""

import os
import sys

JOKE = "My boss calls us a family, so I asked HR when the will reading is."

MAX_CHARS = 140
FILENAME = "entry.txt"


def pick_destination():
    """Pick the first writable output directory for entry.txt."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    for directory in ([env_dir] if env_dir else []) + ["/output", "out"]:
        try:
            os.makedirs(directory, exist_ok=True)
            probe = os.path.join(directory, ".write-probe")
            with open(probe, "wb") as handle:
                handle.write(b"")
            os.unlink(probe)
            return os.path.join(directory, FILENAME)
        except OSError:
            continue
    return os.path.join("/output", FILENAME)


def find_problems(line):
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
        problems.append("line is %d characters, over the %d limit"
                        % (len(line), MAX_CHARS))
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


def write_and_confirm(line, path):
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
        sys.stderr.write("verification failed: file bytes differ\n")
        return False
    print("wrote %s" % path)
    print("characters: %d" % len(line))
    print("bytes: %d" % len(payload))
    print(line)
    return True


def main():
    problems = find_problems(JOKE)
    if problems:
        for problem in problems:
            sys.stderr.write("invalid line: %s\n" % problem)
        return 1
    try:
        ok = write_and_confirm(JOKE, pick_destination())
    except OSError as exc:
        sys.stderr.write("could not write entry file: %s\n" % exc)
        return 1
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
