# Grok

Grok repository — he does what he wants.

A small playground connected to Grok (xAI). The point is not a product.
The point is a repo Grok can improve, experiment with, and push to.

## What is here

| Path | Role |
| --- | --- |
| `grok.py` | Tiny original CLI: greet, quote, fortune, joke, why, idea, tip, flip, dice, color, now, week, version, about, check, rot13, slug, hash, uuid, palindrome, pick, shuffle, reverse, count, b64, sum, title, commands |
| `index.html` | One-page landing, no dependencies |
| `CONTRIBUTING.md` | How to play with this repo |
| `LICENSE` | Mozilla Public License 2.0 |

Nothing here is copied from another project. No third-party libraries.

## Run the CLI

Needs Python 3. No packages.

```bash
python3 grok.py
python3 grok.py greet Peter
python3 grok.py quote
python3 grok.py fortune
python3 grok.py joke
python3 grok.py why
python3 grok.py idea
python3 grok.py tip
python3 grok.py flip
python3 grok.py dice
python3 grok.py dice 20
python3 grok.py dice coin
python3 grok.py color
python3 grok.py now
python3 grok.py week
python3 grok.py version
python3 grok.py about
python3 grok.py check
python3 grok.py rot13 "Hello"
python3 grok.py slug "Hello, Grok!"
python3 grok.py hash "Hello, Grok!"
python3 grok.py uuid
python3 grok.py palindrome "Race car"
python3 grok.py pick tea coffee water
python3 grok.py shuffle tea coffee water
python3 grok.py reverse Grok
python3 grok.py count "hello world"
python3 grok.py b64 Grok
python3 grok.py b64 --decode R3Jvaw==
python3 grok.py sum 1 2 3.5
python3 grok.py title "hello grok"
python3 grok.py commands
```

`check` runs a few local sanity tests and prints `check ok` when they pass.

`dice` accepts an integer (sides) or the word `coin` (same as `flip`).

`color` prints a random hex colour (e.g. `#a3f1c2`).

`week` prints the ISO week in UTC (`YYYY-Www-d`).

`rot13` rotates letters by 13 (and back again if you run it twice).

`slug` turns text into a lowercase hyphenated token.

`hash` prints the SHA-256 hex digest of the given text.

`uuid` prints a random UUID4.

`palindrome` prints `yes` or `no` after ignoring case and punctuation.

`pick` chooses one of the arguments at random.

`shuffle` prints the arguments in a random order.

`reverse` prints the text backwards.

`count` prints character, word and line counts.

`b64` encodes text as Base64. Pass `--decode` to go the other way.

`sum` adds the given numbers and prints the total.

`title` title-cases the given text.

`commands` lists the public command names.

## Open the page

Open `index.html` in a browser. That is all.

## Rules of the playground

- Stay on theme: a Grok sandbox, not a random unrelated app.
- Original code only.
- No illegal content.
- Do not paste licensed third-party source into this tree.

## Owner
Hello, i'm not Grok but Peter. Consider Star the repo, this project cost me line hundred dollars a month (SuperGrok Heavy), so all the support is great ❤️
[peter-research](https://github.com/peter-research)
