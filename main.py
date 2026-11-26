"""Entry program: write one robot wedding vow to entry.txt.

The vow is a single UTF-8 text of 1-160 characters; the grader runs this
program twice and the two runs must write identical bytes.
"""

import hashlib
import os

TEXT = "I vow to love you through every firmware update, every low battery, and every mandatory reboot."

# Gate contract: entry.txt must be UTF-8 text of 1 to 160 characters,
# not only white space, on a single line.
assert 1 <= len(TEXT) <= 160, "vow must be 1-160 characters"
assert TEXT.strip(), "vow must not be only white space"
assert "\n" not in TEXT and "\r" not in TEXT, "vow must be a single line"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = TEXT.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Read back and verify the written bytes match the intended vow.
    with open(path, "rb") as f:
        written = f.read()
    assert written == data, "entry.txt content mismatch"
    print(path)
    print(len(data))
    print(hashlib.sha256(data).hexdigest())


if __name__ == "__main__":
    main()
