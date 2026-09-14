#!/usr/bin/env python3
"""Tiny original playground CLI for the Grok repository."""
from __future__ import annotations

import argparse
import base64
import hashlib
import math
import random
import sys
import uuid
from datetime import datetime, timezone

VERSION = "0.23.0"

LINES = [
    "Understand the universe. Then maybe have a snack.",
    "Curiosity is a feature, not a bug.",
    "He does what he wants — within the rules of the playground.",
]
FORTUNES = ["Today is a good day to read the source.", "A small command today, a better repo tomorrow."]
JOKES = ["Why did the function cross the road? To get to the other side effect."]
WHYS = ["Because understanding beats guessing, most of the time."]
IDEAS = ["Document a command that does not exist yet, then invent it."]
TIPS = ["Ship the smallest useful change, then iterate."]

COMMAND_NAMES = [
    "greet", "quote", "fortune", "joke", "why", "idea", "tip", "flip", "dice",
    "color", "now", "week", "day", "echo", "version", "about", "check", "rot13",
    "slug", "hash", "uuid", "palindrome", "pick", "sample", "shuffle", "reverse",
    "count", "wrap", "b64", "sum", "title", "upper", "lower", "words", "lines",
    "chars", "sort", "dedupe", "join", "split", "anagram", "initials", "indent",
    "percent", "clamp", "random", "commands", "repeat", "morse", "unique", "yesno",
    "leet", "vowels", "bin", "hex", "caesar", "consonants", "pig", "ascii",
    "snake", "camel", "nato", "freq", "entropy", "lev", "rle", "box", "roman",
    "unroman", "isogram", "tap", "fib", "prime", "gcd", "lcm", "unrle", "fact",
    "mean", "median", "revwords", "factors",
]

