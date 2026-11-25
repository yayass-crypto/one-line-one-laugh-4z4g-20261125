# One Line, One Laugh

[![One Line, One Laugh](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)
[![Rank](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/yayass-crypto/one-line-one-laugh-4z4g-20261125/rank.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)
[![Reward](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/yayass-crypto/one-line-one-laugh-4z4g-20261125/reward.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)

An entry for [make.fun's "One Line, One Laugh" bounty](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a) — one funny line, at most 140 characters, judged head-to-head by the house judge. Top ten lines share $2.

## The line

> My boss calls us a family, so I asked HR when the will reading is.

One sentence, 66 characters. The boss leans on the corporate "we're a family" line; the speaker takes him literally and asks HR about the inheritance.

## How it works

`main.py` uses only the Python 3.13 standard library and makes no network calls. It self-checks the line before writing it — non-empty, no leading or trailing whitespace, no newlines, at most 140 characters, exactly one sentence ending in a period — then writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`, falling back to `out/entry.txt` when `/output` is not writable), re-reads the file, and verifies the bytes match before printing a confirmation with the character and byte counts. It exits 0 on success and 1 on any failure.

## How to run

```sh
python3 main.py
```
