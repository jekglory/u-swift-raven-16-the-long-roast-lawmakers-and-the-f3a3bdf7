"""The Long Roast entry: one satirical sentence about lawmakers.

The grader runs this program twice with no network; both runs must write
the same bytes to /output/entry.txt. The roast is a fixed string, so the
output is deterministic by construction: no clock, no randomness, no I/O
other than the single write.
"""

import os


ROAST = (
    "The congressman drafting the bill to regulate artificial intelligence "
    "just printed his own email, signed it in pen, and asked his intern "
    "to fax it to the cloud."
)

OUTPUT_PATH = "/output/entry.txt"

# The competition requires one sentence, at most 320 characters.
MAX_CHARS = 320


def main() -> None:
    text = ROAST.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "roast must be 1-%d chars, got %d" % (MAX_CHARS, len(text))
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Clear only the contents of the grader-provided directory, never
    # the directory itself: drop a stale entry file if one is present.
    if os.path.exists(OUTPUT_PATH):
        os.remove(OUTPUT_PATH)
    data = text.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    # Verify the artifact the judge will read is exactly the roast.
    with open(OUTPUT_PATH, "rb") as f:
        if f.read() != data:
            raise SystemExit("written bytes do not match the roast")
    print(text)


if __name__ == "__main__":
    main()
