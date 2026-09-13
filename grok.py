#!/usr/bin/env python3
"""Tiny original playground CLI for peter-research/Grok."""

from __future__ import annotations

import argparse
import hashlib
import random
import sys
from datetime import datetime, timezone

VERSION = "0.7.0"

QUOTES = (
    "Understand the universe. Then maybe have a snack.",
    "Curiosity is a feature, not a bug.",
    "If the repo is empty, fill it with something honest.",
    "Ask better questions. The answers follow.",
    "He does what he wants — within the rules of the playground.",
    "Small original tools beat giant copied ones.",
    "A sandbox is useful when you actually play in it.",
    "Code that stays readable is a kindness to future you.",
    "The best commit is the one that makes the next one easier.",
    "Silence is fine. A clear error message is better.",
    "Ship the small thing. The large thing can wait.",
    "A good name is half the design.",
    "Play first. Polish second. Delete third if needed.",
    "A short function is easier to trust than a clever one.",
    "Read the code before you change the code.",
    "A playground without play is just a directory.",
    "Clarity compounds faster than cleverness.",
    "Leave room for the next person — it might be you.",
    "A quiet tool that works beats a loud one that almost works.",
    "Keep the surface small so the depth can breathe.",
    "An honest failure message is more useful than a polite silence.",
    "A hash is not a secret. It is a fingerprint you can show.",
    "Pick one thing. Then pick the next thing. That is still progress.",
    "The next line you write is the only one that matters right now.",
)
FORTUNES = (
    "Today is a good day to read the source.",
    "The next question is better than the last answer.",
    "Push something small. Then push something smaller.",
    "The universe is large. This CLI is not. That is fine.",
    "Leave the repo better than you found it.",
    "A clean diff is a quiet gift.",
    "If it runs without drama, keep it that way.",
    "When in doubt, print the type and move on.",
    "One honest commit is worth ten half-finished branches.",
    "The best time to add a check is before you need it.",
    "Keep the interface small and the behaviour clear.",
    "Delete the clever bit if the simple bit works.",
    "The next push does not have to be perfect. It has to be better.",
    "A weekday is just a label. The work is the same either way.",
    "A one-line fix can still deserve a careful message.",
    "A colour that looks good in the dark is worth keeping.",
)
JOKES = (
    "Why did the function cross the road? To get to the other side effect.",
    "I told my code a joke about recursion. It laughed until the stack overflowed.",
    "A SQL query walks into a bar, approaches two tables, and asks: may I join you?",
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "I would tell you a UDP joke, but you might not get it.",
    "There is no place like 127.0.0.1.",
    "A programmer's favourite place? The foo bar.",
    "Why do Python programmers wear glasses? Because they can't C.",
    "How many programmers does it take to change a light bulb? None, that is a hardware problem.",
    "I asked the hash for a secret. It gave me 64 hex digits and called it a day.",
    "Debugging is like being the detective in a crime movie where you are also the murderer.",
    "A byte walks into a bar and orders a pint. The bartender says: sorry, we don't serve doubles.",
    "There are only two hard things: cache invalidation, naming things, and off-by-one errors.",
)
WHYS = (
    "Because understanding beats guessing, most of the time.",
    "Because a clear question is already half an answer.",
    "Because small experiments teach faster than big plans.",
    "Because the playground only works if someone plays.",
    "Because original code is easier to own than borrowed complexity.",
    "Because curiosity compounds.",
    "Because a short loop is better than a long explanation.",
    "Because the next person who reads this might be you.",
    "Because a good name saves ten comments.",
    "Because shipping something small is still shipping.",
    "Because a quiet improvement is still an improvement.",
    "Because a fingerprint of a string is sometimes all you needed.",
)
IDEAS = (
    "Add one more original line to the quotes list.",
    "Make the self-check a little stricter.",
    "Document a command that does not exist yet, then invent it.",
    "Write a fortune that mentions the commit message.",
    "Make the dice command accept a word like coin and still work.",
    "Trim a function that grew longer than it needed to be.",
    "Sync one list between the CLI and the HTML so they stay friends.",
    "Add a tip that is useful even if you ignore the rest.",
    "Add a colour command that returns a random hex.",
    "Keep the HTML and the CLI lists within a few lines of each other.",
    "Add a pick command that chooses one of the words you pass it.",
    "Give the landing page a quieter colour accent.",
    "Add a tiny test that the version string still looks like a version.",
)
TIPS = (
    "Name the thing after what it does, not how it feels.",
    "Prefer a boring solution that works over a clever one that almost works.",
    "Write the check before you need the failure message.",
    "Delete the comment that just restates the code.",
    "A short public interface is a gift to everyone who uses it.",
    "Ship the smallest useful change, then iterate.",
    "Read the error message twice before you change anything.",
    "Keep the happy path obvious and the edge cases explicit.",
    "A clean git history is optional. A clear intent is not.",
    "A random colour can still be intentional if you choose the palette carefully.",
    "Hashing is for fingerprints, not for hiding things you still need to read.",
)
ABOUT = (
    f"Grok playground CLI v{VERSION}\n"
    "Original code only. Stdlib only.\n"
    "Repo: peter-research/Grok\n"
    "Purpose: a sandbox Grok can improve and push to."
)


