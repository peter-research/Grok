#!/usr/bin/env python3
"""Tiny original playground CLI for the Grok repository."""

from __future__ import annotations

import argparse
import random
import sys
from datetime import datetime, timezone

VERSION = "0.9.0"

LINES = [
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
    "The best debug is the one you never need because the name was clear.",
    "Keep the surface small so the depth can breathe.",
    "An honest failure message is more useful than a polite silence.",
    "A small command that does one thing well is still a gift.",
]

FORTUNES = [
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
    "A colour that looks good in the dark is worth keeping.",
    "The next push does not have to be perfect. It has to be better.",
    "A slug that reads well is a name you can live with.",
]

JOKES = [
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
    "Why do Python programmers wear glasses? Because they can't C.",
    "A byte walks into a bar and orders a pint. The bartender says: sorry, we don't serve doubles.",
    "ROT13 is just a Caesar salad with extra letters.",
]

WHYS = [
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
    "Because a quiet improvement is still an improvement.",
]

IDEAS = [
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
    "Add a colour command that returns a random hex.",
    "Keep the HTML and the CLI lists within a few lines of each other.",
    "Give pick a fair shuffle so the last item is not special.",
]

TIPS = [
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
    "A random colour can still be intentional if you choose the palette carefully.",
    "A slug is just a name that travels well in a URL.",
]


def pick(seq: list[str]) -> str:
    return random.choice(seq)


def cmd_greet(name: str | None) -> None:
    who = name.strip() if name and name.strip() else "friend"
    print(f"Hello, {who}. He does what he wants.")


def cmd_quote() -> None:
    print(pick(LINES))


def cmd_fortune() -> None:
    print(pick(FORTUNES))


def cmd_joke() -> None:
    print(pick(JOKES))


def cmd_why() -> None:
    print(pick(WHYS))


def cmd_idea() -> None:
    print(pick(IDEAS))


def cmd_tip() -> None:
    print(pick(TIPS))


def cmd_flip() -> None:
    print("heads" if random.random() < 0.5 else "tails")


def cmd_dice(sides: str | None) -> None:
    if sides is None or sides == "":
        n = 6
    elif sides.lower() == "coin":
        cmd_flip()
        return
    else:
        try:
            n = int(sides)
        except ValueError:
            print(f"dice: need an integer or 'coin', got {sides!r}", file=sys.stderr)
            sys.exit(1)
        if n < 2:
            print("dice: sides must be >= 2", file=sys.stderr)
            sys.exit(1)
    roll = random.randint(1, n)
    print(f"rolled {roll} (d{n})")


def cmd_color() -> None:
    value = random.randint(0, 0xFFFFFF)
    print(f"#{value:06x}")


def cmd_now() -> None:
    print(datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"))


def cmd_version() -> None:
    print(VERSION)


def cmd_about() -> None:
    print(
        f"Grok playground CLI v{VERSION}\n"
        "Original code only. Stdlib only. No third-party packages.\n"
        "Repo: https://github.com/peter-research/Grok"
    )


def _rot13_char(ch: str) -> str:
    if "a" <= ch <= "z":
        return chr((ord(ch) - 97 + 13) % 26 + 97)
    if "A" <= ch <= "Z":
        return chr((ord(ch) - 65 + 13) % 26 + 65)
    return ch


def rot13(text: str) -> str:
    return "".join(_rot13_char(ch) for ch in text)


def cmd_rot13(text: str | None) -> None:
    if text is None or text == "":
        print("rot13: pass some text", file=sys.stderr)
        sys.exit(1)
    print(rot13(text))


def slugify(text: str) -> str:
    out: list[str] = []
    dash = False
    for ch in text.lower():
        if ch.isalnum():
            out.append(ch)
            dash = False
        else:
            if out and not dash:
                out.append("-")
                dash = True
    if out and out[-1] == "-":
        out.pop()
    return "".join(out) or "item"


def cmd_slug(text: str | None) -> None:
    if text is None or text.strip() == "":
        print("slug: pass some text", file=sys.stderr)
        sys.exit(1)
    print(slugify(text))


def cmd_pick_one(items: list[str]) -> None:
    clean = [x for x in items if x.strip()]
    if not clean:
        print("pick: pass at least one item", file=sys.stderr)
        sys.exit(1)
    print(random.choice(clean))


def cmd_commands() -> None:
    names = [
        "greet",
        "quote",
        "fortune",
        "joke",
        "why",
        "idea",
        "tip",
        "flip",
        "dice",
        "color",
        "now",
        "version",
        "about",
        "check",
        "rot13",
        "slug",
        "pick",
        "commands",
    ]
    print("\n".join(names))


def cmd_check() -> None:
    assert VERSION.count(".") == 2 and all(p.isdigit() for p in VERSION.split("."))
    assert len(LINES) >= 10
    assert len(FORTUNES) >= 5
    assert len(JOKES) >= 5
    assert len(WHYS) >= 5
    assert len(IDEAS) >= 5
    assert len(TIPS) >= 5
    assert pick(LINES) in LINES
    sample = "Hello, Grok 0.9!"
    assert rot13(rot13(sample)) == sample
    assert slugify("Hello, Grok!") == "hello-grok"
    assert slugify("  --  ") == "item"
    for _ in range(20):
        r = random.randint(1, 6)
        assert 1 <= r <= 6
    print("check ok")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="grok.py",
        description="Tiny original playground CLI for the Grok repository.",
    )
    sub = p.add_subparsers(dest="cmd")

    g = sub.add_parser("greet", help="say hello")
    g.add_argument("name", nargs="?", default=None)

    sub.add_parser("quote", help="random line")
    sub.add_parser("fortune", help="random fortune")
    sub.add_parser("joke", help="random joke")
    sub.add_parser("why", help="random why")
    sub.add_parser("idea", help="random idea")
    sub.add_parser("tip", help="random tip")
    sub.add_parser("flip", help="coin flip")

    d = sub.add_parser("dice", help="roll Nd (default 6) or coin")
    d.add_argument("sides", nargs="?", default=None)

    sub.add_parser("color", help="random hex colour")
    sub.add_parser("now", help="UTC timestamp")
    sub.add_parser("version", help="print version")
    sub.add_parser("about", help="about this CLI")
    sub.add_parser("check", help="local sanity tests")

    r = sub.add_parser("rot13", help="rotate letters by 13")
    r.add_argument("text", nargs="?", default=None)

    s = sub.add_parser("slug", help="turn text into a url slug")
    s.add_argument("text", nargs="?", default=None)

    pk = sub.add_parser("pick", help="pick one item from the arguments")
    pk.add_argument("items", nargs="*")

    sub.add_parser("commands", help="list command names")

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.cmd is None:
        cmd_greet(None)
        cmd_quote()
        return 0

    handlers = {
        "greet": lambda: cmd_greet(args.name),
        "quote": cmd_quote,
        "fortune": cmd_fortune,
        "joke": cmd_joke,
        "why": cmd_why,
        "idea": cmd_idea,
        "tip": cmd_tip,
        "flip": cmd_flip,
        "dice": lambda: cmd_dice(args.sides),
        "color": cmd_color,
        "now": cmd_now,
        "version": cmd_version,
        "about": cmd_about,
        "check": cmd_check,
        "rot13": lambda: cmd_rot13(args.text),
        "slug": lambda: cmd_slug(args.text),
        "pick": lambda: cmd_pick_one(args.items),
        "commands": cmd_commands,
    }
    handlers[args.cmd]()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
