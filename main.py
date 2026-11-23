"""One Line, Zero Use: The Useless Superpower Sprint.

Writes a single original line (at most 200 characters) describing a
hilariously useless superpower to /output/entry.txt.
"""

import os

LINE = "I can sense exactly when the Wi-Fi is about to drop \u2014 always three seconds after I hit send on something important."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
