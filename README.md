# Grok

Grok repository — he does what he wants.

A small playground connected to Grok (xAI). The point is not a product.
The point is a repo Grok can improve, experiment with, and push to.

## What is here

| Path | Role |
| --- | --- |
| `grok.py` | Loader that concatenates `_part*.py` (stdlib only) |
| `_part1.py` … `_part6.py` | Original CLI pieces |
| `index.html` | One-page landing, no dependencies |
| `test_grok.py` | Stdlib unit tests |
| `CONTRIBUTING.md` | How to play with this repo |
| `LICENSE` | Mozilla Public License 2.0 |

Nothing here is copied from another project. No third-party libraries.

## Run the CLI

Needs Python 3. No packages.

See `python3 grok.py commands` for the full list. v0.27 reaches 100 commands and adds kebab, pascal, perfect, julian and isbn.

```bash
python3 grok.py fact 5
python3 grok.py mean 1 2 3
python3 grok.py weekday 2026-09-15
python3 grok.py kebab Hello Grok
python3 grok.py pascal hello grok
python3 grok.py perfect 28
python3 grok.py julian 2026-09-15
python3 grok.py isbn 0-306-40615-2
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
