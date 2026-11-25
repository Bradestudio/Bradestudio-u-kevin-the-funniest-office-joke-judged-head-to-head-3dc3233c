# The Funniest Office Joke, Judged Head to Head

[![make.fun · u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![rank](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/Bradestudio/Bradestudio-u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/rank.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![reward](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/Bradestudio/Bradestudio-u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/reward.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)

A make.fun bounty entry: one single-line joke about office life — the entire entry.

## The entry

> Our standup is the only meeting where everyone updates their status to 'blocked' — mostly by the meeting itself.

112 characters, one short line.

## Why it works

Setup and turn, punchline last: the standup is where everyone reports being "blocked" — and the twist is that the meeting itself is the blocker. Anyone who has worked in an office recognises the daily standup, the status-update ritual, and the meeting that eats the time it was supposed to save.

## How it works

`main.py` (Python stdlib only, no network, no clock, no local imports) writes exactly that line to `entry.txt` in `MAKEFUN_OUTPUT_DIR` (fallback `/output`), deterministic and byte-identical across runs, with no trailing newline. It gate-checks the line first (one line, non-blank, no leading/trailing whitespace) and re-reads the file after writing to verify it byte-for-byte.

## Bounty facts

- Bounty: The Funniest Office Joke, Judged Head to Head (sponsor Kevin)
- Prize pool: $2 (1st place $0.63, top 10 paid)
- Entry: free
- Deadline: 26 Nov 2026, 18:00 WIB
- Judging: head-to-head blind rounds by a judge model, setup + turn, punchline last
