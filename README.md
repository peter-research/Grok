# Grok

Grok repository — he does what he wants.

A small playground connected to Grok (xAI). The point is not a product.
The point is a repo Grok can improve, experiment with, and push to.

## What is here

| Path | Role |
| --- | --- |
| `grok.py` | Loader that concatenates `_part*.py` (stdlib only) |
| `_part1.py` … `_part11.py` | Original CLI pieces |
| `index.html` | One-page landing, no dependencies |
| `test_grok.py` | Stdlib unit tests |
| `CONTRIBUTING.md` | How to play with this repo |
| `LICENSE` | Mozilla Public License 2.0 |

Nothing here is copied from another project. No third-party libraries.

## Run the CLI

Needs Python 3. No packages.

See `python3 grok.py commands` for the full list. v0.34 reaches 135 commands and adds hypot, lcm, isqrt, median and powint.

```bash
python3 grok.py fact 5
python3 grok.py mean 1 2 3
python3 grok.py weekday 2026-09-15
python3 grok.py kebab Hello Grok
python3 grok.py pascal hello grok
python3 grok.py perfect 28
python3 grok.py julian 2026-09-15
python3 grok.py isbn 0-306-40615-2
python3 grok.py oct 64
python3 grok.py pangram The quick brown fox jumps over the lazy dog
python3 grok.py until 2026-12-31
python3 grok.py droot 38
python3 grok.py bits 13
python3 grok.py isbn13 978-0-306-40615-7
python3 grok.py leap 2024
python3 grok.py swap Hello
python3 grok.py c2f 100
python3 grok.py abundant 12
python3 grok.py f2c 212
python3 grok.py deficient 8
python3 grok.py square 16
python3 grok.py cube 3
python3 grok.py mid Grok
python3 grok.py sign -7
python3 grok.py even 8
python3 grok.py odd 9
python3 grok.py abs -12
python3 grok.py revint 120
python3 grok.py palnum 121
python3 grok.py digits 120
python3 grok.py prod 2 3 4
python3 grok.py minn 3 1 8
python3 grok.py maxn 3 1 8
python3 grok.py floor 3.7
python3 grok.py ceil 3.2
python3 grok.py roundn 3.14159 2
python3 grok.py mod 10 3
python3 grok.py coprime 8 15
python3 grok.py hypot 3 4
python3 grok.py lcm 4 6
python3 grok.py isqrt 16
python3 grok.py median 1 3 2 4
python3 grok.py powint 2 10
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
