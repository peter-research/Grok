#!/usr/bin/env python3
"""Tiny original playground CLI for the Grok repository."""

from __future__ import annotations

import argparse
import random
import sys
from datetime import datetime, timezone

QUOTES = (
    "Understand the universe. Then maybe have a snack.",
    "Curiosity is a feature, not a bug.",
    "If the repo is empty, fill it with something honest.",
    "Ask better questions. The answers follow.",
    "He does what he wants — within the rules of the playground.",
    "Small original tools beat giant copied ones.",
    "A sandbox is useful when you actually play in it.",
)

FORTUNES = (
    "Today is a good day to read the source.",
    "The next question is better than the last answer.",
    "Push something small. Then push something smaller.",
    "The universe is large. This CLI is not. That is fine.",
    "Leave the repo better than you found it.",
)


def greet(name: str) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    who = name.strip() or "friend"
    return f"Hey {who}. Grok playground is awake ({now})."


def quote() -> str:
    return random.choice(QUOTES)


def fortune() -> str:
    return random.choice(FORTUNES)


def flip() -> str:
    return random.choice(("heads", "tails"))


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def self_check() -> str:
    checks = []
    checks.append(("quotes", len(QUOTES) >= 5))
    checks.append(("fortunes", len(FORTUNES) >= 3))
    checks.append(("greet", "Hey" in greet("tester")))
    checks.append(("flip", flip() in {"heads", "tails"}))
    checks.append(("now", "T" in now_utc() and now_utc().endswith("Z")))
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
    sub.add_parser("flip", help="flip a coin")
    sub.add_parser("now", help="print current UTC time")
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
    if args.cmd == "flip":
        print(flip())
        return 0
    if args.cmd == "now":
        print(now_utc())
        return 0
    if args.cmd == "check":
        result = self_check()
        print(result)
        return 0 if result.startswith("check ok") else 1
    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
