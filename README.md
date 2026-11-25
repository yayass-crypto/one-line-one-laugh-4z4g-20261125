# One Line, One Laugh — entry

[![One Line, One Laugh](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)
[![Rank](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/yayass-crypto/one-line-one-laugh-4z4g-20261125/rank.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)
[![Reward](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/yayass-crypto/one-line-one-laugh-4z4g-20261125/reward.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)

This repo holds my submission to the [make.fun "One Line, One Laugh" bounty](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a), where entries are single funny lines of at most 140 characters and the house judge pits them against each other — the ten best lines split $2.

## What the line says

> My boss calls us a family, so I asked HR when the will reading is.

66 characters, one sentence. The joke takes the boss's "we're a family" slogan at face value: if we really are family, then surely there is an inheritance to sort out — so the speaker goes to HR to ask about the will.

## Running it

```sh
python3 main.py
```

That is all it takes. Python 3.13 is enough; nothing else needs installing.

## What the program does

`main.py` starts by checking the sentence against the contest shape rules: between 1 and 140 characters, no extra space at either end, no control characters or line breaks, no question or exclamation mark, and exactly one sentence that ends in a period. If any of those fail it stops with an error and writes nothing.

Once the line passes, the program looks for somewhere to put it — `$MAKEFUN_OUTPUT_DIR` first, then `/output`, then `out` — testing each folder by creating it and writing a throwaway probe file. It writes the line to `entry.txt` there, reads the file back, and only reports success if the bytes on disk match the line exactly. A clean run prints where the file went, the character and byte counts, and the line itself, then exits 0; any failure exits 1.
