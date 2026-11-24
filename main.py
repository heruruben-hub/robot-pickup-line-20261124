"""The Robot Pickup Line Championship — entry program.

Writes a single robot pickup line to the entry file, validates the
bounty gate first (one line, 1-200 characters, not only whitespace),
then reads the file back and checks it holds exactly what was written.

Why this line works: the joke grows out of being a machine. A software
update rebooting the whole system is a robot's most annoying routine —
so admitting you *don't mind* the downtime is the machine's version of
falling head over heels. The reboot is the pickup; the patience is the
charm.
"""

import os
import sys

LINE = (
    "Are you a software update? Because my whole system reboots every "
    "time you walk in \u2014 and for once, I don't mind the downtime."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def validate(line: str) -> None:
    """Enforce the bounty gate: one line, 1-200 chars, not only whitespace."""
    if not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > 200:
        raise ValueError(f"line is {len(line)} characters, over the 200 limit")


def main() -> int:
    validate(LINE)

    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

    # Read back and confirm the file holds exactly what was written.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        stored = f.read()

    if stored != LINE + "\n":
        print(f"error: {OUTPUT_PATH} does not match the entry line", file=sys.stderr)
        return 1

    print(f"Wrote {len(LINE)}-character pickup line to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