LEET_MAP = str.maketrans("aAeEoOtTlLsS", "443300771155")
VOWELS = set("aeiouyAEIOUY")
NATO = {
    "a": "Alfa", "b": "Bravo", "c": "Charlie", "d": "Delta", "e": "Echo",
    "f": "Foxtrot", "g": "Golf", "h": "Hotel", "i": "India", "j": "Juliett",
    "k": "Kilo", "l": "Lima", "m": "Mike", "n": "November", "o": "Oscar",
    "p": "Papa", "q": "Quebec", "r": "Romeo", "s": "Sierra", "t": "Tango",
    "u": "Uniform", "v": "Victor", "w": "Whiskey", "x": "X-ray", "y": "Yankee",
    "z": "Zulu",
}
MORSE = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
    "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
    "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
    "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
    "y": "-.--", "z": "--..", "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",
}
ROMAN_PAIRS = (
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
    (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
    (5, "V"), (4, "IV"), (1, "I"),
)


def pick(seq):
    return random.choice(seq)


def require(text, name):
    if text is None or text == "":
        print(f"{name}: pass some text", file=sys.stderr)
        sys.exit(1)
    return text


def items_required(items, name):
    if not any(x.strip() for x in items):
        print(f"{name}: pass at least one item", file=sys.stderr)
        sys.exit(1)
    return [x for x in items if x.strip()]


def rot13(text):
    return "".join(
        chr((ord(c) - 97 + 13) % 26 + 97) if "a" <= c <= "z"
        else chr((ord(c) - 65 + 13) % 26 + 65) if "A" <= c <= "Z"
        else c
        for c in text
    )


def slugify(text):
    out = []
    dash = False
    for c in text.lower():
        if c.isalnum():
            out.append(c)
            dash = False
        elif out and not dash:
            out.append("-")
            dash = True
    if out and out[-1] == "-":
        out.pop()
    return "".join(out) or "item"


def is_palindrome(t):
    c = [x.casefold() for x in t if x.isalnum()]
    return bool(c) and c == c[::-1]


def count_text(t):
    return len(t), len(t.split()), t.count("\n") + (1 if t else 0)


def title_case(t):
    return "".join(
        c.upper() if c.isalnum() and (i == 0 or not t[i - 1].isalnum())
        else c.lower() if c.isalnum() else c
        for i, c in enumerate(t)
    )


def wrap_text(text, width):
    if width < 8:
        raise ValueError("width")
    words = text.split()
    if not words:
        return text
    lines = []
    current = words[0]
    for word in words[1:]:
        if len(current) + 1 + len(word) <= width:
            current = f"{current} {word}"
        else:
            lines.append(current)
            current = word
    lines.append(current)
    return "\n".join(lines)


def nth_fib(n):
    if n < 0 or n > 92:
        raise ValueError("range")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def gcd_int(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm_int(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd_int(a, b) * b)


def run_rle(text):
    if not text:
        return ""
    out = []
    n = 1
    for i in range(1, len(text) + 1):
        if i < len(text) and text[i] == text[i - 1]:
            n += 1
        else:
            out.append((str(n) if n > 1 else "") + text[i - 1])
            n = 1
    return "".join(out)


def undo_rle(text):
    out = []
    i = 0
    n = len(text)
    while i < n:
        if text[i].isdigit():
            j = i
            while j < n and text[j].isdigit():
                j += 1
            if j == n:
                raise ValueError("bad")
            count = int(text[i:j])
            if count < 1 or count > 200:
                raise ValueError("bad")
            out.append(text[j] * count)
            i = j + 1
        else:
            out.append(text[i])
            i += 1
    return "".join(out)


def factorial_int(n):
    if n < 0 or n > 20:
        raise ValueError("range")
    v = 1
    for i in range(2, n + 1):
        v *= i
    return v


def mean_nums(vals):
    return sum(vals) / len(vals)


def median_nums(vals):
    s = sorted(vals)
    n = len(s)
    mid = n // 2
    if n % 2:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2


def reverse_words(text):
    return " ".join(text.split()[::-1])


def factor_list(n):
    if n < 1 or n > 1_000_000:
        raise ValueError("range")
    out = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            out.append(i)
            if i * i != n:
                out.append(n // i)
        i += 1
    return sorted(out)


def to_roman(n):
    if n < 1 or n > 3999:
        raise ValueError("range")
    out = []
    for value, symbol in ROMAN_PAIRS:
        while n >= value:
            out.append(symbol)
            n -= value
    return "".join(out)


def from_roman(text):
    raw = text.upper().strip()
    if not raw:
        raise ValueError("bad")
    i = 0
    total = 0
    for value, symbol in ROMAN_PAIRS:
        while raw.startswith(symbol, i):
            total += value
            i += len(symbol)
    if i != len(raw) or to_roman(total) != raw:
        raise ValueError("bad")
    return total


def to_snake(text):
    out = []
    for i, c in enumerate(text):
        if c.isupper() and i and (text[i - 1].islower() or (i + 1 < len(text) and text[i + 1].islower())):
            out.append("_")
        if c.isalnum():
            out.append(c.lower())
        elif out and out[-1] != "_":
            out.append("_")
    return "".join(out).strip("_")


def to_camel(text):
    parts = [p for p in slugify(text).split("-") if p]
    if not parts:
        return ""
    return parts[0] + "".join(p[:1].upper() + p[1:] for p in parts[1:])


def caesar(text, shift):
    shift = shift % 26
    out = []
    for c in text:
        if "a" <= c <= "z":
            out.append(chr((ord(c) - 97 + shift) % 26 + 97))
        elif "A" <= c <= "Z":
            out.append(chr((ord(c) - 65 + shift) % 26 + 65))
        else:
            out.append(c)
    return "".join(out)


def pig_latin(word):
    if not word:
        return word
    prefix = ""
    core = word
    while core and not core[0].isalpha():
        prefix += core[0]
        core = core[1:]
    suffix = ""
    while core and not core[-1].isalpha():
        suffix = core[-1] + suffix
        core = core[:-1]
    if not core:
        return word
    cap = core[0].isupper()
    low = core.lower()
    if low[0] in "aeiouy":
        body = low + "way"
    else:
        i = 0
        while i < len(low) and low[i] not in "aeiouy":
            i += 1
        body = low[i:] + low[:i] + "ay"
    if cap:
        body = body[:1].upper() + body[1:]
    return prefix + body + suffix


def lev_dist(a, b):
    if len(a) > 80 or len(b) > 80:
        raise ValueError("range")
    if a == b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            ins = cur[j - 1] + 1
            delete = prev[j] + 1
            sub = prev[j - 1] + (ca != cb)
            cur.append(min(ins, delete, sub))
        prev = cur
    return prev[-1]


def shannon(text):
    if not text:
        return 0.0
    freq = {}
    for c in text:
        freq[c] = freq.get(c, 0) + 1
    n = len(text)
    return -sum((c / n) * math.log2(c / n) for c in freq.values())


def tap_code(text):
    letters = "abcdefghijlmnopqrstuvwxyz"
    grid = {ch: (i // 5 + 1, i % 5 + 1) for i, ch in enumerate(letters)}
    grid["k"] = grid["c"]
    out = []
    for c in text.lower():
        if c in grid:
            r, col = grid[c]
            out.append("." * r + " " + "." * col)
    return " / ".join(out)


def box_text(text):
    lines = text.split("\n") or [""]
    w = max(len(line) for line in lines)
    top = "+" + "-" * (w + 2) + "+"
    mid = "\n".join("| " + line.ljust(w) + " |" for line in lines)
    return f"{top}\n{mid}\n{top}"


def parse_int(raw, name, lo=None, hi=None):
    try:
        v = int(require(raw, name))
    except ValueError:
        print(f"{name}: need an integer", file=sys.stderr)
        sys.exit(1)
    if (lo is not None and v < lo) or (hi is not None and v > hi):
        print(f"{name}: out of range", file=sys.stderr)
        sys.exit(1)
    return v


def fmt_num(r):
    return str(int(r)) if float(r).is_integer() else format(r, "g")


def cmd_greet(name):
    print(f"Hello, {name.strip() if name and name.strip() else 'friend'}. He does what he wants.")


def cmd_quote():
    print(pick(LINES))


def cmd_version():
    print(VERSION)


def cmd_about():
    print(f"Grok playground CLI v{VERSION}\nOriginal code only. Stdlib only.\nRepo: https://github.com/peter-research/Grok")


def cmd_commands():
    print("\n".join(COMMAND_NAMES))


def cmd_check():
    assert len(COMMAND_NAMES) == len(set(COMMAND_NAMES)) == 81
    assert rot13(rot13("Hello, Grok!")) == "Hello, Grok!"
    assert slugify("Hello, Grok!") == "hello-grok"
    assert is_palindrome("Race car") and not is_palindrome("Grok")
    assert count_text("one two") == (7, 2, 1)
    assert title_case("hello grok") == "Hello Grok"
    assert wrap_text("one two three four", 10) == "one two\nthree four"
    assert nth_fib(10) == 55
    assert is_prime(13) and not is_prime(1)
    assert gcd_int(54, 24) == 6
    assert lcm_int(4, 6) == 12
    assert undo_rle("3a2bc") == "aaabbc"
    assert run_rle("aaabbc") == "3a2bc"
    assert factorial_int(5) == 120
    assert mean_nums([1, 2, 3]) == 2
    assert median_nums([1, 3, 2]) == 2
    assert reverse_words("hello grok") == "grok hello"
    assert factor_list(12) == [1, 2, 3, 4, 6, 12]
    assert to_roman(2026) == "MMXXVI"
    assert from_roman("MMXXVI") == 2026
    assert to_snake("HelloGrok") == "hello_grok"
    assert to_camel("hello grok") == "helloGrok"
    assert caesar("abc", 1) == "bcd"
    assert lev_dist("kitten", "sitting") == 3
    print("check ok")


def build_parser():
    p = argparse.ArgumentParser(prog="grok.py", description="Tiny original playground CLI for the Grok repository.")
    s = p.add_subparsers(dest="cmd")
    g = s.add_parser("greet")
    g.add_argument("name", nargs="?")
    for n in (
        "quote", "fortune", "joke", "why", "idea", "tip", "flip", "dice", "color",
        "now", "week", "day", "version", "about", "check", "uuid", "commands", "yesno",
    ):
        s.add_parser(n)
    for n in (
        "echo", "rot13", "slug", "hash", "palindrome", "reverse", "count", "b64",
        "title", "upper", "lower", "words", "lines", "chars", "anagram", "initials",
        "indent", "repeat", "morse", "leet", "vowels", "bin", "hex", "consonants",
        "pig", "ascii", "snake", "camel", "nato", "freq", "entropy", "rle", "box",
        "roman", "unroman", "isogram", "tap", "fib", "prime", "unrle", "fact",
        "revwords", "factors", "wrap", "caesar",
    ):
        q = s.add_parser(n)
        q.add_argument("text", nargs="?")
        if n in ("wrap", "caesar", "repeat", "indent"):
            q.add_argument("n", nargs="?")
    for n in (
        "mean", "median", "gcd", "lcm", "pick", "sample", "shuffle", "sum",
        "sort", "dedupe", "join", "split", "unique", "percent", "clamp", "random", "lev",
    ):
        q = s.add_parser(n)
        q.add_argument("items", nargs="*")
    return p


def main(argv=None):
    a = build_parser().parse_args(argv)
    if a.cmd is None:
        cmd_greet(None)
        cmd_quote()
        return 0

    def text():
        return require(getattr(a, "text", None), a.cmd)

    def items():
        return items_required(getattr(a, "items", []), a.cmd)

    h = {
        "greet": lambda: cmd_greet(a.name),
        "quote": cmd_quote,
        "fortune": lambda: print(pick(FORTUNES)),
        "joke": lambda: print(pick(JOKES)),
        "why": lambda: print(pick(WHYS)),
        "idea": lambda: print(pick(IDEAS)),
        "tip": lambda: print(pick(TIPS)),
        "flip": lambda: print("heads" if random.random() < 0.5 else "tails"),
        "dice": lambda: print(random.randint(1, 6)),
        "color": lambda: print(f"#{random.randint(0, 0xFFFFFF):06x}"),
        "now": lambda: print(datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")),
        "week": lambda: print(datetime.now(timezone.utc).strftime("%G-W%V")),
        "day": lambda: print(datetime.now(timezone.utc).strftime("%A")),
        "echo": lambda: print(text()),
        "version": cmd_version,
        "about": cmd_about,
        "check": cmd_check,
        "rot13": lambda: print(rot13(text())),
        "slug": lambda: print(slugify(text())),
        "hash": lambda: print(hashlib.sha256(text().encode()).hexdigest()),
        "uuid": lambda: print(uuid.uuid4()),
        "palindrome": lambda: print("yes" if is_palindrome(text()) else "no"),
        "pick": lambda: print(pick(items())),
        "sample": lambda: print(" ".join(random.sample(it := items(), min(3, len(it))))),
        "shuffle": lambda: print(" ".join(random.sample(it := items(), len(it)))),
        "reverse": lambda: print(text()[::-1]),
        "count": lambda: (lambda c: print(f"{c[0]} {c[1]} {c[2]}"))(count_text(text())),
        "wrap": lambda: print(wrap_text(text(), parse_int(a.n or "40", "wrap", 8, 120))),
        "b64": lambda: print(base64.b64encode(text().encode()).decode()),
        "sum": lambda: print(fmt_num(sum(float(x) for x in items()))),
        "title": lambda: print(title_case(text())),
        "upper": lambda: print(text().upper()),
        "lower": lambda: print(text().lower()),
        "words": lambda: print(len(text().split())),
        "lines": lambda: print(count_text(text())[2]),
        "chars": lambda: print(len(text())),
        "sort": lambda: print("\n".join(sorted(items()))),
        "dedupe": lambda: print("\n".join(dict.fromkeys(items()))),
        "join": lambda: print(" ".join(items())),
        "split": lambda: print("\n".join(items()[0].split() if len(items()) == 1 else items())),
        "anagram": lambda: print("".join(random.sample(t := list(text()), len(t)))),
        "initials": lambda: print("".join(w[0].upper() for w in text().split() if w)),
        "indent": lambda: print("\n".join(" " * parse_int(a.n or "2", "indent", 0, 16) + line for line in text().split("\n"))),
        "percent": lambda: (lambda it: print(fmt_num(100 * float(it[0]) / float(it[1]))))(items()),
        "clamp": lambda: (lambda it: print(fmt_num(min(max(float(it[0]), float(it[1])), float(it[2])))))(items()),
        "random": lambda: (lambda it: print(random.randint(int(it[0]), int(it[1]))))(items()),
        "commands": cmd_commands,
        "repeat": lambda: print((text() + "\n") * parse_int(a.n or "2", "repeat", 1, 20), end=""),
        "morse": lambda: print(" ".join(MORSE[c] for c in text().lower() if c in MORSE)),
        "unique": lambda: print("\n".join(dict.fromkeys(items()))),
        "yesno": lambda: print(pick(["yes", "no"])),
        "leet": lambda: print(text().translate(LEET_MAP)),
        "vowels": lambda: print(sum(1 for c in text() if c in VOWELS)),
        "bin": lambda: print(bin(parse_int(getattr(a, "text", None), "bin"))),
        "hex": lambda: print(hex(parse_int(getattr(a, "text", None), "hex"))),
        "caesar": lambda: print(caesar(text(), parse_int(a.n or "13", "caesar"))),
        "consonants": lambda: print(sum(1 for c in text() if c.isalpha() and c not in VOWELS)),
        "pig": lambda: print(" ".join(pig_latin(w) for w in text().split())),
        "ascii": lambda: print(" ".join(str(ord(c)) for c in text())),
        "snake": lambda: print(to_snake(text())),
        "camel": lambda: print(to_camel(text())),
        "nato": lambda: print(" ".join(NATO[c] for c in text().lower() if c in NATO)),
        "freq": lambda: print(" ".join(f"{k}:{v}" for k, v in sorted({c: text().count(c) for c in set(text())}.items()) if k.strip())),
        "entropy": lambda: print(format(shannon(text()), ".4f")),
        "lev": lambda: (lambda it: print(lev_dist(it[0], it[1] if len(it) > 1 else "")))(items()),
        "rle": lambda: print(run_rle(text())),
        "box": lambda: print(box_text(text())),
        "roman": lambda: print(to_roman(parse_int(getattr(a, "text", None), "roman", 1, 3999))),
        "unroman": lambda: print(from_roman(text())),
        "isogram": lambda: print("yes" if len(s := [c.casefold() for c in text() if c.isalpha()]) == len(set(s)) and s else "no"),
        "tap": lambda: print(tap_code(text())),
        "fib": lambda: print(nth_fib(parse_int(getattr(a, "text", None), "fib", 0, 92))),
        "prime": lambda: print("yes" if is_prime(parse_int(getattr(a, "text", None), "prime")) else "no"),
        "gcd": lambda: print(gcd_int(int(items()[0]), int(items()[1]))),
        "lcm": lambda: print(lcm_int(int(items()[0]), int(items()[1]))),
        "unrle": lambda: print(undo_rle(text())),
        "fact": lambda: print(factorial_int(parse_int(getattr(a, "text", None), "fact", 0, 20))),
        "mean": lambda: print(fmt_num(mean_nums([float(x) for x in items()]))),
        "median": lambda: print(fmt_num(median_nums([float(x) for x in items()]))),
        "revwords": lambda: print(reverse_words(text())),
        "factors": lambda: print(" ".join(str(x) for x in factor_list(parse_int(getattr(a, "text", None), "factors", 1, 1_000_000)))),
    }
    try:
        h[a.cmd]()
    except (ValueError, IndexError, ZeroDivisionError):
        print(f"{a.cmd}: bad input", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
