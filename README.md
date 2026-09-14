# Grok

Grok repository — he does what he wants.

A small playground connected to Grok (xAI). The point is not a product.
The point is a repo Grok can improve, experiment with, and push to.

## What is here

| Path | Role |
| --- | --- |
| `grok.py` | Tiny original CLI (stdlib only) |
| `index.html` | One-page landing, no dependencies |
| `test_grok.py` | Stdlib unit tests |
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
python3 grok.py day
python3 grok.py echo "hello playground"
python3 grok.py version
python3 grok.py about
python3 grok.py check
python3 grok.py rot13 "Hello"
python3 grok.py slug "Hello, Grok!"
python3 grok.py hash "Hello, Grok!"
python3 grok.py uuid
python3 grok.py palindrome "Race car"
python3 grok.py pick tea coffee water
python3 grok.py sample 2 tea coffee water juice
python3 grok.py shuffle tea coffee water
python3 grok.py reverse Grok
python3 grok.py count "hello world"
python3 grok.py wrap 20 "a short line that should wrap"
python3 grok.py b64 Grok
python3 grok.py b64 --decode R3Jvaw==
python3 grok.py sum 1 2 3.5
python3 grok.py title "hello grok"
python3 grok.py upper grok
python3 grok.py lower GROK
python3 grok.py words "hello grok"
python3 grok.py chars Grok
python3 grok.py sort tea coffee water
python3 grok.py dedupe tea tea coffee
python3 grok.py join tea coffee --sep " / "
python3 grok.py split "tea/coffee" --sep /
python3 grok.py anagram listen silent
python3 grok.py initials "Grok playground"
python3 grok.py indent "hello" --spaces 4
python3 grok.py percent 25 200
python3 grok.py clamp 120 0 100
python3 grok.py random 1 6
python3 grok.py repeat 3 ping
python3 grok.py morse "sos"
python3 grok.py unique bookkeeper
python3 grok.py yesno
python3 grok.py leet Grok
python3 grok.py vowels Grok
python3 grok.py bin A
python3 grok.py hex Grok
python3 grok.py commands
```

`check` runs a few local sanity tests and prints `check ok` when they pass.

New in v0.15: `leet`, `vowels`, `bin`, `hex`.

## Tests

```bash
make check
```

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
