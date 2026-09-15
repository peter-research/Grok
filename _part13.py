"""Part 13 — v0.36 commands."""

import base64


def popcnt_int(n: int) -> int:
    if n < 0:
        raise ValueError("negative")
    return bin(n).count("1")


def gray_int(n: int) -> int:
    if n < 0:
        raise ValueError("negative")
    return n ^ (n >> 1)


def ungray_int(g: int) -> int:
    if g < 0:
        raise ValueError("negative")
    n = g
    shift = 1
    while g >> shift:
        n ^= g >> shift
        shift += 1
    return n


def soundex_word(word: str) -> str:
    letters = [c.upper() for c in word if c.isalpha()]
    if not letters:
        raise ValueError("empty")
    first = letters[0]
    mapping = {
        "B": "1", "F": "1", "P": "1", "V": "1",
        "C": "2", "G": "2", "J": "2", "K": "2", "Q": "2", "S": "2", "X": "2", "Z": "2",
        "D": "3", "T": "3",
        "L": "4",
        "M": "5", "N": "5",
        "R": "6",
    }
    digits = []
    prev = mapping.get(first, "0")
    for c in letters[1:]:
        d = mapping.get(c, "0")
        if d == "0":
            prev = "0"
            continue
        if d != prev:
            digits.append(d)
            prev = d
    code = (first + "".join(digits) + "000")[:4]
    return code


def b32_text(text: str) -> str:
    return base64.b32encode(text.encode("utf-8")).decode("ascii")


def cmd_popcnt(args):
    n = int(_need(1, args)[0])
    return str(popcnt_int(n))


def cmd_gray(args):
    n = int(_need(1, args)[0])
    return str(gray_int(n))


def cmd_ungray(args):
    n = int(_need(1, args)[0])
    return str(ungray_int(n))


def cmd_soundex(args):
    word = _need(1, args)[0]
    return soundex_word(word)


def cmd_b32(args):
    text = " ".join(_need(1, args, "text"))
    return b32_text(text)


COMMANDS.update({
    "popcnt": cmd_popcnt,
    "gray": cmd_gray,
    "ungray": cmd_ungray,
    "soundex": cmd_soundex,
    "b32": cmd_b32,
})
COMMAND_NAMES = list(COMMANDS)

_old_check = cmd_check


def cmd_check(args):
    out = _old_check(args)
    assert popcnt_int(13) == 3
    assert gray_int(7) == 4
    assert ungray_int(4) == 7
    assert soundex_word("Robert") == "R163"
    assert b32_text("hi") == "NBUQ===="
    return out


COMMANDS["check"] = cmd_check
