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

See `python3 grok.py commands` for the full list. New in v0.22: advertised helpers are now wired as commands.

```bash
python3 grok.py fact 5
python3 grok.py mean 1 2 3
python3 grok.py median 1 3 2 4
python3 grok.py revwords "hello grok"
python3 grok.py factors 12
python3 grok.py fib 10
python3 grok.py prime 13
python3 grok.py gcd 54 24
python3 grok.py lcm 4 6
python3 grok.py rot13 "Hello, Grok!"
python3 grok.py slug "Hello, Grok!"
python3 grok.py check
```

`check` runs a few local sanity tests and prints `check ok` when they pass.

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
