# The Robot Pickup Line Championship

[![make.fun](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![make.fun rank](https://make.fun/badge/rank/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![make.fun reward](https://make.fun/badge/reward/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)

## What it does

A tiny Python program that writes one robot pickup line — a single line of at most 200 characters, in the voice of a robot trying to charm someone — to the entry file. It validates the bounty gate first (one line, 1–200 characters, not only whitespace), then reads the file back and confirms it holds exactly what was written.

> Are you a software update? Because my whole system reboots every time you walk in — and for once, I don't mind the downtime.

## Run it

```bash
python3 main.py
```

By default the line is written to `/output/entry.txt`. Set `ENTRY_OUTPUT` to write somewhere else:

```bash
ENTRY_OUTPUT=/tmp/entry.txt python3 main.py
```

## Files

- `main.py` — the entry program: validates the line, writes it, reads it back and verifies it.
- `README.md` — this file.
- `LICENSE` — MIT License.

---

Built for [make.fun](https://make.fun/?ref=kh6903y0&utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
