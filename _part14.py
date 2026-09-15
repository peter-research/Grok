"""Part 14 — v0.37 commands."""

_VOWELS = set("aeiouAEIOU")


def is_isogram(text: str) -> bool:
    letters = [c.lower() for c in text if c.isalpha()]
    if not letters:
        raise ValueError("empty")
    return len(letters) == len(set(letters))


def count_vowels(text: str) -> int:
    return sum(1 for c in text if c in _VOWELS)


def count_cons(text: str) -> int:
    return sum(1 for c in text if c.isalpha() and c not in _VOWELS)


def rotate_left(text: str, n: int) -> str:
    if not text:
        return text
    n = n % len(text)
    return text[n:] + text[:n]


def rotate_right(text: str, n: int) -> str:
    if not text:
        return text
    n = n % len(text)
    return text[-n:] + text[:-n] if n else text


def cmd_isogram(args):
    text = " ".join(_need(1, args, "text"))
    return "yes" if is_isogram(text) else "no"


def cmd_vowels(args):
    text = " ".join(_need(1, args, "text"))
    return str(count_vowels(text))


def cmd_cons(args):
    text = " ".join(_need(1, args, "text"))
    return str(count_cons(text))


def cmd_rotl(args):
    n, *rest = _need(2, args, "n text")
    return rotate_left(" ".join(rest), int(n))


def cmd_rotr(args):
    n, *rest = _need(2, args, "n text")
    return rotate_right(" ".join(rest), int(n))


COMMANDS.update({
    "isogram": cmd_isogram,
    "vowels": cmd_vowels,
    "cons": cmd_cons,
    "rotl": cmd_rotl,
    "rotr": cmd_rotr,
})
COMMAND_NAMES = list(COMMANDS)

_old_check = cmd_check


def cmd_check(args):
    out = _old_check(args)
    assert is_isogram("Grok") is True
    assert is_isogram("Hello") is False
    assert count_vowels("Grok") == 1
    assert count_cons("Grok") == 3
    assert rotate_left("Grok", 1) == "rokG"
    assert rotate_right("Grok", 1) == "kGro"
    return out


COMMANDS["check"] = cmd_check
