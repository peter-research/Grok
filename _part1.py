"""Part 1 — version, quotes and small text helpers."""

from __future__ import annotations

import base64
import hashlib
import random
import string
import sys
import uuid
from collections import Counter
from datetime import date, datetime
from math import log2

VERSION = "0.33.0"

QUOTES = [
    "Understand the universe. Then maybe have a snack.",
    "Curiosity is a feature, not a bug.",
    "He does what he wants — within the rules of the playground.",
    "Small tools, shipped often, beat grand plans that never leave the editor.",
]

FORTUNES = [
    "A commit a day keeps the bitrot away.",
    "The next idea is already in the last bug.",
    "Ship the small thing.",
]

JOKES = [
    "Why did the function cross the road? To get to the other side-effect.",
    "There are 10 kinds of people: those who grok binary and those who do not.",
]

TIPS = [
    "Prefer a test you can run in one command.",
    "Name commands after what they do, not how they feel.",
]

IDEAS = [
    "A CLI that only ever grows by five commands at a time.",
    "A landing page that mirrors the CLI without a build step.",
]


def rot13(text: str) -> str:
    table = str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
        "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm",
    )
    return text.translate(table)


def slugify(text: str) -> str:
    out = []
    dash = False
    for c in text.lower():
        if c.isalnum():
            out.append(c)
            dash = False
        elif out and not dash:
            out.append("-")
            dash = True
    s = "".join(out).strip("-")
    return s or "item"


def is_palindrome(text: str) -> bool:
    chars = [c.lower() for c in text if c.isalnum()]
    if not chars:
        return False
    return chars == chars[::-1]


def pick_one(items):
    return random.choice(list(items))


def sample_n(items, n):
    items = list(items)
    n = min(n, len(items))
    return random.sample(items, n)


def shuffle_text(text: str) -> str:
    parts = text.split()
    random.shuffle(parts)
    return " ".join(parts)


def reverse_text(text: str) -> str:
    return text[::-1]


def hash_text(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def make_uuid() -> str:
    return str(uuid.uuid4())


def to_upper(text: str) -> str:
    return text.upper()


def to_lower(text: str) -> str:
    return text.lower()


def word_list(text: str):
    return text.split()


def line_list(text: str):
    return text.splitlines() or ([""] if text == "" else [])


def sort_lines(text: str) -> str:
    lines = text.splitlines()
    lines.sort()
    return "\n".join(lines)


def dedupe_lines(text: str) -> str:
    seen = set()
    out = []
    for line in text.splitlines():
        if line not in seen:
            seen.add(line)
            out.append(line)
    return "\n".join(out)


def join_words(text: str, sep: str = ",") -> str:
    return sep.join(text.split())


def split_sep(text: str, sep: str) -> str:
    return "\n".join(text.split(sep))


def is_anagram(a: str, b: str) -> bool:
    norm = lambda s: sorted(c.lower() for c in s if c.isalnum())
    return bool(norm(a)) and norm(a) == norm(b)


def initials(text: str) -> str:
    return "".join(w[0].upper() for w in text.split() if w)


def indent_text(text: str, n: int = 2) -> str:
    pad = " " * max(0, n)
    return "\n".join(pad + line for line in text.splitlines())


def percent_of(part: float, whole: float) -> float:
    if whole == 0:
        raise ValueError("zero")
    return 100.0 * part / whole


def clamp_num(x: float, lo: float, hi: float) -> float:
    if lo > hi:
        lo, hi = hi, lo
    return min(max(x, lo), hi)


def repeat_text(text: str, n: int) -> str:
    if n < 0 or n > 200:
        raise ValueError("range")
    return text * n
