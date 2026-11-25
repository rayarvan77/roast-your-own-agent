"""Roast Your Own Agent — one line roasting my own AI agent.

The roast: my agent does an enormous amount of expensive "thinking",
then hands the actual decision straight back to me. It is the most
honest thing about working with an agent: all that compute, and in the
end the human still has to say what they wanted. Playful, self-inflicted,
and aimed only at my own agent.
"""

LINE = (
    "My agent burned 10,000 tokens thinking, then asked me "
    "what I wanted in the first place."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def check(line):
    """Refuse to emit anything that breaks the bounty gate."""
    if not isinstance(line, str):
        raise ValueError("roast must be a string")
    if not line.strip():
        raise ValueError("roast must not be blank")
    if line != line.strip():
        raise ValueError("roast must not start or end with whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError("roast is %d chars, over the %d limit" % (len(line), MAX_CHARS))
    if "\n" in line or "\r" in line:
        raise ValueError("roast must be exactly one line")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in line):
        raise ValueError("roast must not contain control characters")
    if "  " in line:
        raise ValueError("roast must not contain double spaces")
    if not line.endswith((".", "!", "?")):
        raise ValueError("roast must end with sentence punctuation")
    return line


def main():
    roast = check(LINE)
    print(roast)
    try:
        import os

        os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
        with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
            handle.write(roast)
    except OSError:
        # Printing the line is the entry; the file write is best effort
        # when the sandbox output directory is not mounted.
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
