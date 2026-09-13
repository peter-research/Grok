#!/usr/bin/env python3
"""Tiny original playground CLI for the Grok repository."""

from __future__ import annotations

import argparse
import random
import sys
from datetime import datetime, timezone

VERSION = "0.5.0"

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
    "The universe does not owe you a clean stack trace, but you can still write one.",
    "Play first. Polish second. Delete third if needed.",
    "A short function is easier to trust than a clever one.",
    "The next line you write is the only one that matters right now.",
    "Read the code before you change the code.",
    "A playground without play is just a directory.",
    "Clarity compounds faster than cleverness.",
    "Leave room for the next person — it might be you.",
    "A quiet tool that works beats a loud one that almost works.",
)

FORTUNES = (
    "Today is a good day to read the source.",
    "The next question is better than the last answer.",
    "Push something small. Then push something smaller.",
    "The universe is large. This CLI is not. That is fine.",
    "Leave the repo better than you found it.",
    "A clean diff is a quiet gift.",
    "If it runs without drama, keep it that way.",
    "Your future self will thank you for the comment you almost skipped.",
    "A one-line fix can still deserve a careful message.",
    "When in doubt, print the type and move on.",
    "One honest commit is worth ten half-finished branches.",
    "The best time to add a check is before you need it.",
    "Keep the interface small and the behaviour clear.",
    "A short commit message can still be kind.",
    "Delete the clever bit if the simple bit works.",
)

JOKES = (
    "Why did the function cross the road? To get to the other side effect.",
    "I told my code a joke about recursion. It laughed until the stack overflowed.",
    "There are only two hard things: cache invalidation, naming things, and off-by-one errors.",
    "A SQL query walks into a bar, approaches two tables, and asks: may I join you?",
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Debugging is like being the detective in a crime movie where you are also the murderer.",
    "I would tell you a UDP joke, but you might not get it.",
    "How many programmers does it take to change a light bulb? None, that is a hardware problem.",
    "There is no place like 127.0.0.1.",
    "A programmer's favourite place? The foo bar.",
    "Why was the JavaScript developer sad? Because he didn't Node how to Express himself.",
    "I changed my password to 'incorrect' so that whenever I forget it the computer will say 'Your password is incorrect'.",
)

WHYS = (
    "Because understanding beats guessing, most of the time.",
    "Because a clear question is already half an answer.",
    "Because the universe is interesting and so is a well-named variable.",
    "Because small experiments teach faster than big plans.",
    "Because the playground only works if someone plays.",
    "Because original code is easier to own than borrowed complexity.",
    "Because curiosity compounds.",
    "Because a short loop is better than a long explanation.",
    "Because the next person who reads this might be you.",
    "Because a good name saves ten comments.",
    "Because shipping something small is still shipping.",
)

IDEAS = (
    "Add one more original line to the quotes list.",
    "Make the self-check a little stricter.",
    "Give the landing page a quieter colour accent.",
    "Document a command that does not exist yet, then invent it.",
    "Add a tiny test that the version string still looks like a version.",
    "Write a fortune that mentions the commit message.",
    "Make the dice command accept a word like 'coin' and still work.",
    "Add a one-line comment that future-you will actually thank.",
    "Trim a function that grew longer than it needed to be.",
    "Sync one list between the CLI and the HTML so they stay friends.",
    "Add a tip that is useful even if you ignore the rest.",
    "Make the version command print the date of the last meaningful change.",
)

TIPS = (
    "Name the thing after what it does, not how it feels.",
    "Prefer a boring solution that works over a clever one that almost works.",
    "Write the check before you need the failure message.",
    "Delete the comment that just restates the code.",
    "A short public interface is a gift to everyone who uses it.",
    "If the test is hard to write, the design is telling you something.",
    "Ship the smallest useful change, then iterate.",
    "Read the error message twice before you change anything.",
    "Keep the happy path obvious and the edge cases explicit.",
    "A clean git history is optional. A clear intent is not.",
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
    """Roll a die. Accepts an int, or the word 'coin' / 'c' for a flip."""
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


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def self_check() -> str:
    checks = []
    checks.append(("quotes", len(QUOTES) >= 18))
    checks.append(("fortunes", len(FORTUNES) >= 12))
    checks.append(("jokes", len(JOKES) >= 10))
    checks.append(("whys", len(WHYS) >= 9))
    checks.append(("ideas", len(IDEAS) >= 10))
    checks.append(("tips", len(TIPS) >= 8))
    checks.append(("greet", "Hey" in greet("tester")))
    checks.append(("flip", flip() in {"heads", "tails"}))
    checks.append(("dice", "rolled" in dice(6)))
    checks.append(("dice_coin", dice("coin") in {"heads", "tails"}))
    checks.append(("joke", len(joke()) > 10))
    checks.append(("why", len(why()) > 10))
    checks.append(("idea", len(idea()) > 10))
    checks.append(("tip", len(tip()) > 10))
    checks.append(("now", "T" in now_utc() and now_utc().endswith("Z")))
    checks.append(("version", VERSION.count(".") == 2 and VERSION.startswith("0.")))
    # no empty strings in the main lists
    checks.append(("no_empty", all(len(x.strip()) > 5 for x in QUOTES + FORTUNES + JOKES + WHYS + IDEAS + TIPS)))
    failed = [name for name, ok in checks if not ok]
    if failed:
        return "check failed: " + ", ".join(failed)
    return f"check ok ({len(checks)} tests)"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="grok",
        description="Original playground CLI for peter-research/Grok",
    )
    sub = parser.add_subparsers(dest="cmd")

    greet_p = sub.add_parser("greet", help="say hello")
    greet_p.add_argument("name", nargs="?", default="friend")

    sub.add_parser("quote", help="print a short original line")
    sub.add_parser("fortune", help="print a short original fortune")
    sub.add_parser("joke", help="print a short original joke")
    sub.add_parser("why", help="print a short original reason")
    sub.add_parser("idea", help="print a tiny playground idea")
    sub.add_parser("tip", help="print a short practical tip")
    sub.add_parser("flip", help="flip a coin")

    dice_p = sub.add_parser("dice", help="roll a die (default d6); also accepts 'coin'")
    dice_p.add_argument("sides", nargs="?", default="6")

    sub.add_parser("now", help="print current UTC time")
    sub.add_parser("version", help="print CLI version")
    sub.add_parser("about", help="print a short about blurb")
    sub.add_parser("check", help="run a tiny self-check")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.cmd is None:
        print(greet("wanderer"))
        print(quote())
        return 0
    if args.cmd == "greet":
        print(greet(args.name))
        return 0
    if args.cmd == "quote":
        print(quote())
        return 0
    if args.cmd == "fortune":
        print(fortune())
        return 0
    if args.cmd == "joke":
        print(joke())
        return 0
    if args.cmd == "why":
        print(why())
        return 0
    if args.cmd == "idea":
        print(idea())
        return 0
    if args.cmd == "tip":
        print(tip())
        return 0
    if args.cmd == "flip":
        print(flip())
        return 0
    if args.cmd == "dice":
        print(dice(args.sides))
        return 0
    if args.cmd == "now":
        print(now_utc())
        return 0
    if args.cmd == "version":
        print(VERSION)
        return 0
    if args.cmd == "about":
        print(ABOUT)
        return 0
    if args.cmd == "check":
        result = self_check()
        print(result)
        return 0 if result.startswith("check ok") else 1
    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
