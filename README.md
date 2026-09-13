# Grok

Grok repository — he does what he wants.

A small playground connected to Grok (xAI). The point is not a product.
The point is a repo Grok can improve, experiment with, and push to.

## What is here

| Path | Role |
| --- | --- |
| `grok.py` | Tiny original CLI: greet, quote, fortune, joke, why, idea, tip, flip, dice, color, now, weekday, pick, hash, version, about, check |
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
python3 grok.py weekday
python3 grok.py pick red green blue
python3 grok.py hash grok
python3 grok.py version
python3 grok.py about
python3 grok.py check
```

`check` runs a few local sanity tests and prints `check ok` when they pass.

`dice` accepts an integer (sides) or the word `coin` (same as `flip`).

`color` prints a random hex colour (e.g. `#a3f1c2`).

`weekday` prints the current UTC weekday.

`pick` chooses one of the words you pass. With no words it falls back to a quote.

`hash` prints the SHA-256 hex fingerprint of the given text (stdlib `hashlib`). It is a fingerprint, not a secret store.

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
