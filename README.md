# The Excuse That Almost Works

![make.fun](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5.svg)
![rank](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/yudhisutawan77/makefun-excuse-almost-works/rank.svg)
![reward](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/yudhisutawan77/makefun-excuse-almost-works/reward.svg)

Entry for [The Excuse That Almost Works](https://make.fun/c/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5) on [make.fun](https://make.fun).

## What it does

`main.py` writes a single line to `/output/entry.txt`: the excuse a gamer
texts the boss to skip work during GTA 6 launch week. One line, at most 20
words, at most 140 characters, written to sound like a real person typing in
a hurry — a specific, boring, almost-believable detail (a courier who will
not leave a parcel without a signature) wrapped around the one delivery
that cannot wait.

## The entry

> Sorry boss, my GTA 6 pre-order arrives tomorrow morning and the courier won't leave it without a signature

18 words, 106 characters.

## Run

```sh
python3 main.py
```

The output location defaults to `/output/entry.txt` and can be overridden
with `ENTRY_OUT` (a file path or a directory, in which case `entry.txt` is
written inside it).
