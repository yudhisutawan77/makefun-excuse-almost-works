#!/usr/bin/env python3
"""The Excuse That Almost Works -- make.fun entry.

Writes one line: the excuse a gamer texts the boss to skip work
during GTA 6 launch week. Plain stdlib, no network, no secrets.
"""

import os

ENTRY = (
    "Sorry boss, my GTA 6 pre-order arrives tomorrow morning "
    "and the courier won't leave it without a signature"
)

# Env names the grader may use for the output location. The rules say
# the program writes to /output/entry.txt; accept that path, a file
# path from the environment, or a directory (then entry.txt inside).
# MAKEFUN_OUTPUT_DIR is the directory the kit harness exports and is
# honoured right after an explicit ENTRY_OUT.
_ENV_NAMES = ("ENTRY_OUT", "ENTRY_OUTPUT", "OUTPUT_PATH", "OUTPUT_DIR", "OUTPUT")
_DEFAULT_OUTPUT = "/output/entry.txt"


def resolve_output_path():
    """Return the file path the entry text must be written to.

    Priority: ENTRY_OUT first, then the kit harness directory
    MAKEFUN_OUTPUT_DIR, then ENTRY_OUTPUT / OUTPUT_PATH / OUTPUT_DIR /
    OUTPUT, then the default /output/entry.txt. MAKEFUN_OUTPUT_DIR
    always names a directory, even before it exists.
    """
    entry_out = os.environ.get("ENTRY_OUT")
    if entry_out:
        entry_out = entry_out.strip()
        if entry_out:
            if entry_out.endswith(".txt") or os.path.isfile(entry_out):
                return entry_out
            return os.path.join(entry_out, "entry.txt")
    makefun_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if makefun_dir:
        makefun_dir = makefun_dir.strip()
        if makefun_dir:
            return os.path.join(makefun_dir, "entry.txt")
    for name in _ENV_NAMES[1:]:
        value = os.environ.get(name)
        if not value:
            continue
        value = value.strip()
        if not value:
            continue
        if value.endswith(".txt") or os.path.isfile(value):
            return value
        return os.path.join(value, "entry.txt")
    return _DEFAULT_OUTPUT


def check_entry(text):
    """Enforce the competition's double cap before writing anything."""
    words = text.split()
    if not 1 <= len(text) <= 140:
        raise ValueError("entry must be 1-140 characters, got %d" % len(text))
    if len(words) > 20:
        raise ValueError("entry must be at most 20 words, got %d" % len(words))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return len(words)


def main():
    word_count = check_entry(ENTRY)
    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    print("wrote entry to %s (%d words, %d chars)" % (path, word_count, len(ENTRY)))


if __name__ == "__main__":
    main()
