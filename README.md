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

See `python3 grok.py commands` for the full list. v0.23 wires the advertised helpers as real commands (stdlib only).

```bash
python3 grok.py fact 5
python3 grok.py mean 1 2 3
python3 grok.py roman 2026
python3 grok.py snake HelloGrok
python3 grok.py caesar "Hello, Grok!" 13
python3 grok.py rle aaabbc
python3 grok.py prime 13
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
