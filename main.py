#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun entry.

Writes a single emoji to /output/entry.txt: the hugging face (U+1F917).

Why this emoji: a hug reads as warm and friendly at first glance with no
context needed, and it is understood the same way by a stranger of any age
or background — an open-armed welcome, not a joke, not flirtation, not
intimacy. It is also a deliberate pick rather than the first smiley that
comes to mind: the plain 🙂 or 😊 is the default, while 🤗 adds the
gesture of warmth (open hands, smiling face) that makes a stranger smile.
"""

import os

EMOJI = "\U0001F917"  # U+1F917 HUGGING FACE


def main() -> None:
    # Gate: exactly one emoji, 1-8 characters, not only white space.
    assert isinstance(EMOJI, str)
    assert 1 <= len(EMOJI) <= 8, f"entry must be 1-8 chars, got {len(EMOJI)}"
    assert EMOJI.strip(), "entry must not be only white space"
    assert len(EMOJI) == 1, f"entry must be a single character, got {len(EMOJI)}"
    assert ord(EMOJI) == 0x1F917, "entry must be exactly U+1F917 HUGGING FACE"
    assert not EMOJI.isspace(), "entry must not be white space"
    assert ord(EMOJI) > 0xFFFF or EMOJI.isprintable(), "entry must be printable"

    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)

    # Re-read and verify what was written.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == EMOJI, f"written text {written!r} != {EMOJI!r}"
    assert 1 <= len(written) <= 8
    assert written.strip()
    print(f"Wrote {EMOJI!r} ({len(written)} char, "
          f"{len(written.encode('utf-8'))} bytes) to {out_path}")


if __name__ == "__main__":
    main()
