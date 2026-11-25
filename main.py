"""Entry for make.fun bounty u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.

One original line roasting a gadget the writer uses every day, written to
/output/entry.txt. Deterministic, no network, no randomness.
"""

import os
import sys

LINE = "My phone says storage is full, then suggests I delete the photos of my own children to make room for its own update."

MAX_CHARS = 200


def check_line(line: str) -> None:
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 and ch not in ("\t",) for ch in line):
        raise ValueError("entry must not contain control characters")
    line.encode("utf-8")


def main() -> int:
    check_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(path, encoding="utf-8") as f:
        if f.read() != LINE:
            raise ValueError("read-back verification failed")
    print(f"wrote {path}: {len(LINE)} chars")
    return 0


if __name__ == "__main__":
    sys.exit(main())