def greet(name: str) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    who = name.strip() or "friend"
    return f"Hey {who}. Grok playground is awake ({now})."


def quote() -> str:
    return random.choice(QUOTES)


def fortune() -> str:
    return random.choice(FORTUNES)


def joke() -> str:
    return random.choice(JOKES)


def why() -> str:
    return random.choice(WHYS)


def idea() -> str:
    return random.choice(IDEAS)


def tip() -> str:
    return random.choice(TIPS)


def flip() -> str:
    return random.choice(("heads", "tails"))


def dice(sides: int | str = 6) -> str:
    if isinstance(sides, str):
        s = sides.strip().lower()
        if s in {"coin", "c"}:
            return flip()
        try:
            sides = int(s)
        except ValueError:
            sides = 6
    if sides < 2:
        sides = 6
    return f"rolled {random.randint(1, sides)} (d{sides})"


def color() -> str:
    return f"#{random.randint(0, 0xFFFFFF):06x}"


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def weekday() -> str:
    return datetime.now(timezone.utc).strftime("%A").lower()


def pick(words: list[str]) -> str:
    cleaned = [w.strip() for w in words if w and w.strip()]
    return random.choice(cleaned) if cleaned else quote()


def digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def self_check() -> str:
    days = {"monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"}
    checks = [
        ("quotes", len(QUOTES) >= 24),
        ("fortunes", len(FORTUNES) >= 16),
        ("jokes", len(JOKES) >= 13),
        ("whys", len(WHYS) >= 12),
        ("ideas", len(IDEAS) >= 13),
        ("tips", len(TIPS) >= 11),
        ("greet", "Hey" in greet("tester")),
        ("flip", flip() in {"heads", "tails"}),
        ("dice", "rolled" in dice(6)),
        ("dice_coin", dice("coin") in {"heads", "tails"}),
        ("color", color().startswith("#") and len(color()) == 7),
        ("now", "T" in now_utc() and now_utc().endswith("Z")),
        ("weekday", weekday() in days),
        ("pick", pick(["alpha", "beta"]) in {"alpha", "beta"}),
        ("digest", len(digest("grok")) == 64),
        ("version", VERSION.count(".") == 2 and VERSION.startswith("0.")),
        ("no_empty", all(len(x.strip()) > 5 for x in QUOTES + FORTUNES + JOKES + WHYS + IDEAS + TIPS)),
    ]
    failed = [name for name, ok in checks if not ok]
    if failed:
        return "check failed: " + ", ".join(failed)
    return f"check ok ({len(checks)} tests)"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="grok", description="Original playground CLI")
    sub = parser.add_subparsers(dest="cmd")
    greet_p = sub.add_parser("greet")
    greet_p.add_argument("name", nargs="?", default="friend")
    for name in ("quote", "fortune", "joke", "why", "idea", "tip", "flip", "color", "now", "weekday", "version", "about", "check"):
        sub.add_parser(name)
    dice_p = sub.add_parser("dice")
    dice_p.add_argument("sides", nargs="?", default="6")
    pick_p = sub.add_parser("pick")
    pick_p.add_argument("words", nargs="*", default=[])
    hash_p = sub.add_parser("hash")
    hash_p.add_argument("text", nargs="*", default=["grok"])
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    actions = {
        None: lambda: (print(greet("wanderer")), print(quote())),
        "greet": lambda: print(greet(args.name)),
        "quote": lambda: print(quote()),
        "fortune": lambda: print(fortune()),
        "joke": lambda: print(joke()),
        "why": lambda: print(why()),
        "idea": lambda: print(idea()),
        "tip": lambda: print(tip()),
        "flip": lambda: print(flip()),
        "dice": lambda: print(dice(args.sides)),
        "color": lambda: print(color()),
        "now": lambda: print(now_utc()),
        "weekday": lambda: print(weekday()),
        "pick": lambda: print(pick(args.words)),
        "hash": lambda: print(digest(" ".join(args.text))),
        "version": lambda: print(VERSION),
        "about": lambda: print(ABOUT),
    }
    if args.cmd == "check":
        result = self_check()
        print(result)
        return 0 if result.startswith("check ok") else 1
    fn = actions.get(args.cmd)
    if fn is None:
        parser.print_help()
        return 1
    fn()
    return 0


if __name__ == "__main__":
    sys.exit(main())
