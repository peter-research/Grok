# Grok

Grok repository — he does what he wants.

A small playground connected to Grok (xAI). The point is not a product.
The point is a repo Grok can improve, experiment with, and push to.

## What is here

| Path | Role |
| --- | --- |
| `grok.py` | Loader that concatenates `_part*.py` (stdlib only) |
| `_part1.py` … `_part18.py` | Original CLI pieces |
| `index.html` | One-page landing, no dependencies |
| `test_grok.py` | Stdlib unit tests |
| `CONTRIBUTING.md` | How to play with this repo |
| `LICENSE` | Mozilla Public License 2.0 |

Nothing here is copied from another project. No third-party libraries.

## Run the CLI

Needs Python 3. No packages.

See `python3 grok.py commands` for the full list. v0.41 ships 165 unique commands and adds smith, automorphic, lucas, squarefree and duck. The loader now runs `main` only after every part is loaded, so new commands actually work from the CLI.

```bash
python3 grok.py smith 22
python3 grok.py automorphic 25
python3 grok.py lucas 5
python3 grok.py squarefree 10
python3 grok.py duck 101
python3 grok.py happy 19
python3 grok.py catalan 5
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
